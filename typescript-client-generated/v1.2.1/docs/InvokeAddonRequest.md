
# InvokeAddonRequest

Request to invoke an addon with parameters and payload

## Properties

Name | Type
------------ | -------------
`threat_model_id` | string
`object_type` | string
`object_id` | string
`payload` | { [key: string]: any; }

## Example

```typescript
import type { InvokeAddonRequest } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "threat_model_id": null,
  "object_type": null,
  "object_id": null,
  "payload": null,
} satisfies InvokeAddonRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as InvokeAddonRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


