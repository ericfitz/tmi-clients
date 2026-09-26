
# ListAdminAuditEntriesResponse

Cursor-paginated cross-threat-model list of audit entries.

## Properties

Name | Type
------------ | -------------
`entries` | [Array&lt;AuditEntry&gt;](AuditEntry.md)
`total` | number
`limit` | number
`next_cursor` | string
`prev_cursor` | string

## Example

```typescript
import type { ListAdminAuditEntriesResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "entries": null,
  "total": null,
  "limit": null,
  "next_cursor": null,
  "prev_cursor": null,
} satisfies ListAdminAuditEntriesResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListAdminAuditEntriesResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


