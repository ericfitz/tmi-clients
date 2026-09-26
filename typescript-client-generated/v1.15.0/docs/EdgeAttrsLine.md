
# EdgeAttrsLine

Line styling attributes

## Properties

Name | Type
------------ | -------------
`stroke` | string
`strokeWidth` | number
`strokeDasharray` | string
`targetMarker` | [EdgeAttrsLineTargetMarker](EdgeAttrsLineTargetMarker.md)
`sourceMarker` | [EdgeAttrsLineSourceMarker](EdgeAttrsLineSourceMarker.md)

## Example

```typescript
import type { EdgeAttrsLine } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "stroke": null,
  "strokeWidth": null,
  "strokeDasharray": null,
  "targetMarker": null,
  "sourceMarker": null,
} satisfies EdgeAttrsLine

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as EdgeAttrsLine
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


