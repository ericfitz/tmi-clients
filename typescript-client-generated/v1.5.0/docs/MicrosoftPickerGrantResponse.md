
# MicrosoftPickerGrantResponse

Response body for the Microsoft picker-grant endpoint. Returns the Graph permission id created by the grant call (informational; not needed for subsequent fetches).

## Properties

Name | Type
------------ | -------------
`permission_id` | string
`drive_id` | string
`item_id` | string

## Example

```typescript
import type { MicrosoftPickerGrantResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "permission_id": null,
  "drive_id": null,
  "item_id": null,
} satisfies MicrosoftPickerGrantResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as MicrosoftPickerGrantResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


