#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Regenerate the TMI Python client from the OpenAPI spec using openapi-generator."""
from __future__ import annotations

import re
import sys
from pathlib import Path

from regen_common import (
    DEFAULT_SPEC_URL,
    backup_files,
    check_prerequisite,
    clean_paths,
    copy_local_spec,
    count_files,
    download_spec,
    extract_spec_version,
    generate_report,
    print_banner,
    print_error,
    print_step,
    print_success,
    print_summary,
    print_warning,
    restore_files,
    run_codegen_openapi_generator,
    run_command,
    write_file,
)

REPO_ROOT = Path(__file__).resolve().parent
CLIENT_DIR = REPO_ROOT / "python-client-generated"
CONFIG_FILE = CLIENT_DIR / "scripts" / "openapi-generator-config.json"
SPEC_PATH = CLIENT_DIR / "tmi-openapi.json"
BACKUP_DIR = CLIENT_DIR / ".regeneration_backup"


# --- Patches ---


def patch_regex_validators(had_issues: bool) -> bool:
    """Fix openapi-generator bug: regex validators on non-string fields fail
    because Pydantic parses values to native types (UUID, datetime, etc.)
    before field validators run.

    The fix: insert a string conversion at the start of each validator
    function that applies re.match() to a value that may not be a string.
    Uses isoformat() for datetime objects and str() for everything else.
    """
    models_dir = CLIENT_DIR / "tmi_client" / "models"
    if not models_dir.is_dir():
        print_warning("Models directory not found — skipping regex validator patch")
        return True

    patched_count = 0
    conversion_line = "        value = value.isoformat() if hasattr(value, 'isoformat') else str(value)\n"

    for model_file in sorted(models_dir.glob("*.py")):
        content = model_file.read_text(encoding="utf-8")
        if "re.match" not in content:
            continue

        new_content = content
        # Find all @field_validator functions that use re.match
        pattern = (
            r"(@field_validator\('\w+'\)\s*\n"
            r"    def \w+\(cls, value\):\s*\n)"
            r"(        \"\"\".*?\"\"\"\s*\n)"
        )
        matches = list(re.finditer(pattern, new_content))
        # Process in reverse order so insert offsets don't shift
        for m in reversed(matches):
            # Check if this validator uses re.match
            rest = new_content[m.end():m.end() + 500]
            if "re.match" not in rest:
                continue

            # Insert string conversion after the docstring
            insert_point = m.end()
            if conversion_line not in new_content[insert_point:insert_point + 200]:
                new_content = new_content[:insert_point] + conversion_line + new_content[insert_point:]
                patched_count += 1

        if new_content != content:
            model_file.write_text(new_content, encoding="utf-8")

    if patched_count > 0:
        print_success(f"Regex validator patch: {patched_count} validators fixed")
    else:
        print_warning("Regex validator patch: no validators needed fixing")

    return had_issues


# --- Main ---


def main(spec_path: str | None = None) -> int:
    had_issues = False

    # 1. Banner
    print_banner("TMI Python Client Regeneration (openapi-generator)", {
        "Package": "tmi_client",
        "Python": "3.9+",
        "Generator": "openapi-generator 7.x",
        "Models": "Pydantic v2",
        "Testing": "pytest",
    })

    # 2. Prerequisites
    print_step(1, "Checking prerequisites")
    check_prerequisite("openapi-generator", "brew install openapi-generator")
    check_prerequisite("uv", "brew install uv")
    print_success("All prerequisites met")

    # 3. Download/copy spec
    print_step(2, "Getting OpenAPI spec")
    if spec_path:
        copy_local_spec(Path(spec_path), SPEC_PATH)
    else:
        download_spec(DEFAULT_SPEC_URL, SPEC_PATH)

    # 3b. Extract version from spec
    spec_version = extract_spec_version(SPEC_PATH)

    # 4. Backup
    print_step(3, "Backing up custom files")
    backup_files(
        files=[
            CLIENT_DIR / "test_diagram_fixes.py",
            CLIENT_DIR / ".openapi-generator-ignore",
        ],
        dirs=[],
        backup_dir=BACKUP_DIR,
    )
    print_success("Custom files backed up")

    # 5. Clean
    print_step(4, "Cleaning client directory")
    clean_paths([
        CLIENT_DIR / "tmi_client",
        CLIENT_DIR / "test",
        CLIENT_DIR / ".openapi-generator",
    ])
    # Clean docs/*.md but not docs/developer/
    docs_dir = CLIENT_DIR / "docs"
    if docs_dir.is_dir():
        for md in docs_dir.glob("*.md"):
            md.unlink()
    clean_paths([
        CLIENT_DIR / ".gitignore",
        CLIENT_DIR / ".travis.yml",
        CLIENT_DIR / "git_push.sh",
        CLIENT_DIR / "README.md",
    ])
    print_success("Client directory cleaned")

    # 6. Run codegen
    print_step(5, "Running openapi-generator")
    run_codegen_openapi_generator(
        spec_path=SPEC_PATH,
        generator="python",
        output_dir=CLIENT_DIR,
        config_file=CONFIG_FILE,
    )

    # --- Past this point, failures are exit code 2, not 1 ---

    # 7. Apply patches
    print_step(6, "Applying patches")
    had_issues = patch_regex_validators(had_issues)
    print_success("Patches applied")

    # 8. Restore custom files
    print_step(7, "Restoring custom files")
    restore_files(
        backup_dir=BACKUP_DIR,
        dest_dir=CLIENT_DIR,
        files=["test_diagram_fixes.py", ".openapi-generator-ignore"],
        dirs=[],
    )
    # Note: we do NOT restore pyproject.toml — openapi-generator produces
    # a good one with pydantic deps that we want to keep.

    # 9. Install deps
    print_step(8, "Installing dependencies")
    result = run_command(
        ["uv", "pip", "install", "-e", ".", "--quiet"],
        cwd=CLIENT_DIR,
        error_context="Failed to install Python client dependencies.\n  Check that uv is working and pyproject.toml is valid.",
    )
    if result.returncode != 0:
        print_warning("Dependency installation had issues")
        had_issues = True

    # 10. Run tests
    print_step(9, "Running tests")
    result = run_command(
        ["uv", "run", "--with", "pytest", "python3", "-m", "pytest", "test/", "-v", "--tb=short"],
        cwd=CLIENT_DIR,
        capture=True,
        error_context="Test execution failed.\n  Check test/ directory and dependencies.",
    )
    if result.returncode == 0:
        print_success("Auto-generated tests passed")
    else:
        print_warning("Some auto-generated tests failed — see test_output.log")
        had_issues = True
    (CLIENT_DIR / "test_output.log").write_text(result.stdout + result.stderr)

    # Integration test
    integration_test = CLIENT_DIR / "test_diagram_fixes.py"
    if integration_test.is_file():
        result = run_command(
            ["uv", "run", str(integration_test)],
            cwd=CLIENT_DIR,
            capture=True,
            error_context="Integration test failed.",
        )
        if result.returncode == 0:
            print_success("Integration test passed")
        else:
            print_warning("Integration test failed — see integration_test_output.log")
            had_issues = True
        (CLIENT_DIR / "integration_test_output.log").write_text(result.stdout + result.stderr)
    else:
        print_warning("Integration test file not found")

    # 11. Generate report
    print_step(10, "Generating summary report")
    api_count = count_files(CLIENT_DIR / "tmi_client" / "api", "*.py")
    model_count = count_files(CLIENT_DIR / "tmi_client" / "models", "*.py")
    test_count = count_files(CLIENT_DIR / "test", "*.py")

    report = generate_report("Python Client Regeneration Report", [
        {"heading": "Changes Applied", "content": (
            "### Client Regenerated\n"
            f"- Source: `{DEFAULT_SPEC_URL}`\n"
            "- Generator: openapi-generator 7.x\n"
            f"- Package: tmi_client v{spec_version}\n"
            "- Models: Pydantic v2 with full type hints\n\n"
            "### Patches Applied\n"
            "- Regex validator fix (openapi-generator bug: "
            "regex validators on non-string fields like UUID and datetime fail "
            "because Pydantic parses the value before the validator runs)\n\n"
            "### Generated Configuration\n"
            "- pyproject.toml with Pydantic v2 dependencies\n"
            "- Python 3.9+ requirement\n"
            "- pytest-based testing infrastructure\n"
            "- mypy configuration for type checking"
        )},
        {"heading": "Files Generated", "content": (
            f"- API classes: {api_count}\n"
            f"- Model classes: {model_count}\n"
            f"- Test files: {test_count}"
        )},
        {"heading": "Test Results", "content":
            "See test_output.log and integration_test_output.log for detailed test results."
        },
        {"heading": "Next Steps", "content": (
            "1. Review this report\n"
            "2. Check test_output.log for test failures\n"
            "3. Update documentation files\n"
            "4. Test against live API endpoints"
        )},
    ])
    write_file(CLIENT_DIR / "REGENERATION_REPORT.md", report)
    print_success("Summary report generated: REGENERATION_REPORT.md")

    # 12. Cleanup
    print_step(11, "Cleaning up")
    clean_paths([BACKUP_DIR])
    print_success("Cleanup complete")

    # 13. Summary
    print_summary({
        "Client": "regenerated with openapi-generator",
        "Models": "Pydantic v2 with type hints",
        "Patches": "regex validator fix" + (" (with warnings)" if had_issues else ""),
        "Tests": "see logs for results",
        "Report": "REGENERATION_REPORT.md",
    })

    return 2 if had_issues else 0


if __name__ == "__main__":
    spec = sys.argv[1] if len(sys.argv) > 1 else None
    sys.exit(main(spec))
