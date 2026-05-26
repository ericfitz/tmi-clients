
# PickerRegistration

Client-provided registration for a picker-mediated provider attachment. Supplied when a user attaches a file to a threat model via a picker flow (Google Picker, Microsoft File Picker); the server stores these fields on the document and uses them to dispatch fetch and access-validation operations through the matching delegated source.

## Properties

Name | Type
------------ | -------------
`provider_id` | string
`file_id` | string
`mime_type` | string

## Example

```typescript
import type { PickerRegistration } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "provider_id": null,
  "file_id": null,
  "mime_type": null,
} satisfies PickerRegistration

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as PickerRegistration
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


