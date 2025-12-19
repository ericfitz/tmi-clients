# Changelog

All notable changes to the TMI Go client will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-12

### Added

#### Webhook API Support (8 new endpoints)
- **List webhook subscriptions**: `GET /webhooks/subscriptions`
  - Returns all webhook subscriptions for the authenticated user
  - Method: `GeneralApiService.ListWebhookSubscriptions(ctx)`
- **Create webhook subscription**: `POST /webhooks/subscriptions`
  - Subscribe to threat model events (created, updated, deleted)
  - Method: `GeneralApiService.CreateWebhookSubscription(ctx, body)`
- **Get webhook subscription**: `GET /webhooks/subscriptions/{webhook_id}`
  - Retrieve details of a specific webhook subscription
  - Method: `GeneralApiService.GetWebhookSubscription(ctx, webhookId)`
- **Update webhook subscription**: `PUT /webhooks/subscriptions/{webhook_id}`
  - Update an existing webhook subscription
  - Method: `GeneralApiService.UpdateWebhookSubscription(ctx, body, webhookId)`
- **Delete webhook subscription**: `DELETE /webhooks/subscriptions/{webhook_id}`
  - Unsubscribe from webhook events
  - Method: `GeneralApiService.DeleteWebhookSubscription(ctx, webhookId)`
- **Test webhook**: `POST /webhooks/subscriptions/{webhook_id}/test`
  - Send a test payload to verify webhook endpoint
  - Method: `GeneralApiService.TestWebhook(ctx, body, webhookId)`
- **List webhook deliveries**: `GET /webhooks/deliveries`
  - List all webhook delivery attempts
  - Method: `GeneralApiService.ListWebhookDeliveries(ctx)`
- **Get webhook delivery**: `GET /webhooks/deliveries/{delivery_id}`
  - Get details of a specific delivery attempt
  - Method: `GeneralApiService.GetWebhookDelivery(ctx, deliveryId)`

#### New Webhook Models
- `WebhookSubscription` - Webhook subscription details (output schema with readOnly fields)
  - Fields: ID, URL, Events, Secret, Active, CreatedAt, ModifiedAt
- `WebhookSubscriptionInput` - Webhook subscription creation/update (input schema)
  - Fields: URL, Events, Secret, Active
- `WebhookDelivery` - Webhook delivery attempt details
  - Fields: ID, WebhookID, Event, Payload, Response, StatusCode, Timestamp
- `WebhookTestRequest` - Test webhook request payload
  - Fields: EventType
- `WebhookTestResponse` - Test webhook response
  - Fields: Success, StatusCode, Response, ErrorMessage

#### New Diagram Input Schemas
- `BaseDiagramInput` - Base class for diagram input (no readOnly fields)
  - Fields: Type, Name, Description
- `DfdDiagramInput` - DFD diagram input for PUT/PATCH operations
  - Fields: Type, Name, Description, Cells (no ID, CreatedAt, ModifiedAt)

These separate input schemas solve the critical issue where PUT/PATCH operations required readOnly fields (ID, CreatedAt, ModifiedAt), which should never be in request bodies.

#### Regeneration Infrastructure
- **Automated regeneration script**: `scripts/regenerate_client.sh`
  - One-command regeneration from OpenAPI spec
  - Automatic dependency updates via go mod tidy
  - Build verification
  - Test execution and reporting
- **Configuration file**: `scripts/swagger-codegen-config.json`
  - Codegen settings for consistent generation
- **Developer documentation**: `docs/developer/`
  - REGENERATION_README.md - Complete regeneration guide
  - MIGRATION_GUIDE.md - Breaking changes and migration examples
  - CHANGELOG.md - This file

### Changed

#### Breaking: API Method Signatures
Some API methods now accept input schemas for PUT/PATCH operations:

**ThreatModelSubResourcesApi.UpdateThreatModelDiagram()**:
- **Before**: Accepted `Diagram` (with readOnly fields)
- **After**: Should accept `DfdDiagramInput` (no readOnly fields)

**Example migration**:
```go
// Before (broken - includes readOnly fields)
diagram := tmiclient.Diagram{
    DfdDiagram: &tmiclient.DfdDiagram{
        Type:       stringPtr("DFD-1.0.0"),
        Name:       stringPtr("Updated"),
        Cells:      cells,
        Id:         stringPtr("uuid"),      // ❌ readOnly
        CreatedAt:  stringPtr("2025..."),   // ❌ readOnly
        ModifiedAt: stringPtr("2025..."),   // ❌ readOnly
    },
}

// After (correct - no readOnly fields)
input := tmiclient.DfdDiagramInput{
    Type:  stringPtr("DFD-1.0.0"),
    Name:  stringPtr("Updated"),
    Cells: cells,
}
```

#### Dependency Updates

**Runtime Dependencies**:
- `golang.org/x/oauth2`: Updated to `v0.32.0`
  - **Security**: Latest OAuth2 implementation with security fixes
  - **Features**: Improved token refresh, better error handling
- `github.com/antihax/optional`: `v1.0.0`
  - **Stability**: Stable release for optional parameters

#### Module Configuration
- **Module path**: `github.com/efitz/tmi-clients/go-client-generated`
- **Go version**: `1.21+` (LTS support, modern features)
- **Build system**: go.mod with automatic dependency management

### Fixed

#### Critical: Input Schema Support
**Issue**: PUT/PATCH operations required readOnly fields

**Fixed**: Separate input schemas (`DfdDiagramInput`, `BaseDiagramInput`)

**Before** (broken):
```go
// UpdateThreatModelDiagram required all fields including readOnly
diagram := tmiclient.Diagram{
    DfdDiagram: &tmiclient.DfdDiagram{
        Id:         stringPtr("uuid"),    // ❌ readOnly but required
        CreatedAt:  stringPtr("2025..."), // ❌ readOnly but required
        ModifiedAt: stringPtr("2025..."), // ❌ readOnly but required
        Type:       stringPtr("DFD-1.0.0"),
        Name:       stringPtr("name"),
        Cells:      cells,
    },
}
api.UpdateThreatModelDiagram(ctx, diagram, tmId, diagramId)
```

**After** (correct):
```go
// Use DfdDiagramInput for updates - no readOnly fields
input := tmiclient.DfdDiagramInput{
    Type:  stringPtr("DFD-1.0.0"),
    Name:  stringPtr("Updated Name"),
    Cells: cells,
}
result, resp, err := api.UpdateThreatModelDiagram(ctx, input, tmId, diagramId)
// Result is DfdDiagram with server-populated readOnly fields
```

### Security

#### Dependency Security
- **golang.org/x/oauth2**: Updated to v0.32.0 with latest security patches
- **No known CVEs**: All dependencies are current and vulnerability-free

#### Dependency Audit
```bash
# Check for vulnerabilities
go list -m -json all | go-mod-audit

# Or use govulncheck
govulncheck ./...
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
- **Integration tests**: `diagram_fixes_test.go` (when created)
- **Build verification**: Automated in regeneration script
- **Dependency validation**: `go mod tidy` ensures clean dependencies

#### Test Status
- Build: ✅ Compiles successfully
- Dependencies: ✅ All resolved
- Integration tests: Create `diagram_fixes_test.go` for validation

## Migration Guide

See [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) for detailed migration instructions.

### Quick Migration Checklist

- [ ] Update to Go 1.21+ (if not already)
- [ ] Run `go get -u && go mod tidy` to update dependencies
- [ ] Replace `Diagram` with `DfdDiagramInput` in PUT/PATCH calls
- [ ] Remove `Id`, `CreatedAt`, `ModifiedAt` from update requests
- [ ] Verify GET operations still use `DfdDiagram` (output schema)
- [ ] Review webhook API if you need event notifications

## Upgrading

### From Pre-1.0.0 to 1.0.0

```bash
# Update module
go get github.com/efitz/tmi-clients/go-client-generated@v1.0.0

# Tidy dependencies
go mod tidy

# Update your code (see MIGRATION_GUIDE.md)
# Test your application
go test ./...
```

### Dependency Compatibility

**Minimum versions**:
- Go: 1.21.0+
- golang.org/x/oauth2: v0.32.0+
- github.com/antihax/optional: v1.0.0

**Tested with**:
- Go: 1.21, 1.22, 1.23
- oauth2: v0.32.0

## Known Issues

### Input Schema Generation
After regeneration, verify that `model_dfd_diagram_input.go` and `model_base_diagram_input.go` exist. If swagger-codegen doesn't generate these, they may need to be created manually based on the output schemas.

### Nested Cell Classes
The Go client may retain nested cell attribute classes (EdgeAttrsLine, NodeAttrsBody, etc.) for type safety, unlike Python/JavaScript clients that use inline objects. This is intentional and provides better compile-time checking.

## Deprecations

### None in 1.0.0

This is the first major release with automated regeneration support.

## Future Plans

### Planned for Future Releases
- Context-aware examples in documentation
- gRPC client support (if TMI adds gRPC)
- OpenTelemetry instrumentation
- Retry middleware with exponential backoff
- Mock generation for testing
- CLI tool for common operations

## Support

### Getting Help
- Documentation: `docs/` directory
- Issues: GitHub Issues (repository TBD)
- OpenAPI Spec: `/Users/efitz/Projects/tmi/docs/reference/apis/tmi-openapi.json`

### Regeneration
To regenerate the client from the latest OpenAPI spec:
```bash
cd go-client-generated
./scripts/regenerate_client.sh
```

See [REGENERATION_README.md](REGENERATION_README.md) for details.

## License

Apache-2.0

---

[1.0.0]: https://github.com/efitz/tmi-clients/releases/tag/go-v1.0.0
