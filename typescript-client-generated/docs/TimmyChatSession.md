
# TimmyChatSession

A Timmy AI assistant chat session within a threat model

## Properties

Name | Type
------------ | -------------
`id` | string
`threat_model_id` | string
`user_id` | string
`title` | string
`source_snapshot` | [Array&lt;TimmyChatSessionSourceSnapshotInner&gt;](TimmyChatSessionSourceSnapshotInner.md)
`system_prompt_hash` | string
`status` | string
`created_at` | Date
`modified_at` | Date

## Example

```typescript
import type { TimmyChatSession } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "threat_model_id": null,
  "user_id": null,
  "title": null,
  "source_snapshot": null,
  "system_prompt_hash": null,
  "status": null,
  "created_at": null,
  "modified_at": null,
} satisfies TimmyChatSession

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as TimmyChatSession
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


