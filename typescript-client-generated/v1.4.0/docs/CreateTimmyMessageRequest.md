
# CreateTimmyMessageRequest

Request body for creating a message in a Timmy chat session

## Properties

Name | Type
------------ | -------------
`content` | string

## Example

```typescript
import type { CreateTimmyMessageRequest } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "content": null,
} satisfies CreateTimmyMessageRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CreateTimmyMessageRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


