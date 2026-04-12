
# DocumentInput

Input schema for creating or updating Document

## Properties

Name | Type
------------ | -------------
`name` | string
`description` | string
`uri` | string
`include_in_report` | boolean

## Example

```typescript
import type { DocumentInput } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "description": null,
  "uri": null,
  "include_in_report": null,
} satisfies DocumentInput

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DocumentInput
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


