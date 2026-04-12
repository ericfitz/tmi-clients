
# EmbeddingConfig


## Properties

Name | Type
------------ | -------------
`text_embedding` | [EmbeddingProviderConfig](EmbeddingProviderConfig.md)
`code_embedding` | [EmbeddingProviderConfig](EmbeddingProviderConfig.md)

## Example

```typescript
import type { EmbeddingConfig } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "text_embedding": null,
  "code_embedding": null,
} satisfies EmbeddingConfig

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as EmbeddingConfig
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


