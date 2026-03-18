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

import shutil
import sys
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
    """Verify minimum version of a tool. Prints warning if below minimum."""
    import re
    import subprocess

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
            # Simple version comparison (works for dotted versions)
            from packaging.version import Version  # noqa: avoid if unavailable
        else:
            print_warning(
                f"Could not determine {command} version from output.\n"
                f"  Expected pattern: {extract_pattern}\n"
                f"  Got: {output.strip()[:200]}"
            )
    except FileNotFoundError:
        pass  # check_prerequisite should have caught this
    except Exception as e:
        print_warning(f"Version check for {command} failed: {e}")
```

Wait — the spec says no external dependencies. `packaging.version` is not stdlib. Let me use a simple tuple comparison instead.

Replace the `check_version` function with:

```python
def check_version(
    command: str,
    args: list[str],
    min_version: str,
    extract_pattern: str,
) -> None:
    """Verify minimum version of a tool. Prints warning if below minimum."""
    import re
    import subprocess

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

Append to `regen_common.py`:

```python
import subprocess
import urllib.request
import urllib.error


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
    import os

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
import re


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
import glob as glob_module


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
from datetime import datetime


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

The script must:
1. Print banner with config (package: tmi_client, Python: 3.9+, testing: pytest)
2. Check prerequisites: `swagger-codegen`, `uv`
3. Download or copy spec (accept optional CLI arg for local path)
4. Backup: `pyproject.toml`, `test_diagram_fixes.py`, `.swagger-codegen-ignore`
5. Clean: `tmi_client/`, `test/`, `docs/*.md`, `.gitignore`, `.travis.yml`, `git_push.sh`, `README.md`
6. Run codegen with custom templates (`custom-templates/python/`)
7. Apply 5 patches:
   - DfdDiagram constructor: regex insert `kwargs['type'] = type` before `BaseDiagram.__init__`
   - DfdDiagramInput constructor: same, before `BaseDiagramInput.__init__`
   - Edge constructor: regex insert `kwargs['shape'] = shape` before `Cell.__init__`
   - Node constructor: same pattern
   - Configuration.auth_settings(): exact replace empty `return {}` with bearerAuth impl
8. Write config files: `pyproject.toml`, patch `setup.py`, write `requirements.txt`, `test-requirements.txt`, `tox.ini`
9. Restore backed-up files (pyproject.toml overwrites the one written in step 8)
10. Install deps: `uv pip install -e . --quiet`
11. Run tests: pytest and integration test
12. Generate report to `REGENERATION_REPORT.md` (client root)
13. Cleanup backup dir
14. Print summary

The config file contents (pyproject.toml, requirements.txt, etc.) should be taken verbatim from the existing bash script (lines 259-383 of `regenerate_client.sh`).

The patch patterns should be ported from the bash script's sed commands (lines 150-249).

Exit codes: 0 (all good), 1 (fatal before codegen), 2 (completed with issues).

Key implementation notes:
- Use `from __future__ import annotations`
- Use `# /// script` uv metadata header with `requires-python = ">=3.9"` and `dependencies = []`
- All paths relative to the python-client-generated directory (resolved via `Path(__file__).parent / "python-client-generated"`)
- Track `had_issues = False` flag, flip to True on patch failures or test failures
- Return 2 if `had_issues`, 0 otherwise

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

The script must:
1. Print banner (package: tmiclient, Go: 1.21+)
2. Check prerequisites: `swagger-codegen`, `go` (with version check >= 1.21)
3. Download or copy spec
4. Backup: `go.mod`, `go.sum`, `.swagger-codegen-ignore`, `docs/developer/`, `*_test.go`, `model_object.go`, `model_cell_data.go`, `model_model_map.go`
5. Clean: `model_*.go`, `api_*.go`, `client.go`, `configuration.go`, `response.go`, `utils.go`, `api/`, `docs/`, `README.md`, `git_push.sh`, `.travis.yml`
6. Run codegen (language: `"go"`, no custom templates)
7. Apply patch: RevokeToken form params in `api_authentication.go` — exact replace `localVarPostBody = &body` with form param additions (port from bash script lines 216-245)
8. Patch/create `go.mod` (module path, Go version)
9. Restore custom files (go.mod, go.sum, test files, custom model files)
10. Run `go mod tidy`
11. Run `go build ./...` and `go test -v ./...`; integration test if `diagram_fixes_test.go` exists
12. Generate report to `REGENERATION_REPORT.md` (client root)
13. Cleanup
14. Print summary

Key notes:
- Go backup of `*_test.go` requires globbing the client dir for `*_test.go` files
- The `go.mod` patch uses `patch_file_regex` to update module path and Go version
- If `go.mod` doesn't exist after codegen, write a fresh one (content from bash script lines 165-174)

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

The script must:
1. Print banner (package: tmi-js-client, Node.js: 18+)
2. Check prerequisites: `swagger-codegen`, `node` (with version check >= 18)
3. Download or copy spec
4. Backup: `package.json`, `.babelrc`, `test_diagram_fixes.js`, `.swagger-codegen-ignore`, `PRE_REGENERATION_AUDIT.md`, `docs/developer/`, `scripts/swagger-codegen-config.json`
5. Clean: `src/`, `test/api/`, `test/model/`, `docs/`, `README.md`, `git_push.sh`, `mocha.opts`, `.travis.yml`
6. Run codegen (language: `"javascript"`, no custom templates)
7. Apply 3 patches:
   - **`fix_allof_enum_inheritance(client_dir)`** — function in this script. Iterate `src/model/AllOf*.js`, extract parent from `extends` clause, read parent file, check for `const ParentName = {` pattern. If match, rewrite the AllOf file as a non-extending class. Port logic from bash script lines 228-268.
   - **Enum export unwrapping** — use `patch_file_regex` across all `src/model/*.js` files: pattern `^export default \{(\w+)\};$` → `export default \1;`. Port from bash lines 274-289.
   - **`fix_constructor_forwarding(client_dir)`** — function in this script. For each `src/model/*.js`, regex-extract `constructor(...)` and `super(...)` args, find missing params, rewrite constructor line. Port from bash lines 295-329 (the inline Python block).
8. Write config: `package.json` (content from bash lines 380-419), `.babelrc`
9. Restore custom files
10. Run `npm install`
11. Run `npm test`; `node test_diagram_fixes.js` if present
12. Generate report to `REGENERATION_REPORT.md`
13. Cleanup
14. Print summary

Key notes:
- The AllOf enum fix and constructor forwarding fix are complex enough to be standalone functions within this script (not in `regen_common.py`)
- The `scripts/swagger-codegen-config.json` backup needs special handling: back up the single file, not the whole `scripts/` dir

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

- [ ] **Step 1: Verify `regenerate_python.py` runs with `--help` or dry startup**

Run: `cd /Users/efitz/Projects/tmi-clients && python3 regenerate_python.py --help 2>&1 || python3 -c "import regenerate_python; print('Parses OK')"`

Verify the script can be imported without errors. If it has an argparse-based CLI, verify `--help` works.

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

```bash
git add -A
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
git add -A
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
                 ├─> Task 5 (regenerate_python.py)
                 ├─> Task 6 (regenerate_go.py)
                 └─> Task 7 (regenerate_js.py)
                      └─> Task 8 (smoke test all three)
                           └─> Task 9 (delete old scripts)
                                └─> Task 10 (update CLAUDE.md)
```

Tasks 5, 6, 7 can be done in parallel once Task 4 is complete.
