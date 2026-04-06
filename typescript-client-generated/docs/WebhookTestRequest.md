
# WebhookTestRequest

Request to test a webhook subscription with a sample event

## Properties

Name | Type
------------ | -------------
`event_type` | string

## Example

```typescript
import type { WebhookTestRequest } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "event_type": null,
} satisfies WebhookTestRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as WebhookTestRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


