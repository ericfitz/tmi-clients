
# TimmyUsageRecord

Usage record for Timmy AI assistant

## Properties

Name | Type
------------ | -------------
`user_id` | string
`session_id` | string
`threat_model_id` | string
`message_count` | number
`prompt_tokens` | number
`completion_tokens` | number
`embedding_tokens` | number
`period_start` | Date
`period_end` | Date

## Example

```typescript
import type { TimmyUsageRecord } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "user_id": null,
  "session_id": null,
  "threat_model_id": null,
  "message_count": null,
  "prompt_tokens": null,
  "completion_tokens": null,
  "embedding_tokens": null,
  "period_start": null,
  "period_end": null,
} satisfies TimmyUsageRecord

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as TimmyUsageRecord
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


