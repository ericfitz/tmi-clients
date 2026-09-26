
# ContentAuthorizationURL

OAuth authorization URL plus expiry of the associated server-side state.

## Properties

Name | Type
------------ | -------------
`authorization_url` | string
`expires_at` | Date

## Example

```typescript
import type { ContentAuthorizationURL } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "authorization_url": https://auth.atlassian.com/authorize?audience=api.atlassian.com&client_id=...&state=...,
  "expires_at": 2026-04-19T12:34:56Z,
} satisfies ContentAuthorizationURL

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ContentAuthorizationURL
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


