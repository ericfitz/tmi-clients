
# ListThreatsResponse

Paginated list of threats

## Properties

Name | Type
------------ | -------------
`threats` | [Array&lt;Threat&gt;](Threat.md)
`total` | number
`limit` | number
`offset` | number

## Example

```typescript
import type { ListThreatsResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "threats": [{"id":"345e6789-e89b-41d4-a716-446655440002","threat_model_id":"123e4567-e89b-41d4-a716-446655440000","name":"SQL Injection in Payment Query","description":"Unsanitized input in payment lookup query could allow SQL injection","severity":"High","stride_category":"Tampering","status":"Open","threat_type":["spoofing"],"created_at":"2024-01-16T09:00:00Z","modified_at":"2024-01-16T09:00:00Z"}],
  "total": 15,
  "limit": 20,
  "offset": 0,
} satisfies ListThreatsResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListThreatsResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


