
# SurveyResponseBase

Base schema for SurveyResponse with client-writable fields

## Properties

Name | Type
------------ | -------------
`answers` | { [key: string]: any; }
`linked_threat_model_id` | string
`authorization` | [Array&lt;Authorization&gt;](Authorization.md)
`ui_state` | { [key: string]: any; }
`survey_id` | string
`survey_version` | string
`project_id` | string

## Example

```typescript
import type { SurveyResponseBase } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "answers": null,
  "linked_threat_model_id": null,
  "authorization": null,
  "ui_state": null,
  "survey_id": null,
  "survey_version": null,
  "project_id": null,
} satisfies SurveyResponseBase

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SurveyResponseBase
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


