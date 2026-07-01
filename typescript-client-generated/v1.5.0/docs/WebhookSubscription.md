
# WebhookSubscription

Webhook subscription configuration for event notifications

## Properties

Name | Type
------------ | -------------
`id` | string
`owner_id` | string
`threat_model_id` | string
`name` | string
`url` | string
`events` | [Array&lt;WebhookEventType&gt;](WebhookEventType.md)
`secret` | string
`status` | string
`challenges_sent` | number
`created_at` | Date
`modified_at` | Date
`last_successful_use` | Date
`publication_failures` | number

## Example

```typescript
import type { WebhookSubscription } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "owner_id": null,
  "threat_model_id": null,
  "name": null,
  "url": null,
  "events": null,
  "secret": null,
  "status": null,
  "challenges_sent": null,
  "created_at": null,
  "modified_at": null,
  "last_successful_use": null,
  "publication_failures": null,
} satisfies WebhookSubscription

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as WebhookSubscription
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


