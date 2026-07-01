
# InvokeAddonResponse

Response from addon invocation including delivery ID

## Properties

Name | Type
------------ | -------------
`delivery_id` | string
`status` | string
`created_at` | Date

## Example

```typescript
import type { InvokeAddonResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "delivery_id": null,
  "status": null,
  "created_at": null,
} satisfies InvokeAddonResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as InvokeAddonResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


