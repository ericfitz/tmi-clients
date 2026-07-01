
# ListSurveysResponse

Paginated list of surveys

## Properties

Name | Type
------------ | -------------
`total` | number
`limit` | number
`offset` | number
`surveys` | [Array&lt;SurveyListItem&gt;](SurveyListItem.md)

## Example

```typescript
import type { ListSurveysResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "total": 5,
  "limit": 20,
  "offset": 0,
  "surveys": [{"id":"a1b2c3d4-e5f6-7890-abcd-ef1234567890","name":"Security Review Intake","description":"Standard security review intake questionnaire","version":"2024-Q1","status":"active","created_at":"2024-01-15T10:30:00Z","modified_at":"2024-02-01T14:00:00Z","created_by":{"principal_type":"user","provider":"google","provider_id":"118234567890123456789","display_name":"Admin User","email":"admin@example.com"}}],
} satisfies ListSurveysResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListSurveysResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


