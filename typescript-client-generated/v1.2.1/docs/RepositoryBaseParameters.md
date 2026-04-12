
# RepositoryBaseParameters

repo-specific parameters for retrieving the source

## Properties

Name | Type
------------ | -------------
`refType` | string
`refValue` | string
`subPath` | string

## Example

```typescript
import type { RepositoryBaseParameters } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "refType": null,
  "refValue": null,
  "subPath": null,
} satisfies RepositoryBaseParameters

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as RepositoryBaseParameters
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


