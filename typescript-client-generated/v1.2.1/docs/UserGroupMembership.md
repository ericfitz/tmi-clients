
# UserGroupMembership

TMI-managed group that a user belongs to

## Properties

Name | Type
------------ | -------------
`internal_uuid` | string
`group_name` | string
`name` | string

## Example

```typescript
import type { UserGroupMembership } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "internal_uuid": null,
  "group_name": null,
  "name": null,
} satisfies UserGroupMembership

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as UserGroupMembership
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


