
# PortConfiguration

Port configuration for node connections

## Properties

Name | Type
------------ | -------------
`groups` | [{ [key: string]: PortConfigurationGroupsValue; }](PortConfigurationGroupsValue.md)
`items` | [Array&lt;PortConfigurationItemsInner&gt;](PortConfigurationItemsInner.md)

## Example

```typescript
import type { PortConfiguration } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "groups": null,
  "items": null,
} satisfies PortConfiguration

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as PortConfiguration
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


