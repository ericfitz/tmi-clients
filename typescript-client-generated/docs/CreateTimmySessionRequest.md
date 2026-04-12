
# CreateTimmySessionRequest

Optional request body for creating a Timmy chat session

## Properties

Name | Type
------------ | -------------
`title` | string

## Example

```typescript
import type { CreateTimmySessionRequest } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "title": null,
} satisfies CreateTimmySessionRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CreateTimmySessionRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


