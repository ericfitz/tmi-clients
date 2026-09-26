
# NodeAttrsBody

Body/shape styling attributes

## Properties

Name | Type
------------ | -------------
`fill` | string
`stroke` | string
`strokeWidth` | number
`strokeDasharray` | string
`rx` | number
`ry` | number
`lateral` | number
`refWidth` | [NodeAttrsBodyRefWidth](NodeAttrsBodyRefWidth.md)
`refHeight` | [NodeAttrsBodyRefHeight](NodeAttrsBodyRefHeight.md)
`fillOpacity` | number

## Example

```typescript
import type { NodeAttrsBody } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "fill": null,
  "stroke": null,
  "strokeWidth": null,
  "strokeDasharray": null,
  "rx": null,
  "ry": null,
  "lateral": null,
  "refWidth": null,
  "refHeight": null,
  "fillOpacity": null,
} satisfies NodeAttrsBody

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as NodeAttrsBody
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


