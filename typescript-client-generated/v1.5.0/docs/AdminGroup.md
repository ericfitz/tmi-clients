
# AdminGroup

Group object with administrative fields and enriched data

## Properties

Name | Type
------------ | -------------
`internal_uuid` | string
`provider` | string
`group_name` | string
`name` | string
`description` | string
`first_used` | Date
`last_used` | Date
`usage_count` | number
`used_in_authorizations` | boolean
`used_in_admin_grants` | boolean
`member_count` | number

## Example

```typescript
import type { AdminGroup } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "internal_uuid": null,
  "provider": null,
  "group_name": null,
  "name": null,
  "description": null,
  "first_used": null,
  "last_used": null,
  "usage_count": null,
  "used_in_authorizations": null,
  "used_in_admin_grants": null,
  "member_count": null,
} satisfies AdminGroup

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as AdminGroup
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


