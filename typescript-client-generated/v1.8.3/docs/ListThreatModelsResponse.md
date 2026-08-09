
# ListThreatModelsResponse

Paginated list of threat models

## Properties

Name | Type
------------ | -------------
`threat_models` | [Array&lt;TMListItem&gt;](TMListItem.md)
`total` | number
`limit` | number
`offset` | number

## Example

```typescript
import type { ListThreatModelsResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "threat_models": [{"id":"660e8400-e29b-41d4-a716-446655440001","name":"Payment Gateway Threat Model","owner":{"principal_type":"user","provider":"github","provider_id":"alice@example.com","display_name":"Alice Johnson","email":"alice@example.com"},"created_by":{"principal_type":"user","provider":"github","provider_id":"alice@example.com","display_name":"Alice Johnson","email":"alice@example.com"},"threat_model_framework":"STRIDE","created_at":"2024-01-15T10:30:00Z","modified_at":"2024-01-20T15:45:30Z","document_count":3,"repo_count":2,"diagram_count":1,"threat_count":5,"asset_count":4,"note_count":2}],
  "total": 42,
  "limit": 20,
  "offset": 0,
} satisfies ListThreatModelsResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListThreatModelsResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


