
# WebhookSubscriptionInput

Input schema for creating or updating a webhook subscription

## Properties

Name | Type
------------ | -------------
`threat_model_id` | string
`name` | string
`url` | string
`events` | Array&lt;string&gt;
`secret` | string

## Example

```typescript
import type { WebhookSubscriptionInput } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "threat_model_id": null,
  "name": null,
  "url": null,
  "events": null,
  "secret": null,
} satisfies WebhookSubscriptionInput

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as WebhookSubscriptionInput
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


