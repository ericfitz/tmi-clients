# Python Client Regeneration Report

## Date
Sat Feb 28 23:13:24 EST 2026

## Changes Applied

### 1. Client Regenerated
- Source: `https://raw.githubusercontent.com/ericfitz/tmi/refs/heads/main/api-schema/tmi-openapi.json`
- Generator: swagger-codegen 3.0.75
- Package: tmi_client v1.0.0

### 2. Constructor Patches Applied
- ✓ DfdDiagram constructor fixed (type parameter preservation)
- ✓ DfdDiagramInput constructor fixed (type parameter preservation)

### 3. Modern Python Configuration
- ✓ Python 3.8+ requirement
- ✓ Updated dependencies (latest Python 3.8+ compatible versions):
  - certifi >= 2025.11.12
  - six >= 1.17.0
  - python-dateutil >= 2.9.0.post0
  - setuptools >= 75.3.2
  - urllib3 >= 2.2.3
  - pytest >= 8.3.5
  - pytest-cov >= 5.0.0
  - pytest-randomly >= 3.15.0
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
- Total API classes: 25

### Generated Model Classes
- Total model classes: 231

### Test Files
- Total test files: 255

## Next Steps

1. **Review Breaking Changes**: Check MIGRATION_GUIDE.md for cell schema changes
2. **Update Documentation**: Run documentation update tasks
3. **Manual Testing**: Test webhook endpoints and simplified cell schemas
4. **Update Dependent Projects**: Update any projects using this client

## Test Results

See test_output.log and integration_test_output.log for detailed test results.

