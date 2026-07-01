
# GetAuthProviders200Response


## Properties

Name | Type
------------ | -------------
`providers` | [Array&lt;GetAuthProviders200ResponseProvidersInner&gt;](GetAuthProviders200ResponseProvidersInner.md)

## Example

```typescript
import type { GetAuthProviders200Response } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "providers": [{"id":"tmi","name":"TMI Development","icon":"shield","auth_url":"http://localhost:8080/oauth2/authorize?idp=tmi","token_url":"http://localhost:8080/oauth2/token","redirect_uri":"http://localhost:8079/callback","client_id":"tmi-client"}],
} satisfies GetAuthProviders200Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GetAuthProviders200Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


