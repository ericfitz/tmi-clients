
# MicrosoftPickerGrantRequest

Request body for the Microsoft picker-grant endpoint. Carries the drive id and item id of the picked file.

## Properties

Name | Type
------------ | -------------
`drive_id` | string
`item_id` | string

## Example

```typescript
import type { MicrosoftPickerGrantRequest } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "drive_id": null,
  "item_id": null,
} satisfies MicrosoftPickerGrantRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as MicrosoftPickerGrantRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


