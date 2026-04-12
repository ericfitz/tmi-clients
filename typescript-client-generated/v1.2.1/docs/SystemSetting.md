
# SystemSetting

A system-wide configuration setting

## Properties

Name | Type
------------ | -------------
`key` | string
`value` | string
`type` | string
`description` | string
`modified_at` | Date
`modified_by` | string

## Example

```typescript
import type { SystemSetting } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "key": null,
  "value": null,
  "type": null,
  "description": null,
  "modified_at": null,
  "modified_by": null,
} satisfies SystemSetting

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SystemSetting
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


