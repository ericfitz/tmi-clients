
# ListNotesResponse

Paginated list of notes

## Properties

Name | Type
------------ | -------------
`notes` | [Array&lt;NoteListItem&gt;](NoteListItem.md)
`total` | number
`limit` | number
`offset` | number

## Example

```typescript
import type { ListNotesResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "notes": [{"id":"ff0e8400-e29b-41d4-a716-44665544000a","name":"Security Review Notes","created_at":"2024-01-17T14:30:00Z","modified_at":"2024-01-17T15:00:00Z"}],
  "total": 12,
  "limit": 20,
  "offset": 0,
} satisfies ListNotesResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListNotesResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


