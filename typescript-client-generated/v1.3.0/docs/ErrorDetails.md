
# ErrorDetails

Additional context-specific error information

## Properties

Name | Type
------------ | -------------
`code` | string
`context` | { [key: string]: any; }
`suggestion` | string

## Example

```typescript
import type { ErrorDetails } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "code": COLLABORATION_SESSION_NOT_FOUND,
  "context": {"diagram_id":"550e8400-e29b-41d4-a716-446655440000","requested_operation":"end_session"},
  "suggestion": Start a collaboration session first using POST /diagrams/{id}/collaborate,
} satisfies ErrorDetails

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ErrorDetails
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


