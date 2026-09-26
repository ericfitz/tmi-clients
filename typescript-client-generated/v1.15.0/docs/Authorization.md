
# Authorization

Authorization record granting a user access to a resource with a specific role

## Properties

Name | Type
------------ | -------------
`principal_type` | string
`provider` | string
`provider_id` | string
`display_name` | string
`email` | string
`role` | string

## Example

```typescript
import type { Authorization } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "principal_type": null,
  "provider": null,
  "provider_id": null,
  "display_name": null,
  "email": null,
  "role": null,
} satisfies Authorization

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Authorization
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


