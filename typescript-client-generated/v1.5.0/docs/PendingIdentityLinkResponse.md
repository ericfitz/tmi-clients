
# PendingIdentityLinkResponse


## Properties

Name | Type
------------ | -------------
`pending` | [PendingIdentityLinkResponsePending](PendingIdentityLinkResponsePending.md)
`account` | [PendingIdentityLinkResponseAccount](PendingIdentityLinkResponseAccount.md)

## Example

```typescript
import type { PendingIdentityLinkResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "pending": null,
  "account": null,
} satisfies PendingIdentityLinkResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as PendingIdentityLinkResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


