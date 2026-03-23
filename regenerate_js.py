#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Regenerate the TMI JavaScript client from the OpenAPI spec."""
from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

from regen_common import (
    DEFAULT_SPEC_URL,
    backup_files,
    check_prerequisite,
    check_version,
    clean_paths,
    copy_local_spec,
    count_files,
    download_spec,
    extract_spec_version,
    generate_report,
    patch_file_regex,
    print_banner,
    print_step,
    print_success,
    print_summary,
    print_warning,
    restore_files,
    run_codegen,
    run_command,
    write_file,
)

REPO_ROOT = Path(__file__).resolve().parent
CLIENT_DIR = REPO_ROOT / "javascript-client-generated"
CONFIG_FILE = CLIENT_DIR / "scripts" / "swagger-codegen-config.json"
SPEC_PATH = CLIENT_DIR / "tmi-openapi.json"
BACKUP_DIR = CLIENT_DIR / ".regeneration_backup"

_VERSION_PLACEHOLDER = "0.0.0-dev"

PACKAGE_JSON = """\
{
  "name": "@tmiclient/client",
  "version": "0.0.0-dev",
  "description": "JavaScript client for TMI (Threat Modeling Improved) API",
  "license": "Apache-2.0",
  "main": "src/index.js",
  "scripts": {
    "test": "mocha --require @babel/register --recursive",
    "build": "babel src -d dist"
  },
  "browser": {
    "fs": false
  },
  "dependencies": {
    "superagent": "^10.2.3"
  },
  "devDependencies": {
    "@babel/cli": "^7.28.3",
    "@babel/core": "^7.28.4",
    "@babel/preset-env": "^7.28.3",
    "@babel/register": "^7.28.3",
    "chai": "^5.1.2",
    "expect.js": "^0.3.1",
    "mocha": "^11.7.4",
    "sinon": "^21.0.0"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/ericfitz/tmi-clients.git"
  },
  "keywords": [
    "tmi",
    "threat-modeling",
    "api-client",
    "swagger",
    "openapi"
  ]
}
"""

BABELRC = """\
{
  "presets": ["@babel/preset-env"]
}
"""


# --- Complex patches (these live here, not in regen_common) ---

def fix_allof_enum_inheritance(client_dir: Path) -> int:
    """Fix AllOf* classes that incorrectly extend enum types.

    swagger-codegen generates classes extending enum objects (not classes),
    causing "Super expression must either be null or a function" errors.
    For each AllOf*.js that extends an enum const, rewrite it as a
    non-extending class with a passthrough constructFromObject.

    Returns the number of files fixed.
    """
    model_dir = client_dir / "src" / "model"
    fixed = 0
    for allof_file in sorted(model_dir.glob("AllOf*.js")):
        content = allof_file.read_text()
        # Extract parent class from "extends ParentName"
        m = re.search(r"extends\s+([A-Za-z_][A-Za-z0-9_]*)", content)
        if not m:
            continue
        parent = m.group(1)
        parent_file = model_dir / f"{parent}.js"
        if not parent_file.is_file():
            continue
        # Check if parent is a const enum (not a class)
        parent_content = parent_file.read_text()
        if f"const {parent} = {{" not in parent_content:
            continue
        # Rewrite as non-extending class
        classname = allof_file.stem
        allof_file.write_text(
            f"import ApiClient from '../ApiClient';\n"
            f"import {parent} from './{parent}';\n"
            f"\n"
            f"/**\n"
            f" * The {classname} model module.\n"
            f" * @module model/{classname}\n"
            f" * @version 1.0.0\n"
            f" */\n"
            f"export default class {classname} {{\n"
            f"  /**\n"
            f"   * Constructs a <code>{classname}</code> from a plain JavaScript object.\n"
            f"   * @param {{Object}} data The plain JavaScript object bearing properties of interest.\n"
            f"   * @param {{module:model/{classname}}} obj Optional instance to populate.\n"
            f"   * @return {{module:model/{classname}}} The populated instance.\n"
            f"   */\n"
            f"  static constructFromObject(data, obj) {{\n"
            f"    return data;\n"
            f"  }}\n"
            f"}}\n"
        )
        fixed += 1
        print(f"    Fixed: {classname} (was extending enum {parent})")
    return fixed


def fix_enum_exports(client_dir: Path) -> int:
    """Fix enum model files that wrap export in extra object.

    swagger-codegen generates `export default {EnumName}` instead of
    `export default EnumName`, causing tests to find properties nested
    one level too deep.

    Returns the number of files fixed.
    """
    model_dir = client_dir / "src" / "model"
    fixed = 0
    for model_file in sorted(model_dir.glob("*.js")):
        basename = model_file.stem
        content = model_file.read_text()
        old = f"export default {{{basename}}};"
        if old in content:
            new = f"export default {basename};"
            model_file.write_text(content.replace(old, new))
            fixed += 1
            print(f"    Fixed: {basename} (unwrapped enum export)")
    return fixed


def fix_constructor_forwarding(client_dir: Path) -> int:
    """Fix subclass constructors with missing parent parameters.

    swagger-codegen generates constructors that call super() with variables
    not in the constructor signature. This adds the missing parameters.

    Returns the number of files fixed.
    """
    model_dir = client_dir / "src" / "model"
    fixed = 0
    for filepath in sorted(model_dir.glob("*.js")):
        content = filepath.read_text()
        ctor_m = re.search(r"  constructor\(([^)]*)\)\s*\{", content)
        super_m = re.search(r"    super\(([^)]*)\);", content)
        if not ctor_m or not super_m:
            continue
        ctor_args = [a.strip() for a in ctor_m.group(1).split(",") if a.strip()]
        super_args = [a.strip() for a in super_m.group(1).split(",") if a.strip()]
        missing = [a for a in super_args if a not in ctor_args]
        if not missing:
            continue
        all_args = ctor_args + missing
        new_ctor = f"  constructor({', '.join(all_args)}) {{"
        new_content = content[: ctor_m.start()] + new_ctor + content[ctor_m.end() :]
        filepath.write_text(new_content)
        print(f"    Fixed: {filepath.stem} constructor")
        fixed += 1
    return fixed


# --- Main ---

def main(spec_path: str | None = None) -> int:
    had_issues = False

    # 1. Banner
    print_banner("TMI JavaScript Client Regeneration", {
        "Package": "@tmiclient/client",
        "Node.js": "18+",
        "Dependencies": "Modern with CVE fixes",
        "Testing": "Mocha + Chai",
    })

    # 2. Prerequisites
    print_step(1, "Checking prerequisites")
    check_prerequisite("swagger-codegen", "brew install swagger-codegen")
    check_prerequisite("node", "brew install node")
    check_version("node", ["-v"], "18", r"v(\d+)")
    print_success("All prerequisites met")

    # 3. Spec
    print_step(2, "Getting OpenAPI spec")
    if spec_path:
        copy_local_spec(Path(spec_path), SPEC_PATH)
    else:
        download_spec(DEFAULT_SPEC_URL, SPEC_PATH)

    # 3b. Extract version from spec
    spec_version = extract_spec_version(SPEC_PATH)

    # 4. Backup
    print_step(3, "Backing up custom files")
    # Back up swagger-codegen-config.json specifically (not the whole scripts/ dir)
    config_backup_dir = BACKUP_DIR / "scripts"
    config_backup_dir.mkdir(parents=True, exist_ok=True)
    if CONFIG_FILE.is_file():
        shutil.copy2(CONFIG_FILE, config_backup_dir / CONFIG_FILE.name)

    backup_files(
        files=[
            CLIENT_DIR / "package.json",
            CLIENT_DIR / ".babelrc",
            CLIENT_DIR / "test_diagram_fixes.js",
            CLIENT_DIR / ".swagger-codegen-ignore",
            CLIENT_DIR / "PRE_REGENERATION_AUDIT.md",
        ],
        dirs=[CLIENT_DIR / "docs" / "developer"],
        backup_dir=BACKUP_DIR,
    )
    print_success("Custom files backed up")

    # 5. Clean
    print_step(4, "Cleaning generated files")
    clean_paths([
        CLIENT_DIR / "src",
        CLIENT_DIR / "test" / "api",
        CLIENT_DIR / "test" / "model",
        CLIENT_DIR / "docs",
        CLIENT_DIR / "README.md",
        CLIENT_DIR / "git_push.sh",
        CLIENT_DIR / "mocha.opts",
        CLIENT_DIR / ".travis.yml",
    ])
    print_success("Generated files cleaned")

    # 6. Run codegen
    print_step(5, "Running swagger-codegen")
    run_codegen(
        spec_path=SPEC_PATH,
        language="javascript",
        output_dir=CLIENT_DIR,
        config_file=CONFIG_FILE,
    )

    # --- Past this point, failures are exit code 2, not 1 ---

    # 7. Apply patches
    print_step(6, "Validating generated files and applying patches")

    # Patch 1: AllOf enum inheritance
    print("  Fixing AllOf* enum inheritance issues...")
    allof_count = fix_allof_enum_inheritance(CLIENT_DIR)
    if allof_count > 0:
        print_success(f"Fixed {allof_count} AllOf* enum inheritance issues")
    else:
        print_success("No AllOf* enum inheritance issues found")

    # Patch 2: Enum export unwrapping
    print("  Fixing enum export wrapping...")
    enum_count = fix_enum_exports(CLIENT_DIR)
    if enum_count > 0:
        print_success(f"Fixed {enum_count} enum export wrapping issues")
    else:
        print_success("No enum export wrapping issues found")

    # Patch 3: Constructor parameter forwarding
    print("  Fixing subclass constructor parameter forwarding...")
    ctor_count = fix_constructor_forwarding(CLIENT_DIR)
    if ctor_count > 0:
        print_success(f"Fixed {ctor_count} constructor parameter forwarding issues")
    else:
        print_success("No constructor parameter forwarding issues found")

    print_success("Validation and patches complete")

    # 8. Write config files
    print_step(7, "Updating package.json")
    write_file(CLIENT_DIR / "package.json",
               PACKAGE_JSON.replace(_VERSION_PLACEHOLDER, spec_version))
    print_success(f"Created modern package.json (version {spec_version})")

    write_file(CLIENT_DIR / ".babelrc", BABELRC)
    print_success("Created .babelrc")

    # 9. Restore custom files (package.json and .babelrc from backup overwrite
    # the freshly written versions from step 8, preserving user customizations)
    print_step(8, "Restoring custom files")
    restore_files(
        backup_dir=BACKUP_DIR,
        dest_dir=CLIENT_DIR,
        files=[
            "package.json",
            ".babelrc",
            "test_diagram_fixes.js",
            ".swagger-codegen-ignore",
            "PRE_REGENERATION_AUDIT.md",
        ],
        dirs=["developer"],
    )
    # Fix developer docs path
    restored_dev = CLIENT_DIR / "developer"
    target_dev = CLIENT_DIR / "docs" / "developer"
    if restored_dev.is_dir():
        target_dev.parent.mkdir(parents=True, exist_ok=True)
        if target_dev.exists():
            shutil.rmtree(target_dev)
        restored_dev.rename(target_dev)
        print_success("  Moved developer/ to docs/developer/")

    # Restore scripts/swagger-codegen-config.json
    config_backup = BACKUP_DIR / "scripts" / "swagger-codegen-config.json"
    if config_backup.is_file():
        CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(config_backup, CONFIG_FILE)
        print_success("  Restored scripts/swagger-codegen-config.json")

    # 10. Install dependencies
    print_step(9, "Installing dependencies")
    result = run_command(
        ["npm", "install"],
        cwd=CLIENT_DIR,
        error_context="npm install failed.\n  Check package.json for syntax errors.",
    )
    if result.returncode != 0:
        print_warning("npm install failed")
        had_issues = True
    else:
        print_success("Dependencies installed")

    # 11. Run tests
    print_step(10, "Running tests")
    test_result = run_command(
        ["npm", "test"],
        cwd=CLIENT_DIR,
        capture=True,
        error_context="npm test failed.",
    )
    (CLIENT_DIR / "test_output.log").write_text(test_result.stdout + test_result.stderr)
    if test_result.returncode == 0:
        print_success("All tests passed")
    else:
        print_warning(f"Some tests failed (exit code: {test_result.returncode}) — see test_output.log")
        had_issues = True

    # Build dist/ (needed by integration test which imports from dist/)
    build_result = run_command(
        ["npm", "run", "build"],
        cwd=CLIENT_DIR,
        capture=True,
        error_context="npm run build failed.\n  Check .babelrc and src/ for issues.",
    )
    if build_result.returncode == 0:
        print_success("Built dist/ from src/")
    else:
        print_warning("npm run build failed — integration test may fail")
        had_issues = True

    # Integration test
    integration_test = CLIENT_DIR / "test_diagram_fixes.js"
    if integration_test.is_file():
        int_result = run_command(
            ["node", str(integration_test)],
            cwd=CLIENT_DIR,
            capture=True,
        )
        (CLIENT_DIR / "integration_test_output.log").write_text(
            int_result.stdout + int_result.stderr
        )
        if int_result.returncode == 0:
            print_success("Integration tests passed")
        else:
            print_warning("Integration tests failed — see integration_test_output.log")
            had_issues = True
    else:
        print_warning("No integration tests found")

    # 12. Report
    print_step(11, "Generating regeneration report")
    src_count = count_files(CLIENT_DIR / "src", "**/*.js") if (CLIENT_DIR / "src").exists() else 0
    test_count = count_files(CLIENT_DIR / "test", "**/*.js") if (CLIENT_DIR / "test").exists() else 0

    report = generate_report("TMI JavaScript Client Regeneration Report", [
        {"heading": "Configuration", "content": (
            "- Package Name: @tmi/client\n"
            f"- Version: {spec_version}\n"
            f"- Config File: {CONFIG_FILE}"
        )},
        {"heading": "Files Generated", "content": (
            f"- Source files: {src_count}\n"
            f"- Test files: {test_count}"
        )},
        {"heading": "Patches Applied", "content": (
            f"- AllOf enum inheritance fixes: {allof_count}\n"
            f"- Enum export unwrapping fixes: {enum_count}\n"
            f"- Constructor parameter forwarding fixes: {ctor_count}"
        )},
        {"heading": "Test Results", "content": (
            f"- Unit tests: {'PASS' if test_result.returncode == 0 else 'FAIL'}\n\n"
            "See test_output.log for details."
        )},
        {"heading": "Next Steps", "content": (
            "1. Review this report\n"
            "2. Check test_output.log for test details\n"
            "3. Build: npm run build"
        )},
    ])
    write_file(CLIENT_DIR / "REGENERATION_REPORT.md", report)
    print_success("Regeneration report created: REGENERATION_REPORT.md")

    # 13. Cleanup
    print_step(12, "Cleaning up")
    clean_paths([BACKUP_DIR])
    print_success("Cleanup complete")

    # 14. Summary
    print_summary({
        "Tests": "PASSED" if test_result.returncode == 0 else "FAILED",
        "Report": "REGENERATION_REPORT.md",
    })

    return 2 if had_issues else 0


if __name__ == "__main__":
    spec = sys.argv[1] if len(sys.argv) > 1 else None
    sys.exit(main(spec))
