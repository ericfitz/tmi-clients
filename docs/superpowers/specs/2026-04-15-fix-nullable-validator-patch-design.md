# Fix Nullable Field Validator Patch Ordering

**Date:** 2026-04-15
**Issue:** #6 — Python client: generated validators fail on None for optional fields

## Problem

The `patch_regex_validators()` function in `regenerate_python.py` inserts a string conversion line (`value = value.isoformat() if hasattr(value, 'isoformat') else str(value)`) into every `@field_validator` that uses `re.match()`. This is necessary because openapi-generator produces `re.match()` calls on values that Pydantic has already parsed to native types (UUID, datetime).

For **nullable optional fields**, openapi-generator correctly produces a `None` guard:

```python
if value is None:
    return value
```

The patch inserts the conversion line after the docstring, which places it **before** the None guard. `str(None)` produces `"None"`, the subsequent `if value is None:` check is always `False`, and the regex fails on `"None"`.

This affects 260 `None` guards across 101 model files.

## Solution

Modify `patch_regex_validators()` to detect the None guard pattern immediately after the docstring. If found, shift the insertion point past the None guard before inserting the conversion line.

### Change details

**File:** `regenerate_python.py`, function `patch_regex_validators()` (~line 74)

After computing `insert_point = m.end()` and `rest = new_content[m.end():m.end() + 500]`, add a check:

```python
none_guard = re.match(r"        if value is None:\s*\n            return value\s*\n", rest)
if none_guard:
    insert_point += none_guard.end()
    rest = new_content[insert_point:insert_point + 500]
```

This shifts the insertion point past the None guard when present. For non-nullable fields (no None guard), behavior is unchanged.

### Result for nullable fields

Before (broken):
```python
    """Validates the regular expression"""
    value = value.isoformat() if hasattr(value, 'isoformat') else str(value)
    if value is None:
        return value
    if not re.match(r"...", value):
```

After (fixed):
```python
    """Validates the regular expression"""
    if value is None:
        return value
    value = value.isoformat() if hasattr(value, 'isoformat') else str(value)
    if not re.match(r"...", value):
```

### Result for non-nullable fields (unchanged)

```python
    """Validates the regular expression"""
    value = value.isoformat() if hasattr(value, 'isoformat') else str(value)
    if not re.match(r"...", value):
```

## Verification

1. Run regeneration on v1.4.0 to produce fresh generator output with the fixed patch
2. Grep model files to confirm no instance of the conversion line appears before `if value is None`
3. Run pytest to confirm tests pass

## Scope

- One function modified in one file (`regenerate_python.py`)
- No new files, no new dependencies
- All version directories (v1.2.1, v1.3.0, v1.4.0) benefit on next regeneration
