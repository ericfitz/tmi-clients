
# ServerInfoResponse

Server TLS and WebSocket connection information for clients

## Properties

Name | Type
------------ | -------------
`tls_enabled` | boolean
`tls_subject_name` | string
`websocket_base_url` | string

## Example

```typescript
import type { ServerInfoResponse } from '@tmi-dev/client'

// TODO: Update the object below with actual values
const example = {
  "tls_enabled": null,
  "tls_subject_name": null,
  "websocket_base_url": wss://api.example.com/ws,
} satisfies ServerInfoResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ServerInfoResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


