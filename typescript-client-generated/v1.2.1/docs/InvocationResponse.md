
# InvocationResponse

Status and result of an addon invocation

## Properties

Name | Type
------------ | -------------
`id` | string
`addon_id` | string
`threat_model_id` | string
`object_type` | string
`object_id` | string
`invoked_by` | [User](User.md)
`payload` | string
`status` | string
`status_percent` | number
`status_message` | string
`created_at` | Date
`status_updated_at` | Date

## Example

```typescript
import type { InvocationResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "addon_id": null,
  "threat_model_id": null,
  "object_type": null,
  "object_id": null,
  "invoked_by": null,
  "payload": null,
  "status": null,
  "status_percent": null,
  "status_message": null,
  "created_at": null,
  "status_updated_at": null,
} satisfies InvocationResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as InvocationResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


