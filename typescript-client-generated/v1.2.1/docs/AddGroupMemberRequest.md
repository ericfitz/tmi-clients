
# AddGroupMemberRequest

Request to add a user or group to a group. Provide user_internal_uuid for user members or member_group_internal_uuid for group members.

## Properties

Name | Type
------------ | -------------
`user_internal_uuid` | string
`notes` | string
`subject_type` | string
`member_group_internal_uuid` | string

## Example

```typescript
import type { AddGroupMemberRequest } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "user_internal_uuid": null,
  "notes": null,
  "subject_type": null,
  "member_group_internal_uuid": null,
} satisfies AddGroupMemberRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as AddGroupMemberRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


