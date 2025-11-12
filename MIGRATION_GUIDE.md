# TMI OpenAPI Client Migration Guide

## Overview

This guide documents changes made to the TMI OpenAPI specification and Python client, including critical bug fixes, new webhook functionality, and cell schema simplification.

**Version**: Regenerated from tmi-openapi.json (2025-11-12)
**Package**: tmi_client v1.0.0 (renamed from swagger_client)

## Summary of Changes

### Major Updates in This Release

1. **✅ All 6 Original Issues Fixed** - Constructor patches, input schemas, type consistency
2. **🆕 Webhook API Support** - 5 new endpoints for webhook subscriptions and deliveries
3. **🔄 Cell Schema Simplification** - Nested cell attributes now use inline objects (BREAKING)
4. **📦 Package Renamed** - `swagger_client` → `tmi_client`
5. **🐍 Python 3.8+ Only** - Dropped Python 2.x support
6. **🔒 Security Updates** - Modern dependency versions with CVE fixes

---

## Breaking Changes

### 1. Package Name Change

The package has been renamed from `swagger_client` to `tmi_client`.

#### Migration Required:
```python
# OLD (pre-1.0.0)
import swagger_client
from swagger_client.models.dfd_diagram import DfdDiagram

# NEW (1.0.0+)
import tmi_client
from tmi_client.models.dfd_diagram import DfdDiagram
```

**Action**: Update all imports throughout your codebase.

### 2. Cell Schema Simplification (BREAKING)

Cell attributes have been simplified from nested classes to inline objects.

#### What Changed:

**Removed Classes** (7 classes):
- `EdgeAttrsLine` - Now inline in `EdgeAttrs`
- `EdgeAttrsLineTargetMarker` - Now inline in `line` object
- `EdgeAttrsLineSourceMarker` - Now inline in `line` object
- `NodeAttrsBody` - Now inline in `NodeAttrs`
- `NodeAttrsText` - Now inline in `NodeAttrs`
- `EdgeLabelAttrs` - Now inline in `EdgeLabel`
- `EdgeLabelAttrsText` - Now inline in label `attrs`

**What This Means**:
- Nested attributes are now dictionaries/objects, not typed classes
- Loss of IDE autocomplete for nested properties
- More flexible (can pass arbitrary X6 properties)
- Closer to X6's native JSON format

#### Migration Examples:

**Before (Nested Classes):**
```python
from tmi_client.models.edge_attrs import EdgeAttrs
from tmi_client.models.edge_attrs_line import EdgeAttrsLine
from tmi_client.models.edge_attrs_line_target_marker import EdgeAttrsLineTargetMarker

# Type-safe nested objects
edge_attrs = EdgeAttrs()
line = EdgeAttrsLine()
line.stroke = "#808080"
line.stroke_width = 2
line.target_marker = EdgeAttrsLineTargetMarker(name="classic", size=8)
edge_attrs.line = line

edge.attrs = edge_attrs
```

**After (Inline Objects):**
```python
# Dictionary/object-based (more flexible, less type-safe)
edge.attrs = {
    "line": {
        "stroke": "#808080",
        "strokeWidth": 2,
        "targetMarker": {
            "name": "classic",
            "size": 8
        }
    }
}
```

**Property Access Changes:**
```python
# OLD - Class attribute access
stroke_color = edge.attrs.line.stroke

# NEW - Dictionary access
stroke_color = edge.attrs.get("line", {}).get("stroke")
# OR if you're confident the structure exists:
stroke_color = edge.attrs["line"]["stroke"]
```

### 3. New Schema: `DfdDiagramInput`

**For PUT/PATCH operations**, use `DfdDiagramInput` instead of `DfdDiagram`.

#### Before (BROKEN):
```python
from tmi_client.models.dfd_diagram import DfdDiagram

# This FAILED because readOnly fields were required
diagram_update = DfdDiagram(
    id="...",  # ❌ readOnly - shouldn't be in input
    created_at="...",  # ❌ readOnly - shouldn't be in input
    modified_at="...",  # ❌ readOnly - shouldn't be in input
    type="DFD-1.0.0",
    name="Updated Name",
    cells=[...]
)
api.update_threat_model_diagram(diagram_update, tm_id, diagram_id)
```

#### After (CORRECT):
```python
from tmi_client.models.dfd_diagram_input import DfdDiagramInput

# This WORKS - no readOnly fields needed
diagram_update = DfdDiagramInput(
    type="DFD-1.0.0",
    name="Updated Name",
    cells=[...]
)
api.update_threat_model_diagram(diagram_update, tm_id, diagram_id)
```

### 4. Python Version Requirement

**Minimum Python version is now 3.8+**. Python 2.x and Python 3.7 are no longer supported.

```python
# pyproject.toml
requires-python = ">=3.8"
```

---

## New Features

### Webhook API Support

Five new webhook endpoints have been added for event subscriptions.

#### New Endpoints:

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/webhooks/subscriptions` | GET | List all webhook subscriptions |
| `/webhooks/subscriptions` | POST | Create a new webhook subscription |
| `/webhooks/subscriptions/{webhook_id}` | GET | Get a specific webhook subscription |
| `/webhooks/subscriptions/{webhook_id}` | PUT | Update a webhook subscription |
| `/webhooks/subscriptions/{webhook_id}` | DELETE | Delete a webhook subscription |
| `/webhooks/subscriptions/{webhook_id}/test` | POST | Test a webhook subscription |
| `/webhooks/deliveries` | GET | List webhook delivery attempts |
| `/webhooks/deliveries/{delivery_id}` | GET | Get a specific delivery attempt |

#### New Schemas:

- `WebhookSubscription` - Webhook subscription (output with readOnly fields)
- `WebhookSubscriptionInput` - Webhook subscription (input without readOnly fields)
- `WebhookDelivery` - Webhook delivery attempt record
- `WebhookTestRequest` - Request to test a webhook
- `WebhookTestResponse` - Response from webhook test

#### Usage Example:

```python
from tmi_client import ApiClient, Configuration
from tmi_client.api.webhooks_api import WebhooksApi
from tmi_client.models.webhook_subscription_input import WebhookSubscriptionInput

# Configure API client
config = Configuration()
config.host = "https://api.example.com"
config.access_token = "your-token"
client = ApiClient(config)
webhooks_api = WebhooksApi(client)

# Create a webhook subscription
webhook_input = WebhookSubscriptionInput(
    name="My Webhook",
    url="https://myapp.com/webhook",
    events=["threat_model.created", "diagram.updated", "threat.created"]
)

subscription = webhooks_api.create_webhook_subscription(webhook_input)
print(f"Created webhook: {subscription.id}")

# List all webhooks
webhooks = webhooks_api.list_webhook_subscriptions()
for webhook in webhooks:
    print(f"{webhook.name}: {webhook.url}")

# Test a webhook
test_request = WebhookTestRequest()
test_response = webhooks_api.test_webhook_subscription(subscription.id, test_request)
print(f"Test status: {test_response.status}")

# View delivery history
deliveries = webhooks_api.list_webhook_deliveries()
for delivery in deliveries:
    print(f"Delivery {delivery.id}: {delivery.status} at {delivery.delivered_at}")
```

#### Available Events:

- `threat_model.created`
- `threat_model.updated`
- `threat_model.deleted`
- `diagram.created`
- `diagram.updated`
- `diagram.deleted`
- `threat.created`
- `threat.updated`
- `threat.deleted`
- `asset.created`
- `asset.updated`
- `asset.deleted`
- `document.created`
- `document.updated`
- `document.deleted`
- `note.created`
- `note.updated`
- `note.deleted`
- `repository.created`
- `repository.updated`
- `repository.deleted`

---

## Dependency Updates

### Security-Critical Updates

```toml
certifi >= 2024.2.2      # was 14.05.14 (critical security fixes)
six >= 1.16.0            # was 1.10
python-dateutil >= 2.9.0 # was 2.5.3
setuptools >= 70.0.0     # was 21.0.0 (RCE vulnerability CVE-2022-40897)
urllib3 >= 2.0.0         # was 1.15.1 (multiple CVEs fixed)
```

### Testing Infrastructure

Migrated from `nose` (deprecated) to `pytest`:

```toml
[project.optional-dependencies]
test = [
    "pytest >= 7.0.0",
    "pytest-cov >= 4.0.0",
    "pytest-randomly >= 3.12.0",
]
```

---

## Migration Steps

### Step 1: Update Package Import

```bash
# Uninstall old package
pip uninstall swagger-client

# Install new package
pip install tmi-client
# OR with uv:
uv pip install tmi-client
```

Update all imports:
```python
# Find and replace throughout codebase:
# swagger_client → tmi_client
```

### Step 2: Update Python Version

Ensure you're running Python 3.8 or later:

```bash
python3 --version  # Should be >= 3.8.0
```

### Step 3: Update Diagram Operations

Replace `DfdDiagram` with `DfdDiagramInput` for PUT requests:

```python
from tmi_client.models.dfd_diagram_input import DfdDiagramInput

diagram_update = DfdDiagramInput(
    type="DFD-1.0.0",
    name="Updated Name",
    cells=[...],
    description="Optional description",
    metadata=[...]
)
updated = api.update_threat_model_diagram(diagram_update, tm_id, diagram_id)
```

### Step 4: Update Cell Attribute Access

Migrate from class-based to dictionary-based cell attributes:

```python
# OLD - Class attributes
from tmi_client.models.edge_attrs_line import EdgeAttrsLine
line = EdgeAttrsLine()
line.stroke = "#333"
edge.attrs.line = line

# NEW - Dictionary/object
edge.attrs = {
    "line": {
        "stroke": "#333",
        "strokeWidth": 2
    }
}

# When reading:
# OLD
stroke = edge.attrs.line.stroke
# NEW
stroke = edge.attrs.get("line", {}).get("stroke", "#000")
```

### Step 5: Add Webhook Support (Optional)

If you want to use webhooks:

```python
from tmi_client.api.webhooks_api import WebhooksApi
from tmi_client.models.webhook_subscription_input import WebhookSubscriptionInput

webhooks_api = WebhooksApi(api_client)
webhook = webhooks_api.create_webhook_subscription(
    WebhookSubscriptionInput(
        name="My Webhook",
        url="https://myapp.com/webhook",
        events=["threat_model.created"]
    )
)
```

### Step 6: Update Testing

If you were using the old test framework:

```bash
# OLD
python setup.py test

# NEW
pytest test/
# OR with uv:
uv run --with pytest python3 -m pytest test/ -v
```

---

## Resolved Issues from Original 6 Fixes

### ✅ Issue 1: DfdDiagram Inheritance Bug (CRITICAL) - FIXED
- **Problem**: Could not instantiate `DfdDiagram` objects - type field was overwritten to `None`
- **Fix**: Applied constructor patch to pass `type` to parent `BaseDiagram.__init__()`
- **Status**: Fixed in both `DfdDiagram` and `DfdDiagramInput`

### ✅ Issue 2: Inconsistent Return Types - FIXED
- **Problem**: API methods returned mix of `dict` and objects
- **Fix**: All endpoints now use specific `DfdDiagram` type (not generic `Diagram`)
- **Status**: Complete - no more `isinstance()` checks needed

### ✅ Issue 3: ReadOnly Fields in Constructors - FIXED
- **Problem**: `BaseDiagram` required `id`, `created_at`, `modified_at` (all readOnly)
- **Fix**: Created separate `DfdDiagramInput` and `BaseDiagramInput` schemas
- **Status**: Complete - UPDATE operations now work correctly

### ✅ Issue 4: Empty Diagram Base Class - DOCUMENTED
- **Problem**: `Diagram` wrapper class had no properties
- **Fix**: Marked as deprecated in OpenAPI spec
- **Status**: Kept for backward compatibility but deprecated

### ✅ Issue 5: DiagramListItem Relationship - DOCUMENTED
- **Problem**: Unclear relationship between list and detail schemas
- **Fix**: Added comprehensive documentation to `DiagramListItem`
- **Status**: Relationship now clearly documented

### ✅ Issue 6: Discriminator Mapping - FIXED
- **Problem**: Missing `x-discriminator-value` annotations
- **Fix**: Added to `DfdDiagram` and `DfdDiagramInput`
- **Status**: Complete

---

## API Method Changes

### Diagram Endpoints

| Endpoint | Method | Request Body | Response Type |
|----------|--------|--------------|---------------|
| `/diagrams` | POST | `CreateDiagramRequest` | `DfdDiagram` ✨ (was `Diagram`) |
| `/diagrams` | GET | - | `list[DiagramListItem]` (no change) |
| `/diagrams/{id}` | GET | - | `DfdDiagram` ✨ (was `Diagram`) |
| `/diagrams/{id}` | PUT | `DfdDiagramInput` ✨ (was `Diagram`) | `DfdDiagram` ✨ (was `Diagram`) |
| `/diagrams/{id}` | PATCH | JSON Patch | `DfdDiagram` ✨ (was `Diagram`) |

### Webhook Endpoints (NEW)

| Endpoint | Method | Request Body | Response Type |
|----------|--------|--------------|---------------|
| `/webhooks/subscriptions` | GET | - | `list[WebhookSubscription]` ⭐ |
| `/webhooks/subscriptions` | POST | `WebhookSubscriptionInput` ⭐ | `WebhookSubscription` ⭐ |
| `/webhooks/subscriptions/{id}` | GET | - | `WebhookSubscription` ⭐ |
| `/webhooks/subscriptions/{id}` | PUT | `WebhookSubscriptionInput` ⭐ | `WebhookSubscription` ⭐ |
| `/webhooks/subscriptions/{id}` | DELETE | - | - ⭐ |
| `/webhooks/subscriptions/{id}/test` | POST | `WebhookTestRequest` ⭐ | `WebhookTestResponse` ⭐ |
| `/webhooks/deliveries` | GET | - | `list[WebhookDelivery]` ⭐ |
| `/webhooks/deliveries/{id}` | GET | - | `WebhookDelivery` ⭐ |

✨ = Changed from previous version
⭐ = New in this version

---

## Common Patterns

### Pattern 1: Create → Update Workflow

```python
from tmi_client.models.create_diagram_request import CreateDiagramRequest
from tmi_client.models.dfd_diagram_input import DfdDiagramInput

# Create
request = CreateDiagramRequest(name="New Diagram", type="DFD-1.0.0")
diagram = api.create_threat_model_diagram(request, tm_id)

# Update (use DfdDiagramInput, not DfdDiagram)
update = DfdDiagramInput(
    type="DFD-1.0.0",
    name="Updated Name",
    cells=diagram.cells  # Reuse existing cells
)
updated_diagram = api.update_threat_model_diagram(update, tm_id, diagram.id)
```

### Pattern 2: Working with Cell Attributes (New Simplified Format)

```python
# Creating a diagram with cells (new dictionary format)
cells = [
    {
        "id": "node1",
        "shape": "process",
        "x": 100,
        "y": 100,
        "width": 120,
        "height": 60,
        "attrs": {
            "body": {"fill": "#E1F5FE", "stroke": "#01579B"},
            "text": {"text": "Process Data", "fontSize": 14}
        }
    },
    {
        "id": "edge1",
        "shape": "edge",
        "source": {"cell": "node1"},
        "target": {"cell": "node2"},
        "attrs": {
            "line": {
                "stroke": "#666",
                "strokeWidth": 2,
                "targetMarker": {"name": "classic", "size": 8}
            }
        }
    }
]

diagram_input = DfdDiagramInput(
    type="DFD-1.0.0",
    name="My Diagram",
    cells=cells
)
```

### Pattern 3: Webhook Event Handling

```python
from tmi_client.models.webhook_subscription_input import WebhookSubscriptionInput

# Create webhook for threat model events
webhook = webhooks_api.create_webhook_subscription(
    WebhookSubscriptionInput(
        name="Threat Model Monitor",
        url="https://myapp.com/webhooks/tmi",
        events=[
            "threat_model.created",
            "threat_model.updated",
            "diagram.updated",
            "threat.created"
        ],
        active=True
    )
)

# Later: check delivery status
deliveries = webhooks_api.list_webhook_deliveries(
    webhook_id=webhook.id,
    limit=10
)

for delivery in deliveries:
    if delivery.status != "success":
        print(f"Failed delivery: {delivery.id} - {delivery.error}")
```

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'swagger_client'"

**Cause**: Package was renamed from `swagger_client` to `tmi_client`.

**Solution**: Update all imports:
```python
# OLD
import swagger_client

# NEW
import tmi_client
```

### Issue: "Invalid value for `type` (None)"

**Cause**: Using old client without the constructor fix.

**Solution**: Ensure you're using the regenerated client (v1.0.0+).

### Issue: "Invalid value for `id`, must not be `None`"

**Cause**: Using `DfdDiagram` instead of `DfdDiagramInput` for PUT requests.

**Solution**: Use `DfdDiagramInput` for all update operations.

```python
# ❌ Wrong
update = DfdDiagram(...)  # Requires readOnly fields

# ✅ Correct
update = DfdDiagramInput(...)  # No readOnly fields
```

### Issue: AttributeError accessing nested cell attributes

**Cause**: Cell attributes are now dictionaries, not typed classes.

**Solution**: Use dictionary access instead of attribute access:

```python
# ❌ OLD (won't work)
stroke = edge.attrs.line.stroke

# ✅ NEW
stroke = edge.attrs.get("line", {}).get("stroke")
# OR with default value:
stroke = edge.attrs.get("line", {}).get("stroke", "#000000")
```

### Issue: Python version too old

**Cause**: Python 3.8+ is required.

**Solution**: Upgrade Python:
```bash
# Check version
python3 --version

# Upgrade Python (macOS with Homebrew)
brew install python@3.11

# Or use pyenv
pyenv install 3.11.0
pyenv global 3.11.0
```

---

## Validation

Run the integration test to verify everything works:

```bash
cd python-client-generated
uv run --with pytest python3 -m pytest test/ -v
uv run --with six --with certifi python3 test_diagram_fixes.py
```

---

## Files Changed

### OpenAPI Specification
- `/Users/efitz/Projects/tmi/docs/reference/apis/tmi-openapi.json`
  - Added webhook endpoints and schemas
  - Simplified cell attribute schemas (inline objects)
  - Added `BaseDiagramInput` schema
  - Added `DfdDiagramInput` schema
  - Updated endpoint request/response types
  - Added `x-discriminator-value` annotations
  - Marked `Diagram` as deprecated

### Python Client
- **Package renamed**: `swagger_client` → `tmi_client`
- **New models**:
  - `base_diagram_input.py`
  - `dfd_diagram_input.py`
  - `webhook_subscription.py`
  - `webhook_subscription_input.py`
  - `webhook_delivery.py`
  - `webhook_test_request.py`
  - `webhook_test_response.py`
- **Patched models**:
  - `dfd_diagram.py` - Constructor fix applied
  - `dfd_diagram_input.py` - Constructor fix applied
- **Deprecated models**:
  - `diagram.py` - Use `DfdDiagram` instead
- **Removed models** (7 nested cell classes):
  - `edge_attrs_line.py`
  - `edge_attrs_line_target_marker.py`
  - `edge_attrs_line_source_marker.py`
  - `node_attrs_body.py`
  - `node_attrs_text.py`
  - `edge_label_attrs.py`
  - `edge_label_attrs_text.py`
- **New API**:
  - `webhooks_api.py`

### Configuration Files
- `pyproject.toml` - Modern Python packaging with uv support
- `requirements.txt` - Updated with secure dependency versions
- `test-requirements.txt` - Migrated to pytest

---

## Support

For issues or questions:
1. Check [OPENAPI_ISSUES_SUMMARY.md](OPENAPI_ISSUES_SUMMARY.md) for detailed technical analysis
2. Run validation tests: `uv run test_diagram_fixes.py`
3. Review [DFD_DIAGRAM_FIX.md](DFD_DIAGRAM_FIX.md) for deep technical details
4. See [CLIENT_IMPROVEMENTS.md](CLIENT_IMPROVEMENTS.md) for future enhancement recommendations
5. Read [CLAUDE.md](CLAUDE.md) for development guidance

---

**Migration Date**: 2025-11-12
**OpenAPI Spec Version**: 1.0.0
**Client Generator**: swagger-codegen 3.0.75
**Package Version**: 1.0.0
**Python Version**: >= 3.8
