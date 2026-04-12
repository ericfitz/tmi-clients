
# RollbackResponse

Result of a rollback operation

## Properties

Name | Type
------------ | -------------
`restored_entity` | object
`audit_entry` | [AuditEntry](AuditEntry.md)

## Example

```typescript
import type { RollbackResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "restored_entity": {"id":"f0e1d2c3-b4a5-6789-0abc-def123456789","name":"Payment Service Threat Model","description":"Threat model for the payment processing service","owner":{"principal_type":"user","provider":"google","provider_id":"alice@example.com","display_name":"Alice Johnson","email":"alice@example.com"},"authorization":[{"principal_type":"user","provider":"google","provider_id":"alice@example.com","display_name":"Alice Johnson","email":"alice@example.com","role":"owner"}],"threat_model_framework":"STRIDE","status":"in_progress","created_at":"2026-01-10T08:00:00Z","modified_at":"2026-01-15T10:30:00Z"},
  "audit_entry": null,
} satisfies RollbackResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as RollbackResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


