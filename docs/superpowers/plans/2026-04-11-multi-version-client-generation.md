# Multi-Version Client Generation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enable generating and maintaining three concurrent API versions of each client (Python, Go, TypeScript) in versioned subdirectories, driven by a `versions.json` config.

**Architecture:** A `versions.json` file at the repo root declares which three API versions to maintain. A new orchestrator script (`regenerate_all.py`) reads this config, downloads specs, and invokes the existing per-language regen scripts. Each per-language script is refactored to accept a `--spec` flag (path to a local spec file), derive its output directory from the spec version, and write into `{language}-client-generated/v{version}/`.

**Tech Stack:** Python 3.9+ (regen scripts), openapi-generator 7.x, swagger-codegen 3.x (Go only via openapi-generator now), uv, Go 1.21+, Node.js 18+, TypeScript 5.x

**Spec:** `docs/superpowers/specs/2026-04-11-multi-version-client-generation-design.md`

---

### Task 1: Update `regen_common.py` CLI parsing and add tag URL helper

**Files:**
- Modify: `regen_common.py:17-51` (URL template, `parse_regen_args`, `resolve_spec_url`)
- Test: manual — run `python3 -c "from regen_common import ..."` to verify imports

- [ ] **Step 1: Write a test script to verify the new CLI parsing**

Create `test_regen_common_cli.py`:

```python
#!/usr/bin/env python3
"""Test that regen_common CLI parsing and URL helpers work correctly."""
import sys
from unittest.mock import patch

# Test spec_url_for_tag
from regen_common import spec_url_for_tag
url = spec_url_for_tag("v1.3.0")
assert "refs/tags/v1.3.0" in url, f"Expected tags URL, got: {url}"
print(f"PASS: spec_url_for_tag('v1.3.0') -> {url}")

# Test parse_regen_args with --spec
with patch("sys.argv", ["test", "--spec", "/tmp/spec.json"]):
    from regen_common import parse_regen_args
    args = parse_regen_args("test")
    assert args.spec == "/tmp/spec.json", f"Expected /tmp/spec.json, got: {args.spec}"
    assert args.output_dir is None, f"Expected None, got: {args.output_dir}"
    print(f"PASS: --spec parsed correctly")

# Test parse_regen_args with --spec and --output-dir
with patch("sys.argv", ["test", "--spec", "/tmp/spec.json", "--output-dir", "/tmp/out"]):
    args = parse_regen_args("test")
    assert args.output_dir == "/tmp/out", f"Expected /tmp/out, got: {args.output_dir}"
    print(f"PASS: --output-dir parsed correctly")

# Test parse_regen_args without --spec should fail
with patch("sys.argv", ["test"]):
    try:
        args = parse_regen_args("test")
        print("FAIL: should have required --spec")
        sys.exit(1)
    except SystemExit as e:
        if e.code == 2:
            print("PASS: --spec is required")
        else:
            raise

print("\nAll tests passed!")
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 test_regen_common_cli.py`
Expected: ImportError or AttributeError because `spec_url_for_tag` and new `parse_regen_args` don't exist yet.

- [ ] **Step 3: Implement the changes to `regen_common.py`**

In `regen_common.py`, make these changes:

**Add `_TAG_URL_TEMPLATE` and `spec_url_for_tag` (after line 27):**

```python
_TAG_URL_TEMPLATE = (
    "https://raw.githubusercontent.com/ericfitz/tmi/"
    "refs/tags/{tag}/api-schema/tmi-openapi.json"
)


def spec_url_for_tag(tag: str) -> str:
    """Return the raw GitHub URL for the OpenAPI spec at *tag*."""
    return _TAG_URL_TEMPLATE.format(tag=tag)
```

**Replace `parse_regen_args` (lines 30-51) with:**

```python
def parse_regen_args(description: str) -> argparse.Namespace:
    """Parse common CLI arguments for regeneration scripts.

    Returns a namespace with ``spec`` (str, required) and
    ``output_dir`` (str | None).
    """
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "--spec", "-s",
        required=True,
        help="Path to a local OpenAPI spec JSON file",
    )
    parser.add_argument(
        "--output-dir", "-o",
        default=None,
        help="Override the output directory (default: derived from spec version)",
    )
    return parser.parse_args()
```

**Remove `resolve_spec_url` function (lines 54-60)** — spec downloading is now the orchestrator's job.

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 test_regen_common_cli.py`
Expected: All tests pass.

- [ ] **Step 5: Commit**

```bash
git add regen_common.py test_regen_common_cli.py
git commit -m "refactor: update regen_common CLI to use --spec and add tag URL helper"
```

---

### Task 2: Refactor `regenerate_python.py` to use `--spec` and versioned output dirs

**Files:**
- Modify: `regenerate_python.py` (full file — remove CLIENT_DIR, use --spec, derive output dir)

- [ ] **Step 1: Write a test that verifies the script rejects missing `--spec`**

Create `test_regen_python_cli.py`:

```python
#!/usr/bin/env python3
"""Test that regenerate_python.py requires --spec and derives output dir."""
import subprocess
import sys

# Test: running without --spec should fail with exit code 2
result = subprocess.run(
    [sys.executable, "regenerate_python.py"],
    capture_output=True, text=True,
)
assert result.returncode == 2, f"Expected exit 2, got {result.returncode}"
assert "--spec" in result.stderr, f"Expected --spec in error, got: {result.stderr}"
print("PASS: --spec is required")

print("\nAll tests passed!")
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 test_regen_python_cli.py`
Expected: FAIL — the current script doesn't require `--spec`.

- [ ] **Step 3: Refactor `regenerate_python.py`**

Replace the module-level constants (lines 39-43) with:

```python
REPO_ROOT = Path(__file__).resolve().parent
LANG_DIR = REPO_ROOT / "python-client-generated"
CONFIG_FILE = LANG_DIR / "scripts" / "openapi-generator-config.json"
```

Replace the `main` function signature and the spec-handling section. The key changes:

1. `main()` takes `spec_path: str` (required) and `output_dir: str | None = None`
2. It calls `extract_spec_version(spec_path)` to get the version
3. It computes `client_dir = Path(output_dir) if output_dir else LANG_DIR / f"v{spec_version}"`
4. All references to `CLIENT_DIR` become `client_dir` (a local variable)
5. `SPEC_PATH` becomes `client_dir / "tmi-openapi.json"`
6. `BACKUP_DIR` becomes `client_dir / ".regeneration_backup"`
7. The spec download/copy logic is replaced with a simple copy from the provided `spec_path` to `client_dir / "tmi-openapi.json"`
8. Remove imports of `download_spec`, `resolve_spec_url`, `DEFAULT_SPEC_URL`

The `main()` function becomes:

```python
def main(spec_path: str, output_dir: str | None = None) -> int:
    had_issues = False

    # Derive version and output directory from spec
    spec_version = extract_spec_version(spec_path)
    client_dir = Path(output_dir) if output_dir else LANG_DIR / f"v{spec_version}"
    client_dir.mkdir(parents=True, exist_ok=True)
    spec_dest = client_dir / "tmi-openapi.json"
    backup_dir = client_dir / ".regeneration_backup"

    # 1. Banner
    print_banner("TMI Python Client Regeneration (openapi-generator)", {
        "Package": "tmi_client",
        "Version": spec_version,
        "Output": str(client_dir),
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

    # 3. Copy spec to output dir
    print_step(2, "Copying OpenAPI spec")
    copy_local_spec(Path(spec_path), spec_dest)

    # 3b. Update codegen config with version
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
    print_success("Patches applied")

    # 8. Restore custom files
    print_step(7, "Restoring custom files")
    restore_files(
        backup_dir=backup_dir,
        dest_dir=client_dir,
        files=["test_diagram_fixes.py", ".openapi-generator-ignore"],
        dirs=[],
    )

    # 9. Install deps
    print_step(8, "Installing dependencies")
    result = run_command(
        ["uv", "pip", "install", "-e", ".", "--quiet"],
        cwd=client_dir,
        error_context="Failed to install Python client dependencies.",
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
        error_context="Test execution failed.",
    )
    if result.returncode == 0:
        print_success("Auto-generated tests passed")
    else:
        print_warning("Some auto-generated tests failed — see test_output.log")
        had_issues = True
    (client_dir / "test_output.log").write_text(result.stdout + result.stderr)

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

    # 11. Generate report
    print_step(10, "Generating summary report")
    api_count = count_files(client_dir / "tmi_client" / "api", "*.py")
    model_count = count_files(client_dir / "tmi_client" / "models", "*.py")
    test_count = count_files(client_dir / "test", "*.py")

    report = generate_report("Python Client Regeneration Report", [
        {"heading": "Changes Applied", "content": (
            "### Client Regenerated\n"
            f"- Version: {spec_version}\n"
            f"- Output: {client_dir}\n"
            "- Generator: openapi-generator 7.x\n"
            "- Package: tmi_client\n"
            "- Models: Pydantic v2 with full type hints\n\n"
            "### Patches Applied\n"
            "- Regex validator fix\n"
            "- Test return-type fix\n"
            "- urllib3 minimum version bump to >= 2.6.3\n\n"
            "### Generated Configuration\n"
            "- pyproject.toml with Pydantic v2 dependencies\n"
            "- Python 3.9+ requirement\n"
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
    ])
    write_file(client_dir / "REGENERATION_REPORT.md", report)

    # 12. Cleanup
    print_step(11, "Cleaning up")
    clean_paths([backup_dir])
    print_success("Cleanup complete")

    # 13. Summary
    print_summary({
        "Client": f"v{spec_version} regenerated",
        "Output": str(client_dir),
        "Patches": "regex validator fix" + (" (with warnings)" if had_issues else ""),
        "Tests": "see logs for results",
    })

    return 2 if had_issues else 0
```

**Update patch functions to accept `client_dir` parameter.** Each patch function currently uses the global `CLIENT_DIR`. Change their signatures:

- `patch_regex_validators(client_dir: Path, had_issues: bool) -> bool` — replace `CLIENT_DIR` with `client_dir` inside the function body
- `patch_urllib3_minimum_version(client_dir: Path, had_issues: bool) -> bool` — same
- `patch_test_return_types(client_dir: Path, had_issues: bool) -> bool` — same

**Update `__main__` block:**

```python
if __name__ == "__main__":
    args = parse_regen_args("Regenerate the TMI Python client from the OpenAPI spec.")
    sys.exit(main(spec_path=args.spec, output_dir=args.output_dir))
```

- [ ] **Step 4: Run CLI rejection test**

Run: `python3 test_regen_python_cli.py`
Expected: PASS — script now requires --spec.

- [ ] **Step 5: Commit**

```bash
git add regenerate_python.py test_regen_python_cli.py
git commit -m "refactor: regenerate_python.py uses --spec, versioned output dirs"
```

---

### Task 3: Refactor `regenerate_go.py` to use `--spec` and versioned output dirs

**Files:**
- Modify: `regenerate_go.py` (full file — same pattern as Python)

- [ ] **Step 1: Write a test that verifies the script rejects missing `--spec`**

Create `test_regen_go_cli.py`:

```python
#!/usr/bin/env python3
"""Test that regenerate_go.py requires --spec."""
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "regenerate_go.py"],
    capture_output=True, text=True,
)
assert result.returncode == 2, f"Expected exit 2, got {result.returncode}"
assert "--spec" in result.stderr, f"Expected --spec in error, got: {result.stderr}"
print("PASS: --spec is required")
print("\nAll tests passed!")
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 test_regen_go_cli.py`
Expected: FAIL — the current script doesn't require `--spec`.

- [ ] **Step 3: Refactor `regenerate_go.py`**

Apply the same pattern as Task 2. Key differences from Python:

Replace module-level constants (lines 37-41) with:

```python
REPO_ROOT = Path(__file__).resolve().parent
LANG_DIR = REPO_ROOT / "go-client-generated"
CONFIG_FILE = LANG_DIR / "scripts" / "openapi-generator-config.json"
GO_VERSION = "1.21"
```

Replace `main()` signature with `main(spec_path: str, output_dir: str | None = None) -> int`.

Key Go-specific changes inside `main()`:

- `client_dir = Path(output_dir) if output_dir else LANG_DIR / f"v{spec_version}"`
- `GO_MODULE_PATH` becomes dynamic, incorporating the version:
  ```python
  go_module_path = f"github.com/ericfitz/tmi-clients/go-client-generated/v{spec_version}"
  ```
- All references to `CLIENT_DIR` become `client_dir`
- All references to `GO_MODULE_PATH` become `go_module_path`
- Update patch functions to accept `client_dir` parameter:
  - `patch_missing_time_import(client_dir: Path, had_issues: bool) -> bool`
  - `patch_test_module_path(client_dir: Path, go_module_path: str, had_issues: bool) -> bool`
  - `patch_json_literal_defaults(client_dir: Path, had_issues: bool) -> bool`
- Remove imports of `download_spec`, `resolve_spec_url`

**Update `__main__` block:**

```python
if __name__ == "__main__":
    args = parse_regen_args("Regenerate the TMI Go client from the OpenAPI spec.")
    sys.exit(main(spec_path=args.spec, output_dir=args.output_dir))
```

- [ ] **Step 4: Run CLI rejection test**

Run: `python3 test_regen_go_cli.py`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add regenerate_go.py test_regen_go_cli.py
git commit -m "refactor: regenerate_go.py uses --spec, versioned output dirs"
```

---

### Task 4: Refactor `regenerate_ts.py` to use `--spec` and versioned output dirs

**Files:**
- Modify: `regenerate_ts.py` (full file — same pattern as Python/Go)

- [ ] **Step 1: Write a test that verifies the script rejects missing `--spec`**

Create `test_regen_ts_cli.py`:

```python
#!/usr/bin/env python3
"""Test that regenerate_ts.py requires --spec."""
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "regenerate_ts.py"],
    capture_output=True, text=True,
)
assert result.returncode == 2, f"Expected exit 2, got {result.returncode}"
assert "--spec" in result.stderr, f"Expected --spec in error, got: {result.stderr}"
print("PASS: --spec is required")
print("\nAll tests passed!")
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 test_regen_ts_cli.py`
Expected: FAIL.

- [ ] **Step 3: Refactor `regenerate_ts.py`**

Same pattern. Replace module-level constants (lines 39-43) with:

```python
REPO_ROOT = Path(__file__).resolve().parent
LANG_DIR = REPO_ROOT / "typescript-client-generated"
CONFIG_FILE = LANG_DIR / "scripts" / "openapi-generator-config.json"
```

Replace `main()` signature with `main(spec_path: str, output_dir: str | None = None) -> int`.

Key TypeScript-specific changes:
- `client_dir = Path(output_dir) if output_dir else LANG_DIR / f"v{spec_version}"`
- All references to `CLIENT_DIR` become `client_dir`
- Update patch functions to accept `client_dir` parameter:
  - `patch_optional_extends(client_dir: Path, had_issues: bool) -> bool`
  - `patch_missing_token_request(client_dir: Path, had_issues: bool) -> bool`
- Remove imports of `download_spec`, `resolve_spec_url`, `DEFAULT_SPEC_URL`

**Update `__main__` block:**

```python
if __name__ == "__main__":
    args = parse_regen_args("Regenerate the TMI TypeScript client from the OpenAPI spec.")
    sys.exit(main(spec_path=args.spec, output_dir=args.output_dir))
```

- [ ] **Step 4: Run CLI rejection test**

Run: `python3 test_regen_ts_cli.py`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add regenerate_ts.py test_regen_ts_cli.py
git commit -m "refactor: regenerate_ts.py uses --spec, versioned output dirs"
```

---

### Task 5: Create `versions.json`

**Files:**
- Create: `versions.json`

- [ ] **Step 1: Create `versions.json`**

```json
{
  "latest": "1.4.0",
  "versions": [
    {
      "version": "1.2.0",
      "branch": "release/1.2.0"
    },
    {
      "version": "1.3.0",
      "branch": "main",
      "tag": "v1.3.0"
    },
    {
      "version": "1.4.0",
      "branch": "dev/1.4.0"
    }
  ]
}
```

- [ ] **Step 2: Validate the JSON**

Run: `python3 -c "import json; d = json.load(open('versions.json')); print(f'Valid: {len(d[\"versions\"])} versions, latest={d[\"latest\"]}')"`
Expected: `Valid: 3 versions, latest=1.4.0`

- [ ] **Step 3: Commit**

```bash
git add versions.json
git commit -m "feat: add versions.json for multi-version client generation"
```

---

### Task 6: Create `regenerate_all.py` — config loading and validation

**Files:**
- Create: `regenerate_all.py`
- Test: `test_regenerate_all.py`

This task builds the first half of the orchestrator: reading `versions.json`, validating it, downloading specs, and verifying versions match.

- [ ] **Step 1: Write tests for config loading and validation**

Create `test_regenerate_all.py`:

```python
#!/usr/bin/env python3
"""Tests for regenerate_all.py config loading and validation."""
import json
import tempfile
from pathlib import Path

# Test 1: load_versions_config with valid config
from regenerate_all import load_versions_config, ConfigError

with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
    json.dump({
        "latest": "1.4.0",
        "versions": [
            {"version": "1.2.0", "branch": "release/1.2.0"},
            {"version": "1.3.0", "branch": "main", "tag": "v1.3.0"},
            {"version": "1.4.0", "branch": "dev/1.4.0"},
        ],
    }, f)
    config_path = f.name

config = load_versions_config(config_path)
assert config["latest"] == "1.4.0"
assert len(config["versions"]) == 3
print("PASS: valid config loads correctly")

# Test 2: reject config with wrong number of versions
with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
    json.dump({
        "latest": "1.4.0",
        "versions": [
            {"version": "1.3.0", "branch": "main"},
            {"version": "1.4.0", "branch": "dev/1.4.0"},
        ],
    }, f)
    bad_path = f.name

try:
    load_versions_config(bad_path)
    print("FAIL: should have rejected 2-version config")
except ConfigError as e:
    assert "exactly 3" in str(e).lower(), f"Unexpected error: {e}"
    print("PASS: rejects config with != 3 versions")

# Test 3: reject config where latest is not in versions
with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
    json.dump({
        "latest": "2.0.0",
        "versions": [
            {"version": "1.2.0", "branch": "release/1.2.0"},
            {"version": "1.3.0", "branch": "main"},
            {"version": "1.4.0", "branch": "dev/1.4.0"},
        ],
    }, f)
    bad_path2 = f.name

try:
    load_versions_config(bad_path2)
    print("FAIL: should have rejected mismatched latest")
except ConfigError as e:
    assert "latest" in str(e).lower(), f"Unexpected error: {e}"
    print("PASS: rejects config where latest not in versions")

# Test 4: resolve_spec_url picks tag over branch
from regenerate_all import resolve_spec_url_for_entry

url = resolve_spec_url_for_entry({"version": "1.3.0", "branch": "main", "tag": "v1.3.0"})
assert "refs/tags/v1.3.0" in url, f"Expected tag URL, got: {url}"
print("PASS: tag takes precedence over branch")

url2 = resolve_spec_url_for_entry({"version": "1.4.0", "branch": "dev/1.4.0"})
assert "refs/heads/dev/1.4.0" in url2, f"Expected branch URL, got: {url2}"
print("PASS: branch used when no tag")

# Cleanup
Path(config_path).unlink()
Path(bad_path).unlink()
Path(bad_path2).unlink()

print("\nAll tests passed!")
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 test_regenerate_all.py`
Expected: ImportError — `regenerate_all` doesn't exist yet.

- [ ] **Step 3: Implement config loading in `regenerate_all.py`**

Create `regenerate_all.py`:

```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Orchestrator for multi-version TMI client regeneration.

Reads versions.json, downloads OpenAPI specs for each declared version,
and invokes per-language regeneration scripts to produce versioned client
directories.
"""
from __future__ import annotations

import argparse
import json
import sys
import tempfile
from pathlib import Path

from regen_common import (
    download_spec,
    extract_spec_version,
    print_banner,
    print_error,
    print_step,
    print_success,
    print_summary,
    print_warning,
    run_command,
    spec_url_for_branch,
    spec_url_for_tag,
    clean_paths,
)

REPO_ROOT = Path(__file__).resolve().parent
DEFAULT_CONFIG = REPO_ROOT / "versions.json"

LANGUAGES = {
    "python": {
        "script": REPO_ROOT / "regenerate_python.py",
        "dir": REPO_ROOT / "python-client-generated",
    },
    "go": {
        "script": REPO_ROOT / "regenerate_go.py",
        "dir": REPO_ROOT / "go-client-generated",
    },
    "typescript": {
        "script": REPO_ROOT / "regenerate_ts.py",
        "dir": REPO_ROOT / "typescript-client-generated",
    },
}


class ConfigError(Exception):
    """Raised when versions.json is invalid."""


def load_versions_config(config_path: str | Path) -> dict:
    """Load and validate versions.json.

    Validates:
    - JSON is parseable
    - Has 'latest' and 'versions' keys
    - Exactly 3 version entries
    - 'latest' matches one of the declared versions
    - Each version entry has 'version' and 'branch' keys

    Returns the parsed config dict.
    Raises ConfigError on validation failure.
    """
    config_path = Path(config_path)
    try:
        data = json.loads(config_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, FileNotFoundError) as exc:
        raise ConfigError(f"Cannot read config: {exc}") from exc

    if "latest" not in data:
        raise ConfigError("Config missing 'latest' field")
    if "versions" not in data:
        raise ConfigError("Config missing 'versions' field")

    versions = data["versions"]
    if len(versions) != 3:
        raise ConfigError(
            f"Config must have exactly 3 versions, got {len(versions)}"
        )

    version_strings = [v["version"] for v in versions]
    if data["latest"] not in version_strings:
        raise ConfigError(
            f"'latest' value '{data['latest']}' is not in versions: {version_strings}"
        )

    for entry in versions:
        if "version" not in entry:
            raise ConfigError(f"Version entry missing 'version' key: {entry}")
        if "branch" not in entry:
            raise ConfigError(f"Version entry missing 'branch' key: {entry}")

    return data


def resolve_spec_url_for_entry(entry: dict) -> str:
    """Return the spec download URL for a version entry.

    Uses tag if present, otherwise branch.
    """
    if "tag" in entry:
        return spec_url_for_tag(entry["tag"])
    return spec_url_for_branch(entry["branch"])


def parse_args() -> argparse.Namespace:
    """Parse orchestrator CLI arguments."""
    parser = argparse.ArgumentParser(
        description="Regenerate multi-version TMI clients from versions.json.",
    )
    parser.add_argument(
        "--config", "-c",
        default=str(DEFAULT_CONFIG),
        help=f"Path to versions config file (default: {DEFAULT_CONFIG})",
    )
    parser.add_argument(
        "--language", "-l",
        choices=list(LANGUAGES.keys()),
        default=None,
        help="Regenerate only this language (default: all)",
    )
    parser.add_argument(
        "--version", "-v",
        default=None,
        help="Regenerate only this version (default: all)",
    )
    parser.add_argument(
        "--no-prune",
        action="store_true",
        help="Skip pruning of version directories not in config",
    )
    return parser.parse_args()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 test_regenerate_all.py`
Expected: All tests pass.

- [ ] **Step 5: Commit**

```bash
git add regenerate_all.py test_regenerate_all.py
git commit -m "feat: regenerate_all.py config loading and validation"
```

---

### Task 7: Complete `regenerate_all.py` — orchestration, execution, and pruning

**Files:**
- Modify: `regenerate_all.py` (add `main()`, spec downloading, per-language dispatch, pruning)

- [ ] **Step 1: Write a test for the pruning logic**

Add to `test_regenerate_all.py`:

```python
# Test 5: prune_stale_versions removes unlisted dirs
import tempfile
import os
from regenerate_all import prune_stale_versions

with tempfile.TemporaryDirectory() as tmpdir:
    lang_dir = Path(tmpdir)
    # Create version dirs: v1.1.0 (stale), v1.2.0 (keep), v1.3.0 (keep), v1.4.0 (keep)
    for v in ["v1.1.0", "v1.2.0", "v1.3.0", "v1.4.0"]:
        (lang_dir / v).mkdir()
        (lang_dir / v / "dummy.txt").write_text("test")
    # Also create a non-version dir that should be left alone
    (lang_dir / "scripts").mkdir()
    (lang_dir / "scripts" / "config.json").write_text("{}")

    active_versions = ["1.2.0", "1.3.0", "1.4.0"]
    pruned = prune_stale_versions(lang_dir, active_versions)

    assert pruned == ["v1.1.0"], f"Expected ['v1.1.0'], got: {pruned}"
    assert not (lang_dir / "v1.1.0").exists(), "v1.1.0 should be deleted"
    assert (lang_dir / "v1.2.0").exists(), "v1.2.0 should remain"
    assert (lang_dir / "scripts").exists(), "scripts/ should remain"
    print("PASS: prune_stale_versions removes stale dirs, keeps active and non-version dirs")

print("\nAll tests passed!")
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 test_regenerate_all.py`
Expected: ImportError on `prune_stale_versions`.

- [ ] **Step 3: Add orchestration logic to `regenerate_all.py`**

Add these functions after `parse_args()`:

```python
def download_and_validate_spec(entry: dict, dest_dir: Path) -> Path | None:
    """Download spec for a version entry, validate version matches.

    Returns the path to the downloaded spec file, or None on failure.
    Note: download_spec and extract_spec_version call sys.exit on failure,
    so we catch SystemExit to allow the orchestrator to continue with
    remaining versions.
    """
    version = entry["version"]
    url = resolve_spec_url_for_entry(entry)
    spec_path = dest_dir / f"tmi-openapi-{version}.json"

    try:
        download_spec(url, spec_path)
        actual_version = extract_spec_version(spec_path)
    except SystemExit:
        print_error(f"Failed to download or parse spec for version {version}")
        return None

    if actual_version != version:
        print_error(
            f"Version mismatch for {version}: "
            f"spec contains '{actual_version}'"
        )
        return None

    return spec_path


def prune_stale_versions(lang_dir: Path, active_versions: list[str]) -> list[str]:
    """Remove version directories not in active_versions.

    Only removes directories matching the pattern v*.*.* under lang_dir.
    Returns list of pruned directory names.
    """
    active_dirs = {f"v{v}" for v in active_versions}
    pruned = []

    for child in sorted(lang_dir.iterdir()):
        if not child.is_dir():
            continue
        # Only consider directories that look like version dirs (v<digits>...)
        if not child.name.startswith("v"):
            continue
        # Check if it looks like a version (v followed by digit)
        if len(child.name) < 2 or not child.name[1].isdigit():
            continue
        if child.name not in active_dirs:
            clean_paths([child])
            pruned.append(child.name)

    return pruned


def regenerate_version_language(
    spec_path: Path,
    language: str,
) -> int:
    """Run a per-language regeneration script for a single version.

    Returns the script's exit code.
    """
    lang_info = LANGUAGES[language]
    cmd = [
        sys.executable,
        str(lang_info["script"]),
        "--spec", str(spec_path),
    ]
    print(f"  Running: {' '.join(cmd)}")
    result = run_command(cmd, error_context=f"Regenerate {language}")
    return result.returncode


def main() -> int:
    args = parse_args()

    # 1. Load config
    print_banner("TMI Multi-Version Client Regeneration", {
        "Config": args.config,
        "Language filter": args.language or "all",
        "Version filter": args.version or "all",
    })

    print_step(1, "Loading versions config")
    try:
        config = load_versions_config(args.config)
    except ConfigError as exc:
        print_error(str(exc))
        return 1

    versions = config["versions"]
    version_strings = [v["version"] for v in versions]
    print_success(f"Loaded {len(versions)} versions: {', '.join(version_strings)}")
    print_success(f"Latest: {config['latest']}")

    # Apply version filter
    if args.version:
        versions = [v for v in versions if v["version"] == args.version]
        if not versions:
            print_error(f"Version '{args.version}' not found in config")
            return 1

    # Determine languages to process
    languages = [args.language] if args.language else list(LANGUAGES.keys())

    # 2. Check prerequisites
    print_step(2, "Checking prerequisites")
    from regen_common import check_prerequisite
    check_prerequisite("openapi-generator", "brew install openapi-generator")
    print_success("Prerequisites met")

    # 3. Download and validate specs
    print_step(3, "Downloading and validating specs")
    specs: dict[str, Path] = {}  # version -> spec_path
    failures: list[str] = []

    with tempfile.TemporaryDirectory(prefix="tmi-specs-") as tmpdir:
        tmp_path = Path(tmpdir)

        for entry in versions:
            version = entry["version"]
            print(f"\n  Downloading spec for v{version}...")
            spec_path = download_and_validate_spec(entry, tmp_path)
            if spec_path is None:
                failures.append(f"spec-download:{version}")
                continue
            specs[version] = spec_path

        # 4. Regenerate
        print_step(4, "Regenerating clients")
        results: dict[str, int] = {}  # "lang:version" -> exit_code

        for entry in versions:
            version = entry["version"]
            if version not in specs:
                continue  # already failed in download

            for language in languages:
                key = f"{language}:v{version}"
                print(f"\n  --- {key} ---")
                exit_code = regenerate_version_language(specs[version], language)
                results[key] = exit_code
                if exit_code == 0:
                    print_success(f"{key} succeeded")
                elif exit_code == 2:
                    print_warning(f"{key} completed with issues")
                else:
                    print_error(f"{key} failed (exit {exit_code})")
                    failures.append(key)

    # 5. Prune
    if not args.no_prune:
        print_step(5, "Pruning stale version directories")
        # Use full version list from config (not filtered), so we don't
        # accidentally prune versions that were just filtered out
        all_versions = [v["version"] for v in config["versions"]]
        for language in languages:
            lang_dir = LANGUAGES[language]["dir"]
            if not lang_dir.is_dir():
                continue
            pruned = prune_stale_versions(lang_dir, all_versions)
            if pruned:
                print_success(f"  {language}: pruned {', '.join(pruned)}")
            else:
                print_success(f"  {language}: nothing to prune")
    else:
        print_step(5, "Skipping pruning (--no-prune)")

    # 6. Summary
    succeeded = sum(1 for c in results.values() if c == 0)
    warned = sum(1 for c in results.values() if c == 2)
    failed = sum(1 for c in results.values() if c not in (0, 2))

    print_summary({
        "Versions": ", ".join(version_strings),
        "Latest": config["latest"],
        "Languages": ", ".join(languages),
        "Succeeded": str(succeeded),
        "With issues": str(warned),
        "Failed": str(failed + len([f for f in failures if f.startswith("spec-download")])),
    })

    if failures:
        print_error(f"Failures: {', '.join(failures)}")
        return 1 if failed > 0 else 2
    if warned > 0:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 test_regenerate_all.py`
Expected: All tests pass.

- [ ] **Step 5: Verify the orchestrator CLI help works**

Run: `python3 regenerate_all.py --help`
Expected: Shows usage with --config, --language, --version, --no-prune options.

- [ ] **Step 6: Commit**

```bash
git add regenerate_all.py test_regenerate_all.py
git commit -m "feat: regenerate_all.py orchestration, execution, and pruning"
```

---

### Task 8: Clean up old generated code and run full regeneration

**Files:**
- Delete contents of: `python-client-generated/` (keep `scripts/`), `go-client-generated/` (keep `scripts/`), `typescript-client-generated/` (keep `scripts/`)

- [ ] **Step 1: Delete old generated code**

```bash
# Python: keep scripts/, remove everything else
find python-client-generated -mindepth 1 -maxdepth 1 ! -name scripts -exec rm -rf {} +

# Go: keep scripts/, remove everything else
find go-client-generated -mindepth 1 -maxdepth 1 ! -name scripts -exec rm -rf {} +

# TypeScript: keep scripts/, remove everything else
find typescript-client-generated -mindepth 1 -maxdepth 1 ! -name scripts -exec rm -rf {} +
```

- [ ] **Step 2: Verify only `scripts/` remains in each**

```bash
ls python-client-generated/
ls go-client-generated/
ls typescript-client-generated/
```
Expected: Each shows only `scripts`.

- [ ] **Step 3: Run full regeneration**

```bash
python3 regenerate_all.py
```

Expected: Downloads 3 specs, regenerates 9 client directories (3 languages x 3 versions), prints summary. Some versions may have issues (exit code 2) if tests fail for older spec versions — that's acceptable.

- [ ] **Step 4: Verify directory structure**

```bash
ls python-client-generated/
ls go-client-generated/
ls typescript-client-generated/
```

Expected:
```
python-client-generated/: scripts  v1.2.0  v1.3.0  v1.4.0
go-client-generated/:     scripts  v1.2.0  v1.3.0  v1.4.0
typescript-client-generated/: scripts  v1.2.0  v1.3.0  v1.4.0
```

- [ ] **Step 5: Spot-check version correctness**

```bash
python3 -c "import json; print(json.load(open('python-client-generated/v1.3.0/pyproject.toml')))" 2>/dev/null || grep '^version' python-client-generated/v1.3.0/pyproject.toml
grep '"version"' typescript-client-generated/v1.4.0/package.json
head -1 go-client-generated/v1.2.0/go.mod
```

Expected: Each shows the correct version for its directory.

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "feat: multi-version client generation — delete old flat structure, regenerate all"
```

---

### Task 9: Update documentation

**Files:**
- Modify: `CLAUDE.md` (repo root)
- Modify: `README.md` (repo root)

- [ ] **Step 1: Update `CLAUDE.md` to reflect new directory structure**

Update the following sections in the repo-root `CLAUDE.md`:

- **Repository Overview**: mention versioned subdirectories
- **Python Client Development / Running Commands**: update paths (e.g., `cd python-client-generated/v1.4.0`)
- **Python Client Development / Testing**: update test commands to reference version dirs
- **Architecture / Client Structure**: update directory tree to show version subdirs
- **Architecture / Python Client Package Layout**: update to show version nesting
- **Regeneration**: update to describe `regenerate_all.py` and `versions.json`, update the CLI examples
- Remove references to the old flat paths throughout

- [ ] **Step 2: Update `README.md`**

Update installation/usage examples to reference versioned paths. Add a section explaining the multi-version structure and `versions.json`.

- [ ] **Step 3: Verify docs are accurate**

Spot-check that paths mentioned in the updated docs actually exist:

```bash
ls python-client-generated/v1.4.0/tmi_client/
ls python-client-generated/v1.4.0/test/
ls go-client-generated/v1.4.0/go.mod
```

- [ ] **Step 4: Commit**

```bash
git add CLAUDE.md README.md
git commit -m "docs: update CLAUDE.md and README.md for multi-version directory structure"
```

---

### Task 10: Clean up test scripts

**Files:**
- Delete: `test_regen_common_cli.py`, `test_regen_python_cli.py`, `test_regen_go_cli.py`, `test_regen_ts_cli.py`, `test_regenerate_all.py`

- [ ] **Step 1: Run all test scripts one final time**

```bash
python3 test_regen_common_cli.py && python3 test_regen_python_cli.py && python3 test_regen_go_cli.py && python3 test_regen_ts_cli.py && python3 test_regenerate_all.py
```

Expected: All pass.

- [ ] **Step 2: Delete test scripts**

```bash
rm test_regen_common_cli.py test_regen_python_cli.py test_regen_go_cli.py test_regen_ts_cli.py test_regenerate_all.py
```

- [ ] **Step 3: Commit**

```bash
git add -A
git commit -m "chore: remove temporary test scripts for regen refactoring"
```

---

### Task 11: Remove unused exports from `regen_common.py`

**Files:**
- Modify: `regen_common.py`

- [ ] **Step 1: Check which functions are still imported by the per-language scripts**

```bash
grep "from regen_common import" regenerate_python.py regenerate_go.py regenerate_ts.py regenerate_all.py
```

- [ ] **Step 2: Remove unused functions**

Based on the grep results, remove any functions no longer imported by any script. Candidates:
- `resolve_spec_url` (already removed in Task 1)
- `DEFAULT_SPEC_URL` (no longer needed — orchestrator constructs URLs)

- [ ] **Step 3: Verify nothing is broken**

```bash
python3 -c "import regenerate_python; print('python OK')"
python3 -c "import regenerate_go; print('go OK')"
python3 -c "import regenerate_ts; print('ts OK')"
python3 -c "import regenerate_all; print('all OK')"
```

Expected: All print OK.

- [ ] **Step 4: Commit**

```bash
git add regen_common.py
git commit -m "chore: remove unused exports from regen_common.py"
```
