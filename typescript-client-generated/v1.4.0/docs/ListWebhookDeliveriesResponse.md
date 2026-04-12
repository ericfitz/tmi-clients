
# ListWebhookDeliveriesResponse

Paginated list of webhook deliveries

## Properties

Name | Type
------------ | -------------
`deliveries` | [Array&lt;WebhookDelivery&gt;](WebhookDelivery.md)
`total` | number
`limit` | number
`offset` | number

## Example

```typescript
import type { ListWebhookDeliveriesResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "deliveries": [{"id":"aa0e8400-e29b-41d4-a716-446655440005","subscription_id":"550e8400-e29b-41d4-a716-446655440000","event_type":"diagram.updated","status":"delivered","attempts":1,"created_at":"2024-01-20T15:45:30Z","delivered_at":"2024-01-20T15:45:31Z"}],
  "total": 100,
  "limit": 20,
  "offset": 0,
} satisfies ListWebhookDeliveriesResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListWebhookDeliveriesResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


