# Python Client Regeneration Report

Generated: 2026-03-17 22:00:22

## Changes Applied

### Client Regenerated
- Source: `https://raw.githubusercontent.com/ericfitz/tmi/refs/heads/main/api-schema/tmi-openapi.json`
- Generator: swagger-codegen 3.0.75
- Package: tmi_client v1.0.0

### Constructor Patches Applied
- DfdDiagram constructor fixed (type parameter preservation)
- DfdDiagramInput constructor fixed (type parameter preservation)
- Edge constructor fixed (shape parameter preservation)
- Node constructor fixed (shape parameter preservation)
- Configuration.auth_settings() fixed (bearerAuth implementation)

### Modern Python Configuration
- Python 3.9+ requirement
- Updated dependencies (latest Python 3.9+ compatible versions)
- pyproject.toml with UV support
- pytest-based testing infrastructure

## Files Generated

- API classes: 25
- Model classes: 231
- Test files: 255

## Test Results

See test_output.log and integration_test_output.log for detailed test results.

## Next Steps

1. Review this report
2. Check test_output.log for test failures
3. Update documentation files
4. Test webhook endpoints
