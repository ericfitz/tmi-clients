
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


