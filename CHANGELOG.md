# Changelog

All notable changes to the TMI Python Client will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-12

### ⚠️ BREAKING CHANGES

#### Package Renamed
- **BREAKING**: Package renamed from `swagger_client` to `tmi_client`
  - All imports must be updated: `import swagger_client` → `import tmi_client`
  - Affects all model imports, API imports, and configuration

#### Cell Schema Simplification
- **BREAKING**: Cell attributes now use inline objects instead of nested classes
  - Removed 7 nested cell classes:
    - `EdgeAttrsLine`
    - `EdgeAttrsLineTargetMarker`
    - `EdgeAttrsLineSourceMarker`
    - `NodeAttrsBody`
    - `NodeAttrsText`
    - `EdgeLabelAttrs`
    - `EdgeLabelAttrsText`
  - Cell attributes are now dictionaries/objects (no type safety for nested properties)
  - Property access changed: `edge.attrs.line.stroke` → `edge.attrs["line"]["stroke"]`
  - More flexible: can pass arbitrary X6 properties
  - Closer to X6's native JSON format

#### Python Version Requirement
- **BREAKING**: Python 3.8+ is now required
  - Dropped support for Python 2.x and Python 3.7
  - Modern async/await support and type hints now available

### Added

#### Webhook API Support (5 New Endpoints)
- Added `WebhooksApi` class with full webhook subscription management
- New endpoints:
  - `GET /webhooks/subscriptions` - List webhook subscriptions
  - `POST /webhooks/subscriptions` - Create webhook subscription
  - `GET /webhooks/subscriptions/{id}` - Get webhook subscription
  - `PUT /webhooks/subscriptions/{id}` - Update webhook subscription
  - `DELETE /webhooks/subscriptions/{id}` - Delete webhook subscription
  - `POST /webhooks/subscriptions/{id}/test` - Test webhook subscription
  - `GET /webhooks/deliveries` - List webhook deliveries
  - `GET /webhooks/deliveries/{id}` - Get webhook delivery

#### New Schemas
- `WebhookSubscription` - Webhook subscription output (with readOnly fields)
- `WebhookSubscriptionInput` - Webhook subscription input (no readOnly fields)
- `WebhookDelivery` - Webhook delivery attempt record
- `WebhookTestRequest` - Webhook test request
- `WebhookTestResponse` - Webhook test response
- `BaseDiagramInput` - Base diagram input schema (no readOnly fields)
- `DfdDiagramInput` - DFD diagram input schema for PUT/PATCH operations

#### Modern Python Packaging
- Added `pyproject.toml` for modern Python packaging
- UV-compatible dependency management
- Structured project metadata

#### Testing Infrastructure
- Migrated from `nose` (deprecated) to `pytest`
- Added `pytest-cov` for code coverage
- Added `pytest-randomly` for randomized test execution
- Created comprehensive integration test (`test_diagram_fixes.py`)

### Fixed

#### Constructor Patches Applied
- **CRITICAL FIX**: DfdDiagram can now be instantiated without type field being overwritten
  - Fixed: `kwargs['type'] = type` passed to parent `BaseDiagram.__init__()`
  - Fixed: `DfdDiagramInput` has same patch applied
  - Resolves "Invalid value for `type` (None)" error

#### ReadOnly Fields Issue Resolved
- **CRITICAL FIX**: Created separate Input schemas for PUT/PATCH operations
  - `DfdDiagramInput` no longer requires readOnly fields (`id`, `created_at`, `modified_at`)
  - `BaseDiagramInput` provides clean base for input operations
  - Resolves "Invalid value for `id`, must not be `None`" error

#### API Return Type Consistency
- All diagram endpoints now return `DfdDiagram` (not generic `Diagram`)
- Removed need for defensive `isinstance()` checks
- Improved type safety and IDE autocomplete

#### Discriminator Mapping
- Added `x-discriminator-value` annotations to `DfdDiagram` and `DfdDiagramInput`
- Improved polymorphic schema handling

### Changed

#### Dependency Updates (Security-Critical)
- Updated `certifi` from 14.05.14 to >= 2.024.2.2 (critical security fixes)
- Updated `six` from 1.10 to >= 1.16.0
- Updated `python-dateutil` from 2.5.3 to >= 2.9.0
- Updated `setuptools` from 21.0.0 to >= 70.0.0 (fixes CVE-2022-40897 RCE vulnerability)
- Updated `urllib3` from 1.15.1 to >= 2.0.0 (multiple CVE fixes)

#### Build System Modernization
- Migrated from `setup.py` only to `pyproject.toml` + `setup.py`
- Added modern build system requirements
- Improved dependency resolution

### Deprecated

- `Diagram` class - Use `DfdDiagram` instead
  - Kept for backward compatibility
  - Will be removed in future major version

### Removed

- **Python 2.x support** - No longer maintained
- **Python 3.7 support** - End of life
- **7 nested cell classes** - See Breaking Changes section
- **nose test runner** - Migrated to pytest

### Security

- Fixed RCE vulnerability in setuptools (CVE-2022-40897)
- Updated urllib3 to fix multiple CVEs (SSL verification issues)
- Updated certifi with latest CA certificates
- All dependencies now use maintained versions with active security support

---

## Pre-1.0.0 Changes

### Original Issues Fixed (Before 1.0.0 Release)

These fixes were applied to the OpenAPI specification and are included in the 1.0.0 release:

1. **DfdDiagram Inheritance Bug** - Constructor overwrote type field
2. **Inconsistent Return Types** - Mixed dict/object returns
3. **ReadOnly Fields in Constructors** - Required fields that shouldn't be in input
4. **Empty Diagram Base Class** - Wrapper class with no properties
5. **DiagramListItem Relationship** - Unclear relationship documentation
6. **Discriminator Mapping** - Missing x-discriminator-value annotations

See [OPENAPI_ISSUES_SUMMARY.md](OPENAPI_ISSUES_SUMMARY.md) for detailed technical analysis.

---

## Migration Guide

For detailed migration instructions, see [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md).

### Quick Migration Checklist

- [ ] Update all imports: `swagger_client` → `tmi_client`
- [ ] Verify Python version is 3.8 or higher
- [ ] Replace `DfdDiagram` with `DfdDiagramInput` for PUT/PATCH operations
- [ ] Update cell attribute access from object properties to dictionary keys
- [ ] Run tests: `pytest test/` or `uv run --with pytest python3 -m pytest test/ -v`
- [ ] Update dependencies in your project's requirements.txt or pyproject.toml
- [ ] Optional: Add webhook support if needed

---

## Support

For issues or questions:
1. Check [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) for migration help
2. Review [OPENAPI_ISSUES_SUMMARY.md](OPENAPI_ISSUES_SUMMARY.md) for technical details
3. Run integration tests: `uv run test_diagram_fixes.py`
4. See [CLAUDE.md](CLAUDE.md) for development guidance

---

## Release Information

**Release Date**: 2025-11-12
**OpenAPI Spec Version**: 1.0.0
**Generator**: swagger-codegen 3.0.75
**Python Version**: >= 3.8
**Package Name**: tmi-client (formerly swagger-client)
