
# AdminGroupListResponse

Paginated list of groups for administrative management

## Properties

Name | Type
------------ | -------------
`groups` | [Array&lt;AdminGroup&gt;](AdminGroup.md)
`total` | number
`limit` | number
`offset` | number

## Example

```typescript
import type { AdminGroupListResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "groups": null,
  "total": null,
  "limit": null,
  "offset": null,
} satisfies AdminGroupListResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as AdminGroupListResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


