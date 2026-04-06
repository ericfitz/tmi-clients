
# NodeAttrsText

Text/label styling attributes

## Properties

Name | Type
------------ | -------------
`text` | string
`fontSize` | number
`fill` | string
`fontFamily` | string
`refX` | number
`refY` | number
`refDx` | number
`refDy` | number
`textAnchor` | string
`textVerticalAnchor` | string

## Example

```typescript
import type { NodeAttrsText } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "text": null,
  "fontSize": null,
  "fill": null,
  "fontFamily": null,
  "refX": null,
  "refY": null,
  "refDx": null,
  "refDy": null,
  "textAnchor": null,
  "textVerticalAnchor": null,
} satisfies NodeAttrsText

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as NodeAttrsText
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


