
# TimmyChatMessage

A message within a Timmy chat session

## Properties

Name | Type
------------ | -------------
`id` | string
`session_id` | string
`role` | string
`content` | string
`token_count` | number
`sequence` | number
`created_at` | Date

## Example

```typescript
import type { TimmyChatMessage } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "session_id": null,
  "role": null,
  "content": null,
  "token_count": null,
  "sequence": null,
  "created_at": null,
} satisfies TimmyChatMessage

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as TimmyChatMessage
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


