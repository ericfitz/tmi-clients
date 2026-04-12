
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
  "memory_used_bytes": null,
  "memory_budget_bytes": null,
  "memory_utilization_pct": null,
  "loaded_indexes": null,
  "active_sessions": null,
  "evictions_total": null,
  "evictions_pressure": null,
  "sessions_rejected_total": null,
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


