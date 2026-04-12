
# BaseDiagramInput

Base diagram input for PUT/PATCH requests - excludes readOnly server-managed fields

## Properties

Name | Type
------------ | -------------
`name` | string
`type` | string
`metadata` | [Array&lt;Metadata&gt;](Metadata.md)
`image` | [BaseDiagramImage](BaseDiagramImage.md)
`description` | string
`include_in_report` | boolean

## Example

```typescript
import type { BaseDiagramInput } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "type": null,
  "metadata": null,
  "image": null,
  "description": null,
  "include_in_report": null,
} satisfies BaseDiagramInput

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BaseDiagramInput
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


