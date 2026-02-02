# Quick Start - Python Client Regeneration

**Status:** Ready to Execute

## TL;DR

```bash
cd /Users/efitz/Projects/tmi-clients/python-client-generated

# 1. Create backup (5 min)
./scripts/backup_before_regen.sh

# 2. Regenerate (15 min)
./scripts/regenerate_client.sh

# 3. Validate (5 min)
uv run scripts/validate_regeneration.py

# 4. Test (30 min)
uv run --with pytest python3 -m pytest test/ -v
uv run test_diagram_fixes.py

# 5. Review and commit
git status
git diff --stat
```

## What You're About to Do

Update the Python client to work with the latest TMI OpenAPI specification.

**New Features:**
- Add-ons API (extensibility)
- Administration API (enterprise features)
- SAML authentication
- Enhanced webhooks

**Breaking Changes:**
- Cell attribute access (typed objects → dictionaries)
- Some model names changed

**Time Required:** 1-2 hours

## Prerequisites

```bash
# Install required tools if not present
brew install swagger-codegen uv

# Test OpenAPI spec URL is accessible
curl -fsSL https://raw.githubusercontent.com/ericfitz/tmi/refs/heads/main/api-schema/tmi-openapi.json -o /dev/null && echo "✓ Ready"
```

## Step-by-Step

### 1. Review Changes (Optional but Recommended)

```bash
cd /Users/efitz/Projects/tmi-clients/python-client-generated

# See what's changing
cat docs/developer/SPEC_ANALYSIS.md | less

# Read impact assessment
cat docs/developer/REGENERATION_IMPACT.md | less
```

**Time:** 10-15 minutes

### 2. Create Backup

```bash
./scripts/backup_before_regen.sh
```

**Creates:** Timestamped backup with restore script

**Time:** 1-2 minutes

### 3. Run Regeneration

```bash
./scripts/regenerate_client.sh 2>&1 | tee regen.log
```

**Watch for:**
- ✓ All prerequisites met
- ✓ Client regenerated successfully
- ✓ Constructor patches applied
- ✓ Configuration files updated

**Time:** 10-15 minutes

### 4. Validate

```bash
uv run scripts/validate_regeneration.py
```

**Expected Output:**
```
✓ ALL VALIDATIONS PASSED
```

**Time:** 2 minutes

### 5. Test

```bash
# Auto-generated tests
uv run --with pytest python3 -m pytest test/ -v --tb=short

# Integration test
uv run test_diagram_fixes.py

# Import test
uv run python3 -c "import tmi_client; print('✓ Works')"
```

**Expected:**
- Most/all tests pass
- Integration test passes
- Import succeeds

**Time:** 15-30 minutes

### 6. Review & Commit

```bash
# See what changed
git status
git diff --stat

# Review key changes
git diff tmi_client/models/dfd_diagram.py
git diff pyproject.toml
git diff requirements.txt

# Commit
git add -A
git commit -m "regenerate: update Python client from latest OpenAPI spec

- Add Add-ons API (8 endpoints)
- Add Administration API (27 endpoints)
- Add SAML authentication
- Update webhook event types
- Add 36 new models
- Remove 52 deprecated inline response models

Breaking: Cell attributes now use dict access

See MIGRATION_GUIDE.md for details."

# Optional: Create tag
git tag -a v1.1.0 -m "Version 1.1.0"
```

**Time:** 10 minutes

## If Something Goes Wrong

### Quick Rollback

```bash
# Find your backup
ls -lt ../backups/

# Restore it
../backups/pre-regen-TIMESTAMP/restore.sh
```

### Or Use Git

```bash
git checkout -- .
git clean -fd
```

## Common Issues

**Issue:** Constructor patches not applied
**Fix:** Check validation output, may need manual patch

**Issue:** Tests fail
**Fix:** Review failures - some expected if API changed, document in MIGRATION_GUIDE.md

**Issue:** Import errors
**Fix:** Run `uv pip install -e .` to reinstall package

## Need More Details?

- **Complete Guide:** [REGENERATION_PLAN.md](REGENERATION_PLAN.md)
- **Process Documentation:** [docs/developer/REGENERATION_PROCESS.md](python-client-generated/docs/developer/REGENERATION_PROCESS.md)
- **What Changed:** [docs/developer/SPEC_ANALYSIS.md](python-client-generated/docs/developer/SPEC_ANALYSIS.md)
- **Impact Assessment:** [docs/developer/REGENERATION_IMPACT.md](python-client-generated/docs/developer/REGENERATION_IMPACT.md)

## Scripts Reference

| Script | Purpose | When to Use |
|--------|---------|-------------|
| `analyze_spec_changes.py` | Analyze OpenAPI spec | Before regenerating |
| `backup_before_regen.sh` | Create backup | Before regenerating |
| `regenerate_client.sh` | Regenerate client | To update from spec |
| `validate_regeneration.py` | Validate output | After regenerating |

## File Locations

```
/Users/efitz/Projects/tmi-clients/
├── python-client-generated/          # Python client (what you're updating)
│   ├── scripts/                      # All regeneration scripts
│   ├── docs/developer/               # Process documentation
│   └── tmi_client/                   # Generated client code
├── backups/                          # Created by backup script
├── REGENERATION_PLAN.md              # Detailed execution plan
├── SUMMARY.md                        # What was prepared
└── QUICK_START.md                    # This file
```

## Success Checklist

After regeneration:

- [ ] Backup created
- [ ] Regeneration completed without errors
- [ ] Validation passed
- [ ] Tests run (most passing)
- [ ] Constructor patches applied
- [ ] New models present (addon*, admin*, saml*)
- [ ] Documentation reviewed
- [ ] Changes committed

## Ready?

```bash
cd /Users/efitz/Projects/tmi-clients/python-client-generated
./scripts/backup_before_regen.sh
./scripts/regenerate_client.sh
```

Good luck! 🚀
