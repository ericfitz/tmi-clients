
# ListTimmySessionsResponse

Paginated list of Timmy chat sessions

## Properties

Name | Type
------------ | -------------
`sessions` | [Array&lt;TimmyChatSession&gt;](TimmyChatSession.md)
`total` | number
`limit` | number
`offset` | number

## Example

```typescript
import type { ListTimmySessionsResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "sessions": null,
  "total": 5,
  "limit": 20,
  "offset": 0,
} satisfies ListTimmySessionsResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListTimmySessionsResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


