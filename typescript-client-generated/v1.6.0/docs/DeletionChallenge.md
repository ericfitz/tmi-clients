
# DeletionChallenge

Challenge response for user account deletion

## Properties

Name | Type
------------ | -------------
`challenge_text` | string
`expires_at` | Date

## Example

```typescript
import type { DeletionChallenge } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "challenge_text": null,
  "expires_at": null,
} satisfies DeletionChallenge

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DeletionChallenge
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


