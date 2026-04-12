
# TransferOwnershipResult

Result of an ownership transfer operation

## Properties

Name | Type
------------ | -------------
`threat_models_transferred` | [TransferOwnershipResultThreatModelsTransferred](TransferOwnershipResultThreatModelsTransferred.md)
`survey_responses_transferred` | [TransferOwnershipResultSurveyResponsesTransferred](TransferOwnershipResultSurveyResponsesTransferred.md)

## Example

```typescript
import type { TransferOwnershipResult } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "threat_models_transferred": null,
  "survey_responses_transferred": null,
} satisfies TransferOwnershipResult

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as TransferOwnershipResult
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


