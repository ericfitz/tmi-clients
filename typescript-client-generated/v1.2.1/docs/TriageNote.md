
# TriageNote

Complete TriageNote schema with server-generated fields

## Properties

Name | Type
------------ | -------------
`name` | string
`content` | string
`id` | number
`created_at` | Date
`created_by` | object
`modified_at` | Date
`modified_by` | object

## Example

```typescript
import type { TriageNote } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "content": null,
  "id": null,
  "created_at": null,
  "created_by": null,
  "modified_at": null,
  "modified_by": null,
} satisfies TriageNote

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as TriageNote
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


