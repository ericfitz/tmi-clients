
# IntrospectToken500Response


## Properties

Name | Type
------------ | -------------
`error` | string
`request_id` | string

## Example

```typescript
import type { IntrospectToken500Response } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "error": internal_server_error,
  "request_id": req_abc123xyz789,
} satisfies IntrospectToken500Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as IntrospectToken500Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


