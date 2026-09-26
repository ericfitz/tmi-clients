
# CreateDiagramCollaborationSession409Response


## Properties

Name | Type
------------ | -------------
`error` | string
`join_url` | string

## Example

```typescript
import type { CreateDiagramCollaborationSession409Response } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "error": collaboration_session_exists,
  "join_url": http://localhost:8080/threat_models/{threat_model_id}/diagrams/{diagram_id}/collaborate,
} satisfies CreateDiagramCollaborationSession409Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CreateDiagramCollaborationSession409Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


