# TMI Python Client Fixes

This directory contains fixes and documentation for issues in the TMI auto-generated Python client.

## Quick Start

If you're encountering the `DfdDiagram` error:
```
ValueError: Invalid value for `type` (None), must be one of ['DFD-1.0.0']
```

**✅ This has been fixed!** The `dfd_diagram.py` file has been patched.

If you need to create diagram update requests, use this workaround until the spec is fixed:

```python
from tmi_client.models import DfdDiagram

# Workaround: Manual construction bypasses broken __init__
dfd_diagram = DfdDiagram.__new__(DfdDiagram)
dfd_diagram._type = None
dfd_diagram._cells = None
dfd_diagram._id = None
dfd_diagram._name = None
dfd_diagram._created_at = None
dfd_diagram._modified_at = None
dfd_diagram._metadata = None
dfd_diagram._update_vector = None
dfd_diagram._image = None
dfd_diagram._description = None
dfd_diagram.discriminator = "type"

# Set fields (don't set id - it's readOnly)
dfd_diagram._type = "DFD-1.0.0"
dfd_diagram.cells = my_cells
dfd_diagram._name = "My Diagram"

# Use in API call
api.update_threat_model_diagram(dfd_diagram, tm_id, diagram_id)
```

## Documentation Files

| File | Purpose |
|------|---------|
| `DFD_DIAGRAM_FIX.md` | **Technical deep-dive** into the DfdDiagram inheritance bug, with multiple solution approaches |
| `OPENAPI_ISSUES_SUMMARY.md` | **Complete list** of all 6 OpenAPI spec issues with fixes and priorities |
| `CLIENT_IMPROVEMENTS.md` | **Usability improvements** - Recommended helper classes and better APIs for easier client usage |
| `README_FIXES.md` | **This file** - Quick reference and navigation |

## Issue Summary

We've identified **6 issues** with the TMI OpenAPI specification and generated Python client:

1. **DfdDiagram inheritance bug** ⚠️ CRITICAL
   - **Status**: ✅ Patched in `dfd_diagram.py`
   - **Needs**: OpenAPI spec fix for permanent solution

2. **Inconsistent return types** (dict vs objects)
   - **Status**: ⚠️ Workaround with `isinstance` checks
   - **Needs**: Spec + generator configuration

3. **ReadOnly fields required in constructors**
   - **Status**: ⚠️ Workaround with manual object construction
   - **Needs**: Separate request/response schemas

4. **Empty Diagram base class**
   - **Status**: 📝 Documented
   - **Needs**: Spec refactor

5. **DiagramListItem vs Diagram relationship unclear**
   - **Status**: 📝 Documented
   - **Needs**: Better schema documentation

6. **Discriminator mapping incomplete**
   - **Status**: 📝 Documented
   - **Needs**: Add `x-discriminator-value` annotations

## What Was Fixed

### File: `tmi_client/models/dfd_diagram.py`

**Change**: Lines 52-53
```python
# BEFORE (broken)
def __init__(self, type=None, cells=None, *args, **kwargs):
    if type is not None:
        self.type = type
    self.cells = cells
    BaseDiagram.__init__(self, *args, **kwargs)  # type not passed!

# AFTER (fixed)
def __init__(self, type=None, cells=None, *args, **kwargs):
    if type is not None:
        kwargs['type'] = type  # ← Pass type to parent
    if type is not None:
        self.type = type
    self.cells = cells
    BaseDiagram.__init__(self, *args, **kwargs)
```

**Why**: Without this, `BaseDiagram.__init__` gets `type=None` (default), tries to set `self.type = None`, and fails validation.

### File: `tmi_tf/tmi_client_wrapper.py`

**Change**: Lines 286-302 - Added workaround for update operations

Uses manual object construction to bypass constructor requirements for readOnly fields.

## For Spec Maintainers

To permanently fix these issues in the OpenAPI specification:

### Priority 1: Fix DfdDiagram (Critical)

Update the spec to separate request/response schemas:

```yaml
components:
  schemas:
    # Input schema for updates (no readOnly fields)
    DfdDiagramInput:
      type: object
      required: [type, cells]
      properties:
        type:
          type: string
          enum: [DFD-1.0.0]
        cells:
          type: array
          items: {type: object}
        name:
          type: string
        description:
          type: string

    # Output schema for responses (includes readOnly fields)
    DfdDiagram:
      allOf:
        - $ref: '#/components/schemas/BaseDiagram'
        - type: object
          properties:
            type:
              type: string
              enum: [DFD-1.0.0]
            cells:
              type: array
              items: {type: object}
```

Then update endpoints:

```yaml
paths:
  /threat-models/{id}/diagrams/{diagram_id}:
    put:
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DfdDiagramInput'  # Use input schema
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DfdDiagram'  # Use output schema
```

### Priority 2: Fix Return Type Consistency

Ensure all endpoints specify concrete types, not abstract `Diagram`:

```yaml
# DON'T DO THIS (returns dict unpredictably)
schema:
  $ref: '#/components/schemas/Diagram'

# DO THIS (returns consistent type)
schema:
  $ref: '#/components/schemas/DfdDiagram'
```

### Priority 3: Other Improvements

See `OPENAPI_ISSUES_SUMMARY.md` for full list of recommended spec changes.

## Testing

After making spec changes, regenerate the client and run:

```bash
# Test basic instantiation
python -c "
from tmi_client.models import DfdDiagram
dfd = DfdDiagram(type='DFD-1.0.0', cells=[], name='Test')
assert dfd.type == 'DFD-1.0.0'
print('✓ DfdDiagram instantiation works')
"

# Test in real application
cd /path/to/tmi-tf
uv run tmi-tf analyze <threat-model-id>
# Should create diagrams without errors
```

## Questions?

1. **Encountering the DfdDiagram error?**
   → Check that `dfd_diagram.py` has the fix at lines 52-53

2. **Getting dict vs object type errors?**
   → Use workaround: `x = obj["field"] if isinstance(obj, dict) else obj.field`

3. **Can't create update requests?**
   → Use the manual construction workaround shown above

4. **Want to fix the spec permanently?**
   → See `DFD_DIAGRAM_FIX.md` Solutions 2 and 3

5. **Need comprehensive technical details?**
   → Read `DFD_DIAGRAM_FIX.md`

6. **Want to see all issues at a glance?**
   → Read `OPENAPI_ISSUES_SUMMARY.md`

## Status

- ✅ **Client patched** - Immediate workaround applied
- ⏳ **Spec fixes pending** - Requires OpenAPI specification updates
- 📝 **Documented** - All issues cataloged with solutions

**Last Updated**: 2025-11-03
