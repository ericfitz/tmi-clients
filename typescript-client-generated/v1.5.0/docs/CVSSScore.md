
# CVSSScore

CVSS vector and score pair

## Properties

Name | Type
------------ | -------------
`vector` | string
`score` | number

## Example

```typescript
import type { CVSSScore } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "vector": null,
  "score": null,
} satisfies CVSSScore

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CVSSScore
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


