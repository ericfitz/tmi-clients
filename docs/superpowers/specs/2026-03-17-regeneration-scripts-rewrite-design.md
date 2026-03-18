# Design: Rewrite Regeneration Scripts in Python

## Overview

Rewrite the three bash-based client regeneration scripts (`regenerate_client.sh` for Python, Go, and JavaScript) as Python scripts with a shared utility module. The new scripts live at the repository root for easy cross-import.

## Motivation

The current bash scripts contain significant duplicated logic, inline Python patches embedded in bash heredocs, complex sed escaping, and inconsistent error handling. Rewriting in Python provides:

- A single language for all regeneration logic
- Shared utilities without duplication
- Structured error handling with actionable messages
- Easier maintenance and extension

## File Layout

### New files (repo root)

```
tmi-clients/
├── regen_common.py          # Shared utilities
├── regenerate_python.py     # Python client regeneration
├── regenerate_go.py         # Go client regeneration
├── regenerate_js.py         # JavaScript client regeneration
```

### Files deleted

- `python-client-generated/scripts/regenerate_client.sh`
- `python-client-generated/scripts/regenerate_client.sh.new`
- `python-client-generated/scripts/backup_before_regen.sh`
- `go-client-generated/scripts/regenerate_client.sh`
- `javascript-client-generated/scripts/regenerate_client.sh`

### Files unchanged

- `*/scripts/swagger-codegen-config.json` (all three)
- `python-client-generated/scripts/analyze_spec_changes.py`
- `python-client-generated/scripts/validate_regeneration.py`
- `python-client-generated/custom-templates/` (entire directory)

## Shared Module: `regen_common.py`

### Spec Management

- `download_spec(url: str, dest: Path) -> None` — Download OpenAPI spec from URL. On failure: prints the URL, HTTP status, and suggests checking network connectivity or whether the URL has changed.
- `copy_local_spec(src: Path, dest: Path) -> None` — Copy a local spec file. On failure: prints the resolved path and whether the file exists.

### Prerequisites

- `check_prerequisite(command: str, install_hint: str) -> None` — Verify a CLI tool is on PATH. On failure: prints the missing command name and the install hint (e.g., `brew install swagger-codegen`).
- `check_version(command: str, args: list[str], min_version: str, extract_pattern: str) -> None` — Verify minimum version. On failure: prints actual vs. required version and upgrade command.

### Subprocess

- `run_command(cmd: list[str], cwd: Path | None = None, capture: bool = False, env: dict | None = None, error_context: str = "") -> subprocess.CompletedProcess` — Run a command. On failure: prints the command, exit code, stderr, working directory, and the `error_context` string which describes what was being attempted and what to check.

### Code Generation

- `run_codegen(spec_path: Path, language: str, output_dir: Path, config_file: Path, template_dir: Path | None = None) -> None` — Invoke `swagger-codegen generate`. On failure: prints the full command, suggests checking the spec file for validity (`swagger-codegen validate`), and whether the config JSON is correct.

### File Patching

- `patch_file_regex(file_path: Path, pattern: str, replacement: str, description: str = "") -> bool` — Regex-based replacement. Returns True if a substitution was made. On no-match: prints a warning with the pattern and file path, suggests the generated code structure may have changed.
- `patch_file_exact(file_path: Path, old_text: str, new_text: str, description: str = "") -> bool` — Exact string replacement. Returns True if found and replaced. On no-match: prints a warning with a snippet of the expected text and suggests the codegen output may have changed.

Both patch functions accept a `description` parameter (e.g., "DfdDiagram constructor type preservation") used in success/warning messages to make output readable without knowing the implementation details.

### Backup / Restore

- `backup_files(files: list[Path], dirs: list[Path], backup_dir: Path) -> None` — Copy files and directories to backup location. Missing source files are silently skipped (they're optional custom files).
- `restore_files(backup_dir: Path, dest_dir: Path, files: list[str], dirs: list[str]) -> None` — Copy files back from backup. Missing backup files are warned about.

### Output

- `print_banner(title: str, config: dict[str, str]) -> None` — Print a formatted banner with config key-value pairs.
- `print_step(n: int, msg: str) -> None` — Print a numbered step header.
- `print_success(msg: str) -> None` — Green checkmark message.
- `print_warning(msg: str) -> None` — Yellow warning message.
- `print_error(msg: str) -> None` — Red error message.
- `print_summary(results: dict[str, str]) -> None` — Print a final summary table.

### Report Generation

- `generate_report(title: str, sections: list[dict]) -> str` — Takes a title and list of `{"heading": str, "content": str}` dicts, renders as markdown with a date header.

### File Utilities

- `count_files(directory: Path, pattern: str) -> int` — Count files matching a glob pattern.
- `write_file(path: Path, content: str) -> None` — Write content to a file, creating parent directories as needed.
- `clean_paths(paths: list[Path]) -> None` — Remove files and directories. Silently skips non-existent paths.

## Error Handling Philosophy

Every error message should answer three questions:

1. **What failed?** — The specific operation (e.g., "Failed to patch DfdDiagram constructor")
2. **Why might it have failed?** — The likely cause (e.g., "The generated code structure may have changed")
3. **What should the user do?** — A concrete next step (e.g., "Check tmi_client/models/dfd_diagram.py for the __init__ method signature")

### Error severity levels:

- **Fatal errors** (`sys.exit(1)`): Prerequisites missing, codegen fails, spec download fails. These stop the script.
- **Warnings** (continue execution): A patch didn't match (code structure may have changed), optional custom file not found in backup, some tests failed. These print a warning and continue. The final summary highlights all warnings.
- **Patch failures are warnings, not fatals.** A patch not matching likely means codegen output changed. The script should continue so the user can inspect the generated code and update the patches. The final summary clearly lists which patches succeeded and which didn't.

### Test failures:

Test failures are reported but do not cause `sys.exit(1)`. The exit code reflects:
- 0: Everything succeeded including tests
- 1: Fatal error (codegen failed, etc.)
- 2: Completed but with test failures or failed patches

This lets CI distinguish between "broken script" and "regenerated but needs attention."

## Script Structure

Each language script follows the same flow:

```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///

def main(spec_path: str | None = None) -> int:
    # 1. Print banner
    # 2. Check prerequisites
    # 3. Download/copy spec
    # 4. Backup custom files
    # 5. Clean generated files
    # 6. Run swagger-codegen
    # 7. Apply patches (language-specific)
    # 8. Write/update config files (language-specific)
    # 9. Restore custom files
    # 10. Install dependencies (language-specific)
    # 11. Run tests (language-specific)
    # 12. Generate report
    # 13. Cleanup
    # 14. Print summary
    # Returns exit code (0, 1, or 2)

if __name__ == "__main__":
    spec = sys.argv[1] if len(sys.argv) > 1 else None
    sys.exit(main(spec))
```

## Language-Specific Details

### Python (`regenerate_python.py`)

**Prerequisites:** `swagger-codegen`, `uv`

**Patches:**
1. DfdDiagram constructor — insert `kwargs['type'] = type` before `BaseDiagram.__init__`
2. DfdDiagramInput constructor — insert `kwargs['type'] = type` before `BaseDiagramInput.__init__`
3. Edge constructor — insert `kwargs['shape'] = shape` before `Cell.__init__`
4. Node constructor — insert `kwargs['shape'] = shape` before `Cell.__init__`
5. Configuration.auth_settings() — replace empty `return {}` with bearerAuth implementation

**Config files written:**
- `pyproject.toml` (full content)
- `setup.py` (patched in-place for version/deps)
- `requirements.txt` (written fresh)
- `test-requirements.txt` (written fresh)
- `tox.ini` (written fresh)

**Custom files backed up/restored:**
- `pyproject.toml`, `test_diagram_fixes.py`, `.swagger-codegen-ignore`

**Codegen uses custom templates:** `custom-templates/python/`

**Tests:**
- `uv run --with pytest python3 -m pytest test/ -v --tb=short`
- `uv run test_diagram_fixes.py` (integration, if present)

**Report:** `python-client-generated/REGENERATION_REPORT.md`

### Go (`regenerate_go.py`)

**Prerequisites:** `swagger-codegen`, `go` (>= 1.21)

**Patches:**
1. RevokeToken form params — replace `localVarPostBody = &body` with form parameter additions in `api_authentication.go`

**Config files written/patched:**
- `go.mod` — patch module path and Go version, or create fresh if missing

**Custom files backed up/restored:**
- `go.mod`, `go.sum`, `.swagger-codegen-ignore`, `docs/developer/`, `*_test.go`, `model_object.go`, `model_cell_data.go`, `model_model_map.go`

**Build & test:**
- `go mod tidy`
- `go build ./...`
- `go test -v ./...`
- Integration test via `go test -v -run TestDiagramFixes` (if `diagram_fixes_test.go` exists)

**Report:** `go-client-generated/REGENERATION_REPORT.md`

### JavaScript (`regenerate_js.py`)

**Prerequisites:** `swagger-codegen`, `node` (>= 18)

**Patches:**
1. AllOf enum inheritance — scan `src/model/AllOf*.js`, detect classes extending `const` enum objects, rewrite as non-extending classes
2. Enum export unwrapping — fix `export default {EnumName};` to `export default EnumName;` across `src/model/*.js`
3. Subclass constructor parameter forwarding — parse constructor/super() signatures, add missing params to constructor

**Config files written:**
- `package.json` (written fresh with modern deps)
- `.babelrc` (written fresh)

**Custom files backed up/restored:**
- `package.json`, `.babelrc`, `test_diagram_fixes.js`, `.swagger-codegen-ignore`, `PRE_REGENERATION_AUDIT.md`, `docs/developer/`, `scripts/`

**Build & test:**
- `npm install`
- `npm test`
- `node test_diagram_fixes.js` (integration, if present)

**Report:** `javascript-client-generated/REGENERATION_REPORT.md`

## Exit Codes

All three scripts use the same exit code convention:

| Code | Meaning |
|------|---------|
| 0 | Success — codegen, patches, and tests all passed |
| 1 | Fatal error — script could not complete (missing prereqs, codegen failure, spec download failure) |
| 2 | Completed with issues — patches that didn't match, test failures, or build failures |

## CLAUDE.md Updates

After implementation, update `CLAUDE.md` at the repo root to reflect:
- New script locations and names
- `uv run ./regenerate_python.py [spec_path]` usage
- Removal of bash scripts

## Non-Goals

- No changes to `analyze_spec_changes.py` or `validate_regeneration.py`
- No changes to swagger-codegen config JSON files
- No changes to custom Mustache templates
- No changes to the generated client code itself
- No new testing framework — scripts are validated by running them
