
# ContentTokenInfo

Information about a linked delegated content provider token. Does not expose secret token material.

## Properties

Name | Type
------------ | -------------
`provider_id` | string
`provider_account_id` | string
`provider_account_label` | string
`scopes` | Array&lt;string&gt;
`status` | string
`expires_at` | Date
`last_refresh_at` | Date
`created_at` | Date

## Example

```typescript
import type { ContentTokenInfo } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "provider_id": confluence,
  "provider_account_id": 557058:1234-abcd,
  "provider_account_label": alice@example.com,
  "scopes": null,
  "status": null,
  "expires_at": null,
  "last_refresh_at": null,
  "created_at": null,
} satisfies ContentTokenInfo

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ContentTokenInfo
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


