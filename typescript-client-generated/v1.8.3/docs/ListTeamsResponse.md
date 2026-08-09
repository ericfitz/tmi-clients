
# ListTeamsResponse

Paginated list of teams

## Properties

Name | Type
------------ | -------------
`teams` | [Array&lt;TeamListItem&gt;](TeamListItem.md)
`total` | number
`limit` | number
`offset` | number

## Example

```typescript
import type { ListTeamsResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "teams": [{"id":"550e8400-e29b-41d4-a716-446655440000","name":"Platform Engineering","description":"Core platform infrastructure team","status":"active","created_at":"2025-01-15T10:30:00Z","modified_at":"2025-06-20T14:22:00Z"}],
  "total": 1,
  "limit": 20,
  "offset": 0,
} satisfies ListTeamsResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListTeamsResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


