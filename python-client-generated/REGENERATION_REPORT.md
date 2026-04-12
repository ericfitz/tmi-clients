# Python Client Regeneration Report

Generated: 2026-04-11 21:10:19

## Changes Applied

### Client Regenerated
- Source: `https://raw.githubusercontent.com/ericfitz/tmi/refs/heads/main/api-schema/tmi-openapi.json`
- Generator: openapi-generator 7.x
- Package: tmi_client v1.4.0
- Models: Pydantic v2 with full type hints

### Patches Applied
- Regex validator fix (openapi-generator bug: regex validators on non-string fields like UUID and datetime fail because Pydantic parses the value before the validator runs)
- Test return-type fix (openapi-generator bug: make_instance() stubs declare a model return type but body is commented out, causing type-checker errors)
- urllib3 minimum version bump to >= 2.6.3 (CVE fixes for decompression-bomb and redirect vulnerabilities)

### Generated Configuration
- pyproject.toml with Pydantic v2 dependencies
- Python 3.9+ requirement
- pytest-based testing infrastructure
- mypy configuration for type checking

## Files Generated

- API classes: 32
- Model classes: 247
- Test files: 278

## Test Results

See test_output.log and integration_test_output.log for detailed test results.

## Next Steps

1. Review this report
2. Check test_output.log for test failures
3. Update documentation files
4. Test against live API endpoints
