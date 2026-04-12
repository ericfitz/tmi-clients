
# WebhookDelivery

Record of a webhook delivery attempt including status and response

## Properties

Name | Type
------------ | -------------
`id` | string
`subscription_id` | string
`event_type` | [WebhookEventType](WebhookEventType.md)
`payload` | { [key: string]: any; }
`status` | string
`attempts` | number
`next_retry_at` | Date
`last_error` | string
`created_at` | Date
`delivered_at` | Date
`status_percent` | number
`status_message` | string
`last_activity_at` | Date
`addon_id` | string
`invoked_by` | [User](User.md)

## Example

```typescript
import type { WebhookDelivery } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "subscription_id": null,
  "event_type": null,
  "payload": null,
  "status": null,
  "attempts": null,
  "next_retry_at": null,
  "last_error": null,
  "created_at": null,
  "delivered_at": null,
  "status_percent": null,
  "status_message": null,
  "last_activity_at": null,
  "addon_id": null,
  "invoked_by": null,
} satisfies WebhookDelivery

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as WebhookDelivery
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


