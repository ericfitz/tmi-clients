# TMI Go Client Regeneration Report

**Date**: 2026-02-28 23:14:20
**OpenAPI Spec**: /Users/efitz/Projects/tmi-clients/go-client-generated/tmi-openapi.json
**Swagger Codegen**: 3.0.78
**Go Version**: go version go1.26.0 darwin/arm64

## Configuration

- **Package Name**: tmiclient
- **Module Path**: github.com/efitz/tmi-clients/go-client-generated
- **Go Version**: 1.21+
- **Config File**: scripts/swagger-codegen-config.json

## Generation Results

### Files Generated

```
     231 model files
      24 API files
     252 documentation files
```

### Dependencies

```
  require (
  	github.com/antihax/optional v1.0.0
  	golang.org/x/oauth2 v0.35.0
  )
```

### Dependency Status

```
github.com/efitz/tmi-clients/go-client-generated
cloud.google.com/go/compute/metadata v0.3.0
github.com/antihax/optional v1.0.0
golang.org/x/oauth2 v0.35.0
```

## Build Results

### Compilation

Exit Code: 0
Status: ✅ SUCCESS

See `build_output.log` for full details.

### Tests

Exit Code: 0
Status: ✅ PASSED

No tests found.

### Integration Tests

Status: ⚠️ NOT FOUND



## Critical Changes in This Regeneration

### New Features

- **Webhook API**: 8 new endpoints for webhook subscriptions and deliveries
- **Input Schemas**: Separate input/output schemas (DfdDiagramInput vs DfdDiagram)
- **Webhook Models**: WebhookSubscription, WebhookDelivery, etc.

### Breaking Changes

1. **Input Schemas**: PUT/PATCH operations may use *Input types
   - Use DfdDiagramInput for updates (not DfdDiagram)
   - Removes need to provide readOnly fields (id, created_at, modified_at)

2. **API Method Signatures**: Some methods may accept different parameter types

### Security Updates

- golang.org/x/oauth2: Latest stable version
- github.com/antihax/optional: v1.0.0

## Models Generated

### Diagram Models

- model_base_diagram.go
- model_base_diagram_image.go
- model_base_diagram_input.go
- model_create_diagram_request.go
- model_dfd_diagram.go
- model_dfd_diagram_input.go
- model_diagram.go
- model_diagram_list_item.go
- model_diagram_list_item_image.go
- model_list_diagrams_response.go
- model_minimal_diagram_model.go

### Webhook Models

- model_webhook_delivery.go
- model_webhook_event_type.go
- model_webhook_quota.go
- model_webhook_quota_update.go
- model_webhook_subscription.go
- model_webhook_subscription_input.go
- model_webhook_test_request.go
- model_webhook_test_response.go

### Cell Models

- model_cell.go
- model_cell_data.go
- model_edge.go
- model_edge_attrs.go
- model_edge_attrs_line.go
- model_edge_attrs_line_source_marker.go
- model_edge_attrs_line_target_marker.go
- model_edge_connector.go
- model_edge_label.go
- model_edge_label_attrs.go
- model_edge_label_attrs_text.go
- model_edge_router.go
- model_edge_terminal.go
- model_node.go
- model_node_attrs.go
- model_node_attrs_body.go
- model_node_attrs_text.go
- model_node_position.go
- model_node_size.go

## API Services Generated

```
addons
administration
assets
authentication
collaboration
configuration
documents
general
notes
o_auth_discovery
oidc_discovery
projects
repositories
saml
survey_administration
survey_intake
survey_triage
teams
threat_model_sub_resources
threat_models
threats
user_account
users
webhooks
```

## Next Steps

1. ✅ Review build results
2. ✅ Review `REGENERATION_REPORT.md` (this file)
3. ✅ Check `docs/developer/MIGRATION_GUIDE.md` for API changes
4. ⚠️ Verify input schemas exist:
   - model_dfd_diagram_input.go
   - model_base_diagram_input.go
5. ⚠️ Verify webhook models exist:
   - model_webhook_subscription.go
   - model_webhook_delivery.go
6. ✅ Test with your application

## Documentation

- **Usage Guide**: README.md
- **API Reference**: docs/
- **Migration Guide**: docs/developer/MIGRATION_GUIDE.md
- **Regeneration Guide**: docs/developer/REGENERATION_README.md
- **Changelog**: docs/developer/CHANGELOG.md

## Summary

✅ **Regeneration completed successfully**

The Go client has been regenerated from the latest OpenAPI specification.
All dependencies have been updated to current stable versions.

**Build Status**: PASS
**Test Status**: PASS
