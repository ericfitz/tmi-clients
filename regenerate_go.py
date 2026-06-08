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
    extract_spec_version,
    generate_report,
    parse_regen_args,
    patch_file_regex,
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
LANG_DIR = REPO_ROOT / "go-client-generated"
CONFIG_FILE = LANG_DIR / "scripts" / "openapi-generator-config.json"

GO_VERSION = "1.23"


def _go_version_dir(version: str) -> str:
    """Convert a dotted version like ``1.4.0`` to a Go-safe directory name like ``v1_4_0``.

    Go's module system rejects path elements matching a dotted version pattern
    (e.g. ``v1.4.0``) unless they are a major-version suffix (``/v2``, ``/v3``).
    """
    return f"v{version.replace('.', '_')}"


# --- Patches ---


def patch_missing_time_import(client_dir: Path, had_issues: bool) -> bool:
    """Fix openapi-generator bug: missing 'time' import in Go files that use time.Time.

    Some generated constructors reference ``time.Time`` but the import block
    only includes ``encoding/json``, ``bytes``, and ``fmt``.
    """
    import re

    patched_count = 0
    for go_file in sorted(client_dir.glob("model_*.go")):
        content = go_file.read_text(encoding="utf-8")
        if "time.Time" not in content:
            continue
        if '"time"' in content:
            continue
        # Add "time" to the import block
        new_content = re.sub(
            r"(import \(\n)",
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


def patch_test_module_path(
    client_dir: Path, go_module_path: str, had_issues: bool
) -> bool:
    """Fix openapi-generator bug: test stubs may use the wrong import path.

    The Go generator builds the ``openapiclient`` import from the
    ``gitUserId``/``gitRepoId`` config values, which historically omitted the
    versioned subdirectory (e.g. ``.../go-client-generated`` instead of
    ``.../go-client-generated/v1_4_0``).  Some generator versions already emit
    the correct path.

    We normalize the whole quoted import path rather than doing a naive
    substring replace: the old approach replaced a placeholder that is a
    *prefix* of the real module path, which doubled an already-correct import
    (``.../v1_4_0/v1_4_0/...``).  Matching the entire quoted path makes this
    idempotent — files already importing ``go_module_path`` are left alone.
    """
    import re

    test_dir = client_dir / "test"
    if not test_dir.is_dir():
        print_warning("Test directory not found — skipping test module path patch")
        return had_issues

    # Match: openapiclient "github.com/ericfitz/tmi-clients/...<anything>"
    # and rewrite the quoted path to exactly go_module_path.
    import_re = re.compile(
        r'(openapiclient\s+")github\.com/ericfitz/tmi-clients[^"]*(")'
    )
    replacement = rf"\g<1>{go_module_path}\g<2>"
    patched_count = 0

    for test_file in sorted(test_dir.glob("*.go")):
        content = test_file.read_text(encoding="utf-8")
        new_content = import_re.sub(replacement, content)
        if new_content != content:
            test_file.write_text(new_content, encoding="utf-8")
            patched_count += 1

    if patched_count > 0:
        print_success(f"Test module path patch: {patched_count} files fixed")
    else:
        print_success("Test module path patch: no files needed fixing")

    return had_issues


def patch_json_literal_defaults(client_dir: Path, had_issues: bool) -> bool:
    """Fix openapi-generator bug: JSON literal defaults in Go constructors.

    openapi-generator emits default values like ``{"_metadata":[]}`` as Go code,
    which is invalid syntax.  Replace these with empty struct initialization.
    """
    import re

    pattern = re.compile(r"var (\w+) (\w+) = \{[^}]*\}")
    patched_count = 0

    for go_file in sorted(client_dir.glob("model_*.go")):
        content = go_file.read_text(encoding="utf-8")
        new_content, n = pattern.subn(r"var \1 \2", content)
        if n > 0:
            go_file.write_text(new_content, encoding="utf-8")
            patched_count += n

    if patched_count > 0:
        print_success(f"JSON literal defaults patch: {patched_count} occurrences fixed")
    else:
        print_success("JSON literal defaults patch: no occurrences found")

    return had_issues


def patch_embedded_pointer_assignment(client_dir: Path, had_issues: bool) -> bool:
    """Fix openapi-generator bug: wrapper constructors assign a value to an
    embedded pointer field.

    A thin allOf wrapper (e.g. ``Diagram`` embeds ``DfdDiagram``) gets a
    constructor that takes ``type_ string`` and runs ``this.Type = type_``.
    But the embedded ``DfdDiagram.Type`` is ``*string`` (optional/omitempty),
    so the assignment fails to compile:

        cannot use type_ (variable of type string) as *string value

    The generator does not insert the address-of for the embedded pointer.
    Detect constructors whose parameter is ``type_ string`` and whose body
    assigns ``this.Type = type_``, and rewrite the assignment to take the
    address (``this.Type = &type_``).
    """
    import re

    # The distinguishing feature of the broken wrapper: it assigns
    # `this.Type = type_` but its OWN struct declares no `Type` field — so
    # `this.Type` resolves to an *embedded* struct's `Type *string`, and the
    # plain-string assignment is a pointer mismatch.
    #
    # Models that declare their own `Type string` (the common case) are correct
    # and must NOT be touched, or we would break a valid assignment. We gate on
    # the absence of an own `Type` field declaration.
    assign_re = re.compile(r"^(\tthis\.Type = )type_$", re.MULTILINE)
    own_type_field = re.compile(r"^\tType \*?string\b", re.MULTILINE)
    patched_count = 0

    for go_file in sorted(client_dir.glob("model_*.go")):
        content = go_file.read_text(encoding="utf-8")
        if not assign_re.search(content):
            continue
        if own_type_field.search(content):
            # Has its own Type field -> assignment is already correct.
            continue
        new_content, n = assign_re.subn(r"\1&type_", content)
        if n > 0:
            go_file.write_text(new_content, encoding="utf-8")
            patched_count += n

    if patched_count > 0:
        print_success(
            f"Embedded pointer assignment patch: {patched_count} constructors fixed"
        )
    else:
        print_success("Embedded pointer assignment patch: no constructors needed fixing")

    return had_issues


def main(spec_path: str, output_dir: str | None = None) -> int:
    had_issues = False

    # 1. Extract version from spec and compute output directory
    spec_version = extract_spec_version(Path(spec_path))

    version_dir = _go_version_dir(spec_version)
    go_module_path = (
        f"github.com/ericfitz/tmi-clients/go-client-generated/{version_dir}"
    )

    if output_dir:
        client_dir = Path(output_dir)
    else:
        client_dir = LANG_DIR / version_dir

    client_dir.mkdir(parents=True, exist_ok=True)
    spec_dest = client_dir / "tmi-openapi.json"
    backup_dir = client_dir / ".regeneration_backup"

    # 2. Banner
    print_banner(
        "TMI Go Client Regeneration (openapi-generator)",
        {
            "Package": "tmiclient",
            "Module": go_module_path,
            "Go": f"{GO_VERSION}+",
            "Generator": "openapi-generator 7.x",
        },
    )

    # 3. Prerequisites
    print_step(1, "Checking prerequisites")
    check_prerequisite("openapi-generator", "brew install openapi-generator")
    check_prerequisite("go", "brew install go")
    check_version("go", ["version"], GO_VERSION, r"go(\d+\.\d+)")
    print_success("All prerequisites met")

    # 4. Spec
    print_step(2, "Getting OpenAPI spec")
    copy_local_spec(Path(spec_path), spec_dest)

    # 4b. Update codegen config with spec version
    update_json_version(CONFIG_FILE, "packageVersion", spec_version)

    # 5. Backup
    print_step(3, "Backing up custom files")
    test_files = list(client_dir.glob("*_test.go"))
    backup_files(
        files=[
            client_dir / "go.mod",
            client_dir / "go.sum",
            client_dir / ".openapi-generator-ignore",
            *test_files,
        ],
        dirs=[client_dir / "docs" / "developer"],
        backup_dir=backup_dir,
    )
    print_success("Custom files backed up")

    # 6. Clean
    print_step(4, "Cleaning generated files")
    clean_list: list[Path] = []
    for pat in ("model_*.go", "api_*.go"):
        clean_list.extend(client_dir.glob(pat))
    clean_list.extend(
        [
            client_dir / "client.go",
            client_dir / "configuration.go",
            client_dir / "response.go",
            client_dir / "utils.go",
            client_dir / "api",
            client_dir / "docs",
            client_dir / "README.md",
            client_dir / "git_push.sh",
            client_dir / ".travis.yml",
            client_dir / ".openapi-generator",
        ]
    )
    clean_paths(clean_list)
    print_success("Generated files cleaned")

    # 7. Run codegen
    print_step(5, "Running openapi-generator")
    run_codegen_openapi_generator(
        spec_path=spec_dest,
        generator="go",
        output_dir=client_dir,
        config_file=CONFIG_FILE,
    )

    # --- Past this point, failures are exit code 2, not 1 ---

    # 8. Apply patches
    print_step(6, "Applying patches")
    had_issues = patch_json_literal_defaults(client_dir, had_issues)
    had_issues = patch_missing_time_import(client_dir, had_issues)
    had_issues = patch_embedded_pointer_assignment(client_dir, had_issues)
    had_issues = patch_test_module_path(client_dir, go_module_path, had_issues)
    print_success("Patches applied")

    # 9. Patch go.mod (openapi-generator may use different module path / Go version)
    print_step(7, "Updating go.mod")
    go_mod = client_dir / "go.mod"
    if go_mod.is_file():
        patch_file_regex(
            go_mod, r"module .*", f"module {go_module_path}", "go.mod module path"
        )
        patch_file_regex(go_mod, r"go [\d.]+", f"go {GO_VERSION}", "go.mod Go version")
    else:
        print_warning("go.mod not found after codegen — creating fresh one")
        write_file(go_mod, (f"module {go_module_path}\n\ngo {GO_VERSION}\n"))
        print_success("Created go.mod")

    # 10. Restore custom files
    print_step(8, "Restoring custom files")
    test_names = [f.name for f in test_files]
    restore_files(
        backup_dir=backup_dir,
        dest_dir=client_dir,
        files=[".openapi-generator-ignore", *test_names],
        dirs=["developer"],
    )
    # Fix developer docs path (backup stores as "developer/", need it at "docs/developer/")
    restored_dev = client_dir / "developer"
    target_dev = client_dir / "docs" / "developer"
    if restored_dev.is_dir():
        target_dev.parent.mkdir(parents=True, exist_ok=True)
        if target_dev.exists():
            shutil.rmtree(target_dev)
        restored_dev.rename(target_dev)
        print_success("  Moved developer/ to docs/developer/")

    # 11. Go mod tidy
    print_step(9, "Running go mod tidy")
    result = run_command(
        ["go", "mod", "tidy"],
        cwd=client_dir,
        error_context="go mod tidy failed.\n  Check go.mod for syntax errors.",
    )
    if result.returncode != 0:
        print_warning("go mod tidy failed")
        had_issues = True
    else:
        print_success("Dependencies tidied")

    # 12. Build & test
    print_step(10, "Verifying build")
    build_result = run_command(
        ["go", "build", "./..."],
        cwd=client_dir,
        capture=True,
        error_context="go build failed.\n  Check build_output.log for details.",
    )
    (client_dir / "build_output.log").write_text(
        build_result.stdout + build_result.stderr
    )
    if build_result.returncode == 0:
        print_success("Build successful")
    else:
        print_warning("Build failed — see build_output.log")
        had_issues = True

    print_step(11, "Running tests")
    test_result = run_command(
        ["go", "test", "-v", "./..."],
        cwd=client_dir,
        capture=True,
        error_context="go test failed.",
    )
    (client_dir / "test_output.log").write_text(test_result.stdout + test_result.stderr)
    if test_result.returncode == 0:
        print_success("All tests passed")
    else:
        print_warning("Some tests failed — see test_output.log")
        had_issues = True

    # Integration test
    if (client_dir / "diagram_fixes_test.go").is_file():
        int_result = run_command(
            ["go", "test", "-v", "-run", "TestDiagramFixes"],
            cwd=client_dir,
            capture=True,
        )
        (client_dir / "integration_test_output.log").write_text(
            int_result.stdout + int_result.stderr
        )
        if int_result.returncode == 0:
            print_success("Integration tests passed")
        else:
            print_warning("Integration tests failed — see integration_test_output.log")
            had_issues = True

    # 13. Report
    print_step(12, "Generating regeneration report")
    model_count = len(list(client_dir.glob("model_*.go")))
    api_count = len(list(client_dir.glob("api_*.go")))

    report = generate_report(
        "TMI Go Client Regeneration Report",
        [
            {
                "heading": "Configuration",
                "content": (
                    f"- Package Name: tmiclient\n"
                    f"- Module Path: {go_module_path}\n"
                    f"- API Version: {spec_version}\n"
                    f"- Go Version: {GO_VERSION}+\n"
                    f"- Generator: openapi-generator 7.x\n"
                    f"- Config File: {CONFIG_FILE}"
                ),
            },
            {
                "heading": "Files Generated",
                "content": (f"- Model files: {model_count}\n- API files: {api_count}"),
            },
            {
                "heading": "Build Results",
                "content": (
                    f"- Build: {'PASS' if build_result.returncode == 0 else 'FAIL'}\n"
                    f"- Tests: {'PASS' if test_result.returncode == 0 else 'FAIL'}\n\n"
                    "See build_output.log and test_output.log for details."
                ),
            },
            {
                "heading": "Next Steps",
                "content": (
                    "1. Review this report\n"
                    "2. Check build_output.log if build failed\n"
                    "3. Run: go test -v ./..."
                ),
            },
        ],
    )
    write_file(client_dir / "REGENERATION_REPORT.md", report)
    print_success("Regeneration report created: REGENERATION_REPORT.md")

    # 14. Cleanup
    print_step(13, "Cleaning up")
    clean_paths([backup_dir])
    print_success("Cleanup complete")

    # 15. Summary
    print_summary(
        {
            "Client": "regenerated with openapi-generator",
            "Output": str(client_dir),
            "Build": "SUCCESS" if build_result.returncode == 0 else "FAILED",
            "Tests": "PASSED" if test_result.returncode == 0 else "FAILED",
            "Report": "REGENERATION_REPORT.md",
        }
    )

    return 2 if had_issues else 0


if __name__ == "__main__":
    args = parse_regen_args("Regenerate the TMI Go client from the OpenAPI spec.")
    sys.exit(main(spec_path=args.spec, output_dir=args.output_dir))
