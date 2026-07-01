
# UpdateWebhookDeliveryStatusResponse

Response confirming webhook delivery status update

## Properties

Name | Type
------------ | -------------
`id` | string
`status` | string
`status_percent` | number
`status_updated_at` | Date

## Example

```typescript
import type { UpdateWebhookDeliveryStatusResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": 123e4567-e89b-12d3-a456-426614174000,
  "status": in_progress,
  "status_percent": 50,
  "status_updated_at": 2026-04-19T12:34:56Z,
} satisfies UpdateWebhookDeliveryStatusResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as UpdateWebhookDeliveryStatusResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


