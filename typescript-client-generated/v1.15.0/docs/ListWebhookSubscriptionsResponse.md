
# ListWebhookSubscriptionsResponse

Paginated list of webhook subscriptions

## Properties

Name | Type
------------ | -------------
`subscriptions` | [Array&lt;WebhookSubscription&gt;](WebhookSubscription.md)
`total` | number
`limit` | number
`offset` | number

## Example

```typescript
import type { ListWebhookSubscriptionsResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "subscriptions": [{"id":"550e8400-e29b-41d4-a716-446655440000","owner_id":"550e8400-e29b-41d4-a716-446655440020","name":"Production Slack Notifications","url":"https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXX","events":["diagram.updated","threat_model.created"],"status":"active","created_at":"2024-01-15T10:30:00Z","modified_at":"2024-01-15T10:30:00Z"}],
  "total": 6,
  "limit": 20,
  "offset": 0,
} satisfies ListWebhookSubscriptionsResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListWebhookSubscriptionsResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


