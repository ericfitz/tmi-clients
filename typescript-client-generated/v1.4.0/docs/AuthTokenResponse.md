
# AuthTokenResponse

JWT token response for authentication endpoints

## Properties

Name | Type
------------ | -------------
`access_token` | string
`refresh_token` | string
`token_type` | string
`expires_in` | number

## Example

```typescript
import type { AuthTokenResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "access_token": null,
  "refresh_token": null,
  "token_type": null,
  "expires_in": null,
} satisfies AuthTokenResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as AuthTokenResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


