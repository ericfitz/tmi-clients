
# WebhookTestResponse

Response from a webhook test including delivery status

## Properties

Name | Type
------------ | -------------
`delivery_id` | string
`status` | string
`message` | string

## Example

```typescript
import type { WebhookTestResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "delivery_id": null,
  "status": null,
  "message": null,
} satisfies WebhookTestResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as WebhookTestResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


