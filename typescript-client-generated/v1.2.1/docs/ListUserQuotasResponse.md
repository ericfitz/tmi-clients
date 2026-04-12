
# ListUserQuotasResponse

Paginated list of user API quotas

## Properties

Name | Type
------------ | -------------
`quotas` | [Array&lt;UserAPIQuota&gt;](UserAPIQuota.md)
`total` | number
`limit` | number
`offset` | number

## Example

```typescript
import type { ListUserQuotasResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "quotas": [{"user_id":"550e8400-e29b-41d4-a716-446655440000","max_requests_per_minute":60,"created_at":"2024-01-01T00:00:00Z","modified_at":"2024-01-01T00:00:00Z"}],
  "total": 25,
  "limit": 20,
  "offset": 0,
} satisfies ListUserQuotasResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListUserQuotasResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


