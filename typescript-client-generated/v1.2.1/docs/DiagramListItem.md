
# DiagramListItem

Summary diagram object for GET /diagrams list endpoints. Excludes large fields (cells) for performance. Includes image for thumbnail rendering and description for display. Full diagram details available via GET /diagrams/{id} which returns DfdDiagram.

## Properties

Name | Type
------------ | -------------
`id` | string
`name` | string
`type` | string
`description` | string
`created_at` | Date
`modified_at` | Date
`image` | [DiagramListItemImage](DiagramListItemImage.md)
`include_in_report` | boolean

## Example

```typescript
import type { DiagramListItem } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "name": null,
  "type": null,
  "description": null,
  "created_at": null,
  "modified_at": null,
  "image": null,
  "include_in_report": null,
} satisfies DiagramListItem

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DiagramListItem
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


