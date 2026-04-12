
# ExchangeOAuthCodeRequest


## Properties

Name | Type
------------ | -------------
`grant_type` | string
`code` | string
`state` | string
`redirect_uri` | string
`code_verifier` | string
`client_id` | string
`client_secret` | string
`refresh_token` | string

## Example

```typescript
import type { ExchangeOAuthCodeRequest } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "grant_type": authorization_code,
  "code": 0AX4XfWiXY2BZ_example_auth_code_from_google,
  "state": random_state_value_abc123,
  "redirect_uri": https://your-web-app.com/oauth2/callback,
  "code_verifier": dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk,
  "client_id": tmi_cc_AbCdEf123456,
  "client_secret": secret_value,
  "refresh_token": refresh_token_value,
} satisfies ExchangeOAuthCodeRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ExchangeOAuthCodeRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


