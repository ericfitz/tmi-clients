
# TeamListItem

Summary of a team for list views

## Properties

Name | Type
------------ | -------------
`id` | string
`name` | string
`description` | string
`status` | [TeamStatus](TeamStatus.md)
`member_count` | number
`project_count` | number
`created_at` | Date
`modified_at` | Date

## Example

```typescript
import type { TeamListItem } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "name": null,
  "description": null,
  "status": null,
  "member_count": null,
  "project_count": null,
  "created_at": null,
  "modified_at": null,
} satisfies TeamListItem

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as TeamListItem
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


