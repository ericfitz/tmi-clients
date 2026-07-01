# Python Client Migration to openapi-generator — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Migrate the Python client generation from swagger-codegen 3.0.75 to openapi-generator 7.21.0, eliminating all manual patches and producing Pydantic v2 typed models.

**Architecture:** Update `regen_common.py` to be tool-agnostic (supporting both swagger-codegen and openapi-generator), rewrite `regenerate_python.py` to use openapi-generator with no custom templates, add one new patch for a UUID regex validator bug in openapi-generator, update integration tests for Pydantic v2 models, clean up stale artifacts, and regenerate from scratch.

**Tech Stack:** openapi-generator 7.21.0 (Homebrew), Python 3.9+, Pydantic v2, urllib3, pytest, uv

---

### Task 1: Update `regen_common.py` to Support Both Codegen Tools

**Files:**
- Modify: `regen_common.py:259-292` (the `run_codegen` function)

- [ ] **Step 1: Add the `run_codegen_openapi_generator` function**

Add a new function alongside the existing `run_codegen` (which remains for Go/JS). Insert after line 292:

```python
def run_codegen_openapi_generator(
    spec_path: str | Path,
    generator: str,
    output_dir: str | Path,
    config_file: str | Path | None = None,
) -> None:
    """Invoke openapi-generator to generate a client.

    Exits with code 1 if code generation fails.
    """
    cmd: list[str] = [
        "openapi-generator",
        "generate",
        "-i", str(spec_path),
        "-g", generator,
        "-o", str(output_dir),
    ]
    if config_file is not None:
        cmd.extend(["-c", str(config_file)])

    print(f"  Running: {' '.join(cmd)}")
    result = run_command(cmd, error_context="openapi-generator generate")
    if result.returncode != 0:
        print_error(
            "Code generation failed.\n"
            f"  Command: {' '.join(cmd)}\n"
            f"  Exit code: {result.returncode}\n"
            "  Check the openapi-generator output above for details."
        )
        sys.exit(1)
    print_success(f"Code generation complete → {output_dir}")
```

- [ ] **Step 2: Verify Go/JS scripts still import and use `run_codegen` without error**

Run:
```bash
python3 -c "from regen_common import run_codegen; print('OK')"
```
Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add regen_common.py
git commit -m "feat: add openapi-generator support to regen_common.py

Add run_codegen_openapi_generator() function alongside existing
run_codegen() for swagger-codegen. Go/JS scripts are unaffected."
```

---

### Task 2: Rewrite `regenerate_python.py` for openapi-generator

**Files:**
- Modify: `regenerate_python.py` (full rewrite of main logic)
- Rename: `python-client-generated/scripts/swagger-codegen-config.json` → `python-client-generated/scripts/openapi-generator-config.json`

- [ ] **Step 1: Rename the config file**

```bash
mv python-client-generated/scripts/swagger-codegen-config.json python-client-generated/scripts/openapi-generator-config.json
```

- [ ] **Step 2: Rewrite `regenerate_python.py`**

Replace the entire file with the following. Key changes from the original:
- Imports `run_codegen_openapi_generator` instead of `run_codegen`
- References `openapi-generator-config.json` instead of `swagger-codegen-config.json`
- Removes `TEMPLATE_DIR` (no custom templates)
- Removes all patch constants (`AUTH_SETTINGS_OLD`, `AUTH_SETTINGS_NEW`)
- Removes all patch functions (`apply_constructor_patch`, `apply_patches`, `patch_setup_py`)
- Removes config file templates (`PYPROJECT_TOML`, `REQUIREMENTS_TXT`, `TEST_REQUIREMENTS_TXT`, `TOX_INI`)
- Adds one new patch: UUID regex validator fix
- Prerequisite check is `openapi-generator` instead of `swagger-codegen`
- Codegen call uses `-g python` instead of `-l python`
- Backs up `.openapi-generator-ignore` instead of `.swagger-codegen-ignore`
- No longer writes `pyproject.toml`, `requirements.txt`, `test-requirements.txt`, `tox.ini` — openapi-generator generates acceptable versions
- Cleans `.openapi-generator/` metadata directory

```python
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


def patch_uuid_regex_validators(had_issues: bool) -> bool:
    """Fix openapi-generator bug: regex validators on UUID fields fail because
    Pydantic parses the value to a UUID object before the validator runs.

    The fix: insert ``value = str(value)`` at the start of each validator
    function that applies re.match() to a UUID-typed field.
    """
    models_dir = CLIENT_DIR / "tmi_client" / "models"
    if not models_dir.is_dir():
        print_warning("Models directory not found — skipping UUID validator patch")
        return True

    patched_count = 0
    for model_file in sorted(models_dir.glob("*.py")):
        content = model_file.read_text(encoding="utf-8")

        # Find UUID fields
        uuid_fields = set(re.findall(r"(\w+):\s*(?:Optional\[)?(?:Annotated\[)?UUID", content))
        if not uuid_fields:
            continue

        new_content = content
        for field_name in uuid_fields:
            # Find validator functions for this field that use re.match
            # Pattern: @field_validator('field_name')\n    def ...(cls, value):\n        ...re.match...
            pattern = (
                rf"(@field_validator\('{field_name}'\)\s*\n"
                rf"    def \w+\(cls, value\):\s*\n)"
                rf"(        \"\"\".*?\"\"\"\s*\n)"
            )
            matches = list(re.finditer(pattern, new_content))
            for m in matches:
                # Check if this validator uses re.match
                # Find the end of this validator (next def or class-level attribute)
                start = m.start()
                rest = new_content[m.end():]
                if "re.match" not in rest[:500]:  # look ahead in the validator body
                    continue

                # Insert str(value) conversion after the docstring
                insert_point = m.end()
                insert_text = "        value = str(value)\n"
                if insert_text not in new_content[insert_point:insert_point + 100]:
                    new_content = new_content[:insert_point] + insert_text + new_content[insert_point:]
                    patched_count += 1

        if new_content != content:
            model_file.write_text(new_content, encoding="utf-8")

    if patched_count > 0:
        print_success(f"UUID regex validator patch: {patched_count} validators fixed")
    else:
        print_warning("UUID regex validator patch: no validators needed fixing")

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
            CLIENT_DIR / "pyproject.toml",
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
    had_issues = patch_uuid_regex_validators(had_issues)
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
            "- UUID regex validator fix (openapi-generator bug: "
            "regex validators on UUID fields fail because Pydantic parses "
            "the value to UUID before the validator runs)\n\n"
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
        "Patches": "UUID regex fix" + (" (with warnings)" if had_issues else ""),
        "Tests": "see logs for results",
        "Report": "REGENERATION_REPORT.md",
    })

    return 2 if had_issues else 0


if __name__ == "__main__":
    spec = sys.argv[1] if len(sys.argv) > 1 else None
    sys.exit(main(spec))
```

- [ ] **Step 3: Verify the script parses correctly**

Run:
```bash
python3 -c "import regenerate_python; print('OK')"
```
Expected: `OK`

- [ ] **Step 4: Commit**

```bash
git add regenerate_python.py python-client-generated/scripts/openapi-generator-config.json
git rm python-client-generated/scripts/swagger-codegen-config.json
git commit -m "feat: rewrite regenerate_python.py for openapi-generator

Switch from swagger-codegen to openapi-generator 7.x.
Remove all swagger-codegen patches (constructor fixes, auth_settings,
duplicate revoke_token, setup.py patching).
Add UUID regex validator patch for openapi-generator bug.
Remove custom template reference."
```

---

### Task 3: Update Integration Tests for Pydantic v2 Models

**Files:**
- Modify: `python-client-generated/test_diagram_fixes.py`

The integration test needs updates for Pydantic v2:
- Edge `source`/`target` now require `EdgeTerminal` objects (or dicts with valid UUIDs), not plain `{"cell": "node1"}` strings
- `DfdDiagram` cells now require typed objects, not plain dicts
- All UUID fields require valid UUID format strings

- [ ] **Step 1: Rewrite `test_diagram_fixes.py`**

Replace the entire file:

```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "tmi-client",
#     "pydantic",
# ]
# ///
"""
Integration test to verify the openapi-generator Python client works correctly.

Validates:
1. DfdDiagram can be instantiated with type parameter
2. DfdDiagramInput can be instantiated with type parameter
3. Type parameter is preserved after construction
4. to_dict() serialization works correctly
5. Inheritance from Base classes works properly
6. Cell schemas (Edge, Node) exist and can be instantiated
7. Webhook schemas exist and can be instantiated
"""

import sys


def test_dfd_diagram_instantiation():
    """Test 1: DfdDiagram can be instantiated with type parameter"""
    print("Test 1: DfdDiagram instantiation...")
    from tmi_client.models.dfd_diagram import DfdDiagram

    diagram = DfdDiagram(
        type="DFD-1.0.0",
        cells=[],
        name="Test Diagram",
        id="00000000-0000-0000-0000-000000000001",
        created_at="2025-01-01T00:00:00Z",
        modified_at="2025-01-01T00:00:00Z",
    )

    assert diagram is not None, "Failed to instantiate DfdDiagram"
    assert diagram.type == "DFD-1.0.0", f"Type not preserved: {diagram.type}"
    assert diagram.name == "Test Diagram", "Name not set correctly"
    print("  DfdDiagram instantiation successful")


def test_dfd_diagram_input_instantiation():
    """Test 2: DfdDiagramInput can be instantiated with type parameter"""
    print("\nTest 2: DfdDiagramInput instantiation...")
    from tmi_client.models.dfd_diagram_input import DfdDiagramInput

    diagram_input = DfdDiagramInput(
        type="DFD-1.0.0",
        cells=[],
        name="Test Diagram Input",
    )

    assert diagram_input is not None, "Failed to instantiate DfdDiagramInput"
    assert diagram_input.type == "DFD-1.0.0", f"Type not preserved: {diagram_input.type}"
    assert diagram_input.name == "Test Diagram Input", "Name not set correctly"
    print("  DfdDiagramInput instantiation successful")


def test_type_parameter_preservation():
    """Test 3: Type parameter is preserved after construction"""
    print("\nTest 3: Type parameter preservation...")
    from tmi_client.models.dfd_diagram import DfdDiagram
    from tmi_client.models.dfd_diagram_input import DfdDiagramInput

    diagram = DfdDiagram(
        type="DFD-1.0.0",
        cells=[],
        name="Test",
        id="00000000-0000-0000-0000-000000000001",
        created_at="2025-01-01T00:00:00Z",
        modified_at="2025-01-01T00:00:00Z",
    )
    assert diagram.type == "DFD-1.0.0", "DfdDiagram type was overwritten"

    diagram_input = DfdDiagramInput(type="DFD-1.0.0", cells=[], name="Test")
    assert diagram_input.type == "DFD-1.0.0", "DfdDiagramInput type was overwritten"

    print("  Type parameter preserved in both classes")


def test_serialization():
    """Test 4: to_dict() serialization works correctly"""
    print("\nTest 4: Serialization...")
    from tmi_client.models.dfd_diagram import DfdDiagram
    from tmi_client.models.dfd_diagram_input import DfdDiagramInput

    diagram = DfdDiagram(
        type="DFD-1.0.0",
        cells=[],
        name="Serialization Test",
        id="00000000-0000-0000-0000-000000000001",
        created_at="2025-01-01T00:00:00Z",
        modified_at="2025-01-01T00:00:00Z",
    )

    diagram_dict = diagram.to_dict()
    assert diagram_dict["type"] == "DFD-1.0.0", "Type not in serialized dict"
    assert diagram_dict["name"] == "Serialization Test", "Name not in serialized dict"

    diagram_input = DfdDiagramInput(
        type="DFD-1.0.0",
        cells=[],
        name="Input Serialization Test",
    )

    input_dict = diagram_input.to_dict()
    assert input_dict["type"] == "DFD-1.0.0", "Type not in input serialized dict"
    assert input_dict["name"] == "Input Serialization Test", "Name not in input dict"

    print("  Serialization working correctly")


def test_inheritance():
    """Test 5: Inheritance from Base classes works properly"""
    print("\nTest 5: Inheritance...")
    from tmi_client.models.dfd_diagram import DfdDiagram
    from tmi_client.models.dfd_diagram_input import DfdDiagramInput
    from tmi_client.models.base_diagram import BaseDiagram
    from tmi_client.models.base_diagram_input import BaseDiagramInput

    diagram = DfdDiagram(
        type="DFD-1.0.0",
        cells=[],
        name="Test",
        id="00000000-0000-0000-0000-000000000001",
        created_at="2025-01-01T00:00:00Z",
        modified_at="2025-01-01T00:00:00Z",
    )
    assert isinstance(diagram, BaseDiagram), "DfdDiagram not instance of BaseDiagram"
    assert isinstance(diagram, DfdDiagram), "DfdDiagram not instance of itself"

    diagram_input = DfdDiagramInput(type="DFD-1.0.0", cells=[], name="Test")
    assert isinstance(diagram_input, BaseDiagramInput), "DfdDiagramInput not instance of BaseDiagramInput"
    assert isinstance(diagram_input, DfdDiagramInput), "DfdDiagramInput not instance of itself"

    print("  Inheritance working correctly")


def test_cell_schemas():
    """Test 6: Cell schemas exist and can be imported"""
    print("\nTest 6: Cell schemas...")
    from tmi_client.models.edge import Edge
    from tmi_client.models.node import Node
    from tmi_client.models.cell import Cell
    from tmi_client.models.edge_terminal import EdgeTerminal

    assert Edge is not None, "Edge class not found"
    assert Node is not None, "Node class not found"
    assert Cell is not None, "Cell class not found"

    edge = Edge(
        id="00000000-0000-0000-0000-000000000001",
        shape="flow",
        source=EdgeTerminal(cell="00000000-0000-0000-0000-000000000002"),
        target=EdgeTerminal(cell="00000000-0000-0000-0000-000000000003"),
    )
    assert str(edge.id) == "00000000-0000-0000-0000-000000000001", "Edge id not set correctly"
    assert edge.shape == "flow", "Edge shape not set correctly"

    print("  Cell schemas exist and work correctly")


def test_webhooks():
    """Test 7: Webhook schemas exist and can be instantiated"""
    print("\nTest 7: Webhook schemas...")
    from tmi_client.models.webhook_subscription import WebhookSubscription
    from tmi_client.models.webhook_subscription_input import WebhookSubscriptionInput
    from tmi_client.models.webhook_delivery import WebhookDelivery

    webhook_input = WebhookSubscriptionInput(
        name="Test Webhook",
        url="https://example.com/webhook",
        events=["threat_model.created", "diagram.updated"],
    )
    assert webhook_input is not None, "Failed to create WebhookSubscriptionInput"
    assert webhook_input.url == "https://example.com/webhook", "Webhook URL not set"
    assert webhook_input.name == "Test Webhook", "Webhook name not set"

    print("  Webhook schemas working correctly")


def main():
    """Run all tests"""
    print("=" * 60)
    print("TMI Python Client Integration Tests")
    print("=" * 60)

    tests = [
        test_dfd_diagram_instantiation,
        test_dfd_diagram_input_instantiation,
        test_type_parameter_preservation,
        test_serialization,
        test_inheritance,
        test_cell_schemas,
        test_webhooks,
    ]

    failed = []

    for test in tests:
        try:
            test()
        except Exception as e:
            print(f"  {test.__name__} FAILED: {e}")
            failed.append((test.__name__, e))

    print("\n" + "=" * 60)
    if failed:
        print(f"FAILED: {len(failed)} out of {len(tests)} tests failed")
        for name, error in failed:
            print(f"  - {name}: {error}")
        sys.exit(1)
    else:
        print(f"SUCCESS: All {len(tests)} tests passed!")
        print("=" * 60)
        sys.exit(0)


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Commit**

```bash
git add python-client-generated/test_diagram_fixes.py
git commit -m "feat: update integration tests for Pydantic v2 models

Use valid UUIDs for id fields, EdgeTerminal objects for edge
source/target, remove swagger_types/attribute_map references."
```

---

### Task 4: Clean Up Stale Artifacts

**Files:**
- Delete: `python-client-generated/custom-templates/python/` (22 Mustache template files)
- Delete: `spike-openapi-generator/` (spike output directory)
- Modify: `.gitignore` (add `.openapi-generator/`, remove spike entry)
- Create: `python-client-generated/.openapi-generator-ignore` (replace `.swagger-codegen-ignore`)

- [ ] **Step 1: Delete custom templates**

```bash
rm -rf python-client-generated/custom-templates/python/
```

If `custom-templates/` is now empty, remove it too:
```bash
rmdir python-client-generated/custom-templates/ 2>/dev/null || true
```

- [ ] **Step 2: Delete spike directory**

```bash
rm -rf spike-openapi-generator/
```

- [ ] **Step 3: Create `.openapi-generator-ignore`**

Check if `.swagger-codegen-ignore` exists and has content worth preserving:
```bash
cat python-client-generated/.swagger-codegen-ignore 2>/dev/null
```

Create `python-client-generated/.openapi-generator-ignore` with equivalent content. At minimum:
```
# Custom files that should not be overwritten by codegen
test_diagram_fixes.py
docs/developer/**
```

Remove the old file:
```bash
rm -f python-client-generated/.swagger-codegen-ignore
```

- [ ] **Step 4: Update `.gitignore`**

In the repo root `.gitignore`, replace `spike-openapi-generator/**` with entries for generated metadata:

```gitignore
.claude/settings.local.json
backups
backups/**
test_output.log
__pycache__/
python-client-generated/.openapi-generator/
```

- [ ] **Step 5: Commit**

```bash
git rm -r python-client-generated/custom-templates/python/
git rm -f python-client-generated/.swagger-codegen-ignore
git add python-client-generated/.openapi-generator-ignore
git add .gitignore
git commit -m "chore: clean up swagger-codegen artifacts

Delete custom Mustache templates (not needed with openapi-generator).
Delete spike output directory.
Replace .swagger-codegen-ignore with .openapi-generator-ignore.
Update .gitignore for openapi-generator metadata."
```

---

### Task 5: Regenerate Python Client and Verify

**Files:**
- All files under `python-client-generated/` will be regenerated

- [ ] **Step 1: Run regeneration with the GitHub spec (default)**

```bash
python3 regenerate_python.py
```

Expected: Exits 0. Output shows all steps completing, UUID patch applied, tests passing.

- [ ] **Step 2: Verify the UUID regex patch was applied**

```bash
grep -r "value = str(value)" python-client-generated/tmi_client/models/ | head -5
```

Expected: Multiple matches showing the `str(value)` conversion was inserted.

- [ ] **Step 3: Run auto-generated tests independently**

```bash
cd python-client-generated && uv run --with pytest python3 -m pytest test/ -v --tb=short
```

Expected: All tests pass.

- [ ] **Step 4: Run integration test independently**

```bash
cd python-client-generated && uv run test_diagram_fixes.py
```

Expected: All 7 tests pass.

- [ ] **Step 5: Verify Pydantic models work correctly**

```bash
cd python-client-generated && uv run --with pydantic python3 -c "
from tmi_client.models.dfd_diagram import DfdDiagram
from tmi_client.models.edge import Edge
from tmi_client.models.edge_terminal import EdgeTerminal

# Test DfdDiagram
d = DfdDiagram(type='DFD-1.0.0', cells=[], name='Test',
               id='00000000-0000-0000-0000-000000000001',
               created_at='2025-01-01T00:00:00Z',
               modified_at='2025-01-01T00:00:00Z')
print(f'DfdDiagram: type={d.type}, name={d.name}')
print(f'Dict keys: {list(d.to_dict().keys())}')

# Test Edge with EdgeTerminal
e = Edge(id='00000000-0000-0000-0000-000000000010',
         shape='flow',
         source=EdgeTerminal(cell='00000000-0000-0000-0000-000000000002'),
         target=EdgeTerminal(cell='00000000-0000-0000-0000-000000000003'))
print(f'Edge: shape={e.shape}, source={e.source.cell}')
print('All OK')
"
```

Expected: Prints model details and `All OK`.

- [ ] **Step 6: Commit the regenerated client**

```bash
cd /path/to/tmi-clients
git add python-client-generated/
git commit -m "feat: regenerate Python client with openapi-generator 7.x

Pydantic v2 models with full type hints, field validation, and
modern Python packaging. All swagger-codegen patches eliminated.
UUID regex validator patch applied for openapi-generator bug."
```

---

### Task 6: Update CLAUDE.md and Documentation

**Files:**
- Modify: `CLAUDE.md` (repo root)
- Modify: `docs/superpowers/specs/2026-04-05-openapi-generator-migration-design.md` (mark as completed)

- [ ] **Step 1: Update CLAUDE.md references to swagger-codegen**

In the repo root `CLAUDE.md`, update:
- Change "swagger-codegen 3.0.75" references to "openapi-generator 7.x (Python), swagger-codegen 3.0.75 (Go, JavaScript)"
- Update the regeneration command example for Python to mention openapi-generator
- Update the "Requirements" line: add `openapi-generator` alongside `swagger-codegen`
- Remove references to "6 critical OpenAPI issues" / patches for the Python client since they no longer apply
- Remove references to `custom-templates/` directory for Python

- [ ] **Step 2: Commit documentation updates**

```bash
git add CLAUDE.md
git commit -m "docs: update CLAUDE.md for openapi-generator migration

Python client now uses openapi-generator. Go and JavaScript remain
on swagger-codegen."
```
