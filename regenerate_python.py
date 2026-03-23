#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Regenerate the TMI Python client from the OpenAPI spec."""
from __future__ import annotations

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
    patch_file_exact,
    patch_file_regex,
    print_banner,
    print_error,
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
CLIENT_DIR = REPO_ROOT / "python-client-generated"
CONFIG_FILE = CLIENT_DIR / "scripts" / "swagger-codegen-config.json"
TEMPLATE_DIR = CLIENT_DIR / "custom-templates" / "python"
SPEC_PATH = CLIENT_DIR / "tmi-openapi.json"
BACKUP_DIR = CLIENT_DIR / ".regeneration_backup"

# --- Config file contents ---

# Version placeholder — replaced at regeneration time by extract_spec_version()
_VERSION_PLACEHOLDER = "0.0.0-dev"

PYPROJECT_TOML = """\
[project]
name = "tmi-client"
version = "0.0.0-dev"
description = "TMI API Python Client"
readme = "README.md"
requires-python = ">=3.9"
license = {text = "Apache-2.0"}
keywords = ["TMI", "Threat Modeling", "API", "OpenAPI"]
authors = [
    {name = "TMI Contributors"}
]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3.14",
]

dependencies = [
    "certifi >= 2025.11.12",
    "six >= 1.17.0",
    "python-dateutil >= 2.9.0.post0",
    "setuptools >= 78.1.1",
    "urllib3 >= 2.6.3",
]

[project.optional-dependencies]
test = [
    "pytest >= 8.3.5",
    "pytest-cov >= 5.0.0",
    "pytest-randomly >= 3.15.0",
]

[project.urls]
Homepage = "https://github.com/ericfitz/tmi-clients"
Repository = "https://github.com/ericfitz/tmi-clients"
Documentation = "https://github.com/ericfitz/tmi-clients/tree/main/python-client-generated"

[build-system]
requires = ["setuptools>=70.0.0", "wheel"]
build-backend = "setuptools.build_meta"

[tool.pytest.ini_options]
testpaths = ["test"]
python_files = "test_*.py"
python_classes = "Test*"
python_functions = "test_*"
addopts = "-v --strict-markers"

[tool.coverage.run]
source = ["tmi_client"]
omit = ["*/test/*", "*/tests/*"]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise AssertionError",
    "raise NotImplementedError",
    "if __name__ == .__main__.:",
]
"""

REQUIREMENTS_TXT = """\
certifi >= 2025.11.12
six >= 1.17.0
python-dateutil >= 2.9.0.post0
setuptools >= 78.1.1
urllib3 >= 2.6.3
"""

TEST_REQUIREMENTS_TXT = """\
pytest >= 8.3.5
pytest-cov >= 5.0.0
pytest-randomly >= 3.15.0
"""

TOX_INI = """\
[tox]
envlist = py39,py310,py311,py312,py313,py314

[testenv]
deps=-r{toxinidir}/requirements.txt
     -r{toxinidir}/test-requirements.txt

commands=
   pytest test/ -v --tb=short {posargs}
"""

AUTH_SETTINGS_OLD = """\
    def auth_settings(self):
        \"\"\"Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        \"\"\"
        return {
        }"""

AUTH_SETTINGS_NEW = """\
    def auth_settings(self):
        \"\"\"Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        \"\"\"
        auth = {}
        if 'bearerAuth' in self.api_key:
            auth['bearerAuth'] = {
                'type': 'api_key',
                'in': 'header',
                'key': 'Authorization',
                'value': self.get_api_key_with_prefix('bearerAuth')
            }
        return auth"""


# --- Patches ---

def apply_constructor_patch(file_path: Path, parent_class: str, param_name: str, description: str) -> bool:
    """Insert kwargs[param_name] = param_name before ParentClass.__init__ call."""
    return patch_file_regex(
        file_path,
        pattern=rf"(        ){parent_class}\.__init__\(self",
        replacement=rf"\1kwargs['{param_name}'] = {param_name}  # PATCH: Pass {param_name} to parent to prevent overwrite\n\1{parent_class}.__init__(self",
        description=description,
    )


def apply_patches(had_issues: bool) -> bool:
    """Apply all Python client patches. Returns updated had_issues flag."""
    models = CLIENT_DIR / "tmi_client" / "models"

    # 1. DfdDiagram constructor
    if not apply_constructor_patch(
        models / "dfd_diagram.py", "BaseDiagram", "type",
        "DfdDiagram constructor type preservation",
    ):
        had_issues = True

    # 2. DfdDiagramInput constructor
    if not apply_constructor_patch(
        models / "dfd_diagram_input.py", "BaseDiagramInput", "type",
        "DfdDiagramInput constructor type preservation",
    ):
        had_issues = True

    # 3. Edge constructor
    if not apply_constructor_patch(
        models / "edge.py", "Cell", "shape",
        "Edge constructor shape preservation",
    ):
        had_issues = True

    # 4. Node constructor
    if not apply_constructor_patch(
        models / "node.py", "Cell", "shape",
        "Node constructor shape preservation",
    ):
        had_issues = True

    # 5. Configuration.auth_settings()
    if not patch_file_exact(
        CLIENT_DIR / "tmi_client" / "configuration.py",
        AUTH_SETTINGS_OLD,
        AUTH_SETTINGS_NEW,
        "Configuration.auth_settings() bearerAuth implementation",
    ):
        had_issues = True

    # 6. Remove duplicate revoke_token methods (swagger-codegen bug)
    # Codegen generates two pairs: form-params-based (token, token_type_hint, ...)
    # and body-based (body). The body-based version is correct; the form-params
    # version is dead code that references the overwritten signature.
    auth_api = CLIENT_DIR / "tmi_client" / "api" / "authentication_api.py"
    if auth_api.is_file():
        import re as _re
        content = auth_api.read_text()
        # Remove the first revoke_token(self, token, token_type_hint, ...) and its
        # companion revoke_token_with_http_info(self, token, token_type_hint, ...)
        # by matching from the form-params def up to (but not including) the
        # body-based def revoke_token(self, body, ...).
        new_content = _re.sub(
            r'    def revoke_token\(self, token, token_type_hint.*?(?=    def revoke_token\(self, body)',
            '',
            content,
            count=1,
            flags=_re.DOTALL,
        )
        if new_content != content:
            auth_api.write_text(new_content)
            print_success("  Removed duplicate revoke_token form-params methods (codegen bug)")
        else:
            print_warning(
                "Duplicate revoke_token patch did not match.\n"
                "  File: authentication_api.py\n"
                "  The codegen may no longer produce duplicate methods."
            )

    return had_issues


def patch_setup_py(had_issues: bool) -> bool:
    """Patch setup.py for Python 3.9+ and modern deps."""
    setup_py = CLIENT_DIR / "setup.py"
    if not setup_py.is_file():
        print_warning("setup.py not found — skipping patches")
        return had_issues

    patches = [
        (r'python_requires="[^"]*"', 'python_requires=">=3.9"'),
        (r'"certifi[^"]*"', '"certifi>=2025.11.12"'),
        (r'"six[^"]*"', '"six>=1.17.0"'),
        (r'"python-dateutil[^"]*"', '"python-dateutil>=2.9.0.post0"'),
        (r'"urllib3[^"]*"', '"urllib3>=2.6.3"'),
    ]
    for pattern, replacement in patches:
        patch_file_regex(setup_py, pattern, replacement, f"setup.py: {replacement}")

    # Update setuptools if present
    patch_file_regex(setup_py, r'"setuptools[^"]*"', '"setuptools>=78.1.1"',
                     "setup.py: setuptools version")

    print_success("setup.py updated for Python 3.9+")
    return had_issues


# --- Main ---

def main(spec_path: str | None = None) -> int:
    had_issues = False

    # 1. Banner
    print_banner("TMI Python Client Regeneration", {
        "Package": "tmi_client",
        "Python": "3.9+",
        "Dependencies": "Modern with CVE fixes",
        "Testing": "pytest",
    })

    # 2. Prerequisites
    print_step(1, "Checking prerequisites")
    check_prerequisite("swagger-codegen", "brew install swagger-codegen")
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
            CLIENT_DIR / "pyproject.toml",
            CLIENT_DIR / "test_diagram_fixes.py",
            CLIENT_DIR / ".swagger-codegen-ignore",
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
    ])
    # Clean docs/*.md but not docs/developer/
    for md in (CLIENT_DIR / "docs").glob("*.md"):
        md.unlink()
    clean_paths([
        CLIENT_DIR / ".gitignore",
        CLIENT_DIR / ".travis.yml",
        CLIENT_DIR / "git_push.sh",
        CLIENT_DIR / "README.md",
    ])
    print_success("Client directory cleaned")

    # 6. Run codegen
    print_step(5, "Running swagger-codegen")
    run_codegen(
        spec_path=SPEC_PATH,
        language="python",
        output_dir=CLIENT_DIR,
        config_file=CONFIG_FILE,
        template_dir=TEMPLATE_DIR,
    )

    # --- Past this point, failures are exit code 2, not 1 ---

    # 7. Apply patches
    print_step(6, "Applying constructor patches")
    had_issues = apply_patches(had_issues)
    print_success("Constructor patches applied")

    # 8. Write config files
    print_step(7, "Applying modern Python 3.x configuration")
    write_file(CLIENT_DIR / "pyproject.toml",
               PYPROJECT_TOML.replace(_VERSION_PLACEHOLDER, spec_version))
    print_success(f"pyproject.toml created (version {spec_version})")

    had_issues = patch_setup_py(had_issues)

    write_file(CLIENT_DIR / "requirements.txt", REQUIREMENTS_TXT)
    print_success("requirements.txt updated")

    write_file(CLIENT_DIR / "test-requirements.txt", TEST_REQUIREMENTS_TXT)
    print_success("test-requirements.txt updated")

    write_file(CLIENT_DIR / "tox.ini", TOX_INI)
    print_success("tox.ini updated")

    # 9. Restore custom files (pyproject.toml from backup overwrites the one just written)
    print_step(8, "Restoring custom files")
    restore_files(
        backup_dir=BACKUP_DIR,
        dest_dir=CLIENT_DIR,
        files=["pyproject.toml", "test_diagram_fixes.py", ".swagger-codegen-ignore"],
        dirs=[],
    )

    # 10. Install deps
    print_step(9, "Installing dependencies")
    result = run_command(
        ["uv", "pip", "install", "-e", ".", "--quiet"],
        cwd=CLIENT_DIR,
        error_context="Failed to install Python client dependencies.\n  Check that uv is working and pyproject.toml is valid.",
    )
    if result.returncode != 0:
        print_warning("Dependency installation had issues")
        had_issues = True

    # 11. Run tests
    print_step(10, "Running tests")
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

    # 12. Generate report
    print_step(11, "Generating summary report")
    api_count = count_files(CLIENT_DIR / "tmi_client" / "api", "*.py")
    model_count = count_files(CLIENT_DIR / "tmi_client" / "models", "*.py")
    test_count = count_files(CLIENT_DIR / "test", "*.py")

    report = generate_report("Python Client Regeneration Report", [
        {"heading": "Changes Applied", "content": (
            "### Client Regenerated\n"
            f"- Source: `{DEFAULT_SPEC_URL}`\n"
            "- Generator: swagger-codegen 3.0.75\n"
            f"- Package: tmi_client v{spec_version}\n\n"
            "### Constructor Patches Applied\n"
            "- DfdDiagram constructor fixed (type parameter preservation)\n"
            "- DfdDiagramInput constructor fixed (type parameter preservation)\n"
            "- Edge constructor fixed (shape parameter preservation)\n"
            "- Node constructor fixed (shape parameter preservation)\n"
            "- Configuration.auth_settings() fixed (bearerAuth implementation)\n\n"
            "### Modern Python Configuration\n"
            "- Python 3.9+ requirement\n"
            "- Updated dependencies (latest Python 3.9+ compatible versions)\n"
            "- pyproject.toml with UV support\n"
            "- pytest-based testing infrastructure"
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
            "4. Test webhook endpoints"
        )},
    ])
    write_file(CLIENT_DIR / "REGENERATION_REPORT.md", report)
    print_success("Summary report generated: REGENERATION_REPORT.md")

    # 13. Cleanup
    print_step(12, "Cleaning up")
    clean_paths([BACKUP_DIR])
    print_success("Cleanup complete")

    # 14. Summary
    print_summary({
        "Client": "regenerated from latest OpenAPI spec",
        "Patches": "applied" if not had_issues else "applied with warnings",
        "Tests": "see logs for results",
        "Report": "REGENERATION_REPORT.md",
    })

    return 2 if had_issues else 0


if __name__ == "__main__":
    spec = sys.argv[1] if len(sys.argv) > 1 else None
    sys.exit(main(spec))
