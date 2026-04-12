
# ProjectNote

Complete ProjectNote schema with server-generated fields

## Properties

Name | Type
------------ | -------------
`name` | string
`content` | string
`description` | string
`timmy_enabled` | boolean
`sharable` | boolean
`id` | string
`created_at` | Date
`modified_at` | Date

## Example

```typescript
import type { ProjectNote } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "name": Security Review Notes,
  "content": # Security Review

Findings from the quarterly review.,
  "description": Notes from the quarterly security review meeting,
  "timmy_enabled": true,
  "sharable": true,
  "id": null,
  "created_at": null,
  "modified_at": null,
} satisfies ProjectNote

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ProjectNote
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


