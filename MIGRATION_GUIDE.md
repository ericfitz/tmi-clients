# TMI OpenAPI Client Migration Guide

## Overview

This guide documents the changes made to the TMI OpenAPI specification and Python client to resolve critical bugs and improve type consistency.

**Version**: Regenerated from tmi-openapi.json (2025-11-04)

## Summary of Changes

All 6 issues documented in [OPENAPI_ISSUES_SUMMARY.md](OPENAPI_ISSUES_SUMMARY.md) have been resolved:

### ✅ Issue 1: DfdDiagram Inheritance Bug (CRITICAL) - FIXED
- **Problem**: Could not instantiate `DfdDiagram` objects - type field was overwritten to `None`
- **Fix**: Applied constructor patch to pass `type` to parent `BaseDiagram.__init__()`
- **Status**: Fixed in both `DfdDiagram` and `DfdDiagramInput`

### ✅ Issue 2: Inconsistent Return Types - FIXED
- **Problem**: API methods returned mix of `dict` and objects
- **Fix**: All endpoints now use specific `DfdDiagram` type (not generic `Diagram`)
- **Status**: Complete - no more `isinstance()` checks needed

### ✅ Issue 3: ReadOnly Fields in Constructors - FIXED
- **Problem**: `BaseDiagram` required `id`, `created_at`, `modified_at` (all readOnly)
- **Fix**: Created separate `DfdDiagramInput` and `BaseDiagramInput` schemas
- **Status**: Complete - UPDATE operations now work correctly

### ✅ Issue 4: Empty Diagram Base Class - DOCUMENTED
- **Problem**: `Diagram` wrapper class had no properties
- **Fix**: Marked as deprecated in OpenAPI spec
- **Status**: Kept for backward compatibility but deprecated

### ✅ Issue 5: DiagramListItem Relationship - DOCUMENTED
- **Problem**: Unclear relationship between list and detail schemas
- **Fix**: Added comprehensive documentation to `DiagramListItem`
- **Status**: Relationship now clearly documented

### ✅ Issue 6: Discriminator Mapping - FIXED
- **Problem**: Missing `x-discriminator-value` annotations
- **Fix**: Added to `DfdDiagram` and `DfdDiagramInput`
- **Status**: Complete

---

## Breaking Changes

### 1. New Schema: `DfdDiagramInput`

**For PUT/PATCH operations**, use the new `DfdDiagramInput` class instead of `DfdDiagram`.

#### Before (BROKEN):
```python
from swagger_client.models.dfd_diagram import DfdDiagram

# This FAILED because readOnly fields were required
diagram_update = DfdDiagram(
    id="...",  # ❌ readOnly - shouldn't be in input
    created_at="...",  # ❌ readOnly - shouldn't be in input
    modified_at="...",  # ❌ readOnly - shouldn't be in input
    type="DFD-1.0.0",
    name="Updated Name",
    cells=[...]
)
api.update_threat_model_diagram(diagram_update, tm_id, diagram_id)
```

#### After (CORRECT):
```python
from swagger_client.models.dfd_diagram_input import DfdDiagramInput

# This WORKS - no readOnly fields needed
diagram_update = DfdDiagramInput(
    type="DFD-1.0.0",
    name="Updated Name",
    cells=[...]
)
api.update_threat_model_diagram(diagram_update, tm_id, diagram_id)
```

### 2. API Method Return Types

All diagram-related methods now return `DfdDiagram` (not generic `Diagram`).

#### Before:
```python
# Returns: Diagram (empty wrapper class)
diagram = api.create_threat_model_diagram(request, tm_id)

# Had to do defensive checks
diagram_id = diagram["id"] if isinstance(diagram, dict) else diagram.id
```

#### After:
```python
# Returns: DfdDiagram (concrete type)
diagram = api.create_threat_model_diagram(request, tm_id)

# Direct access - no isinstance() needed
diagram_id = diagram.id  # Always works!
```

### 3. Deprecated: `Diagram` Class

The `Diagram` wrapper class is deprecated. Use `DfdDiagram` directly.

```python
# ❌ Deprecated
from swagger_client.models.diagram import Diagram

# ✅ Use this instead
from swagger_client.models.dfd_diagram import DfdDiagram
```

---

## Migration Steps

### Step 1: Update Imports

```python
# Add new imports
from swagger_client.models.dfd_diagram_input import DfdDiagramInput
from swagger_client.models.base_diagram_input import BaseDiagramInput

# Replace deprecated imports
# from swagger_client.models.diagram import Diagram  # ❌ Deprecated
from swagger_client.models.dfd_diagram import DfdDiagram  # ✅ Use this
```

### Step 2: Update Create Operations

No changes needed - `CreateDiagramRequest` remains the same.

```python
# Still works
request = CreateDiagramRequest(name="My Diagram", type="DFD-1.0.0")
diagram = api.create_threat_model_diagram(request, tm_id)
```

### Step 3: Update Update Operations

Replace `DfdDiagram` with `DfdDiagramInput` for PUT requests.

```python
# Before
diagram_update = DfdDiagram(...)  # Required readOnly fields

# After
diagram_update = DfdDiagramInput(
    type="DFD-1.0.0",
    name="Updated Name",
    cells=[...],
    # Optional fields:
    description="Optional description",
    metadata=[...],
    image={"svg": "...", "update_vector": 1}
)
updated = api.update_threat_model_diagram(diagram_update, tm_id, diagram_id)
```

### Step 4: Remove Defensive `isinstance()` Checks

API responses are now consistently typed.

```python
# Before - needed defensive code
diagram = api.get_threat_model_diagram(tm_id, diagram_id)
if isinstance(diagram, dict):
    diagram_id = diagram["id"]
else:
    diagram_id = diagram.id

# After - direct access
diagram = api.get_threat_model_diagram(tm_id, diagram_id)
diagram_id = diagram.id  # Always works!
```

### Step 5: Update Type Hints (Optional but Recommended)

```python
from swagger_client.models.dfd_diagram import DfdDiagram
from swagger_client.models.dfd_diagram_input import DfdDiagramInput

def update_diagram(diagram_id: str, updates: DfdDiagramInput) -> DfdDiagram:
    """Update a diagram with proper typing"""
    return api.update_threat_model_diagram(updates, tm_id, diagram_id)
```

---

## Validation

Run the integration test to verify everything works:

```bash
uv run test_diagram_fixes.py
```

Expected output:
```
======================================================================
TMI OpenAPI Client - Diagram Fixes Verification
======================================================================
Test 1: Testing DfdDiagram instantiation...
  ✓ DfdDiagram instantiation successful
...
Tests passed: 5/5
✓ ALL TESTS PASSED - All issues resolved!
```

---

## API Method Changes

### Diagram Endpoints

| Endpoint | Method | Request Body | Response Type |
|----------|--------|--------------|---------------|
| `/diagrams` | POST | `CreateDiagramRequest` | `DfdDiagram` ✨ (was `Diagram`) |
| `/diagrams` | GET | - | `list[DiagramListItem]` (no change) |
| `/diagrams/{id}` | GET | - | `DfdDiagram` ✨ (was `Diagram`) |
| `/diagrams/{id}` | PUT | `DfdDiagramInput` ✨ (was `Diagram`) | `DfdDiagram` ✨ (was `Diagram`) |
| `/diagrams/{id}` | PATCH | JSON Patch | `DfdDiagram` ✨ (was `Diagram`) |

✨ = Changed from previous version

---

## Common Patterns

### Pattern 1: Create → Update Workflow

```python
from swagger_client.models.create_diagram_request import CreateDiagramRequest
from swagger_client.models.dfd_diagram_input import DfdDiagramInput

# Create
request = CreateDiagramRequest(name="New Diagram", type="DFD-1.0.0")
diagram = api.create_threat_model_diagram(request, tm_id)

# Update (use DfdDiagramInput, not DfdDiagram)
update = DfdDiagramInput(
    type="DFD-1.0.0",
    name="Updated Name",
    cells=diagram.cells  # Reuse existing cells
)
updated_diagram = api.update_threat_model_diagram(update, tm_id, diagram.id)
```

### Pattern 2: Get → Modify → Update

```python
from swagger_client.models.dfd_diagram_input import DfdDiagramInput

# Fetch current
diagram = api.get_threat_model_diagram(tm_id, diagram_id)

# Modify cells
new_cells = diagram.cells + [new_cell]

# Create update request (no readOnly fields)
update = DfdDiagramInput(
    type=diagram.type,
    name=diagram.name,
    cells=new_cells,
    description=diagram.description,
    metadata=diagram.metadata
)

# Update
updated = api.update_threat_model_diagram(update, tm_id, diagram_id)
```

### Pattern 3: List → Get Details

```python
# List returns summaries (id, name, type only)
diagrams = api.get_threat_model_diagrams(tm_id)

# Get full details for specific diagram
for summary in diagrams:
    full_diagram = api.get_threat_model_diagram(tm_id, summary.id)
    # full_diagram now has cells, image, metadata, etc.
```

---

## Troubleshooting

### Issue: "Invalid value for `type` (None)"

**Cause**: Using old client without the constructor fix.

**Solution**: Regenerate client from updated OpenAPI spec.

### Issue: "Invalid value for `id`, must not be `None`"

**Cause**: Using `DfdDiagram` instead of `DfdDiagramInput` for PUT requests.

**Solution**: Use `DfdDiagramInput` for all update operations.

```python
# ❌ Wrong
update = DfdDiagram(...)  # Requires readOnly fields

# ✅ Correct
update = DfdDiagramInput(...)  # No readOnly fields
```

### Issue: AttributeError on response object

**Cause**: API returning `dict` instead of object (pre-fix behavior).

**Solution**: Ensure you're using the regenerated client.

---

## Files Changed

### OpenAPI Specification
- `/Users/efitz/Projects/tmi/docs/reference/apis/tmi-openapi.json`
  - Added `BaseDiagramInput` schema
  - Added `DfdDiagramInput` schema
  - Updated endpoint request/response types
  - Added `x-discriminator-value` annotations
  - Marked `Diagram` as deprecated

### Python Client
- `python-client-generated/swagger_client/models/`
  - `base_diagram_input.py` - NEW
  - `dfd_diagram_input.py` - NEW
  - `dfd_diagram.py` - PATCHED (constructor fix)
  - `diagram.py` - Deprecated (no changes)

---

## Support

For issues or questions:
1. Check [OPENAPI_ISSUES_SUMMARY.md](OPENAPI_ISSUES_SUMMARY.md) for detailed technical analysis
2. Run validation tests: `uv run test_diagram_fixes.py`
3. Review [DFD_DIAGRAM_FIX.md](DFD_DIAGRAM_FIX.md) for deep technical details

---

**Migration Date**: 2025-11-04
**OpenAPI Spec Version**: 1.0.0
**Client Generator**: swagger-codegen 3.0.75
