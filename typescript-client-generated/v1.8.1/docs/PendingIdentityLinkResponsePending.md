
# PendingIdentityLinkResponsePending


## Properties

Name | Type
------------ | -------------
`provider` | string
`provider_user_id` | string
`email` | string
`name` | string

## Example

```typescript
import type { PendingIdentityLinkResponsePending } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "provider": null,
  "provider_user_id": null,
  "email": null,
  "name": null,
} satisfies PendingIdentityLinkResponsePending

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as PendingIdentityLinkResponsePending
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


