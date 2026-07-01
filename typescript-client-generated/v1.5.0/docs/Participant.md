
# Participant

A participant in a collaboration session

## Properties

Name | Type
------------ | -------------
`user` | [User](User.md)
`last_activity` | Date
`permissions` | string

## Example

```typescript
import type { Participant } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "user": null,
  "last_activity": null,
  "permissions": null,
} satisfies Participant

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Participant
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


