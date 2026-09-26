
# AdminUserIdentitiesResponse

A user\'s primary sign-in identity plus any linked identities, as seen by an administrator

## Properties

Name | Type
------------ | -------------
`primary` | [AdminUserIdentitiesResponsePrimary](AdminUserIdentitiesResponsePrimary.md)
`linked` | [Array&lt;LinkedIdentity&gt;](LinkedIdentity.md)

## Example

```typescript
import type { AdminUserIdentitiesResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "primary": null,
  "linked": null,
} satisfies AdminUserIdentitiesResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as AdminUserIdentitiesResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


