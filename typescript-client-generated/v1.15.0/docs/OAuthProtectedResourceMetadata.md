
# OAuthProtectedResourceMetadata

OAuth 2.0 protected resource metadata as defined in RFC 9728

## Properties

Name | Type
------------ | -------------
`resource` | string
`scopes_supported` | Array&lt;string&gt;
`authorization_servers` | Array&lt;string&gt;
`jwks_uri` | string
`bearer_methods_supported` | Array&lt;string&gt;
`resource_name` | string
`resource_documentation` | string
`tls_client_certificate_bound_access_tokens` | boolean

## Example

```typescript
import type { OAuthProtectedResourceMetadata } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "resource": http://localhost:8080,
  "scopes_supported": ["openid","email","profile"],
  "authorization_servers": ["http://localhost:8080"],
  "jwks_uri": http://localhost:8080/.well-known/jwks.json,
  "bearer_methods_supported": ["header","body","query"],
  "resource_name": TMI (Threat Modeling Improved) API,
  "resource_documentation": https://github.com/ericfitz/tmi,
  "tls_client_certificate_bound_access_tokens": false,
} satisfies OAuthProtectedResourceMetadata

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as OAuthProtectedResourceMetadata
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


