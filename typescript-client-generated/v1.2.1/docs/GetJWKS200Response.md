
# GetJWKS200Response


## Properties

Name | Type
------------ | -------------
`keys` | [Array&lt;GetJWKS200ResponseKeysInner&gt;](GetJWKS200ResponseKeysInner.md)

## Example

```typescript
import type { GetJWKS200Response } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "keys": [{"kty":"RSA","use":"sig","kid":"tmi-key-1","alg":"RS256"}],
} satisfies GetJWKS200Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GetJWKS200Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


