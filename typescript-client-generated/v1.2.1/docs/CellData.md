
# CellData

Flexible data storage compatible with X6, with reserved metadata namespace

## Properties

Name | Type
------------ | -------------
`_metadata` | [Array&lt;Metadata&gt;](Metadata.md)
`security_boundary` | boolean
`data_assets` | Set&lt;string&gt;

## Example

```typescript
import type { CellData } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "_metadata": null,
  "security_boundary": null,
  "data_assets": null,
} satisfies CellData

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CellData
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


