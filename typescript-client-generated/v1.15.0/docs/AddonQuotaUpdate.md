
# AddonQuotaUpdate

Configuration update for addon invocation quotas

## Properties

Name | Type
------------ | -------------
`max_active_invocations` | number
`max_invocations_per_hour` | number

## Example

```typescript
import type { AddonQuotaUpdate } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "max_active_invocations": 10,
  "max_invocations_per_hour": 1000,
} satisfies AddonQuotaUpdate

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as AddonQuotaUpdate
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


