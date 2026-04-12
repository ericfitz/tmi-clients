
# GetJWKS200ResponseKeysInner


## Properties

Name | Type
------------ | -------------
`kty` | string
`use` | string
`alg` | string
`kid` | string

## Example

```typescript
import type { GetJWKS200ResponseKeysInner } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "kty": oct,
  "use": sig,
  "alg": HS256,
  "kid": tmi-signing-key,
} satisfies GetJWKS200ResponseKeysInner

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GetJWKS200ResponseKeysInner
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


