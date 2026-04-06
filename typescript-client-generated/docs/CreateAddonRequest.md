
# CreateAddonRequest

Request schema for registering a new addon

## Properties

Name | Type
------------ | -------------
`name` | string
`webhook_id` | string
`description` | string
`icon` | string
`objects` | Array&lt;string&gt;
`threat_model_id` | string
`parameters` | [Array&lt;AddonParameter&gt;](AddonParameter.md)

## Example

```typescript
import type { CreateAddonRequest } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "webhook_id": null,
  "description": null,
  "icon": null,
  "objects": null,
  "threat_model_id": null,
  "parameters": null,
} satisfies CreateAddonRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CreateAddonRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


