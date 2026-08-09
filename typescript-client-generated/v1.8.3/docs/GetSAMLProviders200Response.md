
# GetSAMLProviders200Response


## Properties

Name | Type
------------ | -------------
`providers` | [Array&lt;SAMLProviderInfo&gt;](SAMLProviderInfo.md)

## Example

```typescript
import type { GetSAMLProviders200Response } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "providers": [{"id":"okta","name":"Okta","icon":"okta","auth_url":"http://localhost:8080/saml/okta/login","metadata_url":"http://localhost:8080/saml/okta/metadata","entity_id":"urn:example:tmi","acs_url":"http://localhost:8080/saml/acs","initialized":true}],
} satisfies GetSAMLProviders200Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GetSAMLProviders200Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


