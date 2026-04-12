
# CollaborationSession

Details of an active collaboration session for a diagram

## Properties

Name | Type
------------ | -------------
`session_id` | string
`host` | [User](User.md)
`presenter` | [User](User.md)
`threat_model_id` | string
`threat_model_name` | string
`diagram_id` | string
`diagram_name` | string
`participants` | [Array&lt;Participant&gt;](Participant.md)
`websocket_url` | string

## Example

```typescript
import type { CollaborationSession } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "session_id": null,
  "host": null,
  "presenter": null,
  "threat_model_id": null,
  "threat_model_name": null,
  "diagram_id": null,
  "diagram_name": null,
  "participants": null,
  "websocket_url": null,
} satisfies CollaborationSession

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CollaborationSession
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


