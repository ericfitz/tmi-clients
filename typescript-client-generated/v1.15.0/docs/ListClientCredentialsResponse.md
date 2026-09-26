
# ListClientCredentialsResponse

Paginated list of client credentials

## Properties

Name | Type
------------ | -------------
`credentials` | [Array&lt;ClientCredentialInfo&gt;](ClientCredentialInfo.md)
`total` | number
`limit` | number
`offset` | number

## Example

```typescript
import type { ListClientCredentialsResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "credentials": [{"id":"970eabcd-e89b-41d4-a716-446655440016","owner_id":"550e8400-e29b-41d4-a716-446655440000","name":"Monitoring Service","description":"Metrics collection service","client_id":"tmi_cc_monitoring123","is_active":true,"created_at":"2024-01-15T10:00:00Z","modified_at":"2024-01-15T10:00:00Z"}],
  "total": 4,
  "limit": 20,
  "offset": 0,
} satisfies ListClientCredentialsResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListClientCredentialsResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


