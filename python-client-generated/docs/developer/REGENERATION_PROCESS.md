# Python Client Regeneration Process

**Last Updated:** 2025-12-06
**Version:** 2.0

This document describes the complete process for regenerating the Python client from the latest OpenAPI specification.

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Process Steps](#process-steps)
4. [Scripts Reference](#scripts-reference)
5. [Validation](#validation)
6. [Troubleshooting](#troubleshooting)
7. [Rollback Procedure](#rollback-procedure)

## Overview

The Python client is auto-generated from the TMI OpenAPI specification using swagger-codegen 3.0.75. The regeneration process includes:

- Analyzing spec changes
- Creating backups
- Regenerating code
- Applying patches
- Running validations
- Updating documentation

**Estimated Time:** 1-2 hours (including testing and documentation)

## Prerequisites

### Tools Required

```bash
# Install swagger-codegen
brew install swagger-codegen

# Install uv (Python package manager)
brew install uv

# Verify installations
swagger-codegen version  # Should be 3.0.75
uv --version
```

### OpenAPI Specification

The OpenAPI spec must be available at:
```
/Users/efitz/Projects/tmi/docs/reference/apis/tmi-openapi.json
```

To verify:
```bash
test -f /Users/efitz/Projects/tmi/docs/reference/apis/tmi-openapi.json && echo "✓ Spec found" || echo "✗ Spec not found"
```

## Process Steps

### Step 1: Analyze Specification Changes

**Purpose:** Understand what has changed in the OpenAPI spec before regenerating.

```bash
cd python-client-generated
uv run scripts/analyze_spec_changes.py
```

**Output:**
- `docs/developer/SPEC_ANALYSIS.md` - Human-readable report
- `docs/developer/spec_analysis.json` - Machine-readable analysis

**Review:**
- Number of new/removed models
- New API endpoints
- Breaking changes
- Schema modifications

**Time:** 5 minutes

### Step 2: Review Impact Assessment

Read the impact assessment to understand changes:

```bash
cat docs/developer/REGENERATION_IMPACT.md
```

**Key Items to Review:**
- Breaking changes
- New features
- Migration requirements
- Risk assessment

**Time:** 10 minutes

### Step 3: Create Backup

**Purpose:** Enable rollback if regeneration fails.

```bash
cd python-client-generated
./scripts/backup_before_regen.sh
```

**Output:**
- Timestamped backup directory in `../backups/`
- Compressed archive of entire client
- Pre-regeneration snapshot
- API/model inventories
- Restore script

**Verify Backup:**
```bash
# Check backup was created
ls -lh ../backups/pre-regen-*/client_backup.tar.gz

# Review snapshot
cat ../backups/pre-regen-*/PRE_REGEN_SNAPSHOT.md
```

**Time:** 5 minutes

### Step 4: Run Regeneration

**Purpose:** Generate new client code from OpenAPI spec.

```bash
cd python-client-generated
./scripts/regenerate_client.sh
```

**What This Does:**
1. Validates prerequisites
2. Backs up critical files
3. Cleans client directory
4. Runs swagger-codegen
5. Applies constructor patches
6. Updates configuration files
7. Restores custom files
8. Runs tests
9. Generates report

**Duration:** 10-15 minutes

**Monitor Output For:**
- ✓ All prerequisites met
- ✓ Client regenerated successfully
- ✓ Constructor patches applied
- ✓ Configuration files updated
- ⚠️ Test failures (expected if breaking changes)

### Step 5: Validate Regeneration

**Purpose:** Verify regeneration was successful.

```bash
cd python-client-generated
uv run scripts/validate_regeneration.py
```

**Checks Performed:**
- Constructor patches applied
- Python 3.8+ requirements
- Modern dependencies
- No Python 2.x code
- Expected models present
- API modules present
- Custom files preserved

**Expected Result:**
```
✓ ALL VALIDATIONS PASSED
```

**Time:** 5 minutes

### Step 6: Run Tests

**Purpose:** Ensure generated code works correctly.

```bash
cd python-client-generated

# Auto-generated tests (239+ tests)
uv run --with pytest python3 -m pytest test/ -v --tb=short

# Integration test (custom)
uv run test_diagram_fixes.py

# Quick import test
uv run python3 -c "import tmi_client; print('✓ Import successful')"
```

**Expected Results:**
- Most auto-generated tests should pass
- Some may fail if API has breaking changes (document these)
- Integration test should pass (tests constructor patches)
- Import test should succeed

**Time:** 15-30 minutes (including fixing any issues)

### Step 7: Review Generated Code

**Purpose:** Spot-check critical generated code.

```bash
# Check constructor patches
grep -A 5 "PATCH:" python-client-generated/tmi_client/models/dfd_diagram.py
grep -A 5 "PATCH:" python-client-generated/tmi_client/models/dfd_diagram_input.py

# Check for new models
ls -1 python-client-generated/tmi_client/models/*admin* | head -5
ls -1 python-client-generated/tmi_client/models/*addon* | head -5
ls -1 python-client-generated/tmi_client/models/*webhook* | head -5

# Check API structure
ls -1 python-client-generated/tmi_client/api/
```

**Time:** 10 minutes

### Step 8: Update Documentation

**Purpose:** Document changes for users.

Files to update:

1. **MIGRATION_GUIDE.md** - Breaking changes and migration steps
2. **CHANGELOG.md** - Version history
3. **README.md** - New features
4. **CLAUDE.md** - AI assistant guidance (if needed)

```bash
# Review generated report first
cat docs/developer/REGENERATION_REPORT.md

# Then update documentation files
```

**Time:** 30-60 minutes

### Step 9: Commit Changes

**Purpose:** Save regenerated client to version control.

```bash
cd python-client-generated

# Review changes
git status
git diff --stat

# Add files
git add -A

# Commit (with detailed message)
git commit -m "regenerate: update Python client from latest OpenAPI spec

- Add support for Add-ons API (8 new endpoints)
- Add Administration API (27 new endpoints)
- Add SAML authentication support
- Update webhook event types
- Add 36 new model classes
- Remove 52 deprecated inline response models
- Apply constructor patches for DFD diagrams
- Update dependencies to modern versions

Breaking Changes:
- Cell attribute access changed from typed objects to dictionaries
- Inline response models removed (replaced with proper schemas)

See MIGRATION_GUIDE.md for detailed migration instructions."

# Push (optional, after review)
# git push
```

**Time:** 10 minutes

## Scripts Reference

### analyze_spec_changes.py

**Purpose:** Analyze OpenAPI specification changes

**Usage:**
```bash
uv run scripts/analyze_spec_changes.py
```

**Output:**
- `docs/developer/SPEC_ANALYSIS.md`
- `docs/developer/spec_analysis.json`

**When to Use:** Before regeneration, to understand changes

---

### backup_before_regen.sh

**Purpose:** Create comprehensive backup before regeneration

**Usage:**
```bash
./scripts/backup_before_regen.sh
```

**Output:**
- `../backups/pre-regen-TIMESTAMP/` directory
- Compressed archive
- Snapshot report
- Restore script

**When to Use:** Immediately before regeneration

---

### regenerate_client.sh

**Purpose:** Regenerate client from OpenAPI spec

**Usage:**
```bash
./scripts/regenerate_client.sh
```

**Features:**
- Automatic defaults (Python 3.8+, modern dependencies)
- Constructor patch application
- Configuration file updates
- Test execution
- Report generation

**When to Use:** To regenerate client from spec

---

### validate_regeneration.py

**Purpose:** Validate regeneration was successful

**Usage:**
```bash
uv run scripts/validate_regeneration.py
```

**Checks:**
- Constructor patches
- Python version requirements
- Dependencies
- No Python 2.x code
- Expected models
- API modules
- Custom files

**When to Use:** After regeneration, before committing

## Validation

### Quick Validation Checklist

After regeneration, verify:

- [ ] Constructor patches applied (`grep "PATCH:" tmi_client/models/dfd_diagram*.py`)
- [ ] Python 3.8+ in pyproject.toml and setup.py
- [ ] Modern dependencies in requirements.txt
- [ ] Custom test file present (`test_diagram_fixes.py`)
- [ ] Documentation preserved (`docs/developer/`)
- [ ] Scripts preserved (`scripts/`)
- [ ] Auto-generated tests run (`pytest test/`)
- [ ] Integration test passes (`./test_diagram_fixes.py`)
- [ ] Import works (`python3 -c "import tmi_client"`)

### Detailed Validation

See [POST_REGEN_CHECKLIST.md](../../backups/pre-regen-TIMESTAMP/POST_REGEN_CHECKLIST.md) created by backup script.

## Troubleshooting

### swagger-codegen Fails

**Symptom:** `swagger-codegen generate` returns non-zero exit code

**Causes:**
- Invalid OpenAPI spec
- Missing swagger-codegen
- Incorrect config file

**Solutions:**
```bash
# Validate spec
swagger-codegen validate -i /Users/efitz/Projects/tmi/docs/reference/apis/tmi-openapi.json

# Reinstall swagger-codegen
brew reinstall swagger-codegen

# Check config file
cat scripts/swagger-codegen-config.json
```

### Constructor Patches Not Applied

**Symptom:** Validation reports patches missing

**Causes:**
- File names changed
- File structure changed
- sed patterns didn't match

**Solutions:**
```bash
# Manually check files exist
ls -la tmi_client/models/dfd_diagram*.py

# Manually apply patch
# Edit tmi_client/models/dfd_diagram.py
# Add before BaseDiagram.__init__():
#   kwargs['type'] = type  # PATCH: Pass type to parent
```

### Tests Fail After Regeneration

**Symptom:** pytest returns failures

**Causes:**
- Breaking API changes
- Schema modifications
- Cell structure changes

**Solutions:**
1. Review test failures to identify patterns
2. Check if API changed (consult SPEC_ANALYSIS.md)
3. Update test expectations if needed
4. Document breaking changes in MIGRATION_GUIDE.md

### Import Errors

**Symptom:** `ImportError` or `ModuleNotFoundError`

**Causes:**
- Missing dependencies
- Package not installed
- __init__.py files incorrect

**Solutions:**
```bash
# Reinstall package
uv pip install -e .

# Check __init__.py files
grep -r "import" tmi_client/__init__.py
grep -r "import" tmi_client/models/__init__.py

# Verify dependencies
uv pip list | grep -E "certifi|six|urllib3"
```

## Rollback Procedure

If regeneration fails or causes critical issues:

### Option 1: Use Restore Script

```bash
# Find latest backup
ls -lt ../backups/

# Run restore script
../backups/pre-regen-TIMESTAMP/restore.sh
```

### Option 2: Manual Restore

```bash
# Extract backup
cd /Users/efitz/Projects/tmi-clients
tar -xzf backups/pre-regen-TIMESTAMP/client_backup.tar.gz

# Or copy files
cp -r backups/pre-regen-TIMESTAMP/client_backup/* python-client-generated/
```

### Option 3: Git Revert

```bash
# If already committed
git log --oneline
git revert <commit-hash>

# If not committed
git checkout -- .
git clean -fd
```

### After Rollback

1. Verify client works: `uv run python3 -c "import tmi_client; print('OK')"`
2. Run tests: `uv run --with pytest python3 -m pytest test/ -v`
3. Document issue in GitHub issue or similar
4. Analyze what went wrong before re-attempting

## Best Practices

### Before Regeneration

1. **Always analyze first:** Run `analyze_spec_changes.py`
2. **Always backup:** Run `backup_before_regen.sh`
3. **Read the impact assessment:** Review `REGENERATION_IMPACT.md`
4. **Commit current state:** `git commit -m "pre-regeneration checkpoint"`

### During Regeneration

1. **Monitor output:** Watch for errors and warnings
2. **Don't skip steps:** Follow the script flow
3. **Capture logs:** Redirect output if needed: `./regenerate_client.sh 2>&1 | tee regen.log`

### After Regeneration

1. **Validate immediately:** Run `validate_regeneration.py`
2. **Test thoroughly:** Run all test suites
3. **Review code:** Spot-check generated files
4. **Update docs:** Keep documentation current

### Version Control

1. **Use semantic versioning:** Major.Minor.Patch
2. **Document breaking changes:** In CHANGELOG.md and commit message
3. **Tag releases:** `git tag -a v1.1.0 -m "Version 1.1.0"`
4. **Keep backups:** Don't delete old backups immediately

## Related Documentation

- [SPEC_ANALYSIS.md](SPEC_ANALYSIS.md) - Latest spec analysis
- [REGENERATION_IMPACT.md](REGENERATION_IMPACT.md) - Impact assessment
- [REGENERATION_README.md](REGENERATION_README.md) - Original regen guide
- [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) - User migration guide
- [CHANGELOG.md](CHANGELOG.md) - Version history
- [../../CLAUDE.md](../../CLAUDE.md) - Repository instructions

## Support

For issues or questions:

1. Check [Troubleshooting](#troubleshooting) section
2. Review generated logs
3. Consult OpenAPI spec documentation
4. Open GitHub issue with:
   - Error messages
   - Spec analysis output
   - Validation results
   - Test failure logs
