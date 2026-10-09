
# OAuthError

Error response for OAuth, SAML and discovery routes

## Properties

Name | Type
------------ | -------------
`error` | string
`error_description` | string
`error_uri` | string
`details` | [ErrorDetails](ErrorDetails.md)

## Example

```typescript
import type { OAuthError } from '@tmi-dev/client'

// TODO: Update the object below with actual values
const example = {
  "error": null,
  "error_description": null,
  "error_uri": null,
  "details": null,
} satisfies OAuthError

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as OAuthError
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


