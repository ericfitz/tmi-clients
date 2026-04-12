#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Regenerate the TMI Go client from the OpenAPI spec using openapi-generator."""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

from regen_common import (
    backup_files,
    check_prerequisite,
    check_version,
    clean_paths,
    copy_local_spec,
    download_spec,
    extract_spec_version,
    generate_report,
    parse_regen_args,
    patch_file_regex,
    print_banner,
    print_step,
    print_success,
    print_summary,
    print_warning,
    resolve_spec_url,
    restore_files,
    run_codegen_openapi_generator,
    run_command,
    update_json_version,
    write_file,
)

REPO_ROOT = Path(__file__).resolve().parent
CLIENT_DIR = REPO_ROOT / "go-client-generated"
CONFIG_FILE = CLIENT_DIR / "scripts" / "openapi-generator-config.json"
SPEC_PATH = CLIENT_DIR / "tmi-openapi.json"
BACKUP_DIR = CLIENT_DIR / ".regeneration_backup"

GO_MODULE_PATH = "github.com/ericfitz/tmi-clients/go-client-generated"
GO_VERSION = "1.21"


# --- Patches ---


def patch_missing_time_import(had_issues: bool) -> bool:
    """Fix openapi-generator bug: missing 'time' import in Go files that use time.Time.

    Some generated constructors reference ``time.Time`` but the import block
    only includes ``encoding/json``, ``bytes``, and ``fmt``.
    """
    import re

    patched_count = 0
    for go_file in sorted(CLIENT_DIR.glob("model_*.go")):
        content = go_file.read_text(encoding="utf-8")
        if "time.Time" not in content:
            continue
        if '"time"' in content:
            continue
        # Add "time" to the import block
        new_content = re.sub(
            r'(import \(\n)',
            r'\1\t"time"\n',
            content,
        )
        if new_content != content:
            go_file.write_text(new_content, encoding="utf-8")
            patched_count += 1

    if patched_count > 0:
        print_success(f"Missing time import patch: {patched_count} files fixed")
    else:
        print_success("Missing time import patch: no files needed fixing")

    return had_issues


def patch_test_module_path(had_issues: bool) -> bool:
    """Fix openapi-generator bug: test stubs import GIT_USER_ID/GIT_REPO_ID.

    The Go generator hardcodes a placeholder module path in test files
    regardless of gitUserId/gitRepoId config.  Replace it with the real
    module path.
    """
    test_dir = CLIENT_DIR / "test"
    if not test_dir.is_dir():
        print_warning("Test directory not found — skipping test module path patch")
        return had_issues

    placeholder = "github.com/GIT_USER_ID/GIT_REPO_ID"
    patched_count = 0

    for test_file in sorted(test_dir.glob("*.go")):
        content = test_file.read_text(encoding="utf-8")
        if placeholder not in content:
            continue
        test_file.write_text(
            content.replace(placeholder, GO_MODULE_PATH), encoding="utf-8"
        )
        patched_count += 1

    if patched_count > 0:
        print_success(f"Test module path patch: {patched_count} files fixed")
    else:
        print_success("Test module path patch: no files needed fixing")

    return had_issues


def patch_json_literal_defaults(had_issues: bool) -> bool:
    """Fix openapi-generator bug: JSON literal defaults in Go constructors.

    openapi-generator emits default values like ``{"_metadata":[]}`` as Go code,
    which is invalid syntax.  Replace these with empty struct initialization.
    """
    import re

    pattern = re.compile(
        r'var (\w+) (\w+) = \{[^}]*\}'
    )
    patched_count = 0

    for go_file in sorted(CLIENT_DIR.glob("model_*.go")):
        content = go_file.read_text(encoding="utf-8")
        new_content, n = pattern.subn(r'var \1 \2', content)
        if n > 0:
            go_file.write_text(new_content, encoding="utf-8")
            patched_count += n

    if patched_count > 0:
        print_success(f"JSON literal defaults patch: {patched_count} occurrences fixed")
    else:
        print_success("JSON literal defaults patch: no occurrences found")

    return had_issues


def main(spec_path: str | None = None, branch: str | None = None) -> int:
    had_issues = False

    # 1. Banner
    print_banner("TMI Go Client Regeneration (openapi-generator)", {
        "Package": "tmiclient",
        "Module": GO_MODULE_PATH,
        "Go": f"{GO_VERSION}+",
        "Generator": "openapi-generator 7.x",
    })

    # 2. Prerequisites
    print_step(1, "Checking prerequisites")
    check_prerequisite("openapi-generator", "brew install openapi-generator")
    check_prerequisite("go", "brew install go")
    check_version("go", ["version"], GO_VERSION, r"go(\d+\.\d+)")
    print_success("All prerequisites met")

    # 3. Spec
    print_step(2, "Getting OpenAPI spec")
    if spec_path:
        copy_local_spec(Path(spec_path), SPEC_PATH)
    else:
        spec_url = resolve_spec_url(branch)
        download_spec(spec_url, SPEC_PATH)

    # 3b. Extract version from spec and update codegen config
    spec_version = extract_spec_version(SPEC_PATH)
    update_json_version(CONFIG_FILE, "packageVersion", spec_version)

    # 4. Backup
    print_step(3, "Backing up custom files")
    test_files = list(CLIENT_DIR.glob("*_test.go"))
    backup_files(
        files=[
            CLIENT_DIR / "go.mod",
            CLIENT_DIR / "go.sum",
            CLIENT_DIR / ".openapi-generator-ignore",
            *test_files,
        ],
        dirs=[CLIENT_DIR / "docs" / "developer"],
        backup_dir=BACKUP_DIR,
    )
    print_success("Custom files backed up")

    # 5. Clean
    print_step(4, "Cleaning generated files")
    clean_list: list[Path] = []
    for pattern in ("model_*.go", "api_*.go"):
        clean_list.extend(CLIENT_DIR.glob(pattern))
    clean_list.extend([
        CLIENT_DIR / "client.go",
        CLIENT_DIR / "configuration.go",
        CLIENT_DIR / "response.go",
        CLIENT_DIR / "utils.go",
        CLIENT_DIR / "api",
        CLIENT_DIR / "docs",
        CLIENT_DIR / "README.md",
        CLIENT_DIR / "git_push.sh",
        CLIENT_DIR / ".travis.yml",
        CLIENT_DIR / ".openapi-generator",
    ])
    clean_paths(clean_list)
    print_success("Generated files cleaned")

    # 6. Run codegen
    print_step(5, "Running openapi-generator")
    run_codegen_openapi_generator(
        spec_path=SPEC_PATH,
        generator="go",
        output_dir=CLIENT_DIR,
        config_file=CONFIG_FILE,
    )

    # --- Past this point, failures are exit code 2, not 1 ---

    # 7. Apply patches
    print_step(6, "Applying patches")
    had_issues = patch_json_literal_defaults(had_issues)
    had_issues = patch_missing_time_import(had_issues)
    had_issues = patch_test_module_path(had_issues)
    print_success("Patches applied")

    # 8. Patch go.mod (openapi-generator may use different module path / Go version)
    print_step(7, "Updating go.mod")
    go_mod = CLIENT_DIR / "go.mod"
    if go_mod.is_file():
        patch_file_regex(go_mod, r"module .*", f"module {GO_MODULE_PATH}",
                         "go.mod module path")
        patch_file_regex(go_mod, r"go [\d.]+", f"go {GO_VERSION}",
                         "go.mod Go version")
    else:
        print_warning("go.mod not found after codegen — creating fresh one")
        write_file(go_mod, (
            f"module {GO_MODULE_PATH}\n\n"
            f"go {GO_VERSION}\n"
        ))
        print_success("Created go.mod")

    # 9. Restore custom files
    print_step(8, "Restoring custom files")
    test_names = [f.name for f in test_files]
    restore_files(
        backup_dir=BACKUP_DIR,
        dest_dir=CLIENT_DIR,
        files=[".openapi-generator-ignore", *test_names],
        dirs=["developer"],
    )
    # Fix developer docs path (backup stores as "developer/", need it at "docs/developer/")
    restored_dev = CLIENT_DIR / "developer"
    target_dev = CLIENT_DIR / "docs" / "developer"
    if restored_dev.is_dir():
        target_dev.parent.mkdir(parents=True, exist_ok=True)
        if target_dev.exists():
            shutil.rmtree(target_dev)
        restored_dev.rename(target_dev)
        print_success("  Moved developer/ to docs/developer/")

    # 10. Go mod tidy
    print_step(9, "Running go mod tidy")
    result = run_command(
        ["go", "mod", "tidy"],
        cwd=CLIENT_DIR,
        error_context="go mod tidy failed.\n  Check go.mod for syntax errors.",
    )
    if result.returncode != 0:
        print_warning("go mod tidy failed")
        had_issues = True
    else:
        print_success("Dependencies tidied")

    # 11. Build & test
    print_step(10, "Verifying build")
    build_result = run_command(
        ["go", "build", "./..."],
        cwd=CLIENT_DIR,
        capture=True,
        error_context="go build failed.\n  Check build_output.log for details.",
    )
    (CLIENT_DIR / "build_output.log").write_text(build_result.stdout + build_result.stderr)
    if build_result.returncode == 0:
        print_success("Build successful")
    else:
        print_warning("Build failed — see build_output.log")
        had_issues = True

    print_step(11, "Running tests")
    test_result = run_command(
        ["go", "test", "-v", "./..."],
        cwd=CLIENT_DIR,
        capture=True,
        error_context="go test failed.",
    )
    (CLIENT_DIR / "test_output.log").write_text(test_result.stdout + test_result.stderr)
    if test_result.returncode == 0:
        print_success("All tests passed")
    else:
        print_warning("Some tests failed — see test_output.log")
        had_issues = True

    # Integration test
    if (CLIENT_DIR / "diagram_fixes_test.go").is_file():
        int_result = run_command(
            ["go", "test", "-v", "-run", "TestDiagramFixes"],
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

    # 12. Report
    print_step(12, "Generating regeneration report")
    model_count = len(list(CLIENT_DIR.glob("model_*.go")))
    api_count = len(list(CLIENT_DIR.glob("api_*.go")))

    report = generate_report("TMI Go Client Regeneration Report", [
        {"heading": "Configuration", "content": (
            f"- Package Name: tmiclient\n"
            f"- Module Path: {GO_MODULE_PATH}\n"
            f"- API Version: {spec_version}\n"
            f"- Go Version: {GO_VERSION}+\n"
            f"- Generator: openapi-generator 7.x\n"
            f"- Config File: {CONFIG_FILE}"
        )},
        {"heading": "Files Generated", "content": (
            f"- Model files: {model_count}\n"
            f"- API files: {api_count}"
        )},
        {"heading": "Build Results", "content": (
            f"- Build: {'PASS' if build_result.returncode == 0 else 'FAIL'}\n"
            f"- Tests: {'PASS' if test_result.returncode == 0 else 'FAIL'}\n\n"
            "See build_output.log and test_output.log for details."
        )},
        {"heading": "Next Steps", "content": (
            "1. Review this report\n"
            "2. Check build_output.log if build failed\n"
            "3. Run: go test -v ./..."
        )},
    ])
    write_file(CLIENT_DIR / "REGENERATION_REPORT.md", report)
    print_success("Regeneration report created: REGENERATION_REPORT.md")

    # 13. Cleanup
    print_step(13, "Cleaning up")
    clean_paths([BACKUP_DIR])
    print_success("Cleanup complete")

    # 13. Summary
    print_summary({
        "Client": "regenerated with openapi-generator",
        "Build": "SUCCESS" if build_result.returncode == 0 else "FAILED",
        "Tests": "PASSED" if test_result.returncode == 0 else "FAILED",
        "Report": "REGENERATION_REPORT.md",
    })

    return 2 if had_issues else 0


if __name__ == "__main__":
    args = parse_regen_args("Regenerate the TMI Go client from the OpenAPI spec.")
    sys.exit(main(spec_path=args.spec_path, branch=args.branch))
