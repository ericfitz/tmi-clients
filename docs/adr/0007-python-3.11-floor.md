# ADR 0007: Python client requires Python 3.11+

- **Status:** Accepted
- **Date:** 2026-11-22
- **Decision by:** Eric Fitzgerald (human-made architectural decision)

## Context

The Python client (`tmi-client`) declared `requires-python = ">=3.10"`, set by
`patch_python_minimum_version` in `regenerate_python.py` (openapi-generator's own
floor is lower). The development dependencies tox and virtualenv pull in filelock.
The lock resolved filelock 4.1.0 for Python 3.10, which is affected by CVE-2026-112906
and related advisories (17 Dependabot alerts, one HIGH). The fixed release, 4.2.1, and every
later one require Python 3.11 or newer, so no fix exists for the 3.10 slice of the lock.

## Decision

Raise the Python client's floor to 3.11: `patch_python_minimum_version` sets
`requires-python = ">=3.11"` in `pyproject.toml` and `PYTHON_REQUIRES = ">= 3.11"` in
`setup.py`, and the committed `v3.0.0` client and its `uv.lock` follow.

The repository's own tooling scripts (`regenerate_*.py`, `.github/scripts/*.py`) are
separate. They declare their own `requires-python` in uv inline metadata and are unchanged.

## Consequences

- Python 3.10 users cannot install `tmi-client` releases published after this change.
  Releases already published keep their old metadata.
- The lock no longer carries Python 3.10-only resolutions.
- `python-client-generated/scripts/validate_regeneration.py` checks the floor through
  `MIN_PYTHON`, which must match `patch_python_minimum_version`.
