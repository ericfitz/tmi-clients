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
    backup_files,
    check_prerequisite,
    clean_paths,
    copy_local_spec,
    count_files,
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
LANG_DIR = REPO_ROOT / "python-client-generated"
CONFIG_FILE = LANG_DIR / "scripts" / "openapi-generator-config.json"


# --- Patches ---


def patch_regex_validators(client_dir: Path, had_issues: bool) -> bool:
    """Fix openapi-generator bug: regex validators on non-string fields fail
    because Pydantic parses values to native types (UUID, datetime, etc.)
    before field validators run.

    The fix: insert a string conversion in each validator function that
    applies re.match() to a value that may not be a string.  Uses
    isoformat() for datetime objects and str() for everything else.

    For nullable optional fields the generator emits a None guard
    (``if value is None: return value``) before the re.match call.
    The conversion must be inserted *after* that guard so that
    ``str(None)`` doesn't defeat the check.
    """
    models_dir = client_dir / "tmi_client" / "models"
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

            # Insert string conversion after the docstring — but if a
            # None guard is present (nullable field), insert after it
            # so that str(None) doesn't defeat the check.
            insert_point = m.end()
            none_guard = re.match(
                r"        if value is None:\s*\n            return value\s*\n",
                rest,
            )
            if none_guard:
                insert_point += none_guard.end()

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


def patch_urllib3_minimum_version(client_dir: Path, had_issues: bool) -> bool:
    """Bump urllib3 minimum version to >=2.6.3 across all dependency files.

    openapi-generator defaults to urllib3 >= 2.1.0, but versions before 2.6.3
    have HIGH-severity CVEs (decompression-bomb bypass, unbounded decompression
    chain).  This patch updates pyproject.toml, setup.py, and requirements.txt.
    """
    min_version = "2.6.3"
    files_patched = 0

    for rel_path in ["pyproject.toml", "setup.py", "requirements.txt"]:
        filepath = client_dir / rel_path
        if not filepath.is_file():
            continue
        content = filepath.read_text(encoding="utf-8")
        # Match urllib3 version specifier in all formats:
        #   pyproject.toml / setup.py: "urllib3 (>=1.25.3,<3.0.0)"
        #   requirements.txt:          urllib3 >= 1.25.3
        # Replace the lower bound while preserving upper bound and format.
        new_content = re.sub(
            r'(urllib3\s*)\(?>=?\s*[\d.]+(,\s*<\s*[\d.]+)?\)?',
            lambda m: (
                f'{m.group(1)}(>={min_version}{m.group(2) or ""})'
                if '(' in m.group(0) or rel_path != "requirements.txt"
                else f'{m.group(1)}>= {min_version}'
            ),
            content,
        )
        if new_content != content:
            filepath.write_text(new_content, encoding="utf-8")
            files_patched += 1

    if files_patched > 0:
        print_success(f"urllib3 minimum version patch: {files_patched} files updated to >= {min_version}")
    else:
        print_success(f"urllib3 minimum version already >= {min_version}")

    return had_issues


def patch_test_return_types(client_dir: Path, had_issues: bool) -> bool:
    """Fix openapi-generator bug: generated test stubs declare a return type
    on make_instance() but the body is commented out, so the function always
    returns None.  Change the annotation to ``-> None`` so type checkers
    (ty, mypy) don't report invalid-return-type errors.
    """
    test_dir = client_dir / "test"
    if not test_dir.is_dir():
        print_warning("Test directory not found — skipping test return-type patch")
        return True

    patched_count = 0
    pattern = re.compile(
        r"def make_instance\(self, include_optional\) -> [A-Za-z0-9_]+:"
    )
    replacement = "def make_instance(self, include_optional) -> None:"

    for test_file in sorted(test_dir.glob("*.py")):
        content = test_file.read_text(encoding="utf-8")
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            test_file.write_text(new_content, encoding="utf-8")
            patched_count += n

    if patched_count > 0:
        print_success(f"Test return-type patch: {patched_count} methods fixed")
    else:
        print_warning("Test return-type patch: no methods needed fixing")

    return had_issues


def patch_oneof_return_types(client_dir: Path, had_issues: bool) -> bool:
    """Fix type annotations in oneOf model ``to_json``/``to_dict`` methods.

    openapi-generator produces ``to_json`` and ``to_dict`` methods that
    call ``self.actual_instance.to_json()`` / ``.to_dict()`` behind a
    ``hasattr`` guard.  Type checkers cannot narrow the type through
    ``hasattr``, so the return value is inferred as ``object`` instead
    of the declared return type.

    Fixes:
    - ``to_json``: wrap with ``str()`` (to_json always returns str)
    - ``to_dict``: suppress with ``# type: ignore[return-value]``
    """
    models_dir = client_dir / "tmi_client" / "models"
    if not models_dir.is_dir():
        return had_issues

    patched_count = 0
    for model_file in sorted(models_dir.glob("*.py")):
        content = model_file.read_text(encoding="utf-8")
        if "actual_instance" not in content:
            continue

        new_content = re.sub(
            r"return self\.actual_instance\.to_json\(\)$",
            "return str(self.actual_instance.to_json())",
            content,
            flags=re.MULTILINE,
        )
        new_content = re.sub(
            r"return self\.actual_instance\.to_dict\(\)$",
            "return self.actual_instance.to_dict()  # type: ignore[return-value]",
            new_content,
            flags=re.MULTILINE,
        )

        if new_content != content:
            model_file.write_text(new_content, encoding="utf-8")
            patched_count += 1

    if patched_count > 0:
        print_success(f"OneOf return-type patch: {patched_count} files fixed")
    else:
        print_warning("OneOf return-type patch: no files needed fixing")

    return had_issues


def patch_api_client_types(client_dir: Path, had_issues: bool) -> bool:
    """Fix type annotation issues in the generated api_client.py.

    openapi-generator produces three type-checker issues:
    1. ``response_types_map.get()`` called without a None guard
       (parameter is ``Optional[Dict]``)
    2. ``response_type`` passed to ``deserialize()`` as a generic
       type var instead of ``str``
    3. ``param_serialize`` return tuple doesn't match
       ``RequestSerialized`` alias due to intermediate reassignments
    """
    api_client = client_dir / "tmi_client" / "api_client.py"
    if not api_client.is_file():
        return had_issues

    content = api_client.read_text(encoding="utf-8")
    new_content = content

    # Fix 1: add None guard to response_types_map.get() calls
    new_content = re.sub(
        r"response_type = response_types_map\.get\(str\(response_data\.status\), None\)$",
        "response_type = response_types_map.get(str(response_data.status), None) if response_types_map is not None else None",
        new_content,
        count=1,
        flags=re.MULTILINE,
    )
    new_content = re.sub(
        r'response_type = response_types_map\.get\(str\(response_data\.status\)\[0\] \+ "XX", None\)$',
        'response_type = response_types_map.get(str(response_data.status)[0] + "XX", None) if response_types_map is not None else None',
        new_content,
        count=1,
        flags=re.MULTILINE,
    )

    # Fix 2: coerce response_type to str for deserialize()
    new_content = new_content.replace(
        "return_data = self.deserialize(response_text, response_type, content_type)",
        "return_data = self.deserialize(response_text, str(response_type), content_type)",
    )

    # Fix 3: suppress return-type mismatch on param_serialize tuple
    new_content = re.sub(
        r"return method, url, header_params, body, post_params$",
        "return method, url, header_params, body, post_params  # type: ignore[return-value]",
        new_content,
        count=1,
        flags=re.MULTILINE,
    )

    if new_content != content:
        api_client.write_text(new_content, encoding="utf-8")
        print_success("API client type annotation patch applied")
    else:
        print_warning("API client type annotation patch: no changes needed")

    return had_issues


def patch_configuration_self_type(client_dir: Path, had_issues: bool) -> bool:
    """Fix ``Self`` type annotation issues in configuration.py.

    openapi-generator types the ``_default`` class variable as
    ``ClassVar[Optional[Self]]``.  Type checkers track ``Self``
    per-method, so ``Self@set_default`` != ``Self@get_default`` !=
    the class-level ``Self``, causing assignment and return-type errors.

    Fix: change the class variable type to ``Optional["Configuration"]``
    and suppress the remaining return-type mismatch in ``get_default``.
    """
    config_file = client_dir / "tmi_client" / "configuration.py"
    if not config_file.is_file():
        return had_issues

    content = config_file.read_text(encoding="utf-8")
    new_content = content

    # Fix the ClassVar type to avoid Self scoping issues
    new_content = new_content.replace(
        "_default: ClassVar[Optional[Self]] = None",
        '_default: ClassVar[Optional["Configuration"]] = None',
    )

    # get_default returns cls._default which is Optional["Configuration"],
    # but the return type is Self — suppress the unavoidable mismatch
    new_content = re.sub(
        r"return cls\._default$",
        "return cls._default  # type: ignore[return-value]",
        new_content,
        count=1,
        flags=re.MULTILINE,
    )

    if new_content != content:
        config_file.write_text(new_content, encoding="utf-8")
        print_success("Configuration Self type patch applied")
    else:
        print_warning("Configuration Self type patch: no changes needed")

    return had_issues


# --- Main ---


def main(spec_path: str, output_dir: str | None = None) -> int:
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

    # 3. Extract version from spec and compute output directory
    print_step(2, "Getting OpenAPI spec")
    spec_version = extract_spec_version(Path(spec_path))

    if output_dir:
        client_dir = Path(output_dir)
    else:
        client_dir = LANG_DIR / f"v{spec_version}"

    client_dir.mkdir(parents=True, exist_ok=True)
    spec_dest = client_dir / "tmi-openapi.json"
    backup_dir = client_dir / ".regeneration_backup"

    copy_local_spec(Path(spec_path), spec_dest)

    # 3b. Update codegen config with spec version
    update_json_version(CONFIG_FILE, "packageVersion", spec_version)

    # 4. Backup
    print_step(3, "Backing up custom files")
    backup_files(
        files=[
            client_dir / "test_diagram_fixes.py",
            client_dir / ".openapi-generator-ignore",
        ],
        dirs=[],
        backup_dir=backup_dir,
    )
    print_success("Custom files backed up")

    # 5. Clean
    print_step(4, "Cleaning client directory")
    clean_paths([
        client_dir / "tmi_client",
        client_dir / "test",
        client_dir / ".openapi-generator",
    ])
    # Clean docs/*.md but not docs/developer/
    docs_dir = client_dir / "docs"
    if docs_dir.is_dir():
        for md in docs_dir.glob("*.md"):
            md.unlink()
    clean_paths([
        client_dir / ".gitignore",
        client_dir / ".travis.yml",
        client_dir / "git_push.sh",
        client_dir / "README.md",
    ])
    print_success("Client directory cleaned")

    # 6. Run codegen
    print_step(5, "Running openapi-generator")
    run_codegen_openapi_generator(
        spec_path=spec_dest,
        generator="python",
        output_dir=client_dir,
        config_file=CONFIG_FILE,
    )

    # --- Past this point, failures are exit code 2, not 1 ---

    # 6b. Stamp spec version into generated files
    print_step(6, "Stamping spec version into package files")
    patch_file_regex(
        client_dir / "pyproject.toml",
        r'^version = ".*"',
        f'version = "{spec_version}"',
        "pyproject.toml version",
    )
    patch_file_regex(
        client_dir / "setup.py",
        r'^VERSION = ".*"',
        f'VERSION = "{spec_version}"',
        "setup.py version",
    )

    # 7. Apply patches
    print_step(6, "Applying patches")
    had_issues = patch_regex_validators(client_dir, had_issues)
    had_issues = patch_test_return_types(client_dir, had_issues)
    had_issues = patch_urllib3_minimum_version(client_dir, had_issues)
    had_issues = patch_oneof_return_types(client_dir, had_issues)
    had_issues = patch_api_client_types(client_dir, had_issues)
    had_issues = patch_configuration_self_type(client_dir, had_issues)
    print_success("Patches applied")

    # 8. Restore custom files
    print_step(7, "Restoring custom files")
    restore_files(
        backup_dir=backup_dir,
        dest_dir=client_dir,
        files=["test_diagram_fixes.py", ".openapi-generator-ignore"],
        dirs=[],
    )
    # Note: we do NOT restore pyproject.toml — openapi-generator produces
    # a good one with pydantic deps that we want to keep.

    # 9. Install deps
    print_step(8, "Installing dependencies")
    result = run_command(
        ["uv", "pip", "install", "-e", ".", "--quiet"],
        cwd=client_dir,
        error_context="Failed to install Python client dependencies.\n  Check that uv is working and pyproject.toml is valid.",
    )
    if result.returncode != 0:
        print_warning("Dependency installation had issues")
        had_issues = True

    # 10. Run tests
    print_step(9, "Running tests")
    result = run_command(
        ["uv", "run", "--with", "pytest", "python3", "-m", "pytest", "test/", "-v", "--tb=short"],
        cwd=client_dir,
        capture=True,
        error_context="Test execution failed.\n  Check test/ directory and dependencies.",
    )
    if result.returncode == 0:
        print_success("Auto-generated tests passed")
    else:
        print_warning("Some auto-generated tests failed — see test_output.log")
        had_issues = True
    (client_dir / "test_output.log").write_text(result.stdout + result.stderr)

    # Integration test
    integration_test = client_dir / "test_diagram_fixes.py"
    if integration_test.is_file():
        result = run_command(
            ["uv", "run", str(integration_test)],
            cwd=client_dir,
            capture=True,
            error_context="Integration test failed.",
        )
        if result.returncode == 0:
            print_success("Integration test passed")
        else:
            print_warning("Integration test failed — see integration_test_output.log")
            had_issues = True
        (client_dir / "integration_test_output.log").write_text(result.stdout + result.stderr)
    else:
        print_warning("Integration test file not found")

    # 11. Generate report
    print_step(10, "Generating summary report")
    api_count = count_files(client_dir / "tmi_client" / "api", "*.py")
    model_count = count_files(client_dir / "tmi_client" / "models", "*.py")
    test_count = count_files(client_dir / "test", "*.py")

    report = generate_report("Python Client Regeneration Report", [
        {"heading": "Changes Applied", "content": (
            "### Client Regenerated\n"
            f"- Source spec: `{spec_path}`\n"
            "- Generator: openapi-generator 7.x\n"
            f"- Package: tmi_client v{spec_version}\n"
            "- Models: Pydantic v2 with full type hints\n\n"
            "### Patches Applied\n"
            "- Regex validator fix (openapi-generator bug: "
            "regex validators on non-string fields like UUID and datetime fail "
            "because Pydantic parses the value before the validator runs)\n"
            "- Test return-type fix (openapi-generator bug: "
            "make_instance() stubs declare a model return type but body is "
            "commented out, causing type-checker errors)\n"
            "- urllib3 minimum version bump to >= 2.6.3 "
            "(CVE fixes for decompression-bomb and redirect vulnerabilities)\n"
            "- OneOf model return-type fix (type checkers can't narrow "
            "through hasattr guards on actual_instance)\n"
            "- API client type annotation fix (None guards, str coercion, "
            "return-type suppression)\n"
            "- Configuration Self type fix (ClassVar[Optional[Self]] causes "
            "per-method Self scope conflicts)\n\n"
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
    write_file(client_dir / "REGENERATION_REPORT.md", report)
    print_success("Summary report generated: REGENERATION_REPORT.md")

    # 12. Cleanup
    print_step(11, "Cleaning up")
    clean_paths([backup_dir])
    print_success("Cleanup complete")

    # 13. Summary
    print_summary({
        "Client": "regenerated with openapi-generator",
        "Output": str(client_dir),
        "Models": "Pydantic v2 with type hints",
        "Patches": "regex validator fix" + (" (with warnings)" if had_issues else ""),
        "Tests": "see logs for results",
        "Report": "REGENERATION_REPORT.md",
    })

    return 2 if had_issues else 0


if __name__ == "__main__":
    args = parse_regen_args("Regenerate the TMI Python client from the OpenAPI spec.")
    sys.exit(main(spec_path=args.spec, output_dir=args.output_dir))
