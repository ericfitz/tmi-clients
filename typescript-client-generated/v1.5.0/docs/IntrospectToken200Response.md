
# IntrospectToken200Response


## Properties

Name | Type
------------ | -------------
`active` | boolean
`sub` | string
`email` | string
`name` | string
`exp` | number
`iat` | number
`iss` | string
`token_type` | string
`scope` | string

## Example

```typescript
import type { IntrospectToken200Response } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "active": true,
  "sub": user@example.com,
  "email": user@example.com,
  "name": John Doe,
  "exp": 1640995200,
  "iat": 1640991600,
  "iss": http://localhost:8080,
  "token_type": Bearer,
  "scope": openid profile email,
} satisfies IntrospectToken200Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as IntrospectToken200Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


