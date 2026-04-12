
# CreateAdminGroupRequest

Request body for creating a provider-independent group

## Properties

Name | Type
------------ | -------------
`group_name` | string
`name` | string
`description` | string

## Example

```typescript
import type { CreateAdminGroupRequest } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "group_name": null,
  "name": null,
  "description": null,
} satisfies CreateAdminGroupRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CreateAdminGroupRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


