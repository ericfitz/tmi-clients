
# ListAuditTrailResponse

Paginated list of audit trail entries

## Properties

Name | Type
------------ | -------------
`audit_entries` | [Array&lt;AuditEntry&gt;](AuditEntry.md)
`total` | number
`limit` | number
`offset` | number

## Example

```typescript
import type { ListAuditTrailResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "audit_entries": [{"id":"a1b2c3d4-e5f6-7890-abcd-ef1234567890","threat_model_id":"f0e1d2c3-b4a5-6789-0abc-def123456789","object_type":"threat_model","object_id":"f0e1d2c3-b4a5-6789-0abc-def123456789","version":3,"change_type":"updated","actor":{"email":"alice@example.com","provider":"google","provider_id":"google-12345","display_name":"Alice"},"change_summary":"Updated threat model description","created_at":"2026-01-15T10:30:00Z"}],
  "total": null,
  "limit": null,
  "offset": null,
} satisfies ListAuditTrailResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListAuditTrailResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


