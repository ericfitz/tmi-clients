# Pre-Regeneration Audit Report

**Date**: 2025-12-06
**Client**: JavaScript (tmi-js-client)
**Purpose**: Document state before regenerating from OpenAPI spec v1.0.0

## Current State

### Package Information
- **Name**: tmi-js-client
- **Version**: 1.0.0
- **Last Regenerated**: November 2-3, 2025

### Code Structure
- **API Classes**: 13 files (in src/tmi-client/)
- **Model Classes**: 100 files (in src/model/)
- **Total Source Files**: ~115 files

### Existing API Classes
1. AssetsApi.js
2. AuthenticationApi.js
3. CollaborationApi.js
4. DocumentsApi.js
5. GeneralApi.js
6. NotesApi.js
7. OAuthDiscoveryApi.js
8. OIDCDiscoveryApi.js
9. RepositoriesApi.js
10. ThreatModelSubResourcesApi.js
11. ThreatModelsApi.js
12. ThreatsApi.js
13. UsersApi.js

### Dependencies (Current)
**Production:**
- superagent: ^10.2.3

**Development:**
- @babel/cli: ^7.28.3
- @babel/core: ^7.28.4
- @babel/preset-env: ^7.28.3
- @babel/register: ^7.28.3
- chai: ^5.1.2
- mocha: ^11.7.4
- sinon: ^21.0.0

### Prerequisites Status
- ✅ swagger-codegen: 3.0.75
- ✅ Node.js: v22.21.0 (exceeds minimum 18+)
- ✅ npm: 11.6.1 (exceeds minimum 9+)
- ✅ OpenAPI spec exists: /Users/efitz/Projects/tmi/docs/reference/apis/tmi-openapi.json

### Git Status
- Clean working directory
- Only untracked file: docs/developer/REGENERATION_PLAN.md (just created)

### Infrastructure Files Present
- ✅ scripts/regenerate_client.sh (14KB, executable)
- ✅ scripts/swagger-codegen-config.json (387 bytes)
- ✅ test_diagram_fixes.js (integration test)
- ✅ docs/developer/ directory
- ✅ .babelrc (Babel configuration)
- ✅ package.json (modern dependencies)
- ✅ .swagger-codegen-ignore

### Known Missing Features (from spec analysis)
1. **Input Schemas** (9 total):
   - BaseDiagramInput
   - DfdDiagramInput
   - Plus 7 others (AssetInput, DocumentInput, etc. already exist)

2. **Webhook Models** (7 total):
   - WebhookSubscription
   - WebhookSubscriptionInput
   - WebhookDelivery
   - WebhookTestRequest
   - WebhookTestResponse
   - WebhookEventType
   - WebhookQuota

3. **Administrator Models** (20+ total):
   - Administrator, AdminUser, AdminGroup
   - Various request/response models
   - Group management models

4. **Addon Models** (6+ total):
   - AddonResponse, CreateAddonRequest
   - Invocation models

5. **Miscellaneous**:
   - DeletionStats
   - ClientCredentialInfo, ClientCredentialResponse

### Expected Changes After Regeneration
- **API Classes**: 13 → 14-16 (add AdministratorsApi, AddonsApi, update GeneralApi)
- **Model Classes**: 100 → ~110-120 (add 20+ new schemas)
- **Endpoints**: ~60-70 → 89 (significant expansion)

### Custom Patches Applied (Current)
- None documented in current code (auto-generated only)
- Integration test exists but may not run (ES6 module issues)

### Files to Preserve During Regeneration
1. package.json (modern dependencies)
2. .babelrc (transpilation config)
3. test_diagram_fixes.js (integration test)
4. docs/developer/ (all documentation)
5. scripts/ (regeneration infrastructure)
6. .swagger-codegen-ignore
7. REGENERATION_PLAN.md (just created)

### Risk Assessment
- **Low Risk**: All prerequisites met, clean git state, infrastructure ready
- **Medium Risk**: New constructor patches needed, Input schema validation
- **High Risk**: Breaking changes for users (to be documented)

## Recommendations

1. ✅ Proceed with regeneration
2. ✅ All prerequisites satisfied
3. ✅ Infrastructure ready
4. ⚠️ Monitor constructor patches during generation
5. ⚠️ Validate Input schemas after generation
6. ⚠️ Document all breaking changes

## Next Steps
1. Update regeneration script with better validation
2. Update integration tests for new features
3. Create documentation templates
4. Execute regeneration
5. Run comprehensive testing

---

**Audit Complete**: Ready for Phase 2
