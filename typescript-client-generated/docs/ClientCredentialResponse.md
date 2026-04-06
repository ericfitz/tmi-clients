
# ClientCredentialResponse

Response from creating a client credential. WARNING: The client_secret is ONLY returned once and cannot be retrieved later.

## Properties

Name | Type
------------ | -------------
`id` | string
`client_id` | string
`client_secret` | string
`name` | string
`description` | string
`created_at` | Date
`expires_at` | Date

## Example

```typescript
import type { ClientCredentialResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "client_id": null,
  "client_secret": null,
  "name": null,
  "description": null,
  "created_at": null,
  "expires_at": null,
} satisfies ClientCredentialResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ClientCredentialResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


