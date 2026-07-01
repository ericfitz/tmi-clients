
# ListProjectsResponse

Paginated list of projects

## Properties

Name | Type
------------ | -------------
`projects` | [Array&lt;ProjectListItem&gt;](ProjectListItem.md)
`total` | number
`limit` | number
`offset` | number

## Example

```typescript
import type { ListProjectsResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "projects": [{"id":"660e8400-e29b-41d4-a716-446655440001","name":"API Gateway Modernization","description":"Migrate legacy API gateway to cloud-native architecture","team_id":"550e8400-e29b-41d4-a716-446655440000","status":"active","created_at":"2025-02-01T09:00:00Z","modified_at":"2025-07-10T16:45:00Z"}],
  "total": 1,
  "limit": 20,
  "offset": 0,
} satisfies ListProjectsResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListProjectsResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


