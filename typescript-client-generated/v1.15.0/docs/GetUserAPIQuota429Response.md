
# GetUserAPIQuota429Response


## Properties

Name | Type
------------ | -------------
`error` | string
`retry_after` | number

## Example

```typescript
import type { GetUserAPIQuota429Response } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "error": rate_limit_exceeded,
  "retry_after": 60,
} satisfies GetUserAPIQuota429Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GetUserAPIQuota429Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


