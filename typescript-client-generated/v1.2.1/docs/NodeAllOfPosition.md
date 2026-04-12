
# NodeAllOfPosition

Node position in X6 nested format. Use either this with size object OR use flat x/y/width/height properties.

## Properties

Name | Type
------------ | -------------
`x` | number
`y` | number

## Example

```typescript
import type { NodeAllOfPosition } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "x": null,
  "y": null,
} satisfies NodeAllOfPosition

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as NodeAllOfPosition
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


