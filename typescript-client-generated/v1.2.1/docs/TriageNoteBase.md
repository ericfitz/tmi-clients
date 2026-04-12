
# TriageNoteBase

Base fields for TriageNote (user-writable only)

## Properties

Name | Type
------------ | -------------
`name` | string
`content` | string

## Example

```typescript
import type { TriageNoteBase } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "content": null,
} satisfies TriageNoteBase

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as TriageNoteBase
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


