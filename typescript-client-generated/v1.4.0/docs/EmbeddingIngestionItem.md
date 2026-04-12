
# EmbeddingIngestionItem


## Properties

Name | Type
------------ | -------------
`entity_type` | string
`entity_id` | string
`chunk_index` | number
`chunk_text` | string
`content_hash` | string
`embedding_model` | string
`embedding_dim` | number
`vector` | Array&lt;number&gt;

## Example

```typescript
import type { EmbeddingIngestionItem } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "entity_type": null,
  "entity_id": null,
  "chunk_index": null,
  "chunk_text": null,
  "content_hash": null,
  "embedding_model": null,
  "embedding_dim": null,
  "vector": null,
} satisfies EmbeddingIngestionItem

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as EmbeddingIngestionItem
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


