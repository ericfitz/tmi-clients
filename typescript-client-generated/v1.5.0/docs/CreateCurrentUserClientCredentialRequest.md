
# CreateCurrentUserClientCredentialRequest


## Properties

Name | Type
------------ | -------------
`name` | string
`description` | string
`expires_at` | Date

## Example

```typescript
import type { CreateCurrentUserClientCredentialRequest } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "name": CI/CD Pipeline,
  "description": CI/CD pipeline automation credential,
  "expires_at": 2027-01-17T00:00Z,
} satisfies CreateCurrentUserClientCredentialRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CreateCurrentUserClientCredentialRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


