
# ListDiagramsResponse

Paginated list of diagrams

## Properties

Name | Type
------------ | -------------
`diagrams` | [Array&lt;DiagramListItem&gt;](DiagramListItem.md)
`total` | number
`limit` | number
`offset` | number

## Example

```typescript
import type { ListDiagramsResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "diagrams": [{"id":"880e8400-e29b-41d4-a716-446655440003","name":"Payment Flow Data Flow Diagram","type":"DFD-1.0.0","created_at":"2025-01-15T10:30:00Z","modified_at":"2025-01-15T14:22:00Z"}],
  "total": 5,
  "limit": 20,
  "offset": 0,
} satisfies ListDiagramsResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListDiagramsResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


