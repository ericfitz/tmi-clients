
# IdentityLinkStartResponse


## Properties

Name | Type
------------ | -------------
`link_state` | string
`authorization_url` | string
`expires_at` | Date

## Example

```typescript
import type { IdentityLinkStartResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "link_state": null,
  "authorization_url": null,
  "expires_at": null,
} satisfies IdentityLinkStartResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as IdentityLinkStartResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


