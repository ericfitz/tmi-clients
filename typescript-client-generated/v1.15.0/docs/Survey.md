
# Survey

A survey defining questions for security review intake

## Properties

Name | Type
------------ | -------------
`name` | string
`description` | string
`version` | string
`status` | string
`settings` | [SurveySettings](SurveySettings.md)
`survey_json` | { [key: string]: any; }
`id` | string
`created_at` | Date
`modified_at` | Date
`created_by` | [User](User.md)
`metadata` | [Array&lt;Metadata&gt;](Metadata.md)

## Example

```typescript
import type { Survey } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "description": null,
  "version": null,
  "status": null,
  "settings": null,
  "survey_json": null,
  "id": null,
  "created_at": null,
  "modified_at": null,
  "created_by": null,
  "metadata": null,
} satisfies Survey

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Survey
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


