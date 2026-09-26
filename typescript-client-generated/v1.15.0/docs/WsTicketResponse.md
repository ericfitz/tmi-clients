
# WsTicketResponse

Response containing a short-lived, single-use authentication ticket for WebSocket connection

## Properties

Name | Type
------------ | -------------
`ticket` | string

## Example

```typescript
import type { WsTicketResponse } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "ticket": tmi_ws_abc123def456,
} satisfies WsTicketResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as WsTicketResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


