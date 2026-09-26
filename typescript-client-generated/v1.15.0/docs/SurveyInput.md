
# SurveyInput

Input schema for creating or updating Survey

## Properties

Name | Type
------------ | -------------
`name` | string
`description` | string
`version` | string
`status` | string
`settings` | [SurveySettings](SurveySettings.md)
`survey_json` | { [key: string]: any; }

## Example

```typescript
import type { SurveyInput } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "description": null,
  "version": null,
  "status": null,
  "settings": null,
  "survey_json": null,
} satisfies SurveyInput

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SurveyInput
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


