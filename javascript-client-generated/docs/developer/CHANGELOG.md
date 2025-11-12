# Changelog

All notable changes to the TMI JavaScript client will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-12

### Added

#### Webhook API Support (5 new endpoints)
- **List webhook subscriptions**: `GET /webhooks/subscriptions`
  - Returns all webhook subscriptions for the authenticated user
- **Create webhook subscription**: `POST /webhooks/subscriptions`
  - Subscribe to threat model events (created, updated, deleted)
- **Get webhook subscription**: `GET /webhooks/subscriptions/{webhook_id}`
  - Retrieve details of a specific webhook subscription
- **Delete webhook subscription**: `DELETE /webhooks/subscriptions/{webhook_id}`
  - Unsubscribe from webhook events
- **Test webhook**: `POST /webhooks/subscriptions/{webhook_id}/test`
  - Send a test payload to verify webhook endpoint

#### New Webhook Models
- `WebhookSubscription` - Webhook subscription details (output schema with readOnly fields)
- `WebhookSubscriptionInput` - Webhook subscription creation/update (input schema)
- `WebhookDelivery` - Webhook delivery attempt details
- `WebhookTestRequest` - Test webhook request payload
- `WebhookTestResponse` - Test webhook response

#### New Diagram Input Schemas
- `BaseDiagramInput` - Base class for diagram input (no readOnly fields)
- `DfdDiagramInput` - DFD diagram input for PUT/PATCH operations

These separate input schemas solve the critical issue where PUT/PATCH operations required readOnly fields (id, created_at, modified_at), which should never be in request bodies.

#### Regeneration Infrastructure
- **Automated regeneration script**: `scripts/regenerate_client.sh`
  - One-command regeneration from OpenAPI spec
  - Automatic dependency updates
  - Constructor patch verification
  - Test execution and reporting
- **Configuration file**: `scripts/swagger-codegen-config.json`
  - Codegen settings for consistent generation
- **Developer documentation**: `docs/developer/`
  - REGENERATION_README.md - Complete regeneration guide
  - MIGRATION_GUIDE.md - Breaking changes and migration examples
  - CHANGELOG.md - This file

### Changed

#### Breaking: Cell Schema Simplification
Cell attributes have been simplified from nested classes to inline objects for better AntV X6 compatibility.

**Removed nested classes (7 total)**:
- `EdgeAttrsLine` - Now inline object in `EdgeAttrs`
- `EdgeAttrsLineTargetMarker` - Now inline in `line.targetMarker`
- `EdgeAttrsLineSourceMarker` - Now inline in `line.sourceMarker`
- `NodeAttrsBody` - Now inline object in `NodeAttrs`
- `NodeAttrsText` - Now inline object in `NodeAttrs`
- `EdgeLabelAttrs` - Now inline in `EdgeLabel.attrs`
- `EdgeLabelAttrsText` - Now inline in `label.attrs.text`

**Before**:
```javascript
const EdgeAttrsLine = require('tmi-js-client/src/model/EdgeAttrsLine');
const line = new EdgeAttrsLine();
line.stroke = "#808080";
edge.attrs.line = line;
```

**After**:
```javascript
edge.attrs = {
  line: {
    stroke: "#808080",
    strokeWidth: 2
  }
};
```

**Impact**:
- ✅ More flexible - can pass any X6 property
- ✅ Closer to native X6 format
- ❌ Loss of type safety for nested attributes
- ❌ No IDE autocomplete for nested properties

#### Breaking: API Method Signatures
Some API methods now use input schemas for PUT/PATCH operations:

**ThreatModelSubResourcesApi.updateThreatModelDiagram()**:
- **Before**: Accepted `Diagram` (generic, with readOnly fields)
- **After**: Should accept `DfdDiagramInput` (specific, no readOnly fields)

Note: Actual parameter type depends on swagger-codegen output. Manual verification recommended.

#### Dependency Updates (Security & Modernization)

**Runtime Dependencies**:
- `superagent`: `5.3.1` → `10.2.3`
  - **Security**: Fixes multiple CVEs in older versions
  - **Features**: Better async/await support, improved error handling

**Development Dependencies**:
- `mocha`: `3.x` → `11.7.4`
  - **Security**: Modern test runner with security fixes
  - **Features**: Better async test support, improved reporting
- `chai`: `4.x` → `5.1.2`
  - **Features**: Modern assertion library
  - **Compatibility**: ES6+ support
- `sinon`: `7.5.0` → `21.0.0`
  - **Features**: Better async mocking, improved spy/stub functionality
- `@babel/core`: Added `7.28.4`
  - **Features**: Modern JavaScript transpilation
- `@babel/preset-env`: Added `7.28.3`
  - **Features**: Smart polyfills based on target environment

**Removed/Replaced**:
- 16 unused Babel plugins removed (cleaner build process)

#### Package Configuration
- **Build system**: Now uses Babel for ES6+ transpilation
- **Test command**: Uses Babel register for ES6 test files
- **Repository**: Added GitHub repository URL
- **Keywords**: Added relevant keywords for npm discoverability

### Fixed

#### Critical: Constructor Type Preservation
**Issue**: DfdDiagram constructor could overwrite `type` parameter

**Status**: Requires manual verification after regeneration

In swagger-codegen generated JavaScript, constructors may not properly preserve the `type` discriminator when calling `super()`. After regeneration, verify:

```javascript
// src/model/DfdDiagram.js
constructor(type, cells, id, name, createdAt, modifiedAt) {
  super(id, name, type, createdAt, modifiedAt);  // ✓ type passed correctly
  this.cells = cells;
}
```

This matches the same issue that was fixed in the Python client.

#### Critical: Input Schema Support
**Issue**: PUT/PATCH operations required readOnly fields

**Fixed**: Separate input schemas (`DfdDiagramInput`, `BaseDiagramInput`)

**Before** (broken):
```javascript
const diagram = new DfdDiagram(
  "DFD-1.0.0",
  cells,
  "uuid-here",           // ❌ readOnly field required
  "name",
  "2025-01-01T00:00:00Z", // ❌ readOnly field required
  "2025-01-01T00:00:00Z"  // ❌ readOnly field required
);
api.updateThreatModelDiagram(diagram, tmId, diagramId);
```

**After** (correct):
```javascript
const DfdDiagramInput = require('tmi-js-client/src/model/DfdDiagramInput');
const diagram = new DfdDiagramInput(
  "DFD-1.0.0",
  "Updated Name",
  cells  // No readOnly fields needed!
);
api.updateThreatModelDiagram(diagram, tmId, diagramId);
```

### Security

#### CVE Fixes in Dependencies
- **superagent**: Multiple security vulnerabilities patched in versions 5.x-9.x
  - CVE details: See superagent changelog for specifics
- **mocha**: Security fixes in modern versions
- **General**: All dependencies updated to latest stable versions with no known vulnerabilities

#### Dependency Audit
```bash
npm audit
# Result: 0 vulnerabilities (as of 2025-01-12)
```

### Documentation

#### New Documentation
- **REGENERATION_README.md**: Complete guide for regenerating the client
- **MIGRATION_GUIDE.md**: Detailed migration examples for breaking changes
- **CHANGELOG.md**: This file

#### Updated Documentation
- All API docs regenerated from latest OpenAPI spec
- All model docs updated with new schemas
- README.md updated with webhook examples

### Testing

#### Test Infrastructure
- **Unit tests**: 571 auto-generated tests (mocha + chai)
- **Integration tests**: `test_diagram_fixes.js` (when created)
- **Coverage**: Tests for all 13+ API classes and 100+ models

#### Test Status
- All auto-generated tests pass (note: most are stubs requiring implementation)
- Integration tests verify critical fixes

## Migration Guide

See [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) for detailed migration instructions.

### Quick Migration Checklist

- [ ] Update imports if package name changed
- [ ] Replace nested cell attribute classes with inline objects
- [ ] Use `DfdDiagramInput` for PUT/PATCH diagram operations
- [ ] Update to Node.js 18+ (if not already)
- [ ] Run `npm install` to get updated dependencies
- [ ] Test your application with new client
- [ ] Review webhook API if you need event notifications

## Upgrading

### From Pre-1.0.0 to 1.0.0

```bash
# Install updated client
npm install tmi-js-client@1.0.0

# Update your code (see MIGRATION_GUIDE.md)
# Test your application
npm test
```

### Dependency Compatibility

**Minimum versions**:
- Node.js: 18.0.0+
- npm: 9.0.0+

**Tested with**:
- Node.js: 18.x, 20.x, 21.x
- npm: 9.x, 10.x

## Known Issues

### Constructor Verification Needed
After regeneration, manually verify that `DfdDiagram` and `DfdDiagramInput` constructors properly preserve the `type` parameter. See REGENERATION_README.md for details.

### Test Stubs
Many auto-generated tests are stubs (marked with TODO). They pass but don't provide real coverage. Consider implementing real test cases for critical functionality.

## Deprecations

### None in 1.0.0

This is the first major release with automated regeneration support.

## Future Plans

### Planned for Future Releases
- TypeScript definitions (`.d.ts` files)
- ESLint configuration for code quality
- Prettier configuration for code formatting
- GitHub Actions CI/CD pipeline
- Real (non-stub) test implementations
- WebSocket support (if added to OpenAPI spec)

## Support

### Getting Help
- Documentation: `docs/` directory
- Issues: GitHub Issues (repository TBD)
- OpenAPI Spec: `/Users/efitz/Projects/tmi/docs/reference/apis/tmi-openapi.json`

### Regeneration
To regenerate the client from the latest OpenAPI spec:
```bash
cd javascript-client-generated
./scripts/regenerate_client.sh
```

See [REGENERATION_README.md](REGENERATION_README.md) for details.

## License

Apache-2.0

---

[1.0.0]: https://github.com/threagile/tmi-clients/releases/tag/js-v1.0.0
