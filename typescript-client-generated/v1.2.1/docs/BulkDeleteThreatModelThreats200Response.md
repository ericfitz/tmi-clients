
# BulkDeleteThreatModelThreats200Response


## Properties

Name | Type
------------ | -------------
`deleted_count` | number
`deleted_ids` | Array&lt;string&gt;

## Example

```typescript
import type { BulkDeleteThreatModelThreats200Response } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "deleted_count": 3,
  "deleted_ids": ["550e8400-e29b-41d4-a716-446655440001","550e8400-e29b-41d4-a716-446655440002"],
} satisfies BulkDeleteThreatModelThreats200Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BulkDeleteThreatModelThreats200Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


