
# TokenRefreshRequest

OAuth 2.0 refresh token request

## Properties

Name | Type
------------ | -------------
`refresh_token` | string

## Example

```typescript
import type { TokenRefreshRequest } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "refresh_token": 8xLOxBtZp8_example_refresh_token,
} satisfies TokenRefreshRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as TokenRefreshRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


