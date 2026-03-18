# Regeneration Scripts Python Rewrite — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace three bash regeneration scripts with Python scripts sharing a common utility module.

**Architecture:** A shared `regen_common.py` at the repo root provides spec download, prerequisites, subprocess, patching, backup/restore, colored output, and report generation. Three language-specific scripts (`regenerate_python.py`, `regenerate_go.py`, `regenerate_js.py`) import from it and define language-specific patches, config, and test invocation.

**Tech Stack:** Python 3.9+ (stdlib only — subprocess, urllib.request, shutil, pathlib, re, json, glob, argparse). No external dependencies.

**Spec:** `docs/superpowers/specs/2026-03-17-regeneration-scripts-rewrite-design.md`

**Existing bash scripts (reference implementations):**
- `python-client-generated/scripts/regenerate_client.sh`
- `go-client-generated/scripts/regenerate_client.sh`
- `javascript-client-generated/scripts/regenerate_client.sh`
- `python-client-generated/scripts/backup_before_regen.sh`

---

## File Map

| File | Action | Responsibility |
|------|--------|---------------|
| `regen_common.py` | Create | Shared utilities: output, prerequisites, spec download, subprocess, patching, backup/restore, file utils, report generation |
| `regenerate_python.py` | Create | Python client regeneration: patches (DfdDiagram, DfdDiagramInput, Edge, Node, Configuration), config files, tests |
| `regenerate_go.py` | Create | Go client regeneration: patches (RevokeToken), go.mod, build, tests |
| `regenerate_js.py` | Create | JS client regeneration: patches (AllOf enum, enum export, constructor forwarding), package.json, tests |
| `python-client-generated/scripts/regenerate_client.sh` | Delete | Replaced by `regenerate_python.py` |
| `python-client-generated/scripts/regenerate_client.sh.new` | Delete | Dead file |
| `python-client-generated/scripts/backup_before_regen.sh` | Delete | Absorbed into `regenerate_python.py` |
| `go-client-generated/scripts/regenerate_client.sh` | Delete | Replaced by `regenerate_go.py` |
| `javascript-client-generated/scripts/regenerate_client.sh` | Delete | Replaced by `regenerate_js.py` |
| `CLAUDE.md` (repo root) | Modify | Update script paths and usage instructions |

---

### Task 1: Create `regen_common.py` — Output and Prerequisites

**Files:**
- Create: `regen_common.py`

This task creates the shared module with the output functions and prerequisite checks. These are the foundation used by all subsequent tasks.

- [ ] **Step 1: Create `regen_common.py` with output functions and constants**

```python
#!/usr/bin/env python3
"""Shared utilities for TMI client regeneration scripts."""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

DEFAULT_SPEC_URL = (
    "https://raw.githubusercontent.com/ericfitz/tmi/"
    "refs/heads/main/api-schema/tmi-openapi.json"
)

# ANSI color codes
_RED = "\033[0;31m"
_GREEN = "\033[0;32m"
_YELLOW = "\033[1;33m"
_NC = "\033[0m"


def print_banner(title: str, config: dict[str, str]) -> None:
    """Print a formatted banner with config key-value pairs."""
    print("=" * 50)
    print(title)
    print("=" * 50)
    print()
    for key, value in config.items():
        print(f"  - {key}: {value}")
    print()


def print_step(n: int, msg: str) -> None:
    """Print a numbered step header."""
    print(f"Step {n}: {msg}...")


def print_success(msg: str) -> None:
    """Print a green checkmark message."""
    print(f"{_GREEN}\u2713 {msg}{_NC}")


def print_warning(msg: str) -> None:
    """Print a yellow warning message."""
    print(f"{_YELLOW}\u26a0 {msg}{_NC}")


def print_error(msg: str) -> None:
    """Print a red error message."""
    print(f"{_RED}ERROR: {msg}{_NC}")


def print_summary(results: dict[str, str]) -> None:
    """Print a final summary table."""
    print()
    print("=" * 50)
    print("Summary")
    print("=" * 50)
    for key, value in results.items():
        print(f"  {key}: {value}")
    print()


def check_prerequisite(command: str, install_hint: str) -> None:
    """Verify a CLI tool is on PATH. Exits with code 1 if not found."""
    if shutil.which(command) is None:
        print_error(
            f"'{command}' not found on PATH.\n"
            f"  Install it with: {install_hint}\n"
            f"  Then re-run this script."
        )
        sys.exit(1)


def check_version(
    command: str,
    args: list[str],
    min_version: str,
    extract_pattern: str,
) -> None:
    """Verify minimum version of a tool. Prints warning if below minimum.

    Uses simple tuple comparison of dotted version numbers (no external deps).
    """
    try:
        result = subprocess.run(
            [command] + args,
            capture_output=True,
            text=True,
            timeout=10,
        )
        output = result.stdout + result.stderr
        match = re.search(extract_pattern, output)
        if match:
            actual = match.group(1)
            actual_parts = tuple(int(x) for x in actual.split("."))
            min_parts = tuple(int(x) for x in min_version.split("."))
            if actual_parts < min_parts:
                print_warning(
                    f"{command} version {actual} is below minimum {min_version}.\n"
                    f"  Upgrade with your package manager (e.g., brew upgrade {command})."
                )
            else:
                print_success(f"{command} version {actual} (>= {min_version})")
        else:
            print_warning(
                f"Could not determine {command} version.\n"
                f"  Expected pattern matching: {extract_pattern}\n"
                f"  Got: {output.strip()[:200]}"
            )
    except FileNotFoundError:
        pass  # check_prerequisite handles this
    except Exception as e:
        print_warning(f"Version check for {command} failed: {e}")
```

- [ ] **Step 2: Verify it imports cleanly**

Run: `cd /Users/efitz/Projects/tmi-clients && python3 -c "import regen_common; print('OK')"`
Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add regen_common.py
git commit -m "feat: add regen_common.py with output functions and prerequisite checks"
```

---

### Task 2: Add Spec Management and Subprocess to `regen_common.py`

**Files:**
- Modify: `regen_common.py`

- [ ] **Step 1: Add `download_spec`, `copy_local_spec`, and `run_command`**

Append to `regen_common.py` (imports already at module level from Task 1):

```python
def download_spec(url: str, dest: Path) -> None:
    """Download OpenAPI spec from URL."""
    try:
        urllib.request.urlretrieve(url, dest)
        print_success(f"OpenAPI spec downloaded to {dest.name}")
    except urllib.error.HTTPError as e:
        print_error(
            f"Failed to download OpenAPI spec.\n"
            f"  URL: {url}\n"
            f"  HTTP status: {e.code}\n"
            f"  Check that the URL is correct and accessible.\n"
            f"  If the repo has moved, update DEFAULT_SPEC_URL in regen_common.py."
        )
        sys.exit(1)
    except urllib.error.URLError as e:
        print_error(
            f"Failed to download OpenAPI spec.\n"
            f"  URL: {url}\n"
            f"  Error: {e.reason}\n"
            f"  Check your network connection."
        )
        sys.exit(1)


def copy_local_spec(src: Path, dest: Path) -> None:
    """Copy a local spec file to the working location."""
    src = src.resolve()
    if not src.is_file():
        print_error(
            f"Local spec file not found.\n"
            f"  Path: {src}\n"
            f"  Verify the file exists and the path is correct."
        )
        sys.exit(1)
    shutil.copy2(src, dest)
    print_success(f"OpenAPI spec copied from {src}")


def run_command(
    cmd: list[str],
    cwd: Path | None = None,
    capture: bool = False,
    env: dict | None = None,
    error_context: str = "",
) -> subprocess.CompletedProcess:
    """Run a shell command with structured error reporting.

    If capture=True, stdout/stderr are captured and returned.
    If capture=False, output streams to the terminal.
    Returns the CompletedProcess. Does NOT raise on non-zero exit.
    """
    full_env = None
    if env:
        full_env = {**os.environ, **env}

    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=capture,
            text=True,
            env=full_env,
        )
        return result
    except FileNotFoundError:
        print_error(
            f"Command not found: {cmd[0]}\n"
            f"  Full command: {' '.join(cmd)}\n"
            f"  Working directory: {cwd or Path.cwd()}\n"
            f"  {error_context}"
        )
        sys.exit(1)
    except Exception as e:
        print_error(
            f"Command failed to execute: {' '.join(cmd)}\n"
            f"  Error: {e}\n"
            f"  Working directory: {cwd or Path.cwd()}\n"
            f"  {error_context}"
        )
        sys.exit(1)
```

- [ ] **Step 2: Verify imports**

Run: `cd /Users/efitz/Projects/tmi-clients && python3 -c "from regen_common import download_spec, run_command; print('OK')"`
Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add regen_common.py
git commit -m "feat: add spec download, local copy, and subprocess runner to regen_common"
```

---

### Task 3: Add Code Generation, Patching, and File Utilities to `regen_common.py`

**Files:**
- Modify: `regen_common.py`

- [ ] **Step 1: Add `run_codegen`**

```python
def run_codegen(
    spec_path: Path,
    language: str,
    output_dir: Path,
    config_file: Path,
    template_dir: Path | None = None,
) -> None:
    """Run swagger-codegen generate. Exits with code 1 on failure."""
    cmd = [
        "swagger-codegen", "generate",
        "-i", str(spec_path),
        "-l", language,
        "-o", str(output_dir),
        "-c", str(config_file),
    ]
    if template_dir is not None:
        cmd.extend(["-t", str(template_dir)])

    print(f"  Command: {' '.join(cmd)}")
    result = run_command(
        cmd,
        error_context=(
            f"swagger-codegen failed for language '{language}'.\n"
            f"  Try: swagger-codegen validate -i {spec_path}\n"
            f"  Check that {config_file} is valid JSON."
        ),
    )
    if result.returncode != 0:
        print_error(
            f"swagger-codegen exited with code {result.returncode}.\n"
            f"  Language: {language}\n"
            f"  Spec: {spec_path}\n"
            f"  Config: {config_file}\n"
            f"  Try: swagger-codegen validate -i {spec_path}\n"
            f"  Check that {config_file} is valid JSON and the spec is well-formed."
        )
        sys.exit(1)
    print_success("Client generated successfully")
```

- [ ] **Step 2: Add `patch_file_regex` and `patch_file_exact`**

```python
def patch_file_regex(
    file_path: Path,
    pattern: str,
    replacement: str,
    description: str = "",
) -> bool:
    """Regex-based file patch. Returns True if a substitution was made."""
    label = description or str(file_path)
    if not file_path.is_file():
        print_warning(
            f"Patch target not found: {file_path}\n"
            f"  Patch: {label}\n"
            f"  The generated code structure may have changed."
        )
        return False

    content = file_path.read_text()
    new_content, count = re.subn(pattern, replacement, content)
    if count == 0:
        print_warning(
            f"Patch did not match: {label}\n"
            f"  File: {file_path}\n"
            f"  Pattern: {pattern[:100]}...\n"
            f"  The generated code structure may have changed.\n"
            f"  Inspect the file and update the patch pattern if needed."
        )
        return False

    file_path.write_text(new_content)
    print_success(f"  {label}")
    return True


def patch_file_exact(
    file_path: Path,
    old_text: str,
    new_text: str,
    description: str = "",
) -> bool:
    """Exact string replacement in a file. Returns True if found and replaced."""
    label = description or str(file_path)
    if not file_path.is_file():
        print_warning(
            f"Patch target not found: {file_path}\n"
            f"  Patch: {label}\n"
            f"  The generated code structure may have changed."
        )
        return False

    content = file_path.read_text()
    if old_text not in content:
        snippet = old_text[:80].replace("\n", "\\n")
        print_warning(
            f"Patch did not match: {label}\n"
            f"  File: {file_path}\n"
            f"  Expected text: {snippet}...\n"
            f"  The codegen output may have changed.\n"
            f"  Inspect the file and update the patch text if needed."
        )
        return False

    new_content = content.replace(old_text, new_text, 1)
    file_path.write_text(new_content)
    print_success(f"  {label}")
    return True
```

- [ ] **Step 3: Add file utilities**

```python
def count_files(directory: Path, pattern: str) -> int:
    """Count files matching a glob pattern."""
    return len(list(directory.glob(pattern)))


def write_file(path: Path, content: str) -> None:
    """Write content to a file, creating parent directories."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def clean_paths(paths: list[Path]) -> None:
    """Remove files and directories. Silently skips non-existent paths."""
    for path in paths:
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            shutil.rmtree(path)
        # else: doesn't exist, skip silently
```

- [ ] **Step 4: Verify imports**

Run: `cd /Users/efitz/Projects/tmi-clients && python3 -c "from regen_common import run_codegen, patch_file_regex, patch_file_exact, count_files, write_file, clean_paths; print('OK')"`
Expected: `OK`

- [ ] **Step 5: Commit**

```bash
git add regen_common.py
git commit -m "feat: add codegen, patching, and file utilities to regen_common"
```

---

### Task 4: Add Backup/Restore and Report Generation to `regen_common.py`

**Files:**
- Modify: `regen_common.py`

- [ ] **Step 1: Add `backup_files` and `restore_files`**

```python
def backup_files(
    files: list[Path],
    dirs: list[Path],
    backup_dir: Path,
) -> None:
    """Copy files and directories to backup location.

    Missing source files/dirs are silently skipped (they're optional).
    """
    backup_dir.mkdir(parents=True, exist_ok=True)
    for f in files:
        if f.is_file():
            shutil.copy2(f, backup_dir / f.name)
    for d in dirs:
        if d.is_dir():
            dest = backup_dir / d.name
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(d, dest)


def restore_files(
    backup_dir: Path,
    dest_dir: Path,
    files: list[str],
    dirs: list[str],
) -> None:
    """Restore files from backup. Warns about missing backup entries."""
    for name in files:
        src = backup_dir / name
        if src.is_file():
            shutil.copy2(src, dest_dir / name)
            print_success(f"  Restored {name}")
        else:
            print_warning(f"  {name} not found in backup")
    for name in dirs:
        src = backup_dir / name
        if src.is_dir():
            dest = dest_dir / name
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(src, dest)
            print_success(f"  Restored {name}/")
        else:
            print_warning(f"  {name}/ not found in backup")
```

- [ ] **Step 2: Add `generate_report`**

```python
def generate_report(title: str, sections: list[dict]) -> str:
    """Generate a markdown report from titled sections.

    Each section: {"heading": str, "content": str}
    """
    lines = [
        f"# {title}",
        "",
        f"**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
    ]
    for section in sections:
        lines.append(f"## {section['heading']}")
        lines.append("")
        lines.append(section["content"])
        lines.append("")
    return "\n".join(lines)
```

- [ ] **Step 3: Verify imports**

Run: `cd /Users/efitz/Projects/tmi-clients && python3 -c "from regen_common import backup_files, restore_files, generate_report; print('OK')"`
Expected: `OK`

- [ ] **Step 4: Commit**

```bash
git add regen_common.py
git commit -m "feat: add backup/restore and report generation to regen_common"
```

---

### Task 5: Create `regenerate_python.py`

**Files:**
- Create: `regenerate_python.py`

**Reference:** `python-client-generated/scripts/regenerate_client.sh` (lines 1-545)

This is the largest single task. The script implements all 14 steps from the spec for the Python client.

- [ ] **Step 1: Create `regenerate_python.py` with the full implementation**

Write the complete file. Key path notes:
- `REPO_ROOT`: `Path(__file__).resolve().parent`
- `CLIENT_DIR`: `REPO_ROOT / "python-client-generated"`
- `CONFIG_FILE`: `CLIENT_DIR / "scripts" / "swagger-codegen-config.json"`
- `TEMPLATE_DIR`: `CLIENT_DIR / "custom-templates" / "python"`
- `SPEC_PATH`: `CLIENT_DIR / "tmi-openapi.json"`

```python
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

PYPROJECT_TOML = """\
[project]
name = "tmi-client"
version = "1.0.0"
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
Homepage = "https://github.com/threagile/tmi-clients"
Repository = "https://github.com/threagile/tmi-clients"
Documentation = "https://github.com/threagile/tmi-clients/tree/main/python-client-generated"

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
    write_file(CLIENT_DIR / "pyproject.toml", PYPROJECT_TOML)
    print_success("pyproject.toml created")

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
            "- Package: tmi_client v1.0.0\n\n"
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
```

- [ ] **Step 2: Verify it imports and parses cleanly**

Run: `cd /Users/efitz/Projects/tmi-clients && python3 -c "import regenerate_python; print('OK')"`
Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add regenerate_python.py
git commit -m "feat: add regenerate_python.py — Python client regeneration script"
```

---

### Task 6: Create `regenerate_go.py`

**Files:**
- Create: `regenerate_go.py`

**Reference:** `go-client-generated/scripts/regenerate_client.sh` (lines 1-470)

- [ ] **Step 1: Create `regenerate_go.py` with the full implementation**

Key path notes:
- `REPO_ROOT`: `Path(__file__).resolve().parent`
- `CLIENT_DIR`: `REPO_ROOT / "go-client-generated"`
- `CONFIG_FILE`: `CLIENT_DIR / "scripts" / "swagger-codegen-config.json"`
- `SPEC_PATH`: `CLIENT_DIR / "tmi-openapi.json"`

**IMPORTANT:** `go.mod` and `go.sum` are backed up for rollback reference only. They are NOT restored after codegen — the script patches the codegen-generated `go.mod` (or creates a fresh one), then runs `go mod tidy` which regenerates `go.sum`. Restoring old versions would undo the patches and reintroduce stale dependencies.

```python
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
    write_file,
)

REPO_ROOT = Path(__file__).resolve().parent
CLIENT_DIR = REPO_ROOT / "go-client-generated"
CONFIG_FILE = CLIENT_DIR / "scripts" / "swagger-codegen-config.json"
SPEC_PATH = CLIENT_DIR / "tmi-openapi.json"
BACKUP_DIR = CLIENT_DIR / ".regeneration_backup"

GO_MODULE_PATH = "github.com/efitz/tmi-clients/go-client-generated"
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
```

- [ ] **Step 2: Verify it imports and parses cleanly**

Run: `cd /Users/efitz/Projects/tmi-clients && python3 -c "import regenerate_go; print('OK')"`
Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add regenerate_go.py
git commit -m "feat: add regenerate_go.py — Go client regeneration script"
```

---

### Task 7: Create `regenerate_js.py`

**Files:**
- Create: `regenerate_js.py`

**Reference:** `javascript-client-generated/scripts/regenerate_client.sh` (lines 1-618)

- [ ] **Step 1: Create `regenerate_js.py` with the full implementation**

Key path notes:
- `REPO_ROOT`: `Path(__file__).resolve().parent`
- `CLIENT_DIR`: `REPO_ROOT / "javascript-client-generated"`
- `CONFIG_FILE`: `CLIENT_DIR / "scripts" / "swagger-codegen-config.json"`
- `SPEC_PATH`: `CLIENT_DIR / "tmi-openapi.json"`

The `scripts/swagger-codegen-config.json` backup needs special handling: back up the single file (not the whole `scripts/` dir) to avoid restoring the old deleted bash script.

```python
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

PACKAGE_JSON = """\
{
  "name": "tmi-js-client",
  "version": "1.0.0",
  "description": "JavaScript client for TMI (Threat Modeling Improved) API v1.0.0",
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
    "url": "https://github.com/threagile/tmi-clients.git"
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
        "Package": "tmi-js-client",
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
    write_file(CLIENT_DIR / "package.json", PACKAGE_JSON)
    print_success("Created modern package.json")

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
            "- Package Name: tmi-js-client\n"
            "- Version: 1.0.0\n"
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
```

- [ ] **Step 2: Verify it imports and parses cleanly**

Run: `cd /Users/efitz/Projects/tmi-clients && python3 -c "import regenerate_js; print('OK')"`
Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add regenerate_js.py
git commit -m "feat: add regenerate_js.py — JavaScript client regeneration script"
```

---

### Task 8: Smoke Test All Three Scripts

**Files:** None modified — this is a validation task.

Each script should be runnable and produce correct output. Since we don't want to actually regenerate the clients (that would modify generated code), we verify the scripts at least start up, check prerequisites, and fail gracefully if we choose not to proceed.

- [ ] **Step 1: Verify `regenerate_python.py` parses cleanly**

Run: `cd /Users/efitz/Projects/tmi-clients && python3 -c "import regenerate_python; print('Parses OK')"`

- [ ] **Step 2: Verify `regenerate_go.py` runs similarly**

Run: `cd /Users/efitz/Projects/tmi-clients && python3 -c "import regenerate_go; print('Parses OK')"`

- [ ] **Step 3: Verify `regenerate_js.py` runs similarly**

Run: `cd /Users/efitz/Projects/tmi-clients && python3 -c "import regenerate_js; print('Parses OK')"`

- [ ] **Step 4: Run the Python regeneration script for real to verify end-to-end**

Run: `cd /Users/efitz/Projects/tmi-clients && python3 regenerate_python.py`

This will actually regenerate the Python client. Verify:
- All steps print with colored output
- Patches report success or clear warnings
- Tests run (results may vary)
- Report is generated at `python-client-generated/REGENERATION_REPORT.md`
- Exit code is 0 or 2 (not 1)

- [ ] **Step 5: Run the Go regeneration script**

Run: `cd /Users/efitz/Projects/tmi-clients && python3 regenerate_go.py`

Verify same criteria as step 4 but for Go client.

- [ ] **Step 6: Run the JavaScript regeneration script**

Run: `cd /Users/efitz/Projects/tmi-clients && python3 regenerate_js.py`

Verify same criteria as step 4 but for JS client.

- [ ] **Step 7: Commit any fixes discovered during smoke testing**

Stage only the specific files that were modified during smoke testing:
```bash
git add regen_common.py regenerate_python.py regenerate_go.py regenerate_js.py
git commit -m "fix: address issues found during regeneration script smoke testing"
```

---

### Task 9: Delete Old Bash Scripts

**Files:**
- Delete: `python-client-generated/scripts/regenerate_client.sh`
- Delete: `python-client-generated/scripts/regenerate_client.sh.new`
- Delete: `python-client-generated/scripts/backup_before_regen.sh`
- Delete: `go-client-generated/scripts/regenerate_client.sh`
- Delete: `javascript-client-generated/scripts/regenerate_client.sh`

- [ ] **Step 1: Delete all five bash scripts**

```bash
cd /Users/efitz/Projects/tmi-clients
rm python-client-generated/scripts/regenerate_client.sh
rm python-client-generated/scripts/regenerate_client.sh.new
rm python-client-generated/scripts/backup_before_regen.sh
rm go-client-generated/scripts/regenerate_client.sh
rm javascript-client-generated/scripts/regenerate_client.sh
```

- [ ] **Step 2: Verify the scripts directories still contain their config files**

Run: `ls python-client-generated/scripts/ go-client-generated/scripts/ javascript-client-generated/scripts/`

Expected: Each directory still contains `swagger-codegen-config.json` (and the Python one also has `analyze_spec_changes.py` and `validate_regeneration.py`).

- [ ] **Step 3: Commit**

```bash
git add python-client-generated/scripts/regenerate_client.sh python-client-generated/scripts/regenerate_client.sh.new python-client-generated/scripts/backup_before_regen.sh go-client-generated/scripts/regenerate_client.sh javascript-client-generated/scripts/regenerate_client.sh
git commit -m "chore: delete old bash regeneration scripts, replaced by Python equivalents"
```

---

### Task 10: Update `CLAUDE.md`

**Files:**
- Modify: `CLAUDE.md` (repo root at `/Users/efitz/Projects/tmi-clients/CLAUDE.md`)

- [ ] **Step 1: Update regeneration section**

Replace references to bash scripts with the new Python scripts. Key changes:
- `./scripts/regenerate_client.sh` → `python3 regenerate_python.py` (or `uv run ./regenerate_python.py`)
- Add the three new script paths
- Update any Python 3.8 references to 3.9
- Remove mention of `backup_before_regen.sh`

- [ ] **Step 2: Verify CLAUDE.md is valid markdown**

Skim the file to ensure no broken formatting.

- [ ] **Step 3: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: update CLAUDE.md with new Python regeneration script paths"
```

---

## Task Dependency Graph

```
Task 1 (output + prereqs)
  └─> Task 2 (spec + subprocess)
       └─> Task 3 (codegen + patching + file utils)
            └─> Task 4 (backup/restore + reports)
                 ├─> Task 5 (regenerate_python.py) ──┐
                 ├─> Task 6 (regenerate_go.py) ──────┼─> Task 8 (smoke test all three)
                 └─> Task 7 (regenerate_js.py) ──────┘        └─> Task 9 (delete old scripts)
                                                                        └─> Task 10 (update CLAUDE.md)
```

Tasks 5, 6, 7 can be done in parallel once Task 4 is complete. Task 8 depends on all three.
