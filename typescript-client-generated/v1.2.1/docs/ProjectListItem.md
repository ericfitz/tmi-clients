
# ProjectListItem

Summary of a project for list views

## Properties

Name | Type
------------ | -------------
`id` | string
`name` | string
`description` | string
`status` | string
`team_id` | string
`team_name` | string
`created_at` | Date
`modified_at` | Date

## Example

```typescript
import type { ProjectListItem } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "name": null,
  "description": null,
  "status": null,
  "team_id": null,
  "team_name": null,
  "created_at": null,
  "modified_at": null,
} satisfies ProjectListItem

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ProjectListItem
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


