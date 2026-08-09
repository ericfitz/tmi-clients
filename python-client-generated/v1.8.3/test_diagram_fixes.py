#!/usr/bin/env python3
"""Integration checks for the TMI Python client's diagram models.

`regenerate_python.py` runs this file (``uv run test_diagram_fixes.py``) after
regenerating, and preserves it across runs via its backup/restore step. It is
hand-written: openapi-generator emits per-model unit tests, but nothing that
exercises the behaviours this repo actually patches or documents.

Deliberately **no** uv inline script metadata. Inline metadata would make uv
build an isolated environment and resolve `tmi-client` from PyPI, which is the
opposite of what this needs — the point is to test the freshly generated client
in this directory. Without metadata, `uv run` uses the project environment and
installs the local package.

Covered:
  1. The X6 cell structure documented in CLAUDE.md validates through the
     diagram models, and `to_dict()` preserves it.
  2. The input/output schema split — `*Input` models must not carry readOnly
     fields, output models must.
  3. Native UUID/datetime values survive the regex validators. This is the
     scenario the `patch_regex_validators` fix in regenerate_python.py exists
     for: Pydantic coerces values to native types before field validators run,
     so an unguarded `re.match()` raises TypeError on a UUID or datetime.
  4. Validation still rejects genuinely invalid input, so 1 and 3 cannot pass
     by having been neutered.

Cells are built with `from_dict`, not the constructor. Passing raw dicts to the
constructor does *not* resolve the `oneOf` and silently yields empty cells —
see the KNOWN DEFECTS note at the bottom of this file.

Version-portable: asserts on the presence or absence of specific fields rather
than exact field lists, since the schema grows between API versions.
"""
from __future__ import annotations

import sys
import traceback
from datetime import datetime, timezone
from uuid import UUID

from tmi_client.models.dfd_diagram import DfdDiagram
from tmi_client.models.dfd_diagram_input import DfdDiagramInput

NODE_ID = "11111111-1111-4111-8111-111111111111"
EDGE_ID = "22222222-2222-4222-8222-222222222222"
DIAGRAM_ID = "33333333-3333-4333-8333-333333333333"

# X6 node/edge cells. Note `shape: "flow"` for the edge: the generated Edge
# model constrains shape to the enum ('flow'), even though the example in
# CLAUDE.md writes "edge".
NODE_CELL = {
    "id": NODE_ID,
    "shape": "process",
    "x": 100,
    "y": 100,
    "width": 120,
    "height": 60,
    "attrs": {"body": {"fill": "#E1F5FE"}, "text": {"text": "Component"}},
}
EDGE_CELL = {
    "id": EDGE_ID,
    "shape": "flow",
    "source": {"cell": NODE_ID},
    "target": {"cell": NODE_ID},
    "attrs": {"line": {"stroke": "#333"}},
}

READONLY_FIELDS = ("id", "created_at", "modified_at")

_results: list[tuple[str, str, str]] = []


def check(name):
    """Register a zero-arg check. Any exception is a failure."""
    def decorator(fn):
        try:
            fn()
        except Exception:  # noqa: BLE001 - a failing check must not stop the run
            _results.append((name, "FAIL", traceback.format_exc()))
        else:
            _results.append((name, "PASS", ""))
        return fn
    return decorator


def _properties(model_cls) -> list[str]:
    """Read the generated __properties list through its mangled name."""
    return getattr(model_cls, f"_{model_cls.__name__}__properties")


def _input_with_cells(cells: list[dict]) -> DfdDiagramInput:
    diagram = DfdDiagramInput.from_dict(
        {"name": "Test Diagram", "type": "DFD-1.0.0", "cells": cells}
    )
    assert diagram is not None, "from_dict returned None"
    return diagram


@check("X6 node and edge cells resolve to their oneOf variants")
def _cells_resolve() -> None:
    diagram = _input_with_cells([NODE_CELL, EDGE_CELL])
    assert len(diagram.cells) == 2, f"expected 2 cells, got {len(diagram.cells)}"
    kinds = [type(c.actual_instance).__name__ for c in diagram.cells]
    assert kinds == ["Node", "Edge"], f"oneOf resolved to {kinds}"


@check("to_dict preserves cell contents")
def _cells_serialise() -> None:
    diagram = _input_with_cells([NODE_CELL, EDGE_CELL])
    cells = diagram.to_dict()["cells"]
    assert cells and all(c is not None for c in cells), f"cells lost on to_dict: {cells}"
    assert str(cells[0]["id"]) == NODE_ID, f"node id not preserved: {cells[0].get('id')}"
    assert cells[0]["shape"] == "process", f"node shape not preserved: {cells[0]}"


@check("DfdDiagramInput excludes readOnly fields")
def _input_excludes_readonly() -> None:
    props = _properties(DfdDiagramInput)
    present = [f for f in READONLY_FIELDS if f in props]
    assert not present, f"input schema must not expose readOnly fields: {present}"
    assert "cells" in props and "name" in props, f"unexpected input schema: {props}"


@check("DfdDiagram includes readOnly fields")
def _output_includes_readonly() -> None:
    props = _properties(DfdDiagram)
    missing = [f for f in READONLY_FIELDS if f not in props]
    assert not missing, f"output schema missing readOnly fields: {missing}"


@check("native UUID and datetime values pass the regex validators")
def _native_types_accepted() -> None:
    # The regression this guards: Pydantic coerces these to UUID/datetime
    # before field validators run, so an unguarded re.match() raises
    # TypeError: expected string or bytes-like object.
    now = datetime.now(timezone.utc)
    diagram = DfdDiagram(
        id=UUID(DIAGRAM_ID),
        name="Test Diagram",
        type="DFD-1.0.0",
        created_at=now,
        modified_at=now,
        cells=[],
    )
    assert diagram.id == UUID(DIAGRAM_ID)
    assert diagram.created_at == now


@check("string UUID and datetime values are coerced and accepted")
def _string_types_accepted() -> None:
    diagram = DfdDiagram(
        id=DIAGRAM_ID,
        name="Test Diagram",
        type="DFD-1.0.0",
        created_at="2026-01-01T00:00:00Z",
        modified_at="2026-01-01T00:00:00Z",
        cells=[],
    )
    assert diagram.id == UUID(DIAGRAM_ID)
    assert isinstance(diagram.created_at, datetime)


@check("invalid UUID is still rejected")
def _invalid_uuid_rejected() -> None:
    now = datetime.now(timezone.utc)
    try:
        DfdDiagram(
            id="not-a-uuid",
            name="Test Diagram",
            type="DFD-1.0.0",
            created_at=now,
            modified_at=now,
            cells=[],
        )
    except Exception:
        return
    raise AssertionError("an invalid UUID was accepted")


@check("a cell matching neither oneOf branch is rejected")
def _invalid_cell_rejected() -> None:
    try:
        _input_with_cells([{"not_a_cell": True}])
    except Exception:
        return
    raise AssertionError("a malformed cell was accepted")


@check("an undersized node is rejected")
def _undersized_node_rejected() -> None:
    # Node constrains width >= 40 and height >= 30.
    try:
        _input_with_cells([{**NODE_CELL, "width": 2, "height": 2}])
    except Exception:
        return
    raise AssertionError("an undersized node was accepted")


def main() -> int:
    width = max(len(name) for name, _, _ in _results)
    for name, status, detail in _results:
        print(f"[{status}] {name.ljust(width)}")
        if detail:
            print(detail)
    failed = sum(1 for _, status, _ in _results if status == "FAIL")
    total = len(_results)
    print(f"\n{total - failed}/{total} checks passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())


# KNOWN DEFECTS in the generated client (not asserted here, so this file stays
# green; see the repo issue tracker):
#
# 1. Passing raw dicts as `cells` to the model constructor — the pattern shown
#    in CLAUDE.md — does not resolve the oneOf. `actual_instance` stays None and
#    `to_dict()` emits `"cells": [None, ...]`, silently discarding every cell.
#    Use `DfdDiagramInput.from_dict({...})`, as this file does.
#
# 2. `to_dict()` output cannot be fed back into `from_dict()`. to_dict() leaves
#    native UUID objects inside cells, and the oneOf wrapper's from_dict does
#    `json.dumps(obj)`, which raises
#    "TypeError: Object of type UUID is not JSON serializable".
