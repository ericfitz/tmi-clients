
# TokenRevocationRequest

OAuth 2.0 token revocation request per RFC 7009

## Properties

Name | Type
------------ | -------------
`token` | string
`token_type_hint` | string
`client_id` | string
`client_secret` | string

## Example

```typescript
import type { TokenRevocationRequest } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "token": eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...,
  "token_type_hint": access_token,
  "client_id": tmi_cc_abc123...,
  "client_secret": secret123...,
} satisfies TokenRevocationRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as TokenRevocationRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


