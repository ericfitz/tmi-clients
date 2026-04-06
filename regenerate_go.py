#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Regenerate the TMI Go client from the OpenAPI spec."""
from __future__ import annotations

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
    patch_file_exact,
    patch_file_regex,
    print_banner,
    print_step,
    print_success,
    print_summary,
    print_warning,
    restore_files,
    run_codegen,
    run_command,
    update_json_version,
    write_file,
)

REPO_ROOT = Path(__file__).resolve().parent
CLIENT_DIR = REPO_ROOT / "go-client-generated"
CONFIG_FILE = CLIENT_DIR / "scripts" / "swagger-codegen-config.json"
SPEC_PATH = CLIENT_DIR / "tmi-openapi.json"
BACKUP_DIR = CLIENT_DIR / ".regeneration_backup"

GO_MODULE_PATH = "github.com/ericfitz/tmi-clients/go-client-generated"
GO_VERSION = "1.21"

FRESH_GO_MOD = f"""\
module {GO_MODULE_PATH}

go {GO_VERSION}

require (
\tgithub.com/antihax/optional v1.0.0
\tgolang.org/x/oauth2 v0.32.0
)
"""

REVOKE_TOKEN_OLD = """\t// body params
\tlocalVarPostBody = &body"""

REVOKE_TOKEN_NEW = """\t// form params
\tlocalVarFormParams.Add("token", parameterToString(token, ""))
\tlocalVarFormParams.Add("token_type_hint", parameterToString(tokenTypeHint, ""))
\tif clientId != "" {
\t\tlocalVarFormParams.Add("client_id", parameterToString(clientId, ""))
\t}
\tif clientSecret != "" {
\t\tlocalVarFormParams.Add("client_secret", parameterToString(clientSecret, ""))
\t}"""


def main(spec_path: str | None = None) -> int:
    had_issues = False

    # 1. Banner
    print_banner("TMI Go Client Regeneration", {
        "Package": "tmiclient",
        "Module": GO_MODULE_PATH,
        "Go": f"{GO_VERSION}+",
        "Dependencies": "Modern with security updates",
    })

    # 2. Prerequisites
    print_step(1, "Checking prerequisites")
    check_prerequisite("swagger-codegen", "brew install swagger-codegen")
    check_prerequisite("go", "brew install go")
    check_version("go", ["version"], GO_VERSION, r"go(\d+\.\d+)")
    print_success("All prerequisites met")

    # 3. Spec
    print_step(2, "Getting OpenAPI spec")
    if spec_path:
        copy_local_spec(Path(spec_path), SPEC_PATH)
    else:
        download_spec(DEFAULT_SPEC_URL, SPEC_PATH)

    # 3b. Extract version from spec and update codegen config
    spec_version = extract_spec_version(SPEC_PATH)
    update_json_version(CONFIG_FILE, "packageVersion", spec_version)

    # 4. Backup
    print_step(3, "Backing up custom files")
    # Glob test files and custom model files
    test_files = list(CLIENT_DIR.glob("*_test.go"))
    custom_models = [
        CLIENT_DIR / f for f in ("model_object.go", "model_cell_data.go", "model_model_map.go")
    ]
    backup_files(
        files=[
            CLIENT_DIR / "go.mod",
            CLIENT_DIR / "go.sum",
            CLIENT_DIR / ".swagger-codegen-ignore",
            *test_files,
            *custom_models,
        ],
        dirs=[CLIENT_DIR / "docs" / "developer"],
        backup_dir=BACKUP_DIR,
    )
    print_success("Custom files backed up")

    # 5. Clean
    print_step(4, "Cleaning generated files")
    # Clean glob patterns
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
    ])
    clean_paths(clean_list)
    print_success("Generated files cleaned")

    # 6. Run codegen
    print_step(5, "Running swagger-codegen")
    run_codegen(
        spec_path=SPEC_PATH,
        language="go",
        output_dir=CLIENT_DIR,
        config_file=CONFIG_FILE,
    )

    # --- Past this point, failures are exit code 2, not 1 ---

    # 7. Apply patches
    print_step(6, "Applying codegen patches")
    # RevokeToken: replace body params with form params (last occurrence)
    auth_file = CLIENT_DIR / "api_authentication.go"
    if auth_file.is_file():
        content = auth_file.read_text()
        idx = content.rfind(REVOKE_TOKEN_OLD)
        if idx >= 0:
            content = content[:idx] + REVOKE_TOKEN_NEW + content[idx + len(REVOKE_TOKEN_OLD):]
            auth_file.write_text(content)
            print_success("RevokeToken form params patch applied")
        else:
            print_warning(
                "RevokeToken patch did not match.\n"
                "  File: api_authentication.go\n"
                "  The generated code structure may have changed.\n"
                "  Look for the RevokeToken function and check its body params block."
            )
            had_issues = True
    else:
        print_warning("api_authentication.go not found — skipping RevokeToken patch")
        had_issues = True

    # 8. Patch/create go.mod
    print_step(7, "Updating go.mod")
    go_mod = CLIENT_DIR / "go.mod"
    if go_mod.is_file():
        patch_file_regex(go_mod, r"module .*", f"module {GO_MODULE_PATH}",
                         "go.mod module path")
        patch_file_regex(go_mod, r"go [\d.]+", f"go {GO_VERSION}",
                         "go.mod Go version")
    else:
        print_warning("go.mod not found after codegen — creating fresh one")
        write_file(go_mod, FRESH_GO_MOD)
        print_success("Created go.mod")

    # 9. Restore custom files (NOT go.mod/go.sum — those are for rollback reference only)
    print_step(8, "Restoring custom files")
    # Restore test files
    test_names = [f.name for f in test_files]
    custom_model_names = [f.name for f in custom_models]
    restore_files(
        backup_dir=BACKUP_DIR,
        dest_dir=CLIENT_DIR,
        files=[".swagger-codegen-ignore", *test_names, *custom_model_names],
        dirs=["developer"],  # restores to CLIENT_DIR/developer — need to handle docs/developer
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

    # 14. Summary
    print_summary({
        "Build": "SUCCESS" if build_result.returncode == 0 else "FAILED",
        "Tests": "PASSED" if test_result.returncode == 0 else "FAILED",
        "Report": "REGENERATION_REPORT.md",
    })

    return 2 if had_issues else 0


if __name__ == "__main__":
    spec = sys.argv[1] if len(sys.argv) > 1 else None
    sys.exit(main(spec))
