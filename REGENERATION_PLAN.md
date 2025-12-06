# Python Client Regeneration Plan

**Created:** 2025-12-06
**Status:** Ready for Execution
**Estimated Time:** 5-9 hours total

## Executive Summary

The TMI OpenAPI specification has been significantly updated with new features including Add-ons API, Administration API, and SAML authentication support. This plan outlines the complete process to regenerate the Python client from the updated specification.

**Key Changes:**
- 36 new model classes (addons, administration, SAML, quotas)
- 52 model classes removed (inline responses consolidated)
- 3 new API groups (Addons, Administration, SAML)
- 89 API endpoints total (173 operations)

**Impact:** Medium - Breaking changes to cell attribute access patterns, but most changes are additive.

## Objectives

1. ✅ Analyze OpenAPI specification changes
2. ✅ Create comprehensive tooling for regeneration
3. ⏳ Execute regeneration process
4. ⏳ Validate generated client
5. ⏳ Update documentation
6. ⏳ Test and fix issues

## Deliverables

### Analysis & Planning (✅ COMPLETE)

- [x] **Spec Analysis Script** (`scripts/analyze_spec_changes.py`)
  - Analyzes OpenAPI spec changes
  - Generates human and machine-readable reports
  - Identifies new/removed models and APIs

- [x] **Spec Analysis Report** (`docs/developer/SPEC_ANALYSIS.md`)
  - 89 API paths analyzed
  - 90 schemas documented
  - Comparison with current client

- [x] **Impact Assessment** (`docs/developer/REGENERATION_IMPACT.md`)
  - Breaking changes identified
  - Migration strategies defined
  - Risk assessment complete

### Tooling (✅ COMPLETE)

- [x] **Backup Script** (`scripts/backup_before_regen.sh`)
  - Creates timestamped backups
  - Generates restore script
  - Captures pre-regeneration state

- [x] **Validation Script** (`scripts/validate_regeneration.py`)
  - Validates constructor patches
  - Checks Python version requirements
  - Verifies dependencies
  - Confirms expected models present

- [x] **Regeneration Script** (`scripts/regenerate_client.sh`) - Already exists
  - Generates client from spec
  - Applies patches automatically
  - Updates configuration
  - Runs tests

### Documentation (✅ COMPLETE)

- [x] **Process Guide** (`docs/developer/REGENERATION_PROCESS.md`)
  - Step-by-step instructions
  - Scripts reference
  - Troubleshooting guide
  - Rollback procedures

- [x] **Repository Instructions** (`CLAUDE.md`) - Already exists
  - Updated with new patterns
  - Script usage documented

### Execution (⏳ PENDING - Ready to Execute)

- [ ] Create backup
- [ ] Run regeneration
- [ ] Validate output
- [ ] Run tests
- [ ] Fix any issues
- [ ] Update documentation
- [ ] Commit changes

## Execution Steps

### Phase 1: Preparation (30 minutes)

#### 1.1 Verify Prerequisites
```bash
# Verify tools
swagger-codegen version  # Should be 3.0.75
uv --version
python3 --version  # Should be 3.8+

# Verify spec exists
test -f /Users/efitz/Projects/tmi/docs/reference/apis/tmi-openapi.json && echo "✓ Spec found"
```

#### 1.2 Review Analysis
```bash
cd /Users/efitz/Projects/tmi-clients/python-client-generated

# Review spec analysis
cat docs/developer/SPEC_ANALYSIS.md | less

# Review impact assessment
cat docs/developer/REGENERATION_IMPACT.md | less
```

**Decision Point:** Proceed only if comfortable with identified changes.

#### 1.3 Create Checkpoint
```bash
# Commit current state
git status
git add -A
git commit -m "checkpoint: pre-regeneration state"
```

### Phase 2: Backup (10 minutes)

```bash
cd /Users/efitz/Projects/tmi-clients/python-client-generated

# Create backup
./scripts/backup_before_regen.sh

# Verify backup created
ls -lh ../backups/pre-regen-*/client_backup.tar.gz
```

**Output:** Backup directory with restore script and snapshot.

### Phase 3: Regeneration (15 minutes)

```bash
cd /Users/efitz/Projects/tmi-clients/python-client-generated

# Run regeneration
./scripts/regenerate_client.sh 2>&1 | tee regeneration.log
```

**Monitor for:**
- ✓ Prerequisites met
- ✓ Client regenerated successfully
- ✓ Constructor patches applied
- ⚠️ Expected test failures (document these)

**Output:**
- Regenerated client code
- `docs/developer/REGENERATION_REPORT.md`
- Test logs

### Phase 4: Validation (30 minutes)

#### 4.1 Automated Validation
```bash
cd /Users/efitz/Projects/tmi-clients/python-client-generated

# Run validation
uv run scripts/validate_regeneration.py
```

**Expected:** All validations pass (✓ ALL VALIDATIONS PASSED)

#### 4.2 Manual Verification
```bash
# Check constructor patches
grep -C 3 "PATCH:" tmi_client/models/dfd_diagram.py
grep -C 3 "PATCH:" tmi_client/models/dfd_diagram_input.py

# Check new models exist
ls -1 tmi_client/models/*admin* | head -5
ls -1 tmi_client/models/*addon* | head -5

# Verify configuration
grep 'requires-python' pyproject.toml
grep 'certifi >=' requirements.txt
```

### Phase 5: Testing (1-2 hours)

#### 5.1 Auto-generated Tests
```bash
cd /Users/efitz/Projects/tmi-clients/python-client-generated

# Run all tests
uv run --with pytest python3 -m pytest test/ -v --tb=short 2>&1 | tee test_results.log

# Count results
grep -E "PASSED|FAILED|ERROR" test_results.log | tail -1
```

**Expected:**
- Most tests pass (239+)
- Some may fail if API changed (document these)

#### 5.2 Integration Test
```bash
# Run custom integration test
uv run test_diagram_fixes.py
```

**Expected:** Test passes (validates constructor patches)

#### 5.3 Import Test
```bash
# Quick import check
uv run python3 -c "import tmi_client; print('✓ Import successful')"
```

#### 5.4 New Features Smoke Test
```bash
# Test new models can be imported
uv run python3 -c "
from tmi_client.models.addon_response import AddonResponse
from tmi_client.models.administrator import Administrator
from tmi_client.models.admin_user import AdminUser
from tmi_client.models.webhook_event_type import WebhookEventType
print('✓ New models import successfully')
"
```

### Phase 6: Fix Issues (1-2 hours)

**If tests fail:**

1. **Analyze failures:**
   ```bash
   grep "FAILED" test_results.log | head -20
   ```

2. **Categorize:**
   - API changes (expected) - Document in MIGRATION_GUIDE.md
   - Cell schema changes (expected) - Update integration test
   - Unexpected failures - Investigate and fix

3. **Fix critical issues:**
   - Constructor patches not applied → Apply manually
   - Import errors → Check __init__.py files
   - Dependency issues → Verify requirements.txt

4. **Re-run tests:**
   ```bash
   uv run --with pytest python3 -m pytest test/ -v
   ```

### Phase 7: Documentation (2-3 hours)

#### 7.1 Update MIGRATION_GUIDE.md

Add section for latest version with:
- Breaking changes (cell attribute access)
- New features (Add-ons, Administration, SAML)
- Migration examples
- Code snippets

#### 7.2 Update CHANGELOG.md

Add entry:
```markdown
## [1.1.0] - 2025-12-06

### Added
- Add-ons API support (8 new endpoints)
- Administration API (27 new endpoints)
- SAML authentication support
- 36 new model classes for enterprise features
- Webhook event type enhancements

### Changed
- Cell attribute access now uses dictionaries instead of typed objects
- Removed 52 inline response models in favor of proper schemas

### Breaking Changes
- Cell attributes now accessed as `cell.attrs["line"]["stroke"]` instead of `cell.attrs.line.stroke`
- InlineResponse* models removed, replaced with proper schema classes

### Migration
See MIGRATION_GUIDE.md for detailed instructions.
```

#### 7.3 Update README.md

Add sections for:
- New Add-ons API
- Administration features
- SAML authentication
- Updated examples

#### 7.4 Review Generated Report

```bash
cat docs/developer/REGENERATION_REPORT.md
```

Verify it's accurate and complete.

### Phase 8: Commit (15 minutes)

```bash
cd /Users/efitz/Projects/tmi-clients/python-client-generated

# Review all changes
git status
git diff --stat

# Add all files
git add -A

# Commit with detailed message
git commit -F - << 'EOF'
regenerate: update Python client from latest OpenAPI spec v1.0.0

This regeneration adds enterprise features and consolidates the API structure.

New Features:
- Add-ons API (8 endpoints) - Extensibility support
- Administration API (27 endpoints) - User/group/quota management
- SAML authentication - Enterprise SSO support
- Enhanced webhook event types
- 36 new model classes

Changes:
- Cell attribute access changed from typed objects to dictionaries
- Removed 52 inline response models, replaced with proper schemas
- Updated dependencies to modern versions with CVE fixes
- Python 3.8+ required

Breaking Changes:
- Cell attributes: Use cell.attrs["line"]["stroke"] not cell.attrs.line.stroke
- InlineResponse* models removed (internal, low user impact)
- API organization updated (17 tags vs 14 modules)

Migration:
- See docs/developer/MIGRATION_GUIDE.md for detailed instructions
- Constructor patches applied for DFD diagram type preservation
- All tests updated and passing (239+ tests)

Technical Details:
- Generated with swagger-codegen 3.0.75
- Source: /Users/efitz/Projects/tmi/docs/reference/apis/tmi-openapi.json
- Analysis: docs/developer/SPEC_ANALYSIS.md
- Process: docs/developer/REGENERATION_PROCESS.md

Co-authored-by: Claude Sonnet 4.5 <noreply@anthropic.com>
EOF

# Create annotated tag
git tag -a v1.1.0 -m "Version 1.1.0 - Add enterprise features"

# Show commit
git show --stat HEAD
```

**Decision Point:** Review commit before pushing.

### Phase 9: Optional - Push (5 minutes)

```bash
# Push commit and tag
git push origin main
git push origin v1.1.0
```

## Success Criteria

- [ ] All validation checks pass
- [ ] Auto-generated tests pass (or failures documented)
- [ ] Integration test passes
- [ ] Import test succeeds
- [ ] New models can be imported
- [ ] Constructor patches applied
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] MIGRATION_GUIDE.md updated
- [ ] Committed to git

## Rollback Plan

If critical issues arise:

### Immediate Rollback
```bash
# Use restore script
cd /Users/efitz/Projects/tmi-clients
./backups/pre-regen-TIMESTAMP/restore.sh
```

### Git Revert
```bash
# If already committed
git revert HEAD
git push origin main
```

### Analysis
1. Document what went wrong
2. Review logs and error messages
3. Check spec validity
4. Verify tooling
5. Fix issues before re-attempting

## Timeline

| Phase | Duration | Status |
|-------|----------|--------|
| Analysis & Planning | 2 hours | ✅ Complete |
| Tooling Development | 2 hours | ✅ Complete |
| Preparation | 30 min | ⏳ Pending |
| Backup | 10 min | ⏳ Pending |
| Regeneration | 15 min | ⏳ Pending |
| Validation | 30 min | ⏳ Pending |
| Testing | 1-2 hours | ⏳ Pending |
| Fix Issues | 1-2 hours | ⏳ Pending |
| Documentation | 2-3 hours | ⏳ Pending |
| Commit | 15 min | ⏳ Pending |
| **Total** | **5-9 hours** | **45% Complete** |

## Risk Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Constructor patches fail | Low | High | Automated validation script |
| Tests fail unexpectedly | Medium | Medium | Comprehensive backup for rollback |
| Cell schema breaks code | Medium | Medium | Integration test validates patterns |
| Spec has errors | Low | High | Validation before regeneration |
| Lost custom code | Low | Critical | Backup script preserves all custom files |

## Communication

### Internal
- Document all changes in CHANGELOG.md
- Update MIGRATION_GUIDE.md
- Generate REGENERATION_REPORT.md

### External (if applicable)
- Release notes for v1.1.0
- Migration guide for users
- API documentation updates

## Next Steps

**Immediate (Today):**
1. Review this plan
2. Execute Phase 1: Preparation
3. Execute Phase 2: Backup
4. Execute Phase 3: Regeneration

**Short-term (This Week):**
5. Execute Phase 4: Validation
6. Execute Phase 5: Testing
7. Execute Phase 6: Fix Issues

**Follow-up (Next Week):**
8. Execute Phase 7: Documentation
9. Execute Phase 8: Commit
10. Execute Phase 9: Push (optional)

## Resources

### Documentation
- [SPEC_ANALYSIS.md](python-client-generated/docs/developer/SPEC_ANALYSIS.md)
- [REGENERATION_IMPACT.md](python-client-generated/docs/developer/REGENERATION_IMPACT.md)
- [REGENERATION_PROCESS.md](python-client-generated/docs/developer/REGENERATION_PROCESS.md)
- [CLAUDE.md](python-client-generated/CLAUDE.md)

### Scripts
- `scripts/analyze_spec_changes.py` - Analyze spec
- `scripts/backup_before_regen.sh` - Create backup
- `scripts/regenerate_client.sh` - Regenerate client
- `scripts/validate_regeneration.py` - Validate output

### OpenAPI Spec
- Location: `/Users/efitz/Projects/tmi/docs/reference/apis/tmi-openapi.json`
- Version: 1.0.0
- Paths: 89
- Schemas: 90

## Notes

- All scripts are executable and ready to use
- Backup system tested and verified
- Validation script covers all critical checks
- Documentation is comprehensive and up-to-date
- Rollback procedures are in place

## Approval

**Plan Author:** Claude Sonnet 4.5
**Date:** 2025-12-06
**Status:** ✅ Ready for Execution

**Execute when ready by following Phase 1: Preparation**
