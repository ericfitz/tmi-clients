
# CreateDiagramRequest

Request body for creating a new diagram - only includes client-provided fields

## Properties

Name | Type
------------ | -------------
`name` | string
`type` | string

## Example

```typescript
import type { CreateDiagramRequest } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "type": null,
} satisfies CreateDiagramRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CreateDiagramRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


