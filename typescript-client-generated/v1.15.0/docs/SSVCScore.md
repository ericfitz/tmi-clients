
# SSVCScore

SSVC (Stakeholder-Specific Vulnerability Categorization) assessment result

## Properties

Name | Type
------------ | -------------
`vector` | string
`decision` | string
`methodology` | string

## Example

```typescript
import type { SSVCScore } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "vector": null,
  "decision": null,
  "methodology": null,
} satisfies SSVCScore

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SSVCScore
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


