
# ClientConfigFeatures

Feature flags indicating enabled functionality

## Properties

Name | Type
------------ | -------------
`websocket_enabled` | boolean
`saml_enabled` | boolean
`webhooks_enabled` | boolean

## Example

```typescript
import type { ClientConfigFeatures } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "websocket_enabled": null,
  "saml_enabled": null,
  "webhooks_enabled": null,
} satisfies ClientConfigFeatures

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ClientConfigFeatures
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


