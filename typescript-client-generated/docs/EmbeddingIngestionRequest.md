
# EmbeddingIngestionRequest


## Properties

Name | Type
------------ | -------------
`index_type` | string
`embeddings` | [Array&lt;EmbeddingIngestionItem&gt;](EmbeddingIngestionItem.md)

## Example

```typescript
import type { EmbeddingIngestionRequest } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "index_type": null,
  "embeddings": null,
} satisfies EmbeddingIngestionRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as EmbeddingIngestionRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


