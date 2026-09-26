
# AddonInvocationQuota

Addon invocation quota for a user

## Properties

Name | Type
------------ | -------------
`owner_id` | string
`max_active_invocations` | number
`max_invocations_per_hour` | number
`created_at` | Date
`modified_at` | Date

## Example

```typescript
import type { AddonInvocationQuota } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "owner_id": null,
  "max_active_invocations": null,
  "max_invocations_per_hour": null,
  "created_at": null,
  "modified_at": null,
} satisfies AddonInvocationQuota

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as AddonInvocationQuota
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


