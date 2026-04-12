
# AdminUser

User object with administrative fields and enriched data

## Properties

Name | Type
------------ | -------------
`internal_uuid` | string
`provider` | string
`provider_user_id` | string
`email` | string
`name` | string
`email_verified` | boolean
`created_at` | Date
`modified_at` | Date
`last_login` | Date
`is_admin` | boolean
`groups` | Array&lt;string&gt;
`active_threat_models` | number

## Example

```typescript
import type { AdminUser } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "internal_uuid": null,
  "provider": null,
  "provider_user_id": null,
  "email": null,
  "name": null,
  "email_verified": null,
  "created_at": null,
  "modified_at": null,
  "last_login": null,
  "is_admin": null,
  "groups": null,
  "active_threat_models": null,
} satisfies AdminUser

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as AdminUser
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


