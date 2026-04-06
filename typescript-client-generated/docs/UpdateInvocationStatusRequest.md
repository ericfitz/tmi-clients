
# UpdateInvocationStatusRequest

Request to update the status of an async addon invocation

## Properties

Name | Type
------------ | -------------
`status` | string
`status_percent` | number
`status_message` | string

## Example

```typescript
import type { UpdateInvocationStatusRequest } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "status": null,
  "status_percent": null,
  "status_message": null,
} satisfies UpdateInvocationStatusRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as UpdateInvocationStatusRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


