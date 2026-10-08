
# Edge

Diagram edge representing a data flow connection between nodes  Fully compatible with X6 Edge objects and supports X6 routing algorithms (manhattan, orth, one_side, metro, er), connector styles (normal, rounded, smooth, jumpover), custom markup, tools, and convenience properties (label, style) for easier integration.

## Properties

Name | Type
------------ | -------------
`id` | string
`data` | [CellData](CellData.md)
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
import type { Edge } from '@tmi-dev/client'

// TODO: Update the object below with actual values
const example = {
  "id": 37eaedfa-bf37-4996-8665-242fec34bbff,
  "data": null,
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


