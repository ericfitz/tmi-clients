# TMI JavaScript Client Migration Guide

## Overview

This guide documents changes made to the TMI OpenAPI specification and JavaScript client, including critical bug fixes, new webhook functionality, and cell schema simplification.

**Version**: Generated from tmi-openapi.json v1.0.0
**Package**: tmi-js-client v1.0.0
**Language**: JavaScript (ES6)

## Summary of Changes

### Major Updates in This Release

1. **✅ Constructor Bug Awareness** - Manual verification needed for type parameter preservation
2. **🆕 Webhook API Support** - 5 new endpoints for webhook subscriptions and deliveries
3. **🔄 Cell Schema Simplification** - Nested cell attributes now use inline objects (BREAKING)
4. **📦 Input Schemas Added** - Separate schemas for PUT/PATCH operations
5. **⬆️ Node.js 18+ Recommended** - Modern JavaScript features and security
6. **🔒 Security Updates** - Modern dependency versions with CVE fixes

---

## Breaking Changes

### 1. Cell Schema Simplification (BREAKING)

Cell attributes have been simplified from nested classes to inline objects for better AntV X6 compatibility.

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
- Nested attributes are now plain JavaScript objects, not typed classes
- Loss of constructor validation for nested properties
- More flexible (can pass arbitrary X6 properties)
- Closer to X6's native JSON format

#### Migration Examples:

**Before (Nested Classes):**
```javascript
const EdgeAttrs = require('tmi-js-client/src/model/EdgeAttrs');
const EdgeAttrsLine = require('tmi-js-client/src/model/EdgeAttrsLine');
const EdgeAttrsLineTargetMarker = require('tmi-js-client/src/model/EdgeAttrsLineTargetMarker');

// Type-safe nested objects
const edgeAttrs = new EdgeAttrs();
const line = new EdgeAttrsLine();
line.stroke = "#808080";
line.strokeWidth = 2;
line.targetMarker = new EdgeAttrsLineTargetMarker();
line.targetMarker.name = "classic";
line.targetMarker.size = 8;
edgeAttrs.line = line;

edge.attrs = edgeAttrs;
```

**After (Inline Objects):**
```javascript
// Plain object-based (more flexible, less type-safe)
edge.attrs = {
  line: {
    stroke: "#808080",
    strokeWidth: 2,
    targetMarker: {
      name: "classic",
      size: 8
    }
  }
};
```

**Property Access Changes:**
```javascript
// OLD - Class property access
const strokeColor = edge.attrs.line.stroke;

// NEW - Object property access (same syntax, but no type safety)
const strokeColor = edge.attrs.line.stroke;

// SAFE - Defensive access with optional chaining
const strokeColor = edge.attrs?.line?.stroke || "#000000";
```

### 2. New Schema: `DfdDiagramInput`

**For PUT/PATCH operations**, use `DfdDiagramInput` instead of `DfdDiagram`.

#### Why This Matters:

The `DfdDiagram` class includes readOnly fields (`id`, `created_at`, `modified_at`) that are set by the server. These fields should NOT be in request bodies for updates. The new `DfdDiagramInput` class excludes these fields.

#### Before (BROKEN):
```javascript
const DfdDiagram = require('tmi-js-client/src/model/DfdDiagram');
const ThreatModelSubResourcesApi = require('tmi-js-client/src/tmi-client/ThreatModelSubResourcesApi');

const api = new ThreatModelSubResourcesApi();

// This FAILED because readOnly fields were required
const diagramUpdate = new DfdDiagram(
  "DFD-1.0.0",              // type
  updatedCells,             // cells
  "existing-uuid",          // ❌ id (readOnly - shouldn't be in input)
  "Updated Name",           // name
  "2025-01-01T00:00:00Z",  // ❌ created_at (readOnly)
  "2025-01-01T00:00:00Z"   // ❌ modified_at (readOnly)
);

api.updateThreatModelDiagram(diagramUpdate, tmId, diagramId)
  .then(response => console.log(response))
  .catch(error => console.error(error));
```

#### After (CORRECT):
```javascript
const DfdDiagramInput = require('tmi-js-client/src/model/DfdDiagramInput');
const ThreatModelSubResourcesApi = require('tmi-js-client/src/tmi-client/ThreatModelSubResourcesApi');

const api = new ThreatModelSubResourcesApi();

// This WORKS - no readOnly fields needed
const diagramUpdate = new DfdDiagramInput(
  "DFD-1.0.0",       // type
  "Updated Name",    // name
  updatedCells       // cells
  // No id, created_at, modified_at!
);

api.updateThreatModelDiagram(diagramUpdate, tmId, diagramId)
  .then(response => {
    // Response is a DfdDiagram (with readOnly fields)
    console.log('Updated:', response.id, response.modified_at);
  })
  .catch(error => console.error(error));
```

### 3. Node.js Version Requirement

**Recommended Node.js version is now 18+** for modern JavaScript features and security updates.

```javascript
// package.json
{
  "engines": {
    "node": ">=18.0.0"
  }
}
```

**Why upgrade?**
- Native ES6 module support
- Better async/await performance
- Security fixes
- Modern JavaScript features (optional chaining, nullish coalescing, etc.)

---

## New Features

### 1. Webhook API

TMI now supports webhooks for real-time event notifications.

#### Available Webhook Events

- `threat_model.created` - New threat model created
- `threat_model.updated` - Threat model updated
- `threat_model.deleted` - Threat model deleted

#### Webhook Models

**New classes:**
- `WebhookSubscription` - Subscription details (includes readOnly fields)
- `WebhookSubscriptionInput` - Create/update subscription (no readOnly fields)
- `WebhookDelivery` - Delivery attempt record
- `WebhookTestRequest` - Test webhook payload
- `WebhookTestResponse` - Test result

#### Usage Examples

**List webhook subscriptions:**
```javascript
const GeneralApi = require('tmi-js-client/src/tmi-client/GeneralApi');

const api = new GeneralApi();
api.apiClient.authentications['BearerAuth'].accessToken = 'your-token';

api.listWebhookSubscriptions()
  .then(subscriptions => {
    console.log('Subscriptions:', subscriptions);
  })
  .catch(error => console.error(error));
```

**Create webhook subscription:**
```javascript
const WebhookSubscriptionInput = require('tmi-js-client/src/model/WebhookSubscriptionInput');
const GeneralApi = require('tmi-js-client/src/tmi-client/GeneralApi');

const api = new GeneralApi();
api.apiClient.authentications['BearerAuth'].accessToken = 'your-token';

const subscription = new WebhookSubscriptionInput(
  "https://your-app.com/webhooks/tmi",  // url
  ["threat_model.created", "threat_model.updated"],  // events
  "my-secret-key",  // secret (optional, for HMAC verification)
  true  // active
);

api.createWebhookSubscription(subscription)
  .then(created => {
    console.log('Created webhook:', created.id);
  })
  .catch(error => console.error(error));
```

**Test webhook:**
```javascript
const WebhookTestRequest = require('tmi-js-client/src/model/WebhookTestRequest');
const GeneralApi = require('tmi-js-client/src/tmi-client/GeneralApi');

const api = new GeneralApi();
api.apiClient.authentications['BearerAuth'].accessToken = 'your-token';

const testRequest = new WebhookTestRequest(
  "threat_model.created"  // event type
);

api.testWebhook(testRequest, webhookId)
  .then(result => {
    if (result.success) {
      console.log('Webhook test successful:', result.response_code);
    } else {
      console.error('Webhook test failed:', result.error_message);
    }
  })
  .catch(error => console.error(error));
```

**Verify webhook signature (in your webhook endpoint):**
```javascript
const crypto = require('crypto');

function verifyWebhookSignature(payload, signature, secret) {
  const hmac = crypto.createHmac('sha256', secret);
  const digest = 'sha256=' + hmac.update(payload).digest('hex');
  return crypto.timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(digest)
  );
}

// Express.js webhook endpoint example
app.post('/webhooks/tmi', express.raw({type: 'application/json'}), (req, res) => {
  const signature = req.headers['x-tmi-signature'];
  const secret = 'my-secret-key';

  if (!verifyWebhookSignature(req.body, signature, secret)) {
    return res.status(401).send('Invalid signature');
  }

  const event = JSON.parse(req.body);
  console.log('Received event:', event.type, event.data);

  res.status(200).send('OK');
});
```

### 2. Improved Diagram Operations

#### Creating Diagrams

```javascript
const CreateDiagramRequest = require('tmi-js-client/src/model/CreateDiagramRequest');
const ThreatModelSubResourcesApi = require('tmi-js-client/src/tmi-client/ThreatModelSubResourcesApi');

const api = new ThreatModelSubResourcesApi();
api.apiClient.authentications['BearerAuth'].accessToken = 'your-token';

const createRequest = new CreateDiagramRequest(
  "My DFD Diagram",    // name
  "DFD-1.0.0"          // type
);

api.createThreatModelDiagram(createRequest, tmId)
  .then(diagram => {
    console.log('Created diagram:', diagram.id);
    // Returns DfdDiagram with id, created_at, modified_at
  })
  .catch(error => console.error(error));
```

#### Reading Diagrams

```javascript
// GET returns DfdDiagram (with readOnly fields)
api.getThreatModelDiagram(tmId, diagramId)
  .then(diagram => {
    console.log('Diagram:', diagram.id, diagram.name);
    console.log('Created:', diagram.created_at);
    console.log('Modified:', diagram.modified_at);
    console.log('Cells:', diagram.cells.length);
  })
  .catch(error => console.error(error));
```

#### Updating Diagrams

```javascript
const DfdDiagramInput = require('tmi-js-client/src/model/DfdDiagramInput');

// ✓ CORRECT - Use DfdDiagramInput for updates
const update = new DfdDiagramInput(
  "DFD-1.0.0",           // type
  "Updated Name",        // name
  updatedCells           // cells
);

api.updateThreatModelDiagram(update, tmId, diagramId)
  .then(updated => {
    // Returns DfdDiagram (with readOnly fields populated by server)
    console.log('Updated:', updated.id, updated.modified_at);
  })
  .catch(error => console.error(error));
```

### 3. Working with Cells (AntV X6 Format)

Diagrams use the AntV X6 graph library format for cells.

#### Node Example

```javascript
const processNode = {
  id: require('uuid').v4(),
  shape: "process",
  x: 100,
  y: 100,
  width: 120,
  height: 60,
  attrs: {
    body: {
      fill: "#E1F5FE",
      stroke: "#01579B",
      strokeWidth: 2
    },
    text: {
      text: "Web Server",
      fill: "#000000",
      fontSize: 14
    }
  }
};
```

#### Edge Example

```javascript
const dataFlow = {
  id: require('uuid').v4(),
  shape: "edge",
  source: {
    cell: processNode.id
  },
  target: {
    cell: databaseNode.id
  },
  attrs: {
    line: {
      stroke: "#808080",
      strokeWidth: 2,
      targetMarker: {
        name: "classic",
        size: 8
      }
    }
  },
  labels: [
    {
      attrs: {
        text: {
          text: "SQL Query"
        }
      },
      position: 0.5
    }
  ]
};
```

#### Complete Diagram Update

```javascript
const DfdDiagramInput = require('tmi-js-client/src/model/DfdDiagramInput');
const { v4: uuidv4 } = require('uuid');

// Build cells array
const cells = [
  {
    id: uuidv4(),
    shape: "process",
    x: 100, y: 100,
    width: 120, height: 60,
    attrs: {
      body: { fill: "#E1F5FE" },
      text: { text: "Web Server" }
    }
  },
  {
    id: uuidv4(),
    shape: "datastore",
    x: 300, y: 100,
    width: 100, height: 80,
    attrs: {
      body: { fill: "#FFF9C4" },
      text: { text: "Database" }
    }
  }
  // ... more cells
];

const diagramUpdate = new DfdDiagramInput(
  "DFD-1.0.0",
  "System Architecture",
  cells
);

api.updateThreatModelDiagram(diagramUpdate, tmId, diagramId)
  .then(result => console.log('Diagram updated:', result.id))
  .catch(error => console.error(error));
```

---

## Dependency Updates

### Security-Critical Updates

**Before (Vulnerable):**
```json
{
  "dependencies": {
    "superagent": "^5.3.1"  // ❌ Multiple CVEs
  },
  "devDependencies": {
    "mocha": "^3.5.0",      // ❌ Outdated
    "chai": "^4.2.0",       // ⚠️ Old
    "sinon": "^7.5.0"       // ⚠️ Old
  }
}
```

**After (Secure):**
```json
{
  "dependencies": {
    "superagent": "^10.2.3"  // ✅ Latest, CVE-free
  },
  "devDependencies": {
    "@babel/cli": "^7.28.3",
    "@babel/core": "^7.28.4",
    "@babel/preset-env": "^7.28.3",
    "@babel/register": "^7.28.3",
    "mocha": "^11.7.4",      // ✅ Modern
    "chai": "^5.1.2",        // ✅ Modern
    "sinon": "^21.0.0"       // ✅ Modern
  }
}
```

### Update Instructions

```bash
# Remove old dependencies
rm -rf node_modules package-lock.json

# Install updated dependencies
npm install

# Verify no vulnerabilities
npm audit
# Should show: 0 vulnerabilities
```

---

## Migration Checklist

### For All Users

- [ ] Update to Node.js 18+ (recommended)
- [ ] Run `npm install` to update dependencies
- [ ] Update cell attribute code to use inline objects (not nested classes)
- [ ] Search codebase for removed classes and replace:
  - [ ] `EdgeAttrsLine` → inline object
  - [ ] `EdgeAttrsLineTargetMarker` → inline in `line.targetMarker`
  - [ ] `EdgeAttrsLineSourceMarker` → inline in `line.sourceMarker`
  - [ ] `NodeAttrsBody` → inline in `attrs.body`
  - [ ] `NodeAttrsText` → inline in `attrs.text`
  - [ ] `EdgeLabelAttrs` → inline in label
  - [ ] `EdgeLabelAttrsText` → inline in `label.attrs.text`

### For Diagram Users

- [ ] Replace `DfdDiagram` with `DfdDiagramInput` in PUT/PATCH calls
- [ ] Remove `id`, `created_at`, `modified_at` from update requests
- [ ] Verify GET operations still use `DfdDiagram` (output schema)

### For Webhook Users (New Feature)

- [ ] Review webhook API documentation
- [ ] Create webhook endpoint in your application
- [ ] Implement signature verification for security
- [ ] Subscribe to relevant events
- [ ] Test webhooks with test endpoint

### Optional Enhancements

- [ ] Add TypeScript definitions (`.d.ts` files) for type safety
- [ ] Configure ESLint for code quality
- [ ] Add Prettier for code formatting
- [ ] Set up CI/CD for automated testing

---

## Troubleshooting

### Common Migration Issues

#### Issue: Constructor errors with nested attributes

**Error:**
```
TypeError: EdgeAttrsLine is not a constructor
```

**Solution:**
Use inline objects instead:
```javascript
// OLD
const line = new EdgeAttrsLine();

// NEW
const line = { stroke: "#000", strokeWidth: 2 };
```

#### Issue: PUT/PATCH fails with "unknown field" errors

**Error:**
```
400 Bad Request: unknown field 'id' in request body
```

**Solution:**
Use `DfdDiagramInput` instead of `DfdDiagram`:
```javascript
// OLD
const update = new DfdDiagram(...);

// NEW
const DfdDiagramInput = require('tmi-js-client/src/model/DfdDiagramInput');
const update = new DfdDiagramInput(...);
```

#### Issue: npm audit shows vulnerabilities

**Solution:**
```bash
# Update all dependencies
npm update

# Check for remaining issues
npm audit

# Fix automatically if possible
npm audit fix
```

#### Issue: Tests fail after update

**Possible causes:**
1. Breaking changes in cell schema (nested → inline)
2. Wrong schema used for updates (DfdDiagram → DfdDiagramInput)
3. Outdated Node.js version

**Solution:**
1. Review MIGRATION_GUIDE.md (this file)
2. Update code per checklist above
3. Upgrade to Node.js 18+

---

## API Changes Reference

### Diagram Operations

| Operation | Old Schema | New Schema | Notes |
|-----------|------------|------------|-------|
| GET diagram | `DfdDiagram` | `DfdDiagram` | No change (output) |
| POST diagram | `CreateDiagramRequest` | `CreateDiagramRequest` | No change |
| PUT diagram | `Diagram` (generic) | `DfdDiagramInput` | Now specific input schema |
| PATCH diagram | `Diagram` (generic) | `DfdDiagramInput` | Now specific input schema |

### Webhook Operations (New)

| Operation | Method | Endpoint | Schema |
|-----------|--------|----------|--------|
| List subscriptions | GET | `/webhooks/subscriptions` | `[WebhookSubscription]` |
| Create subscription | POST | `/webhooks/subscriptions` | `WebhookSubscriptionInput` |
| Get subscription | GET | `/webhooks/subscriptions/{id}` | `WebhookSubscription` |
| Delete subscription | DELETE | `/webhooks/subscriptions/{id}` | None |
| Test webhook | POST | `/webhooks/subscriptions/{id}/test` | `WebhookTestRequest` |

---

## Support & Resources

### Documentation
- **API Reference**: `../docs/` (auto-generated from OpenAPI)
- **Regeneration Guide**: `REGENERATION_README.md`
- **Changelog**: `CHANGELOG.md`

### Getting Help
1. Check this migration guide
2. Review auto-generated API docs in `docs/`
3. Check OpenAPI spec for authoritative schema definitions
4. File issues on GitHub (repository TBD)

### Regenerating the Client
If you need to regenerate from the latest OpenAPI spec:
```bash
cd javascript-client-generated
./scripts/regenerate_client.sh
```

See `REGENERATION_README.md` for details.

---

## License

Apache-2.0 (same as TMI project)
