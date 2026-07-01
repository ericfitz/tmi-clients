
# EdgeTerminal

Connection point for an edge (source or target)

## Properties

Name | Type
------------ | -------------
`cell` | string
`port` | string

## Example

```typescript
import type { EdgeTerminal } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "cell": null,
  "port": null,
} satisfies EdgeTerminal

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as EdgeTerminal
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


