# TMI Go Client Migration Guide

## Overview

This guide documents changes made to the TMI OpenAPI specification and Go client, including input schemas for proper updates, new webhook functionality, and modern dependency updates.

**Version**: Generated from tmi-openapi.json v1.0.0
**Package**: tmiclient v1.0.0
**Module**: github.com/efitz/tmi-clients/go-client-generated
**Language**: Go 1.21+

## Summary of Changes

### Major Updates in This Release

1. **✅ Input Schema Support** - Separate input/output types for PUT/PATCH operations
2. **🆕 Webhook API Support** - 8 new endpoints for webhook subscriptions and deliveries  
3. **⬆️ Go 1.21+ Required** - Modern Go features and security
4. **🔒 Security Updates** - Latest oauth2 v0.32.0 with security fixes

---

## Breaking Changes

### 1. Input Schemas for Diagram Updates

**For PUT/PATCH operations**, use `DfdDiagramInput` instead of `Diagram` or `DfdDiagram`.

#### Why This Matters

The `DfdDiagram` type includes readOnly fields (`Id`, `CreatedAt`, `ModifiedAt`) that are set by the server. These fields should NOT be in request bodies for updates. The new `DfdDiagramInput` type excludes these fields.

#### Before (BROKEN):
```go
// This FAILS because readOnly fields are required
diagram := tmiclient.Diagram{
    DfdDiagram: &tmiclient.DfdDiagram{
        Type:       stringPtr("DFD-1.0.0"),
        Name:       stringPtr("Updated Name"),
        Cells:      updatedCells,
        Id:         stringPtr("existing-uuid"),      // ❌ readOnly
        CreatedAt:  stringPtr("2025-01-01T00:00:00Z"), // ❌ readOnly
        ModifiedAt: stringPtr("2025-01-01T00:00:00Z"), // ❌ readOnly
    },
}

result, resp, err := api.UpdateThreatModelDiagram(ctx, diagram, tmId, diagramId)
```

#### After (CORRECT):
```go
// This WORKS - no readOnly fields needed
input := tmiclient.DfdDiagramInput{
    Type:  stringPtr("DFD-1.0.0"),
    Name:  stringPtr("Updated Name"),
    Cells: updatedCells,
}

result, resp, err := api.UpdateThreatModelDiagram(ctx, input, tmId, diagramId)
// result is DfdDiagram with server-populated readOnly fields
if err != nil {
    return err
}

fmt.Printf("Updated: %s at %s\n", *result.Id, *result.ModifiedAt)
```

### 2. Go Version Requirement

**Minimum Go version is now 1.21+** for modern features and security.

```go
// go.mod
module github.com/efitz/tmi-clients/go-client-generated

go 1.21
```

**Why upgrade?**
- Security fixes in standard library
- Better generics support
- Performance improvements
- Modern tooling compatibility

---

## New Features

### 1. Webhook API

TMI now supports webhooks for real-time event notifications.

#### Available Webhook Events

- `threat_model.created` - New threat model created
- `threat_model.updated` - Threat model updated
- `threat_model.deleted` - Threat model deleted

#### Webhook Models

**New types:**
- `WebhookSubscription` - Subscription details (includes readOnly fields)
- `WebhookSubscriptionInput` - Create/update subscription (no readOnly fields)
- `WebhookDelivery` - Delivery attempt record
- `WebhookTestRequest` - Test webhook payload
- `WebhookTestResponse` - Test result

#### Usage Examples

**List webhook subscriptions:**
```go
import (
    "context"
    tmiclient "github.com/efitz/tmi-clients/go-client-generated"
)

ctx := context.Background()
cfg := tmiclient.NewConfiguration()
cfg.AddDefaultHeader("Authorization", "Bearer "+token)
client := tmiclient.NewAPIClient(cfg)

subscriptions, resp, err := client.GeneralApi.ListWebhookSubscriptions(ctx)
if err != nil {
    return err
}

for _, sub := range subscriptions {
    fmt.Printf("Webhook: %s -> %s\n", *sub.Id, *sub.Url)
}
```

**Create webhook subscription:**
```go
input := tmiclient.WebhookSubscriptionInput{
    Url:    stringPtr("https://your-app.com/webhooks/tmi"),
    Events: []string{"threat_model.created", "threat_model.updated"},
    Secret: stringPtr("your-secret-key"),
    Active: boolPtr(true),
}

subscription, resp, err := client.GeneralApi.CreateWebhookSubscription(ctx, input)
if err != nil {
    return err
}

fmt.Printf("Created webhook: %s\n", *subscription.Id)
```

**Test webhook:**
```go
testReq := tmiclient.WebhookTestRequest{
    EventType: stringPtr("threat_model.created"),
}

testResp, resp, err := client.GeneralApi.TestWebhook(ctx, testReq, webhookId)
if err != nil {
    return err
}

if *testResp.Success {
    fmt.Printf("Test successful! Status: %d\n", *testResp.StatusCode)
} else {
    fmt.Printf("Test failed: %s\n", *testResp.ErrorMessage)
}
```

**Verify webhook signature (in your webhook endpoint):**
```go
import (
    "crypto/hmac"
    "crypto/sha256"
    "encoding/hex"
    "io"
    "net/http"
)

func webhookHandler(w http.ResponseWriter, r *http.Request) {
    signature := r.Header.Get("X-TMI-Signature")
    secret := "your-secret-key"
    
    body, _ := io.ReadAll(r.Body)
    
    if !verifySignature(body, signature, secret) {
        http.Error(w, "Invalid signature", http.StatusUnauthorized)
        return
    }
    
    // Process webhook event
    w.WriteHeader(http.StatusOK)
}

func verifySignature(payload []byte, signature, secret string) bool {
    mac := hmac.New(sha256.New, []byte(secret))
    mac.Write(payload)
    expectedMAC := "sha256=" + hex.EncodeToString(mac.Sum(nil))
    return hmac.Equal([]byte(signature), []byte(expectedMAC))
}
```

### 2. Improved Diagram Operations

#### Creating Diagrams

```go
import (
    "context"
    tmiclient "github.com/efitz/tmi-clients/go-client-generated"
)

ctx := context.Background()
cfg := tmiclient.NewConfiguration()
cfg.AddDefaultHeader("Authorization", "Bearer "+token)
client := tmiclient.NewAPIClient(cfg)

createReq := tmiclient.CreateDiagramRequest{
    Name: stringPtr("My DFD Diagram"),
    Type: stringPtr("DFD-1.0.0"),
}

diagram, resp, err := client.ThreatModelSubResourcesApi.CreateThreatModelDiagram(ctx, createReq, tmId)
if err != nil {
    return err
}

fmt.Printf("Created diagram: %s\n", *diagram.Id)
```

#### Reading Diagrams

```go
// GET returns DfdDiagram (with readOnly fields)
diagram, resp, err := client.ThreatModelSubResourcesApi.GetThreatModelDiagram(ctx, tmId, diagramId)
if err != nil {
    return err
}

fmt.Printf("Diagram: %s\n", *diagram.Name)
fmt.Printf("Created: %s\n", *diagram.CreatedAt)
fmt.Printf("Modified: %s\n", *diagram.ModifiedAt)
fmt.Printf("Cells: %d\n", len(diagram.Cells))
```

#### Updating Diagrams

```go
// ✓ CORRECT - Use DfdDiagramInput for updates
update := tmiclient.DfdDiagramInput{
    Type:  stringPtr("DFD-1.0.0"),
    Name:  stringPtr("Updated Name"),
    Cells: updatedCells,
}

updated, resp, err := client.ThreatModelSubResourcesApi.UpdateThreatModelDiagram(ctx, update, tmId, diagramId)
if err != nil {
    return err
}

// Returns DfdDiagram (with readOnly fields populated by server)
fmt.Printf("Updated: %s at %s\n", *updated.Id, *updated.ModifiedAt)
```

### 3. Working with Cells (AntV X6 Format)

Diagrams use the AntV X6 graph library format for cells.

#### Node Example

```go
import "github.com/google/uuid"

processNode := tmiclient.Node{
    Id:     stringPtr(uuid.New().String()),
    Shape:  stringPtr("process"),
    X:      float64Ptr(100),
    Y:      float64Ptr(100),
    Width:  float64Ptr(120),
    Height: float64Ptr(60),
    Attrs: &tmiclient.NodeAttrs{
        Body: &tmiclient.NodeAttrsBody{
            Fill:        stringPtr("#E1F5FE"),
            Stroke:      stringPtr("#01579B"),
            StrokeWidth: float64Ptr(2),
        },
        Text: &tmiclient.NodeAttrsText{
            Text:     stringPtr("Web Server"),
            Fill:     stringPtr("#000000"),
            FontSize: float64Ptr(14),
        },
    },
}
```

#### Edge Example

```go
dataFlow := tmiclient.Edge{
    Id:    stringPtr(uuid.New().String()),
    Shape: stringPtr("edge"),
    Source: &tmiclient.EdgeTerminal{
        Cell: stringPtr(processNode.Id),
    },
    Target: &tmiclient.EdgeTerminal{
        Cell: stringPtr(databaseNode.Id),
    },
    Attrs: &tmiclient.EdgeAttrs{
        Line: &tmiclient.EdgeAttrsLine{
            Stroke:      stringPtr("#808080"),
            StrokeWidth: float64Ptr(2),
            TargetMarker: &tmiclient.EdgeAttrsLineTargetMarker{
                Name: stringPtr("classic"),
                Size: float64Ptr(8),
            },
        },
    },
}
```

---

## Dependency Updates

### Before (Potentially Outdated):
```go
require (
    github.com/antihax/optional v1.0.0
    golang.org/x/oauth2 v0.0.0-...  // Old version
)
```

### After (Secure):
```go
require (
    github.com/antihax/optional v1.0.0
    golang.org/x/oauth2 v0.32.0      // ✅ Latest
)
```

### Update Instructions

```bash
# Update dependencies
go get -u
go mod tidy

# Verify no vulnerabilities
govulncheck ./...
```

---

## Migration Checklist

### For All Users

- [ ] Update to Go 1.21+ (if not already)
- [ ] Run `go get -u && go mod tidy` to update dependencies
- [ ] Replace `Diagram`/`DfdDiagram` with `DfdDiagramInput` in PUT/PATCH calls
- [ ] Remove `Id`, `CreatedAt`, `ModifiedAt` from update requests
- [ ] Verify GET operations still use `DfdDiagram` (output schema)

### For Webhook Users (New Feature)

- [ ] Review webhook API documentation
- [ ] Create webhook endpoint in your application
- [ ] Implement signature verification for security
- [ ] Subscribe to relevant events
- [ ] Test webhooks with test endpoint

### Optional Enhancements

- [ ] Add integration tests
- [ ] Set up CI/CD for automated testing
- [ ] Configure govulncheck for security scanning

---

## Helper Functions

```go
// Helper functions for pointer conversions
func stringPtr(s string) *string {
    return &s
}

func boolPtr(b bool) *bool {
    return &b
}

func float64Ptr(f float64) *float64 {
    return &f
}

func int32Ptr(i int32) *int32 {
    return &i
}
```

## Support & Resources

### Documentation
- **API Reference**: `docs/` (auto-generated from OpenAPI)
- **Regeneration Guide**: `REGENERATION_README.md`
- **Changelog**: `CHANGELOG.md`

### Regenerating the Client
```bash
cd go-client-generated
./scripts/regenerate_client.sh
```

## License

Apache-2.0 (same as TMI project)
