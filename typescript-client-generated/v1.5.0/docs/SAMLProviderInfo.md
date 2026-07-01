
# SAMLProviderInfo

SAML identity provider configuration and metadata

## Properties

Name | Type
------------ | -------------
`id` | string
`name` | string
`icon` | string
`auth_url` | string
`metadata_url` | string
`entity_id` | string
`acs_url` | string
`slo_url` | string
`initialized` | boolean

## Example

```typescript
import type { SAMLProviderInfo } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "name": null,
  "icon": null,
  "auth_url": null,
  "metadata_url": null,
  "entity_id": null,
  "acs_url": null,
  "slo_url": null,
  "initialized": null,
} satisfies SAMLProviderInfo

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SAMLProviderInfo
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


