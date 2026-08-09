
# TeamProjectNoteBase

Base fields for TeamProjectNote (user-writable only)

## Properties

Name | Type
------------ | -------------
`name` | string
`content` | string
`description` | string
`timmy_enabled` | boolean
`sharable` | boolean

## Example

```typescript
import type { TeamProjectNoteBase } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "name": Security Review Notes,
  "content": # Security Review

Findings from the quarterly review.,
  "description": Notes from the quarterly security review meeting,
  "timmy_enabled": true,
  "sharable": true,
} satisfies TeamProjectNoteBase

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as TeamProjectNoteBase
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


