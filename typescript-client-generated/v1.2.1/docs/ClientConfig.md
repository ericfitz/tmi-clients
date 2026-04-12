
# ClientConfig

Client configuration for tmi-ux and other client applications

## Properties

Name | Type
------------ | -------------
`features` | [ClientConfigFeatures](ClientConfigFeatures.md)
`operator` | [ClientConfigOperator](ClientConfigOperator.md)
`limits` | [ClientConfigLimits](ClientConfigLimits.md)
`ui` | [ClientConfigUi](ClientConfigUi.md)

## Example

```typescript
import type { ClientConfig } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "features": null,
  "operator": null,
  "limits": null,
  "ui": null,
} satisfies ClientConfig

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ClientConfig
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


