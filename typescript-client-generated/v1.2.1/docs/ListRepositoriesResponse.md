
# ListRepositoriesResponse

Paginated list of repositories

## Properties

Name | Type
------------ | -------------
`repositories` | [Array&lt;Repository&gt;](Repository.md)
`total` | number
`limit` | number
`offset` | number

## Example

```typescript
import type { ListRepositoriesResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "repositories": [{"id":"789eabcd-e89b-41d4-a716-446655440006","threat_model_id":"123e4567-e89b-41d4-a716-446655440000","name":"payment-service","description":"Main payment processing microservice","url":"https://github.com/example/payment-service","repo_type":"github","uri":"https://github.com/example/repo","created_at":"2024-01-15T10:00:00Z","modified_at":"2024-01-15T10:00:00Z"}],
  "total": 3,
  "limit": 20,
  "offset": 0,
} satisfies ListRepositoriesResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListRepositoriesResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


