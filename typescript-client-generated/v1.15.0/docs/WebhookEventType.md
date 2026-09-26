
# WebhookEventType

Webhook event type following {resource}.{action} pattern. CRUD events are emitted for resource lifecycle changes (created, updated, deleted). The addon.invoked event is emitted when an add-on is invoked.

## Properties

Name | Type
------------ | -------------

## Example

```typescript
import type { WebhookEventType } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
} satisfies WebhookEventType

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as WebhookEventType
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


