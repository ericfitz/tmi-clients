
# ContentFeedbackInput


## Properties

Name | Type
------------ | -------------
`sentiment` | string
`target_type` | string
`target_id` | string
`target_field` | string
`verbatim` | string
`false_positive_reason` | string
`false_positive_subreason` | string
`client_id` | string
`client_version` | string
`screenshot` | string

## Example

```typescript
import type { ContentFeedbackInput } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "sentiment": null,
  "target_type": null,
  "target_id": null,
  "target_field": null,
  "verbatim": null,
  "false_positive_reason": null,
  "false_positive_subreason": null,
  "client_id": null,
  "client_version": null,
  "screenshot": null,
} satisfies ContentFeedbackInput

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ContentFeedbackInput
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


