
# ContentProvider


## Properties

Name | Type
------------ | -------------
`id` | string
`name` | string
`kind` | string
`icon` | string
`picker_config` | { [key: string]: string; }

## Example

```typescript
import type { ContentProvider } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": google_workspace,
  "name": null,
  "kind": null,
  "icon": null,
  "picker_config": {"client_id":"1234567890-abc.apps.googleusercontent.com","developer_key":"AIzaSyB-1234example","app_id":"1234567890"},
} satisfies ContentProvider

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ContentProvider
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


