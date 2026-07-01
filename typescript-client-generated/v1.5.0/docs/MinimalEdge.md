
# MinimalEdge

Minimal edge representation without visual styling or routing information

## Properties

Name | Type
------------ | -------------
`id` | string
`shape` | string
`source` | [EdgeTerminal](EdgeTerminal.md)
`target` | [EdgeTerminal](EdgeTerminal.md)
`labels` | Array&lt;string&gt;
`metadata` | { [key: string]: string; }
`data_asset_ids` | Array&lt;string&gt;

## Example

```typescript
import type { MinimalEdge } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "shape": null,
  "source": null,
  "target": null,
  "labels": null,
  "metadata": null,
  "data_asset_ids": null,
} satisfies MinimalEdge

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as MinimalEdge
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


