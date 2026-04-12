
# BaseDiagram

Base diagram object with common properties - used for API responses

## Properties

Name | Type
------------ | -------------
`id` | string
`name` | string
`type` | string
`created_at` | Date
`modified_at` | Date
`metadata` | [Array&lt;Metadata&gt;](Metadata.md)
`update_vector` | number
`image` | [BaseDiagramImage](BaseDiagramImage.md)
`description` | string
`include_in_report` | boolean
`timmy_enabled` | boolean
`deleted_at` | Date
`color_palette` | [Array&lt;ColorPaletteEntry&gt;](ColorPaletteEntry.md)

## Example

```typescript
import type { BaseDiagram } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "name": null,
  "type": null,
  "created_at": null,
  "modified_at": null,
  "metadata": null,
  "update_vector": null,
  "image": null,
  "description": null,
  "include_in_report": null,
  "timmy_enabled": null,
  "deleted_at": null,
  "color_palette": null,
} satisfies BaseDiagram

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BaseDiagram
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


