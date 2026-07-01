
# ListTriageNotesResponse

Paginated list of triage notes

## Properties

Name | Type
------------ | -------------
`triage_notes` | [Array&lt;TriageNoteListItem&gt;](TriageNoteListItem.md)
`total` | number
`limit` | number
`offset` | number

## Example

```typescript
import type { ListTriageNotesResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "triage_notes": [{"id":1,"name":"Initial Triage Assessment","created_at":"2026-02-08T14:30:00Z"}],
  "total": 3,
  "limit": 20,
  "offset": 0,
} satisfies ListTriageNotesResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListTriageNotesResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


