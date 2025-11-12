# Python Client Regeneration Report

## Date
Wed Nov 12 14:34:19 EST 2025

## Changes Applied

### 1. Client Regenerated
- Source: `/Users/efitz/Projects/tmi/docs/reference/apis/tmi-openapi.json`
- Generator: swagger-codegen 3.0.75
- Package: tmi_client v1.0.0

### 2. Constructor Patches Applied
- ✓ DfdDiagram constructor fixed (type parameter preservation)
- ✓ DfdDiagramInput constructor fixed (type parameter preservation)

### 3. Modern Python Configuration
- ✓ Python 3.8+ requirement
- ✓ Updated dependencies:
  - certifi >= 2024.2.2 (security fixes)
  - six >= 1.16.0
  - python-dateutil >= 2.9.0
  - setuptools >= 70.0.0 (RCE vulnerability fix)
  - urllib3 >= 2.0.0 (CVE fixes)
- ✓ pyproject.toml with UV support
- ✓ pytest-based testing infrastructure

### 4. New Features in Generated Client
- Webhook API endpoints (5 new endpoints)
- Webhook schemas (WebhookSubscription, WebhookDelivery, etc.)
- Simplified cell schemas (inline objects instead of nested classes)

### 5. Breaking Changes
- Cell schema simplification: Property access changed from object attributes to dictionary access
- Removed classes: EdgeAttrsLine, NodeAttrsBody, NodeAttrsText, EdgeLabelAttrs, etc.
- Type safety reduced for nested cell properties

## Files Modified

### Generated API Classes
- Total API classes: 15

### Generated Model Classes
- Total model classes: 107

### Test Files
- Total test files: 121

## Next Steps

1. **Review Breaking Changes**: Check MIGRATION_GUIDE.md for cell schema changes
2. **Update Documentation**: Run documentation update tasks
3. **Manual Testing**: Test webhook endpoints and simplified cell schemas
4. **Update Dependent Projects**: Update any projects using this client

## Test Results

See test_output.log and integration_test_output.log for detailed test results.

