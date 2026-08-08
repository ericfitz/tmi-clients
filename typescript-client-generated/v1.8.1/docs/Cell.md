
# Cell

Base schema for all diagram cells (nodes and edges). Contains common properties shared by Node and Edge types.

## Properties

Name | Type
------------ | -------------
`id` | string
`shape` | string
`data` | [CellData](CellData.md)

## Example

```typescript
import type { Cell } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": 37eaedfa-bf37-4996-8665-242fec34bbff,
  "shape": process,
  "data": null,
} satisfies Cell

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Cell
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


