
# GetProviderGroups200Response


## Properties

Name | Type
------------ | -------------
`idp` | string
`groups` | [Array&lt;GetProviderGroups200ResponseGroupsInner&gt;](GetProviderGroups200ResponseGroupsInner.md)

## Example

```typescript
import type { GetProviderGroups200Response } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "idp": azure,
  "groups": [{"name":"admins","display_name":"Administrators","used_in_authorizations":true},{"name":"developers","display_name":"Development Team","used_in_authorizations":false},{"name":"users","display_name":"General Users","used_in_authorizations":false}],
} satisfies GetProviderGroups200Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GetProviderGroups200Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


