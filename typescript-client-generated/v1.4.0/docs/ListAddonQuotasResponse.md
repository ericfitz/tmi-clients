
# ListAddonQuotasResponse

Paginated list of addon quotas

## Properties

Name | Type
------------ | -------------
`quotas` | [Array&lt;AddonInvocationQuota&gt;](AddonInvocationQuota.md)
`total` | number
`limit` | number
`offset` | number

## Example

```typescript
import type { ListAddonQuotasResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "quotas": [{"owner_id":"550e8400-e29b-41d4-a716-446655440000","max_active_invocations":10,"max_invocations_per_hour":100,"created_at":"2024-01-01T00:00:00Z","modified_at":"2024-01-01T00:00:00Z"}],
  "total": 8,
  "limit": 20,
  "offset": 0,
} satisfies ListAddonQuotasResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListAddonQuotasResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


