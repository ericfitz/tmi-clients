
# ListSAMLUsers200ResponseUsersInner


## Properties

Name | Type
------------ | -------------
`internal_uuid` | string
`email` | string
`name` | string
`last_login` | Date

## Example

```typescript
import type { ListSAMLUsers200ResponseUsersInner } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "internal_uuid": 123e4567-e89b-12d3-a456-426614174000,
  "email": alice@example.com,
  "name": Alice Smith,
  "last_login": 2026-01-15T10:30Z,
} satisfies ListSAMLUsers200ResponseUsersInner

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListSAMLUsers200ResponseUsersInner
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


