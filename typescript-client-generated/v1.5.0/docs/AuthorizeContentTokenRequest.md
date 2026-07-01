
# AuthorizeContentTokenRequest

Authorize request body.

## Properties

Name | Type
------------ | -------------
`client_callback` | string

## Example

```typescript
import type { AuthorizeContentTokenRequest } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "client_callback": http://localhost:4200/oauth2/content-callback,
} satisfies AuthorizeContentTokenRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as AuthorizeContentTokenRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


