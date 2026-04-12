
# ReencryptSystemSettings200Response


## Properties

Name | Type
------------ | -------------
`reencrypted` | number
`errors` | [Array&lt;ReencryptSystemSettings200ResponseErrorsInner&gt;](ReencryptSystemSettings200ResponseErrorsInner.md)
`total` | number

## Example

```typescript
import type { ReencryptSystemSettings200Response } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "reencrypted": 8,
  "errors": [{"key":"smtp.password","error":"decryption failed: invalid key"}],
  "total": 8,
} satisfies ReencryptSystemSettings200Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ReencryptSystemSettings200Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


