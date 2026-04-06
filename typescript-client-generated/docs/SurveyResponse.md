
# SurveyResponse

A survey response containing answers to survey questions

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
`id` | string
`status` | string
`is_confidential` | boolean
`revision_notes` | string
`created_threat_model_id` | string
`owner` | object
`created_at` | Date
`modified_at` | Date
`submitted_at` | Date
`reviewed_at` | Date
`reviewed_by` | object
`survey_json` | { [key: string]: any; }
`metadata` | [Array&lt;Metadata&gt;](Metadata.md)
`created_by` | object

## Example

```typescript
import type { SurveyResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "answers": null,
  "linked_threat_model_id": null,
  "authorization": null,
  "ui_state": null,
  "survey_id": null,
  "survey_version": null,
  "project_id": null,
  "id": null,
  "status": null,
  "is_confidential": null,
  "revision_notes": null,
  "created_threat_model_id": null,
  "owner": null,
  "created_at": null,
  "modified_at": null,
  "submitted_at": null,
  "reviewed_at": null,
  "reviewed_by": null,
  "survey_json": null,
  "metadata": null,
  "created_by": null,
} satisfies SurveyResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SurveyResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


