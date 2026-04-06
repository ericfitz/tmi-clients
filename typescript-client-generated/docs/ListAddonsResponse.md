
# ListAddonsResponse

Paginated list of registered addons

## Properties

Name | Type
------------ | -------------
`addons` | [Array&lt;AddonResponse&gt;](AddonResponse.md)
`total` | number
`limit` | number
`offset` | number

## Example

```typescript
import type { ListAddonsResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "addons": null,
  "total": null,
  "limit": null,
  "offset": null,
} satisfies ListAddonsResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListAddonsResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


