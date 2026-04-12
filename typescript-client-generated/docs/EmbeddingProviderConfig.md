
# EmbeddingProviderConfig


## Properties

Name | Type
------------ | -------------
`provider` | string
`model` | string
`api_key` | string
`base_url` | string

## Example

```typescript
import type { EmbeddingProviderConfig } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "provider": openai,
  "model": text-embedding-3-small,
  "api_key": null,
  "base_url": ,
} satisfies EmbeddingProviderConfig

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as EmbeddingProviderConfig
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


