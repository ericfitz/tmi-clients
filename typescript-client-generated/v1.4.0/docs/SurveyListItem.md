
# SurveyListItem

Summary of a survey for list responses

## Properties

Name | Type
------------ | -------------
`id` | string
`name` | string
`description` | string
`version` | string
`status` | string
`created_at` | Date
`modified_at` | Date
`created_by` | [User](User.md)

## Example

```typescript
import type { SurveyListItem } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "name": null,
  "description": null,
  "version": null,
  "status": null,
  "created_at": null,
  "modified_at": null,
  "created_by": null,
} satisfies SurveyListItem

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SurveyListItem
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


