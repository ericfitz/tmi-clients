
# ClientConfigLimits

System limits and quotas

## Properties

Name | Type
------------ | -------------
`max_file_upload_mb` | number
`max_diagram_participants` | number

## Example

```typescript
import type { ClientConfigLimits } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "max_file_upload_mb": null,
  "max_diagram_participants": null,
} satisfies ClientConfigLimits

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ClientConfigLimits
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


