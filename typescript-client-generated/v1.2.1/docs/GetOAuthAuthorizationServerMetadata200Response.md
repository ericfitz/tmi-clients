
# GetOAuthAuthorizationServerMetadata200Response


## Properties

Name | Type
------------ | -------------
`issuer` | string
`authorization_endpoint` | string
`token_endpoint` | string
`introspection_endpoint` | string
`response_types_supported` | Array&lt;string&gt;
`grant_types_supported` | Array&lt;string&gt;
`token_endpoint_auth_methods_supported` | Array&lt;string&gt;

## Example

```typescript
import type { GetOAuthAuthorizationServerMetadata200Response } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "issuer": http://localhost:8080,
  "authorization_endpoint": http://localhost:8080/oauth2/authorize,
  "token_endpoint": http://localhost:8080/oauth2/token,
  "introspection_endpoint": http://localhost:8080/oauth2/introspect,
  "response_types_supported": ["code","token","id_token"],
  "grant_types_supported": ["authorization_code","implicit","refresh_token"],
  "token_endpoint_auth_methods_supported": ["client_secret_post","none"],
} satisfies GetOAuthAuthorizationServerMetadata200Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GetOAuthAuthorizationServerMetadata200Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


