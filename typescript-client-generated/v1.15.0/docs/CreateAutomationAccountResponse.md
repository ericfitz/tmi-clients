
# CreateAutomationAccountResponse

Response from creating an automation account. Contains the created user and a client credential with the plaintext secret (shown only once).

## Properties

Name | Type
------------ | -------------
`user` | [AdminUser](AdminUser.md)
`client_credential` | [ClientCredentialResponse](ClientCredentialResponse.md)

## Example

```typescript
import type { CreateAutomationAccountResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "user": null,
  "client_credential": null,
} satisfies CreateAutomationAccountResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CreateAutomationAccountResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


