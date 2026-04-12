
# TriageNoteInput

Input schema for creating a TriageNote

## Properties

Name | Type
------------ | -------------
`name` | string
`content` | string

## Example

```typescript
import type { TriageNoteInput } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "content": null,
} satisfies TriageNoteInput

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as TriageNoteInput
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


