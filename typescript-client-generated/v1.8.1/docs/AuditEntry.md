
# AuditEntry

An entry in the audit trail recording a mutation to an entity

## Properties

Name | Type
------------ | -------------
`id` | string
`threat_model_id` | string
`object_type` | string
`object_id` | string
`version` | number
`change_type` | string
`actor` | [AuditActor](AuditActor.md)
`change_summary` | string
`created_at` | Date

## Example

```typescript
import type { AuditEntry } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": a1b2c3d4-e5f6-7890-abcd-ef1234567890,
  "threat_model_id": null,
  "object_type": null,
  "object_id": null,
  "version": null,
  "change_type": null,
  "actor": null,
  "change_summary": null,
  "created_at": null,
} satisfies AuditEntry

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as AuditEntry
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


