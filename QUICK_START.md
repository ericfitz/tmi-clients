# Quick Start - Client Regeneration

## TL;DR

```bash
cd /Users/efitz/Projects/tmi-clients

# Regenerate a client from the latest OpenAPI spec
python3 regenerate_python.py
python3 regenerate_go.py
python3 regenerate_ts.py

# Or use a local spec file
python3 regenerate_python.py path/to/tmi-openapi.json
```

Each script automatically downloads the latest spec, runs the appropriate code generator, applies bug-fix patches, runs tests, and produces a `REGENERATION_REPORT.md`.

## What You're About to Do

Regenerate one or more TMI API clients from the latest OpenAPI specification. The repository contains clients for three languages:

| Client | Directory | Generator | Package |
|--------|-----------|-----------|---------|
| Python | `python-client-generated/` | openapi-generator 7.x | `tmi-client` (PyPI) |
| Go | `go-client-generated/` | swagger-codegen 3.0.75 | `go-client-generated` (Go module) |
| TypeScript | `typescript-client-generated/` | openapi-generator 7.x | `@tmiclient/client` (npm) |

## Prerequisites

```bash
# Python client
brew install openapi-generator uv

# Go client
brew install swagger-codegen go

# TypeScript client
brew install openapi-generator node

# Verify the OpenAPI spec URL is accessible
curl -fsSL https://raw.githubusercontent.com/ericfitz/tmi/refs/heads/main/api-schema/tmi-openapi.json -o /dev/null && echo "Ready"
```

## Step-by-Step (Python Example)

### 1. Review Changes (Optional)

```bash
cd python-client-generated

# Analyze what changed in the spec
uv run scripts/analyze_spec_changes.py
```

### 2. Regenerate

```bash
cd /Users/efitz/Projects/tmi-clients
python3 regenerate_python.py
```

The script will:
- Download the latest OpenAPI spec from GitHub
- Run openapi-generator with the config in `python-client-generated/scripts/openapi-generator-config.json`
- Apply codegen bug-fix patches (e.g., UUID/datetime regex validator)
- Write modern config files (`pyproject.toml`)
- Back up and restore custom files
- Run tests and generate `REGENERATION_REPORT.md`

**Exit codes:** 0 = success, 1 = fatal error, 2 = completed with issues (test failures or patch warnings)

### 3. Validate

```bash
cd python-client-generated
uv run scripts/validate_regeneration.py
```

### 4. Test

```bash
cd python-client-generated

# Auto-generated tests
uv run --with pytest python3 -m pytest test/ -v --tb=short

# Integration test
uv run test_diagram_fixes.py

# Import test
uv run python3 -c "import tmi_client; print('Works')"
```

### 5. Review & Commit

```bash
git status
git diff --stat
```

## If Something Goes Wrong

### Use Git

```bash
git checkout -- .
git clean -fd
```

## Common Issues

**Issue:** Tests fail after regeneration
**Fix:** Review failures -- some are expected if the API changed. Check `REGENERATION_REPORT.md` for details.

**Issue:** Import errors
**Fix:** Run `uv pip install -e .` in the client directory to reinstall the package.

**Issue:** Codegen not found
**Fix:** Install the correct generator: `brew install openapi-generator` (Python/TypeScript) or `brew install swagger-codegen` (Go).

## More Information

- **Regeneration guide:** [REGENERATION_README.md](python-client-generated/docs/developer/REGENERATION_README.md)
- **Migration guide:** [MIGRATION_GUIDE.md](python-client-generated/docs/developer/MIGRATION_GUIDE.md)
- **Spec analysis:** [SPEC_ANALYSIS.md](python-client-generated/docs/developer/SPEC_ANALYSIS.md)
- **Releasing:** [RELEASING.md](RELEASING.md)

## Scripts Reference

| Script | Location | Purpose |
|--------|----------|---------|
| `regenerate_python.py` | repo root | Regenerate Python client |
| `regenerate_go.py` | repo root | Regenerate Go client |
| `regenerate_ts.py` | repo root | Regenerate TypeScript client |
| `regen_common.py` | repo root | Shared utilities for all regeneration scripts |
| `analyze_spec_changes.py` | `python-client-generated/scripts/` | Analyze OpenAPI spec changes |
| `validate_regeneration.py` | `python-client-generated/scripts/` | Validate regeneration output |

## Repository Layout

```
tmi-clients/
├── regenerate_python.py              # Python client regeneration script
├── regenerate_go.py                  # Go client regeneration script
├── regenerate_ts.py                  # TypeScript client regeneration script
├── regen_common.py                   # Shared regeneration utilities
├── release_python.sh                 # Python release helper
├── RELEASING.md                      # Publishing guide (PyPI, npm, Go)
├── python-client-generated/          # Python client
│   ├── tmi_client/                   # Generated client code
│   ├── test/                         # Generated tests
│   ├── docs/developer/               # Developer documentation
│   └── scripts/                      # Analysis and validation scripts
├── go-client-generated/              # Go client
├── typescript-client-generated/      # TypeScript client
└── QUICK_START.md                    # This file
```
