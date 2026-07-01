
# TimmyStatusResponse

Timmy AI assistant system status

## Properties

Name | Type
------------ | -------------
`memory_used_bytes` | number
`memory_budget_bytes` | number
`memory_utilization_pct` | number
`loaded_indexes` | number
`active_sessions` | number
`evictions_total` | number
`evictions_pressure` | number
`sessions_rejected_total` | number

## Example

```typescript
import type { TimmyStatusResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "memory_used_bytes": 104857600,
  "memory_budget_bytes": 1073741824,
  "memory_utilization_pct": 9.77,
  "loaded_indexes": 3,
  "active_sessions": 2,
  "evictions_total": 0,
  "evictions_pressure": 0,
  "sessions_rejected_total": 0,
} satisfies TimmyStatusResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as TimmyStatusResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


