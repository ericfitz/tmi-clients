
# AddonResponse

Addon details including configuration and status

## Properties

Name | Type
------------ | -------------
`id` | string
`created_at` | Date
`name` | string
`webhook_id` | string
`description` | string
`icon` | string
`objects` | Array&lt;string&gt;
`threat_model_id` | string
`parameters` | [Array&lt;AddonParameter&gt;](AddonParameter.md)

## Example

```typescript
import type { AddonResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "created_at": null,
  "name": null,
  "webhook_id": null,
  "description": null,
  "icon": null,
  "objects": null,
  "threat_model_id": null,
  "parameters": null,
} satisfies AddonResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as AddonResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


