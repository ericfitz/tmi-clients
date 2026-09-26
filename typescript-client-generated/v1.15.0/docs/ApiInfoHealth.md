
# ApiInfoHealth

Detailed health status of system components. Only present when status is DEGRADED.

## Properties

Name | Type
------------ | -------------
`database` | [ComponentHealth](ComponentHealth.md)
`redis` | [ComponentHealth](ComponentHealth.md)

## Example

```typescript
import type { ApiInfoHealth } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "database": null,
  "redis": null,
} satisfies ApiInfoHealth

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ApiInfoHealth
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


