
# GroupMember

Member of a group with role information

## Properties

Name | Type
------------ | -------------
`id` | string
`group_internal_uuid` | string
`user_internal_uuid` | string
`user_email` | string
`user_name` | string
`user_provider` | string
`user_provider_user_id` | string
`added_by_internal_uuid` | string
`added_by_email` | string
`added_at` | Date
`notes` | string
`subject_type` | string
`member_group_internal_uuid` | string
`member_group_name` | string

## Example

```typescript
import type { GroupMember } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "group_internal_uuid": null,
  "user_internal_uuid": null,
  "user_email": null,
  "user_name": null,
  "user_provider": null,
  "user_provider_user_id": null,
  "added_by_internal_uuid": null,
  "added_by_email": null,
  "added_at": null,
  "notes": null,
  "subject_type": null,
  "member_group_internal_uuid": null,
  "member_group_name": null,
} satisfies GroupMember

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GroupMember
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


