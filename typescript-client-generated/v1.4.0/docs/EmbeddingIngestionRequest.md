
# EmbeddingIngestionRequest

Request body for submitting a batch of pre-computed embeddings into a threat model index.

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
  "index_type": text,
  "embeddings": [{"entity_type":"repository","entity_id":"123e4567-e89b-12d3-a456-426614174000","chunk_index":0,"chunk_text":"This is an example chunk of source text.","content_hash":"sha256:abc123def456","embedding_model":"text-embedding-3-small","embedding_dim":3,"vector":[0.1,0.2,0.3]}],
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


