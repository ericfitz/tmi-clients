
# PickerTokenResponse

Response body for `POST /me/picker_tokens/{provider_id}`. Carries a short-lived access token and the public picker configuration values that the browser client needs to initialize the provider\'s picker widget.

## Properties

Name | Type
------------ | -------------
`access_token` | string
`expires_at` | Date
`developer_key` | string
`app_id` | string
`provider_config` | { [key: string]: string; }

## Example

```typescript
import type { PickerTokenResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "access_token": ya29.a0AfH6SMBxExample-token-string,
  "expires_at": 2026-04-19T12:34:56Z,
  "developer_key": AIzaSyB-1234example,
  "app_id": 123456789012,
  "provider_config": null,
} satisfies PickerTokenResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as PickerTokenResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


