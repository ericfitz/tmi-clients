
# ListTimmyMessagesResponse

Paginated list of Timmy chat messages

## Properties

Name | Type
------------ | -------------
`messages` | [Array&lt;TimmyChatMessage&gt;](TimmyChatMessage.md)
`total` | number
`limit` | number
`offset` | number

## Example

```typescript
import type { ListTimmyMessagesResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "messages": null,
  "total": 42,
  "limit": 20,
  "offset": 0,
} satisfies ListTimmyMessagesResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListTimmyMessagesResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


