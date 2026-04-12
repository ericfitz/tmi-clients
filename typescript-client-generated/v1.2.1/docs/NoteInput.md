
# NoteInput

Input schema for creating or updating Note

## Properties

Name | Type
------------ | -------------
`name` | string
`content` | string
`description` | string
`include_in_report` | boolean

## Example

```typescript
import type { NoteInput } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "content": null,
  "description": null,
  "include_in_report": null,
} satisfies NoteInput

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as NoteInput
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


