
# AdminUserListResponse

Paginated list of users for administrative management

## Properties

Name | Type
------------ | -------------
`users` | [Array&lt;AdminUser&gt;](AdminUser.md)
`total` | number
`limit` | number
`offset` | number

## Example

```typescript
import type { AdminUserListResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "users": null,
  "total": null,
  "limit": null,
  "offset": null,
} satisfies AdminUserListResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as AdminUserListResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


