
# WebhookQuota

Webhook subscription quota configuration for a user

## Properties

Name | Type
------------ | -------------
`owner_id` | string
`max_subscriptions` | number
`max_events_per_minute` | number
`max_subscription_requests_per_minute` | number
`max_subscription_requests_per_day` | number
`created_at` | Date
`modified_at` | Date

## Example

```typescript
import type { WebhookQuota } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "owner_id": null,
  "max_subscriptions": null,
  "max_events_per_minute": null,
  "max_subscription_requests_per_minute": null,
  "max_subscription_requests_per_day": null,
  "created_at": null,
  "modified_at": null,
} satisfies WebhookQuota

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as WebhookQuota
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


