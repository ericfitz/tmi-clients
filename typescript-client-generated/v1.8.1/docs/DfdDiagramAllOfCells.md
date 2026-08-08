
# DfdDiagramAllOfCells


## Properties

Name | Type
------------ | -------------
`id` | string
`shape` | string
`data` | [CellData](CellData.md)
`position` | [NodeAllOfPosition](NodeAllOfPosition.md)
`size` | [NodeAllOfSize](NodeAllOfSize.md)
`angle` | number
`attrs` | [EdgeAttrs](EdgeAttrs.md)
`ports` | [PortConfiguration](PortConfiguration.md)
`parent` | string
`children` | Array&lt;string&gt;
`x` | number
`y` | number
`width` | number
`height` | number
`source` | [EdgeTerminal](EdgeTerminal.md)
`target` | [EdgeTerminal](EdgeTerminal.md)
`labels` | [Array&lt;EdgeLabel&gt;](EdgeLabel.md)
`vertices` | [Array&lt;Point&gt;](Point.md)
`router` | [EdgeRouter](EdgeRouter.md)
`connector` | [EdgeConnector](EdgeConnector.md)
`defaultLabel` | [EdgeLabel](EdgeLabel.md)

## Example

```typescript
import type { DfdDiagramAllOfCells } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": 37eaedfa-bf37-4996-8665-242fec34bbff,
  "shape": null,
  "data": null,
  "position": null,
  "size": null,
  "angle": null,
  "attrs": null,
  "ports": null,
  "parent": null,
  "children": null,
  "x": null,
  "y": null,
  "width": null,
  "height": null,
  "source": null,
  "target": null,
  "labels": null,
  "vertices": null,
  "router": null,
  "connector": null,
  "defaultLabel": null,
} satisfies DfdDiagramAllOfCells

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DfdDiagramAllOfCells
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


