
# TeamMemberInput

Client-writable fields of TeamMember (excludes the server-resolved user).

## Properties

Name | Type
------------ | -------------
`user_id` | string
`role` | [TeamMemberRole](TeamMemberRole.md)
`custom_role` | string

## Example

```typescript
import type { TeamMemberInput } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "user_id": null,
  "role": null,
  "custom_role": null,
} satisfies TeamMemberInput

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as TeamMemberInput
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


