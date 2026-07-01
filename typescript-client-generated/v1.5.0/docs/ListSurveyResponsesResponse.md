
# ListSurveyResponsesResponse

Paginated list of survey responses

## Properties

Name | Type
------------ | -------------
`survey_responses` | [Array&lt;SurveyResponseListItem&gt;](SurveyResponseListItem.md)
`total` | number
`limit` | number
`offset` | number

## Example

```typescript
import type { ListSurveyResponsesResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "survey_responses": [{"id":"b2c3d4e5-f6a7-8901-bcde-f12345678901","survey_id":"a1b2c3d4-e5f6-7890-abcd-ef1234567890","survey_name":"Security Review Intake","survey_version":"2024-Q1","status":"submitted","is_confidential":false,"owner":{"principal_type":"user","provider":"google","provider_id":"109876543210987654321","display_name":"Alice Developer","email":"alice@example.com"},"created_at":"2024-02-15T09:00:00Z","submitted_at":"2024-02-15T10:30:00Z","modified_at":"2024-02-15T10:30:00Z"}],
  "total": 42,
  "limit": 20,
  "offset": 0,
} satisfies ListSurveyResponsesResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListSurveyResponsesResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


