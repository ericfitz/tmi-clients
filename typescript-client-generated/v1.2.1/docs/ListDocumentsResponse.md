
# ListDocumentsResponse

Paginated list of documents

## Properties

Name | Type
------------ | -------------
`documents` | [Array&lt;Document&gt;](Document.md)
`total` | number
`limit` | number
`offset` | number

## Example

```typescript
import type { ListDocumentsResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "documents": [{"id":"567e89ab-e89b-41d4-a716-446655440004","threat_model_id":"123e4567-e89b-41d4-a716-446655440000","name":"Security Architecture Review","description":"Q1 2024 security review findings","uri":"https://example.com/docs/security-policy.pdf","format":"markdown","created_at":"2024-01-17T14:00:00Z","modified_at":"2024-01-17T14:00:00Z"}],
  "total": 8,
  "limit": 20,
  "offset": 0,
} satisfies ListDocumentsResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListDocumentsResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


