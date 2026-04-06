
# GetCurrentUser200Response

OIDC-compliant userinfo response per OpenID Connect Core 1.0 Section 5.1

## Properties

Name | Type
------------ | -------------
`sub` | string
`email` | string
`name` | string
`idp` | string
`groups` | Array&lt;string&gt;

## Example

```typescript
import type { GetCurrentUser200Response } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "sub": alice,
  "email": user@example.com,
  "name": John Doe,
  "idp": github,
  "groups": ["admins","users"],
} satisfies GetCurrentUser200Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GetCurrentUser200Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


