
# GetOpenIDConfiguration200Response


## Properties

Name | Type
------------ | -------------
`issuer` | string
`authorization_endpoint` | string
`token_endpoint` | string
`userinfo_endpoint` | string
`jwks_uri` | string
`response_types_supported` | Array&lt;string&gt;
`subject_types_supported` | Array&lt;string&gt;
`id_token_signing_alg_values_supported` | Array&lt;string&gt;
`scopes_supported` | Array&lt;string&gt;
`claims_supported` | Array&lt;string&gt;
`introspection_endpoint` | string
`code_challenge_methods_supported` | Array&lt;string&gt;
`grant_types_supported` | Array&lt;string&gt;
`revocation_endpoint` | string
`token_endpoint_auth_methods_supported` | Array&lt;string&gt;

## Example

```typescript
import type { GetOpenIDConfiguration200Response } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "issuer": http://localhost:8080,
  "authorization_endpoint": http://localhost:8080/oauth2/authorize,
  "token_endpoint": http://localhost:8080/oauth2/token,
  "userinfo_endpoint": http://localhost:8080/oauth2/userinfo,
  "jwks_uri": http://localhost:8080/.well-known/jwks.json,
  "response_types_supported": ["code","token","id_token","code token","code id_token","token id_token","code token id_token"],
  "subject_types_supported": ["public"],
  "id_token_signing_alg_values_supported": ["HS256"],
  "scopes_supported": ["openid","email","profile"],
  "claims_supported": ["sub","email","email_verified","name","given_name","family_name","picture","locale"],
  "introspection_endpoint": http://localhost:8080/oauth2/introspect,
  "code_challenge_methods_supported": ["S256"],
  "grant_types_supported": ["authorization_code","refresh_token","client_credentials"],
  "revocation_endpoint": http://localhost:8080/oauth2/revoke,
  "token_endpoint_auth_methods_supported": ["client_secret_post","none"],
} satisfies GetOpenIDConfiguration200Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GetOpenIDConfiguration200Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


