
# RepositoryBase

Base fields for Repository (user-writable only)

## Properties

Name | Type
------------ | -------------
`name` | string
`description` | string
`type` | string
`parameters` | [RepositoryBaseParameters](RepositoryBaseParameters.md)
`uri` | string
`include_in_report` | boolean
`timmy_enabled` | boolean

## Example

```typescript
import type { RepositoryBase } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "description": null,
  "type": null,
  "parameters": null,
  "uri": null,
  "include_in_report": null,
  "timmy_enabled": null,
} satisfies RepositoryBase

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as RepositoryBase
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


