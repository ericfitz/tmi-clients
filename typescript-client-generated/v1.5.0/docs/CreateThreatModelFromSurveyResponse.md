
# CreateThreatModelFromSurveyResponse

Response after creating a threat model from a survey response

## Properties

Name | Type
------------ | -------------
`threat_model_id` | string
`survey_response_id` | string

## Example

```typescript
import type { CreateThreatModelFromSurveyResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "threat_model_id": null,
  "survey_response_id": null,
} satisfies CreateThreatModelFromSurveyResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CreateThreatModelFromSurveyResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


