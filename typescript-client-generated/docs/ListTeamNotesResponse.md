
# ListTeamNotesResponse

Paginated list of team notes

## Properties

Name | Type
------------ | -------------
`notes` | [Array&lt;TeamNoteListItem&gt;](TeamNoteListItem.md)
`total` | number
`limit` | number
`offset` | number

## Example

```typescript
import type { ListTeamNotesResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "notes": [{"id":"550e8400-e29b-41d4-a716-446655440001","name":"Security Review Notes","description":"Notes from quarterly security review","created_at":"2026-01-15T10:30:00Z","modified_at":"2026-01-15T10:30:00Z"}],
  "total": 5,
  "limit": 20,
  "offset": 0,
} satisfies ListTeamNotesResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListTeamNotesResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


