
# Edge

Diagram edge representing a data flow connection between nodes

## Properties

Name | Type
------------ | -------------
`shape` | string
`source` | [EdgeTerminal](EdgeTerminal.md)
`target` | [EdgeTerminal](EdgeTerminal.md)
`attrs` | [EdgeAttrs](EdgeAttrs.md)
`labels` | [Array&lt;EdgeLabel&gt;](EdgeLabel.md)
`vertices` | [Array&lt;Point&gt;](Point.md)
`router` | [EdgeRouter](EdgeRouter.md)
`connector` | [EdgeConnector](EdgeConnector.md)
`defaultLabel` | [EdgeLabel](EdgeLabel.md)

## Example

```typescript
import type { Edge } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "shape": null,
  "source": null,
  "target": null,
  "attrs": null,
  "labels": null,
  "vertices": null,
  "router": null,
  "connector": null,
  "defaultLabel": null,
} satisfies Edge

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Edge
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


