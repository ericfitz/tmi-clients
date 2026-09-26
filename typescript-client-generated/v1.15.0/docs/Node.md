
# Node

Diagram node representing a process, data store, external entity, or trust boundary

## Properties

Name | Type
------------ | -------------
`shape` | string
`position` | [NodeAllOfPosition](NodeAllOfPosition.md)
`size` | [NodeAllOfSize](NodeAllOfSize.md)
`angle` | number
`attrs` | [NodeAttrs](NodeAttrs.md)
`ports` | [PortConfiguration](PortConfiguration.md)
`parent` | string
`children` | Array&lt;string&gt;
`x` | number
`y` | number
`width` | number
`height` | number

## Example

```typescript
import type { Node } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "shape": null,
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
} satisfies Node

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Node
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


