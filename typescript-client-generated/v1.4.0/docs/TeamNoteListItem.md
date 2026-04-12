
# TeamNoteListItem

Summary information for TeamNote in list responses

## Properties

Name | Type
------------ | -------------
`id` | string
`name` | string
`description` | string
`timmy_enabled` | boolean
`sharable` | boolean
`created_at` | Date
`modified_at` | Date

## Example

```typescript
import type { TeamNoteListItem } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "name": null,
  "description": null,
  "timmy_enabled": null,
  "sharable": null,
  "created_at": null,
  "modified_at": null,
} satisfies TeamNoteListItem

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as TeamNoteListItem
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


