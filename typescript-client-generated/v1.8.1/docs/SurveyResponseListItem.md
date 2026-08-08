
# SurveyResponseListItem

Summary of a survey response for list endpoints

## Properties

Name | Type
------------ | -------------
`id` | string
`status` | string
`is_confidential` | boolean
`owner` | [User](User.md)
`created_at` | Date
`submitted_at` | Date
`modified_at` | Date
`survey_id` | string
`survey_name` | string
`survey_version` | string

## Example

```typescript
import type { SurveyResponseListItem } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "status": null,
  "is_confidential": null,
  "owner": null,
  "created_at": null,
  "submitted_at": null,
  "modified_at": null,
  "survey_id": null,
  "survey_name": null,
  "survey_version": null,
} satisfies SurveyResponseListItem

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SurveyResponseListItem
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


