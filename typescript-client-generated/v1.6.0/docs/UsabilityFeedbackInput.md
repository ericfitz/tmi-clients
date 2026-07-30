
# UsabilityFeedbackInput


## Properties

Name | Type
------------ | -------------
`sentiment` | string
`verbatim` | string
`surface` | string
`client_id` | string
`client_version` | string
`client_build` | string
`user_agent` | string
`user_agent_data` | { [key: string]: any; }
`viewport` | string
`screenshot` | string

## Example

```typescript
import type { UsabilityFeedbackInput } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "sentiment": null,
  "verbatim": null,
  "surface": null,
  "client_id": null,
  "client_version": null,
  "client_build": null,
  "user_agent": null,
  "user_agent_data": null,
  "viewport": null,
  "screenshot": null,
} satisfies UsabilityFeedbackInput

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as UsabilityFeedbackInput
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


