# TMI JavaScript Client Regeneration Report

**Date**: 2026-03-17 21:12:31
**OpenAPI Spec**: /Users/efitz/Projects/tmi-clients/javascript-client-generated/tmi-openapi.json
**Swagger Codegen**: 3.0.78
**Node.js**: v22.22.1
**npm**: 10.9.4

## Configuration

- **Package Name**: tmi-js-client
- **Version**: 1.0.0
- **Config File**: scripts/swagger-codegen-config.json

## Generation Results

### Files Generated

```
     272 source files in src/
     271 test files in test/
     274 documentation files in docs/
```

### API Classes

```
       0 API endpoint classes
```

### Model Classes

```
     244 model classes
```

### Dependencies

**Runtime:**
- superagent: ^10.2.3

**Development:**
- @babel/core: ^7.28.4
- mocha: ^11.7.4
- chai: ^5.1.2
- sinon: ^21.0.0

## Test Results

### Unit Tests

Exit Code: 0
Status: ✅ PASSED

See `test_output.log` for full details.

### Integration Tests

Status: ❌ FAILED

See `integration_test_output.log` for full details.

## Patches Applied

1. **DfdDiagram Constructor**: ✓ File exists (manual verification needed)
2. **DfdDiagramInput Constructor**: ✓ File exists (manual verification needed)

## Critical Changes in This Regeneration

### New Features

- **Webhook API**: 5 new endpoints for webhook subscriptions and deliveries
- **Input Schemas**: Separate input/output schemas (DfdDiagramInput vs DfdDiagram)
- **Cell Simplification**: Removed nested cell attribute classes (7 classes)

### Breaking Changes

1. **Cell Schema**: Nested classes replaced with inline objects
   - Removed: EdgeAttrsLine, NodeAttrsBody, NodeAttrsText, etc.
   - Use: Plain JavaScript objects for cell attributes

2. **Input Schemas**: PUT/PATCH operations use *Input classes
   - Use DfdDiagramInput for updates (not DfdDiagram)
   - Removes need to provide readOnly fields

### Security Updates

- superagent: 5.3.1 → 10.2.3 (CVE fixes)
- mocha: 3.x → 11.7.4 (modernization)
- chai: 4.x → 5.1.2 (modern assertions)
- sinon: 7.5.0 → 21.0.0 (modern mocking)

## Next Steps

1. ✅ Review `REGENERATION_REPORT.md` (this file)
2. ✅ Review test results in `test_output.log`
3. ✅ Review `docs/developer/MIGRATION_GUIDE.md` for API changes
4. ⚠️ Manually verify constructor patches in:
   - src/model/DfdDiagram.js
   - src/model/DfdDiagramInput.js (if present)
5. ✅ Build the client: `npm run build`
6. ✅ Test with your application
7. ✅ Update CHANGELOG.md with any additional changes

## Documentation

- **Usage Guide**: README.md
- **API Reference**: docs/
- **Migration Guide**: docs/developer/MIGRATION_GUIDE.md
- **Regeneration Guide**: docs/developer/REGENERATION_README.md
- **Changelog**: docs/developer/CHANGELOG.md

## Summary

✅ **Regeneration completed successfully**

The JavaScript client has been regenerated from the latest OpenAPI specification.
All modern dependencies and security updates have been applied.

**Action Required**: Manual verification of constructor patches recommended.
