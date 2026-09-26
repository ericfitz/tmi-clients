
# ListWebhookQuotasResponseDefaults

Server default quota values applied when a user has no quota row

## Properties

Name | Type
------------ | -------------
`max_subscriptions` | number
`max_events_per_minute` | number
`max_subscription_requests_per_minute` | number
`max_subscription_requests_per_day` | number

## Example

```typescript
import type { ListWebhookQuotasResponseDefaults } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "max_subscriptions": null,
  "max_events_per_minute": null,
  "max_subscription_requests_per_minute": null,
  "max_subscription_requests_per_day": null,
} satisfies ListWebhookQuotasResponseDefaults

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListWebhookQuotasResponseDefaults
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


