# JavaScript Client Regeneration Plan

## Executive Summary

This plan outlines the strategy for updating the JavaScript client from the latest OpenAPI specification (v1.0.0). The specification has been significantly enhanced since the last generation, adding **20+ new schemas**, **30+ new endpoints**, and **2 new API categories** (webhooks and administrators).

**Key Changes Since Last Generation:**
- 90 schemas in spec vs. 100 existing models (schema reorganization)
- 89 API endpoints (significant expansion)
- New webhook API (7 endpoints)
- New administrators API (17 endpoints)
- New addon system (3 endpoints)
- Missing Input schemas (DfdDiagramInput, BaseDiagramInput, etc.)
- Admin/group/quota management features

## Current State Analysis

### Existing JavaScript Client

**Package**: `tmi-js-client` v1.0.0
- **API Classes**: 13 (in `src/tmi-client/`)
- **Model Classes**: 100 (in `src/model/`)
- **Dependencies**: Modern and secure (superagent 10.2.3, mocha 11.7.4, babel 7.28.x)
- **Build System**: ES6 modules with Babel transpilation
- **Testing**: Mocha + Chai + Sinon
- **Last Regenerated**: November 2, 2025

**Existing APIs:**
1. AssetsApi
2. AuthenticationApi
3. CollaborationApi
4. DocumentsApi
5. GeneralApi
6. NotesApi
7. OAuthDiscoveryApi
8. OIDCDiscoveryApi
9. RepositoriesApi
10. ThreatModelSubResourcesApi
11. ThreatModelsApi
12. ThreatsApi
13. UsersApi

**Infrastructure Ready:**
- ✅ Regeneration script exists (`scripts/regenerate_client.sh`)
- ✅ Swagger-codegen config exists (`scripts/swagger-codegen-config.json`)
- ✅ Developer documentation structure in place
- ✅ Integration test file exists (`test_diagram_fixes.js`)
- ✅ Modern package.json with security-hardened dependencies

### OpenAPI Specification v1.0.0

**Schemas**: 90 total
**Endpoints**: 89 total across multiple categories
**New Tags**: `webhooks`, `Administrators` (plus existing categories)

**Critical Missing Schemas in Current Client:**
1. **Input Schemas** (9 total):
   - `BaseDiagramInput` - Base class for diagram inputs
   - `DfdDiagramInput` - DFD diagram input (no readOnly fields)
   - Plus 7 existing Input schemas (Asset, Document, Note, etc.)

2. **Webhook Schemas** (7 total):
   - `WebhookSubscription`
   - `WebhookSubscriptionInput`
   - `WebhookDelivery`
   - `WebhookTestRequest`
   - `WebhookTestResponse`
   - `WebhookEventType`
   - `WebhookQuota`

3. **Administrator Schemas** (20+ total):
   - `Administrator`, `AdminUser`, `AdminGroup`
   - `AdminUserListResponse`, `AdminGroupListResponse`
   - `CreateAdministratorRequest`, `CreateAdminGroupRequest`
   - `UpdateAdminUserRequest`, `UpdateAdminGroupRequest`
   - `AddGroupMemberRequest`
   - `Group`, `GroupMember`, `GroupMemberListResponse`
   - `UserWithAdminStatus`

4. **Addon Schemas** (6+ total):
   - `AddonResponse`, `ListAddonsResponse`
   - `CreateAddonRequest`
   - `InvokeAddonRequest`, `InvokeAddonResponse`
   - `AddonInvocationQuota`
   - `InvocationListResponse`

5. **Miscellaneous**:
   - `DeletionStats` - Stats from bulk delete operations
   - `ClientCredentialInfo`, `ClientCredentialResponse` - OAuth client credentials

**Expected New/Updated API Classes:**
- Existing `GeneralApi` may gain webhook endpoints (7 endpoints)
- New `AdministratorsApi` for admin operations (17 endpoints)
- New `AddonsApi` for addon management (3 endpoints)
- Possible new `AdminQuotasApi` or quota endpoints in existing APIs

## Regeneration Strategy

### Phase 1: Pre-Regeneration (Investigation & Backup)

**Objectives:**
1. Document current state completely
2. Identify all custom modifications to preserve
3. Verify prerequisites
4. Create comprehensive backup

**Tasks:**
1. **Audit Current Client**
   - Count existing APIs and models
   - Document any manual patches applied
   - Identify custom test files
   - Review integration test coverage

2. **Analyze OpenAPI Spec Changes**
   - Compare schema counts (spec vs. current)
   - Identify new schemas by category
   - Map endpoint growth by tag
   - Document breaking changes

3. **Verify Prerequisites**
   - swagger-codegen 3.0.75+
   - Node.js 18+
   - npm 9+
   - OpenAPI spec exists at expected path

4. **Backup Critical Files**
   - `package.json` (modern dependencies)
   - `.babelrc` (transpilation config)
   - `test_diagram_fixes.js` (integration tests)
   - `docs/developer/` (all documentation)
   - `scripts/` (regeneration infrastructure)
   - `.swagger-codegen-ignore` (custom ignores)

### Phase 2: Update Regeneration Infrastructure

**Objectives:**
1. Update regeneration script for new changes
2. Ensure configuration handles all new schemas
3. Add validation steps for critical features

**Tasks:**
1. **Review and Update `regenerate_client.sh`**
   - Verify backup/restore logic
   - Update patch application for new models
   - Add validation for Input schemas
   - Add validation for webhook models
   - Add validation for admin models
   - Improve reporting (count APIs, models, endpoints)

2. **Review `swagger-codegen-config.json`**
   - Verify all settings are optimal
   - Check if any new options needed for v1.0.0 spec
   - Ensure ES6 and Promise settings correct

3. **Update Integration Tests**
   - Add tests for `DfdDiagramInput` existence
   - Add tests for `BaseDiagramInput` existence
   - Add tests for webhook models
   - Add tests for admin models
   - Verify constructor patches work

4. **Update Documentation Templates**
   - Prepare CHANGELOG.md for JavaScript client
   - Prepare MIGRATION_GUIDE.md for JavaScript client
   - Update REGENERATION_README.md with new process details

### Phase 3: Execute Regeneration

**Objectives:**
1. Generate fresh client from latest OpenAPI spec
2. Apply all necessary patches
3. Verify all expected schemas and APIs generated

**Tasks:**
1. **Run Regeneration Script**
   ```bash
   cd javascript-client-generated
   ./scripts/regenerate_client.sh
   ```

2. **Verify Generation Output**
   - Check API count (should be 14-16, up from 13)
   - Check model count (should be ~110+, reorganized from 100)
   - Verify Input schemas exist (9 files)
   - Verify webhook models exist (7 files)
   - Verify admin models exist (20+ files)
   - Verify addon models exist (6+ files)

3. **Manual Patch Verification**
   - `src/model/DfdDiagram.js` - Constructor preserves type
   - `src/model/DfdDiagramInput.js` - Constructor preserves type (new file)
   - Any other inheritance issues

### Phase 4: Testing & Validation

**Objectives:**
1. Ensure all generated code compiles
2. Run comprehensive test suite
3. Validate critical features work correctly

**Tasks:**
1. **Install Dependencies**
   ```bash
   npm install
   ```

2. **Build Client**
   ```bash
   npm run build
   ```
   - Verify Babel transpilation succeeds
   - Check for any syntax errors
   - Verify dist/ directory created

3. **Run Unit Tests**
   ```bash
   npm test
   ```
   - All auto-generated tests should pass
   - Review any failures
   - Document any known issues

4. **Run Integration Tests**
   ```bash
   node test_diagram_fixes.js
   ```
   - Verify DfdDiagram constructor works
   - Verify DfdDiagramInput exists and works
   - Verify webhook models exist
   - Verify admin models exist

5. **Manual Smoke Tests**
   - Import main index.js
   - Instantiate each API class
   - Verify model constructors work
   - Test critical Input schemas

### Phase 5: Documentation & Finalization

**Objectives:**
1. Document all changes comprehensively
2. Create migration guide for users
3. Generate regeneration report

**Tasks:**
1. **Create CHANGELOG.md**
   - Document all new APIs
   - Document all new models
   - Document breaking changes
   - Document fixes applied

2. **Create MIGRATION_GUIDE.md**
   - Breaking changes section
   - New features guide
   - Code examples for webhook API
   - Code examples for admin API
   - Migration path from previous version

3. **Update REGENERATION_README.md**
   - Document any new prerequisites
   - Update script instructions
   - Add troubleshooting section

4. **Generate REGENERATION_REPORT.md**
   - Timestamp and versions
   - Schema counts (before/after)
   - API counts (before/after)
   - Test results
   - Known issues
   - Manual verification needed

5. **Update Main README.md**
   - Add webhook API examples
   - Add admin API examples
   - Update version references
   - Update feature list

## Critical Patches Required

Based on Python client experience, these patches will be needed:

### 1. DfdDiagram Constructor Patch

**File**: `src/model/DfdDiagram.js`
**Issue**: Constructor calls `super()` which may overwrite `type` parameter
**Fix**: Ensure `type` is preserved when calling parent constructor

**Python Pattern** (for reference):
```python
def __init__(self, type, cells, ...):
    kwargs['type'] = type  # Preserve type before super().__init__()
    super().__init__(...)
```

**JavaScript Pattern** (expected):
```javascript
constructor(type, cells, id, name, createdAt, modifiedAt) {
    super(id, name, type, createdAt, modifiedAt);  // Ensure type passed correctly
    this.cells = cells;
}
```

### 2. DfdDiagramInput Constructor Patch

**File**: `src/model/DfdDiagramInput.js` (NEW FILE)
**Issue**: Same as DfdDiagram
**Fix**: Same pattern - preserve type parameter

### 3. Verify Input Schema Separation

**Critical Models to Check:**
- `BaseDiagramInput.js` - Should NOT have readOnly fields (id, created_at, modified_at)
- `DfdDiagramInput.js` - Should extend BaseDiagramInput, no readOnly fields
- All other *Input.js files - Verify no readOnly fields

## Expected File Changes

### New Files (Expected)

**Models** (~30+ new files):
- `src/model/BaseDiagramInput.js`
- `src/model/DfdDiagramInput.js`
- `src/model/WebhookSubscription.js`
- `src/model/WebhookSubscriptionInput.js`
- `src/model/WebhookDelivery.js`
- `src/model/WebhookTestRequest.js`
- `src/model/WebhookTestResponse.js`
- `src/model/WebhookEventType.js`
- `src/model/WebhookQuota.js`
- `src/model/Administrator.js`
- `src/model/AdminUser.js`
- `src/model/AdminGroup.js`
- `src/model/AdminUserListResponse.js`
- `src/model/AdminGroupListResponse.js`
- `src/model/CreateAdministratorRequest.js`
- `src/model/CreateAdminGroupRequest.js`
- `src/model/UpdateAdminUserRequest.js`
- `src/model/UpdateAdminGroupRequest.js`
- `src/model/AddGroupMemberRequest.js`
- `src/model/Group.js`
- `src/model/GroupMember.js`
- `src/model/GroupMemberListResponse.js`
- `src/model/UserWithAdminStatus.js`
- `src/model/AddonResponse.js`
- `src/model/ListAddonsResponse.js`
- `src/model/CreateAddonRequest.js`
- `src/model/InvokeAddonRequest.js`
- `src/model/InvokeAddonResponse.js`
- `src/model/AddonInvocationQuota.js`
- `src/model/InvocationListResponse.js`
- `src/model/DeletionStats.js`
- `src/model/ClientCredentialInfo.js`
- `src/model/ClientCredentialResponse.js`

**APIs** (~1-3 new files):
- `src/tmi-client/AdministratorsApi.js` (possible - 17 endpoints)
- `src/tmi-client/AddonsApi.js` (possible - 3 endpoints)
- Updates to `src/tmi-client/GeneralApi.js` (webhook endpoints)

**Tests** (~30+ new test files):
- `test/model/BaseDiagramInput.spec.js`
- `test/model/DfdDiagramInput.spec.js`
- `test/model/WebhookSubscription.spec.js`
- (and ~27+ more for other new models)
- `test/api/AdministratorsApi.spec.js` (if new API created)
- `test/api/AddonsApi.spec.js` (if new API created)

**Documentation** (~30+ new doc files):
- `docs/BaseDiagramInput.md`
- `docs/DfdDiagramInput.md`
- `docs/WebhookSubscription.md`
- (and ~27+ more for other new models)
- `docs/AdministratorsApi.md` (if new API created)
- `docs/AddonsApi.md` (if new API created)

### Modified Files (Expected)

**Core Files**:
- `src/index.js` - Updated exports for new models and APIs
- `README.md` - Auto-generated with new content

**Existing API Files** (may gain endpoints):
- `src/tmi-client/GeneralApi.js` - Webhook endpoints
- `src/tmi-client/UsersApi.js` - Possible admin user endpoints
- `src/tmi-client/AuthenticationApi.js` - Possible client credential endpoints

**Test Files**:
- Various existing test files may be updated

### Removed Files (Unlikely)

Based on schema comparison, some models may be removed or renamed due to OpenAPI spec reorganization. This will be evident during regeneration.

## Risk Assessment

### High Risk Items

1. **Constructor Type Preservation**
   - **Risk**: Type parameter overwritten in DfdDiagram/DfdDiagramInput
   - **Impact**: Cannot create diagrams programmatically
   - **Mitigation**: Automatic patch in regeneration script + manual verification
   - **Validation**: Integration test must verify type preservation

2. **Input Schema Separation**
   - **Risk**: Input schemas generated with readOnly fields
   - **Impact**: Cannot update diagrams (validation errors)
   - **Mitigation**: Verify OpenAPI spec defines separate Input schemas
   - **Validation**: Check for BaseDiagramInput.js and DfdDiagramInput.js files

3. **Breaking Changes for Existing Users**
   - **Risk**: API signature changes, model removals
   - **Impact**: User code breaks after upgrade
   - **Mitigation**: Comprehensive MIGRATION_GUIDE.md + CHANGELOG.md
   - **Validation**: Document all breaking changes

### Medium Risk Items

1. **Dependency Version Conflicts**
   - **Risk**: New generated code requires different dependency versions
   - **Impact**: Build failures, runtime errors
   - **Mitigation**: Restore modern package.json from backup
   - **Validation**: `npm install` and `npm audit` succeed

2. **Test Coverage Gaps**
   - **Risk**: New features not covered by tests
   - **Impact**: Bugs in new code
   - **Mitigation**: Add integration tests for webhooks, admin APIs
   - **Validation**: Integration test coverage report

3. **Documentation Accuracy**
   - **Risk**: Auto-generated docs incomplete or incorrect
   - **Impact**: User confusion, support burden
   - **Mitigation**: Manual review of critical API docs
   - **Validation**: Spot-check webhook and admin API documentation

### Low Risk Items

1. **Babel Transpilation Issues**
   - **Risk**: Generated ES6 code incompatible with Babel
   - **Impact**: Build failures
   - **Mitigation**: `.babelrc` preserved from backup
   - **Validation**: `npm run build` succeeds

2. **Git Merge Conflicts**
   - **Risk**: Conflicts when committing regenerated client
   - **Impact**: Manual conflict resolution
   - **Mitigation**: Commit current state before regeneration
   - **Validation**: Clean git status before starting

## Success Criteria

The regeneration is successful when:

### Generation Success
- ✅ Swagger-codegen completes without errors
- ✅ All expected files created (models, APIs, tests, docs)
- ✅ Model count ≥ 110 (was 100)
- ✅ API count ≥ 14 (was 13)
- ✅ Input schemas exist (9 files)
- ✅ Webhook models exist (7 files)
- ✅ Admin models exist (20+ files)

### Build Success
- ✅ `npm install` completes without errors
- ✅ `npm audit` shows no vulnerabilities
- ✅ `npm run build` completes without errors
- ✅ `dist/` directory created with transpiled code

### Test Success
- ✅ `npm test` passes (all auto-generated unit tests)
- ✅ Integration tests pass (`node test_diagram_fixes.js`)
- ✅ No regressions in existing functionality
- ✅ New models instantiate correctly

### Patch Success
- ✅ DfdDiagram constructor preserves type parameter
- ✅ DfdDiagramInput constructor preserves type parameter
- ✅ BaseDiagramInput has no readOnly fields
- ✅ All Input schemas validate correctly

### Documentation Success
- ✅ CHANGELOG.md created with all changes
- ✅ MIGRATION_GUIDE.md created with examples
- ✅ REGENERATION_REPORT.md generated
- ✅ API documentation includes webhook examples
- ✅ API documentation includes admin examples

### Integration Success
- ✅ Can create DfdDiagram instances
- ✅ Can create DfdDiagramInput instances
- ✅ Webhook models importable and functional
- ✅ Admin models importable and functional
- ✅ No breaking changes for basic usage (or documented)

## Post-Regeneration Tasks

1. **Code Review**
   - Review all constructor implementations
   - Spot-check new API classes
   - Verify Input schema implementations
   - Check for any deprecated patterns

2. **Testing**
   - Run full test suite multiple times
   - Test with real TMI API (if available)
   - Verify webhook subscription flow
   - Verify admin operations (if test account available)

3. **Documentation Review**
   - Read through MIGRATION_GUIDE.md
   - Verify code examples work
   - Check API reference accuracy
   - Update main project README if needed

4. **Git Workflow**
   - Review `git diff` for unexpected changes
   - Commit regenerated client
   - Tag release (e.g., `js-client-v1.0.0`)
   - Push to repository

5. **Communication**
   - Announce update to users
   - Highlight new features (webhooks, admin API)
   - Provide migration timeline if breaking changes
   - Update any external documentation

## Rollback Plan

If regeneration fails or introduces critical bugs:

1. **Immediate Rollback**
   ```bash
   git reset --hard HEAD  # If not committed
   git revert <commit>    # If committed
   ```

2. **Restore from Backup**
   ```bash
   cp -r .regeneration_backup/* .
   npm install
   npm test
   ```

3. **Investigation**
   - Review REGENERATION_REPORT.md
   - Check test_output.log
   - Review integration_test_output.log
   - Examine specific failures

4. **Iterative Fix**
   - Fix specific issues (patches, config)
   - Re-run regeneration
   - Test incrementally
   - Document workarounds

## Timeline Estimate

- **Phase 1 (Investigation & Backup)**: 1-2 hours
- **Phase 2 (Update Infrastructure)**: 2-3 hours
- **Phase 3 (Execute Regeneration)**: 30 minutes
- **Phase 4 (Testing & Validation)**: 2-3 hours
- **Phase 5 (Documentation)**: 2-3 hours
- **Total**: 8-12 hours

## Dependencies

### Required Tools
- swagger-codegen 3.0.75+
- Node.js 18+
- npm 9+
- Git

### Required Files
- OpenAPI spec: `/Users/efitz/Projects/tmi/docs/reference/apis/tmi-openapi.json`
- Config: `scripts/swagger-codegen-config.json`
- Script: `scripts/regenerate_client.sh`

### Optional Tools
- jq (for OpenAPI spec analysis)
- diff tools (for comparing changes)

## Appendix A: Schema Comparison

### Schemas in Spec but Not in Current Client (20+)

Based on preliminary analysis:
- AddGroupMemberRequest
- AddonInvocationQuota
- AddonResponse
- AdminGroup
- AdminGroupListResponse
- AdminUser
- AdminUserListResponse
- Administrator
- BaseDiagramInput ⚠️ **CRITICAL**
- ClientCredentialInfo
- ClientCredentialResponse
- CreateAddonRequest
- CreateAdminGroupRequest
- CreateAdministratorRequest
- DeletionStats
- DfdDiagramInput ⚠️ **CRITICAL**
- Group
- GroupMember
- GroupMemberListResponse
- InvocationListResponse
- (Plus more - full list TBD after regeneration)

### Schemas in Client but Not in Spec

This will be determined during regeneration. Some models may have been:
- Renamed in the spec
- Merged into other models
- Removed from the spec
- Reorganized

## Appendix B: Endpoint Comparison

### Current Endpoints Coverage
- 13 API classes covering ~60-70 endpoints (estimated)

### Expected Endpoints in Spec
- 89 total endpoints
- ~7 webhook endpoints (new)
- ~17 admin endpoints (new)
- ~3 addon endpoints (new)
- Remaining endpoints in existing categories

### Growth Areas
- **Webhooks**: Subscription management, delivery tracking, testing
- **Administrators**: User/group management, privilege assignment
- **Addons**: Custom addon system
- **Quotas**: Resource quota management
- **OAuth**: Client credential management

## Appendix C: References

- Python client MIGRATION_GUIDE.md (similar changes expected)
- Python client CHANGELOG.md (feature reference)
- OpenAPI spec v1.0.0 at `/Users/efitz/Projects/tmi/docs/reference/apis/tmi-openapi.json`
- Swagger Codegen JavaScript docs: https://github.com/swagger-api/swagger-codegen
