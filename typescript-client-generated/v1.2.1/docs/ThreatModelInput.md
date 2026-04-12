
# ThreatModelInput

Input schema for creating/updating ThreatModel

## Properties

Name | Type
------------ | -------------
`name` | string
`description` | string
`threat_model_framework` | string
`authorization` | [Array&lt;Authorization&gt;](Authorization.md)
`metadata` | [Array&lt;Metadata&gt;](Metadata.md)
`issue_uri` | string
`is_confidential` | boolean

## Example

```typescript
import type { ThreatModelInput } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "description": null,
  "threat_model_framework": null,
  "authorization": null,
  "metadata": null,
  "issue_uri": null,
  "is_confidential": null,
} satisfies ThreatModelInput

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ThreatModelInput
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


