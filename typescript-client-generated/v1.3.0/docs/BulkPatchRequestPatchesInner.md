
# BulkPatchRequestPatchesInner


## Properties

Name | Type
------------ | -------------
`id` | string
`operations` | [Array&lt;JsonPatchDocumentInner&gt;](JsonPatchDocumentInner.md)

## Example

```typescript
import type { BulkPatchRequestPatchesInner } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "operations": null,
} satisfies BulkPatchRequestPatchesInner

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BulkPatchRequestPatchesInner
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


