
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
  "id": 123e4567-e89b-12d3-a456-426614174000,
  "threat_model_id": 223e4567-e89b-12d3-a456-426614174001,
  "user_id": 323e4567-e89b-12d3-a456-426614174002,
  "title": Payment flow threat analysis,
  "source_snapshot": [],
  "system_prompt_hash": sha256:abc123def456789,
  "status": active,
  "created_at": 2026-04-19T12:00Z,
  "modified_at": 2026-04-19T12:34:56Z,
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


