
# ClientCredentialInfo

Client credential information without the secret

## Properties

Name | Type
------------ | -------------
`id` | string
`client_id` | string
`name` | string
`description` | string
`is_active` | boolean
`last_used_at` | Date
`created_at` | Date
`modified_at` | Date
`expires_at` | Date

## Example

```typescript
import type { ClientCredentialInfo } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "client_id": null,
  "name": null,
  "description": null,
  "is_active": null,
  "last_used_at": null,
  "created_at": null,
  "modified_at": null,
  "expires_at": null,
} satisfies ClientCredentialInfo

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ClientCredentialInfo
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


