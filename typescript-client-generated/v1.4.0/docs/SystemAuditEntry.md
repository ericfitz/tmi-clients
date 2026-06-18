
# SystemAuditEntry

An immutable system-level audit record of a successful /admin/_* write (T7 evidence). Old/new values are redacted at write time.

## Properties

Name | Type
------------ | -------------
`id` | string
`actor` | [AuditActor](AuditActor.md)
`http_method` | string
`http_path` | string
`field_path` | string
`old_value_redacted` | string
`new_value_redacted` | string
`change_summary` | string
`created_at` | Date

## Example

```typescript
import type { SystemAuditEntry } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "actor": null,
  "http_method": null,
  "http_path": null,
  "field_path": null,
  "old_value_redacted": null,
  "new_value_redacted": null,
  "change_summary": null,
  "created_at": null,
} satisfies SystemAuditEntry

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SystemAuditEntry
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


