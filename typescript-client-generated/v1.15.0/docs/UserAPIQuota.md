
# UserAPIQuota

API rate limit and quota configuration for a user

## Properties

Name | Type
------------ | -------------
`user_id` | string
`max_requests_per_minute` | number
`max_requests_per_hour` | number
`created_at` | Date
`modified_at` | Date

## Example

```typescript
import type { UserAPIQuota } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "user_id": null,
  "max_requests_per_minute": null,
  "max_requests_per_hour": null,
  "created_at": null,
  "modified_at": null,
} satisfies UserAPIQuota

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as UserAPIQuota
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


