#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Regenerate the TMI TypeScript client from the OpenAPI spec using openapi-generator."""
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
    print_banner,
    print_step,
    print_success,
    print_summary,
    print_warning,
    restore_files,
    run_codegen_openapi_generator,
    run_command,
    update_json_version,
    write_file,
)

REPO_ROOT = Path(__file__).resolve().parent
CLIENT_DIR = REPO_ROOT / "typescript-client-generated"
CONFIG_FILE = CLIENT_DIR / "scripts" / "openapi-generator-config.json"
SPEC_PATH = CLIENT_DIR / "tmi-openapi.json"
BACKUP_DIR = CLIENT_DIR / ".regeneration_backup"

_VERSION_PLACEHOLDER = "0.0.0-dev"

PACKAGE_JSON = """\
{
  "name": "@tmiclient/client",
  "version": "0.0.0-dev",
  "description": "TypeScript client for TMI (Threat Modeling Improved) API",
  "license": "Apache-2.0",
  "main": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "module": "./dist/esm/index.js",
  "sideEffects": false,
  "scripts": {
    "build": "tsc && tsc -p tsconfig.esm.json",
    "prepare": "npm run build"
  },
  "devDependencies": {
    "typescript": "^5.0"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/ericfitz/tmi-clients.git"
  },
  "keywords": [
    "tmi",
    "threat-modeling",
    "api-client",
    "openapi",
    "typescript"
  ]
}
"""

TSCONFIG = """\
{
  "compilerOptions": {
    "declaration": true,
    "target": "ES2022",
    "module": "commonjs",
    "moduleResolution": "node",
    "outDir": "dist",
    "typeRoots": [
      "node_modules/@types"
    ]
  },
  "exclude": [
    "dist",
    "node_modules"
  ]
}
"""

TSCONFIG_ESM = """\
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "module": "esnext",
    "outDir": "dist/esm"
  }
}
"""


# --- Patches ---


def patch_optional_extends(had_issues: bool) -> bool:
    """Fix openapi-generator bug: allOf child interfaces declare inherited
    required properties as optional, causing TS2430/TS2345 errors.

    The pattern: a child interface (e.g., DfdDiagram) extends a parent
    (e.g., BaseDiagram) but marks an inherited required property (e.g., `type`)
    as optional (`type?`).  The fix removes the `?` to make it required,
    matching the parent interface.

    Known affected pairs:
    - DfdDiagram extends BaseDiagram (property: type)
    - DfdDiagramInput extends BaseDiagramInput (property: type)
    - Edge extends Cell (property: shape)
    - Node extends Cell (property: shape)
    """
    models_dir = CLIENT_DIR / "src" / "models"
    if not models_dir.is_dir():
        print_warning("Models directory not found — skipping optional-extends patch")
        return True

    # Map of (child_file, parent_file, property_name)
    fixes = [
        ("DfdDiagram.ts", "BaseDiagram.ts", "type"),
        ("DfdDiagramInput.ts", "BaseDiagramInput.ts", "type"),
        ("Edge.ts", "Cell.ts", "shape"),
        ("Node.ts", "Cell.ts", "shape"),
    ]

    patched_count = 0
    for child_file, _parent_file, prop_name in fixes:
        child_path = models_dir / child_file
        if not child_path.is_file():
            continue

        content = child_path.read_text(encoding="utf-8")
        # Match the optional property declaration in the interface
        # e.g., "    type?: DfdDiagramTypeEnum;" -> "    type: DfdDiagramTypeEnum;"
        pattern = rf"(\s+){prop_name}\?:"
        replacement = rf"\1{prop_name}:"
        new_content, count = re.subn(pattern, replacement, content)
        if count > 0:
            child_path.write_text(new_content, encoding="utf-8")
            patched_count += count
            print(f"    Fixed: {child_file} ({prop_name}? -> {prop_name})")

    if patched_count > 0:
        print_success(f"Optional-extends patch: {patched_count} properties fixed")
    else:
        print_warning("Optional-extends patch: no properties needed fixing")

    return had_issues


def patch_missing_token_request(had_issues: bool) -> bool:
    """Fix openapi-generator bug: AuthenticationApi.ts imports TokenRequest
    but no TokenRequest model is generated.

    The fix removes the TokenRequest import and replaces usages with
    inline object type or any.  This happens because the OpenAPI spec uses
    application/x-www-form-urlencoded for the token endpoint, and
    openapi-generator generates a reference to a model it never creates.
    """
    api_file = CLIENT_DIR / "src" / "apis" / "AuthenticationApi.ts"
    if not api_file.is_file():
        print_warning("AuthenticationApi.ts not found — skipping TokenRequest patch")
        return had_issues

    content = api_file.read_text(encoding="utf-8")
    if "TokenRequest" not in content:
        print_warning("TokenRequest not referenced in AuthenticationApi.ts — skipping")
        return had_issues

    # Remove TokenRequest from imports
    # Remove lines importing TokenRequest, TokenRequestFromJSON, TokenRequestToJSON
    new_content = re.sub(r"^\s+TokenRequest,?\n", "", content, flags=re.MULTILINE)
    new_content = re.sub(r"^\s+TokenRequestFromJSON,?\n", "", new_content, flags=re.MULTILINE)
    new_content = re.sub(r"^\s+TokenRequestToJSON,?\n", "", new_content, flags=re.MULTILINE)

    # Replace TokenRequestToJSON(...) calls with the raw body
    new_content = re.sub(
        r"TokenRequestToJSON\(([^)]+)\)",
        r"\1 as any",
        new_content,
    )

    if new_content != content:
        api_file.write_text(new_content, encoding="utf-8")
        print_success("TokenRequest patch: removed missing model references")
    else:
        print_warning("TokenRequest patch: no changes needed")

    return had_issues


# --- Main ---


def main(spec_path: str | None = None) -> int:
    had_issues = False

    # 1. Banner
    print_banner("TMI TypeScript Client Regeneration (openapi-generator)", {
        "Package": "@tmiclient/client",
        "Node.js": "18+",
        "Generator": "openapi-generator 7.x",
        "Language": "TypeScript (fetch)",
        "Target": "ES2022",
    })

    # 2. Prerequisites
    print_step(1, "Checking prerequisites")
    check_prerequisite("openapi-generator", "brew install openapi-generator")
    check_prerequisite("node", "brew install node")
    check_version("node", ["-v"], "18", r"v(\d+)")
    print_success("All prerequisites met")

    # 3. Spec
    print_step(2, "Getting OpenAPI spec")
    if spec_path:
        copy_local_spec(Path(spec_path), SPEC_PATH)
    else:
        download_spec(DEFAULT_SPEC_URL, SPEC_PATH)

    # 3b. Extract version from spec and update codegen config
    spec_version = extract_spec_version(SPEC_PATH)
    update_json_version(CONFIG_FILE, "npmVersion", spec_version)

    # 4. Backup
    print_step(3, "Backing up custom files")
    backup_files(
        files=[
            CLIENT_DIR / ".openapi-generator-ignore",
        ],
        dirs=[CLIENT_DIR / "docs" / "developer"],
        backup_dir=BACKUP_DIR,
    )
    print_success("Custom files backed up")

    # 5. Clean
    print_step(4, "Cleaning generated files")
    clean_paths([
        CLIENT_DIR / "src",
        CLIENT_DIR / "dist",
        CLIENT_DIR / "docs",
        CLIENT_DIR / ".openapi-generator",
    ])
    clean_paths([
        CLIENT_DIR / "README.md",
        CLIENT_DIR / ".gitignore",
        CLIENT_DIR / ".npmignore",
    ])
    print_success("Generated files cleaned")

    # 6. Run codegen
    print_step(5, "Running openapi-generator")
    run_codegen_openapi_generator(
        spec_path=SPEC_PATH,
        generator="typescript-fetch",
        output_dir=CLIENT_DIR,
        config_file=CONFIG_FILE,
    )

    # --- Past this point, failures are exit code 2, not 1 ---

    # 7. Apply patches
    print_step(6, "Applying patches")
    had_issues = patch_optional_extends(had_issues)
    had_issues = patch_missing_token_request(had_issues)
    print_success("Patches applied")

    # 8. Write config files (overwrite openapi-generator defaults)
    print_step(7, "Writing package.json and tsconfig.json")
    write_file(CLIENT_DIR / "package.json",
               PACKAGE_JSON.replace(_VERSION_PLACEHOLDER, spec_version))
    write_file(CLIENT_DIR / "tsconfig.json", TSCONFIG)
    write_file(CLIENT_DIR / "tsconfig.esm.json", TSCONFIG_ESM)
    print_success(f"Config files written (version {spec_version})")

    # 9. Restore custom files
    print_step(8, "Restoring custom files")
    restore_files(
        backup_dir=BACKUP_DIR,
        dest_dir=CLIENT_DIR,
        files=[".openapi-generator-ignore"],
        dirs=["developer"],
    )
    # Fix developer docs path (restore puts it at CLIENT_DIR/developer/)
    restored_dev = CLIENT_DIR / "developer"
    target_dev = CLIENT_DIR / "docs" / "developer"
    if restored_dev.is_dir():
        target_dev.parent.mkdir(parents=True, exist_ok=True)
        if target_dev.exists():
            shutil.rmtree(target_dev)
        restored_dev.rename(target_dev)
        print_success("  Moved developer/ to docs/developer/")

    # 10. Install dependencies
    print_step(9, "Installing dependencies")
    result = run_command(
        ["npm", "install", "--ignore-scripts"],
        cwd=CLIENT_DIR,
        error_context="npm install failed.\n  Check package.json for syntax errors.",
    )
    if result.returncode != 0:
        print_warning("npm install failed")
        had_issues = True
    else:
        print_success("Dependencies installed")

    # 11. Build (compile TypeScript)
    print_step(10, "Building TypeScript")
    build_result = run_command(
        ["npx", "tsc", "--noEmit"],
        cwd=CLIENT_DIR,
        capture=True,
        error_context="TypeScript compilation failed.",
    )
    (CLIENT_DIR / "build_output.log").write_text(build_result.stdout + build_result.stderr)
    if build_result.returncode == 0:
        print_success("TypeScript compilation succeeded (no errors)")
    else:
        print_warning("TypeScript compilation failed — see build_output.log")
        had_issues = True

    # Full build (emit dist/)
    if build_result.returncode == 0:
        dist_result = run_command(
            ["npm", "run", "build"],
            cwd=CLIENT_DIR,
            capture=True,
            error_context="npm run build failed.",
        )
        if dist_result.returncode == 0:
            print_success("Built dist/ successfully")
        else:
            print_warning("npm run build failed — see build_output.log")
            (CLIENT_DIR / "build_output.log").write_text(
                (CLIENT_DIR / "build_output.log").read_text()
                + "\n--- npm run build ---\n"
                + dist_result.stdout + dist_result.stderr
            )
            had_issues = True

    # 12. Report
    print_step(11, "Generating regeneration report")
    api_count = count_files(CLIENT_DIR / "src" / "apis", "*.ts")
    model_count = count_files(CLIENT_DIR / "src" / "models", "*.ts")

    report = generate_report("TMI TypeScript Client Regeneration Report", [
        {"heading": "Configuration", "content": (
            "- Package: @tmiclient/client\n"
            f"- Version: {spec_version}\n"
            "- Generator: openapi-generator 7.x (typescript-fetch)\n"
            "- Target: ES2022\n"
            "- HTTP Client: native fetch"
        )},
        {"heading": "Files Generated", "content": (
            f"- API classes: {api_count}\n"
            f"- Model classes: {model_count}"
        )},
        {"heading": "Patches Applied", "content": (
            "- Optional-extends fix (allOf child interfaces incorrectly "
            "mark inherited required properties as optional)\n"
            "- TokenRequest fix (AuthenticationApi references a model "
            "that openapi-generator does not generate)"
        )},
        {"heading": "Build Results", "content": (
            f"- TypeScript compilation: "
            f"{'PASS' if build_result.returncode == 0 else 'FAIL'}\n\n"
            "See build_output.log for details."
        )},
        {"heading": "Next Steps", "content": (
            "1. Review this report\n"
            "2. Check build_output.log for any issues\n"
            "3. Test against live API endpoints"
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
        "Client": "regenerated with openapi-generator (typescript-fetch)",
        "Target": "ES2022",
        "Build": "PASSED" if build_result.returncode == 0 else "FAILED",
        "Report": "REGENERATION_REPORT.md",
    })

    return 2 if had_issues else 0


if __name__ == "__main__":
    spec = sys.argv[1] if len(sys.argv) > 1 else None
    sys.exit(main(spec))
