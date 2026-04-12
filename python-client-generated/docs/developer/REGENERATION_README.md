# TMI Client Regeneration Guide

This directory contains automated tools for regenerating the TMI Python client from the OpenAPI specification with intelligent defaults.

## Quick Start

```bash
cd /Users/efitz/Projects/tmi-clients
python3 regenerate_python.py
```

That's it! The script automatically downloads the latest spec, runs openapi-generator, applies patches, and runs tests.

## Automatic Defaults

The regeneration process automatically applies these intelligent defaults:

### Package Configuration
- **Package name**: `tmi_client` (not `swagger_client`)
- **Project name**: `tmi-client`
- **Version**: `1.0.0`
- **Library**: `urllib3`
- **Property naming**: `snake_case`

### Python Version
- **Minimum Python**: `3.8+`
- **Dropped support**: Python 2.x, Python 3.0-3.7
- **Reason**: Modern async/await, type hints, and security fixes

### Dependency Versions (Security-Hardened)

All dependencies are automatically updated to secure, modern versions:

| Package | Old Version | New Version | Reason |
|---------|-------------|-------------|--------|
| `certifi` | 14.05.14 | >= 2024.2.2 | Critical security fixes, latest CA certs |
| `setuptools` | 21.0.0 | >= 70.0.0 | CVE-2022-40897 RCE vulnerability fix |
| `urllib3` | 1.15.1 | >= 2.0.0 | Multiple CVE fixes (SSL, security) |
| `six` | 1.10 | >= 1.16.0 | Python 3 compatibility improvements |
| `python-dateutil` | 2.5.3 | >= 2.9.0 | Bug fixes and improvements |

### Testing Framework
- **Test runner**: `pytest` (not deprecated `nose`)
- **Plugins**: `pytest-cov`, `pytest-randomly`
- **Test requirements**: Automatically updated in `test-requirements.txt`

### Modern Packaging
- **Format**: `pyproject.toml` + `setup.py` (dual format)
- **Build system**: `setuptools >= 70.0.0` with `wheel`
- **UV compatible**: Works with modern Python package managers
- **Structured metadata**: Author, keywords, classifiers, URLs

### Critical Patches

The script automatically applies these bug fixes:

1. **DfdDiagram Constructor Patch**
   - Fixes: Type parameter overwritten to None
   - Location: `tmi_client/models/dfd_diagram.py` line ~53
   - Patch: `kwargs['type'] = type` before calling parent `__init__`

2. **DfdDiagramInput Constructor Patch**
   - Same fix as DfdDiagram
   - Location: `tmi_client/models/dfd_diagram_input.py` line ~53
   - Ensures input schemas work correctly

## Files

### Configuration Files

#### `scripts/openapi-generator-config.json`

**Purpose**: Tells openapi-generator how to generate the client with correct naming and settings.

### Regeneration Script

#### `regenerate_python.py` (at repo root)
**Purpose**: Fully automated regeneration with all patches and updates.

**What it does**:
1. ✅ Downloads latest OpenAPI spec from GitHub (or uses local file)
2. ✅ Backs up custom files (docs/developer, tests)
3. ✅ Cleans old client directory
4. ✅ Runs openapi-generator with configuration
5. ✅ Applies codegen bug-fix patches (UUID/datetime regex validator)
6. ✅ Writes modern pyproject.toml
7. ✅ Restores custom files
8. ✅ Runs tests
9. ✅ Generates REGENERATION_REPORT.md

**Exit codes**:
- `0`: Success - all tests passing
- `1`: Fatal error - codegen failed
- `2`: Completed with issues (test failures or patch warnings)

## Prerequisites

### Required Tools

```bash
# Install openapi-generator
brew install openapi-generator

# Install uv (Python package manager)
brew install uv

# Verify installations
openapi-generator version  # Should be 7.x
uv --version
python3 --version          # Should be >= 3.9.0
```

### Required Files

- OpenAPI spec: Downloaded automatically from `https://raw.githubusercontent.com/ericfitz/tmi/refs/heads/main/api-schema/tmi-openapi.json`
- Must be valid OpenAPI 3.0+ specification

## Usage

### Basic Regeneration

```bash
# From the tmi-clients repo root
cd /Users/efitz/Projects/tmi-clients
python3 regenerate_python.py

# Or with a local spec file
python3 regenerate_python.py path/to/tmi-openapi.json
```

### Verify Results

```bash
# Check the report
cat python-client-generated/REGENERATION_REPORT.md

# Run tests manually
cd python-client-generated
uv run --with pytest python3 -m pytest test/ -v

# Run integration tests
uv run test_diagram_fixes.py
```

### Output Files

After regeneration, you'll find:

```
python-client-generated/
├── tmi_client/              # Main package (107 models, 15 APIs)
├── test/                    # 121 test files (239 tests)
├── docs/                    # Auto-generated documentation
├── pyproject.toml           # Modern Python packaging
├── setup.py                 # Traditional setup (updated)
├── requirements.txt         # Runtime dependencies
├── test-requirements.txt    # Test dependencies
└── test_diagram_fixes.py    # Integration tests

REGENERATION_REPORT.md       # Detailed report
test_output.log              # Test results
integration_test_output.log  # Integration test results
```

## What Gets Preserved

The script automatically preserves:

- ✅ `pyproject.toml` (custom configuration)
- ✅ `test_diagram_fixes.py` (integration tests)
- ✅ `.swagger-codegen-ignore` (if exists)

All other files are regenerated from scratch.

## What Gets Updated

### Always Updated
- All model files (`tmi_client/models/*.py`)
- All API files (`tmi_client/api/*.py`)
- All test files (`test/*.py`)
- Auto-generated documentation (`docs/*.md`)

### Automatically Patched
- `tmi_client/models/dfd_diagram.py` - Constructor fix
- `tmi_client/models/dfd_diagram_input.py` - Constructor fix
- `setup.py` - Python 3.8+ requirement, modern dependencies
- `requirements.txt` - Secure dependency versions
- `test-requirements.txt` - pytest instead of nose

## Customization

### Change Package Version

The version is automatically extracted from the OpenAPI spec's `info.version` field during regeneration. To override, edit `scripts/openapi-generator-config.json`.

### Add Custom Patches

Edit `regenerate_python.py` to add new patch functions. See existing `patch_regex_validators()` as an example.

## Troubleshooting

### "openapi-generator not found"

```bash
brew install openapi-generator
```

### "Failed to download OpenAPI spec"

Check that the URL is accessible:
```bash
curl -fsSL https://raw.githubusercontent.com/ericfitz/tmi/refs/heads/main/api-schema/tmi-openapi.json -o /dev/null
```

Or use a local spec file: `python3 regenerate_python.py path/to/tmi-openapi.json`

### "uv not found"

```bash
brew install uv
```

### Tests Failing After Regeneration

1. Check `test_output.log` for details
2. Verify OpenAPI spec is valid
3. Check if new breaking changes in spec
4. Review `REGENERATION_REPORT.md`

### Constructor Patches Not Applied

Check the patch functions in `regenerate_python.py`. The regex patterns may need adjustment if openapi-generator output format changes.

Verify patch was applied:
```bash
grep "kwargs\['type'\] = type" python-client-generated/tmi_client/models/dfd_diagram.py
```

Should show:
```python
kwargs['type'] = type  # PATCH: Pass type to parent to prevent overwrite
```

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Regenerate TMI Client

on:
  schedule:
    - cron: '0 0 * * 0'  # Weekly on Sunday
  workflow_dispatch:

jobs:
  regenerate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Install dependencies
        run: |
          brew install openapi-generator uv

      - name: Regenerate client
        run: python3 regenerate_python.py

      - name: Create PR
        uses: peter-evans/create-pull-request@v5
        with:
          title: "chore: regenerate TMI Python client"
          body: "Automated client regeneration from latest OpenAPI spec"
          branch: "automated/regenerate-client"
```

## Version History

### 1.0.0 (2025-11-12)
- Initial automated regeneration script
- Python 3.8+ support
- Modern dependency versions with CVE fixes
- Automatic constructor patches
- pytest migration
- Webhook API support
- Cell schema simplification

## Best Practices

### Before Regeneration
- [ ] Commit any local changes
- [ ] Update OpenAPI spec to latest version
- [ ] Review spec for breaking changes
- [ ] Back up custom code if any

### After Regeneration
- [ ] Review `REGENERATION_REPORT.md`
- [ ] Check test results (all should pass)
- [ ] Review git diff for unexpected changes
- [ ] Update CHANGELOG.md if needed
- [ ] Test with dependent projects
- [ ] Create PR for review

### Frequency
- **On OpenAPI spec changes**: Always regenerate
- **Security updates**: Monthly dependency check
- **Regular maintenance**: Quarterly regeneration
- **Before releases**: Always regenerate and test

## Support

For issues with regeneration:

1. Check this README
2. Review `REGENERATION_REPORT.md` after running
3. Check `test_output.log` for test failures
4. See [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) for usage
5. See [CLAUDE.md](CLAUDE.md) for development guidance

## License

Same as TMI project.
