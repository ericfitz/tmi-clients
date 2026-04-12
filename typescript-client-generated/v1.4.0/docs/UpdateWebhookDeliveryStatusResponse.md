
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
  "id": null,
  "status": null,
  "status_percent": null,
  "status_updated_at": null,
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


