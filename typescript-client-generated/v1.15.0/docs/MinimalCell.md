
# MinimalCell

Minimal diagram cell data for WebSocket collaboration updates

## Properties

Name | Type
------------ | -------------
`id` | string
`shape` | string
`parent` | string
`children` | Array&lt;string&gt;
`labels` | Array&lt;string&gt;
`metadata` | { [key: string]: string; }
`security_boundary` | boolean
`data_asset_ids` | Array&lt;string&gt;
`source` | [EdgeTerminal](EdgeTerminal.md)
`target` | [EdgeTerminal](EdgeTerminal.md)

## Example

```typescript
import type { MinimalCell } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "shape": null,
  "parent": null,
  "children": null,
  "labels": null,
  "metadata": null,
  "security_boundary": null,
  "data_asset_ids": null,
  "source": null,
  "target": null,
} satisfies MinimalCell

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as MinimalCell
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


