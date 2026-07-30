
# NodeAttrs

Visual attributes for a node

## Properties

Name | Type
------------ | -------------
`body` | [NodeAttrsBody](NodeAttrsBody.md)
`text` | [NodeAttrsText](NodeAttrsText.md)

## Example

```typescript
import type { NodeAttrs } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "body": null,
  "text": null,
} satisfies NodeAttrs

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as NodeAttrs
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


