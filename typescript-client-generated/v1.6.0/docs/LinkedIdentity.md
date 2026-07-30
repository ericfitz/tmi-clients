
# LinkedIdentity


## Properties

Name | Type
------------ | -------------
`id` | string
`provider` | string
`provider_user_id` | string
`email` | string
`name` | string
`linked_at` | Date
`last_used_at` | Date

## Example

```typescript
import type { LinkedIdentity } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "provider": null,
  "provider_user_id": null,
  "email": null,
  "name": null,
  "linked_at": null,
  "last_used_at": null,
} satisfies LinkedIdentity

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as LinkedIdentity
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


