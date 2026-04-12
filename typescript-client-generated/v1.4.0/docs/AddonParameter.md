
# AddonParameter

Typed parameter declaration for an add-on, used to drive client UI generation

## Properties

Name | Type
------------ | -------------
`name` | string
`type` | string
`description` | string
`required` | boolean
`enum_values` | Array&lt;string&gt;
`default_value` | string
`metadata_key` | string
`number_min` | number
`number_max` | number
`string_max_length` | number
`string_validation_regex` | string

## Example

```typescript
import type { AddonParameter } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "type": null,
  "description": null,
  "required": null,
  "enum_values": null,
  "default_value": null,
  "metadata_key": null,
  "number_min": null,
  "number_max": null,
  "string_max_length": null,
  "string_validation_regex": null,
} satisfies AddonParameter

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as AddonParameter
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


