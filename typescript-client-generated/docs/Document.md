
# Document

Complete Document schema with server-generated fields

## Properties

Name | Type
------------ | -------------
`name` | string
`description` | string
`uri` | string
`include_in_report` | boolean
`timmy_enabled` | boolean
`id` | string
`metadata` | [Array&lt;Metadata&gt;](Metadata.md)
`created_at` | Date
`modified_at` | Date
`deleted_at` | Date
`access_status` | string
`content_source` | string

## Example

```typescript
import type { Document } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "description": null,
  "uri": null,
  "include_in_report": null,
  "timmy_enabled": null,
  "id": null,
  "metadata": null,
  "created_at": null,
  "modified_at": null,
  "deleted_at": null,
  "access_status": null,
  "content_source": google_drive,
} satisfies Document

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Document
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


