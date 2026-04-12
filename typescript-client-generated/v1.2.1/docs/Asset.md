
# Asset

Complete Asset schema with server-generated fields

## Properties

Name | Type
------------ | -------------
`name` | string
`description` | string
`type` | string
`criticality` | string
`classification` | Array&lt;string&gt;
`sensitivity` | string
`include_in_report` | boolean
`id` | string
`metadata` | [Array&lt;Metadata&gt;](Metadata.md)
`created_at` | Date
`modified_at` | Date

## Example

```typescript
import type { Asset } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "description": null,
  "type": null,
  "criticality": null,
  "classification": null,
  "sensitivity": null,
  "include_in_report": null,
  "id": null,
  "metadata": null,
  "created_at": null,
  "modified_at": null,
} satisfies Asset

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Asset
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


