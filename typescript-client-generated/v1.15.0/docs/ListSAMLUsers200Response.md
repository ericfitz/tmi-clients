
# ListSAMLUsers200Response

Lightweight SAML user list for UI autocomplete.

## Properties

Name | Type
------------ | -------------
`idp` | string
`users` | [Array&lt;ListSAMLUsers200ResponseUsersInner&gt;](ListSAMLUsers200ResponseUsersInner.md)
`total` | number

## Example

```typescript
import type { ListSAMLUsers200Response } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "idp": tmi,
  "users": null,
  "total": 41,
} satisfies ListSAMLUsers200Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListSAMLUsers200Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


