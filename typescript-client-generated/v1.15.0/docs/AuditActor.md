
# AuditActor

Denormalized user information stored with audit entries. Persists after user deletion.

## Properties

Name | Type
------------ | -------------
`email` | string
`provider` | string
`provider_id` | string
`display_name` | string

## Example

```typescript
import type { AuditActor } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "email": null,
  "provider": null,
  "provider_id": null,
  "display_name": null,
} satisfies AuditActor

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as AuditActor
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


