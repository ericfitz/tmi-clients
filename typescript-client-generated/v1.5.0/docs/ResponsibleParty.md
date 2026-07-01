
# ResponsibleParty

A responsible party for a team or project with their role

## Properties

Name | Type
------------ | -------------
`user_id` | string
`user` | [User](User.md)
`role` | [TeamMemberRole](TeamMemberRole.md)
`custom_role` | string

## Example

```typescript
import type { ResponsibleParty } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "user_id": null,
  "user": null,
  "role": null,
  "custom_role": null,
} satisfies ResponsibleParty

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ResponsibleParty
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


