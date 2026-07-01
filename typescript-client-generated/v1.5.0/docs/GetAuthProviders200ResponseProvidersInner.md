
# GetAuthProviders200ResponseProvidersInner


## Properties

Name | Type
------------ | -------------
`id` | string
`name` | string
`icon` | string
`auth_url` | string
`token_url` | string
`redirect_uri` | string
`client_id` | string

## Example

```typescript
import type { GetAuthProviders200ResponseProvidersInner } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "name": null,
  "icon": null,
  "auth_url": null,
  "token_url": null,
  "redirect_uri": null,
  "client_id": null,
} satisfies GetAuthProviders200ResponseProvidersInner

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GetAuthProviders200ResponseProvidersInner
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


