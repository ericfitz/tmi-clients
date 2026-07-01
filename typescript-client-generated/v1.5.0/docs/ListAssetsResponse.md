
# ListAssetsResponse

Paginated list of assets

## Properties

Name | Type
------------ | -------------
`assets` | [Array&lt;Asset&gt;](Asset.md)
`total` | number
`limit` | number
`offset` | number

## Example

```typescript
import type { ListAssetsResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "assets": [{"id":"b50e8400-e29b-41d4-a716-446655440001","name":"Payment Database","type":"data","description":"PostgreSQL database storing customer payment information","criticality":"high","created_at":"2024-01-15T10:30:00Z","modified_at":"2024-01-20T15:45:30Z"}],
  "total": 10,
  "limit": 20,
  "offset": 0,
} satisfies ListAssetsResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListAssetsResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


