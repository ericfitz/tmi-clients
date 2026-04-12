
# ThreatModelBase

Base schema for ThreatModel with client-writable fields

## Properties

Name | Type
------------ | -------------
`name` | string
`description` | string
`owner` | [User](User.md)
`threat_model_framework` | string
`authorization` | [Array&lt;Authorization&gt;](Authorization.md)
`metadata` | [Array&lt;Metadata&gt;](Metadata.md)
`issue_uri` | string
`status` | string
`alias` | Set&lt;string&gt;
`security_reviewer` | [User](User.md)
`project_id` | string

## Example

```typescript
import type { ThreatModelBase } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "description": null,
  "owner": null,
  "threat_model_framework": null,
  "authorization": null,
  "metadata": null,
  "issue_uri": null,
  "status": null,
  "alias": null,
  "security_reviewer": null,
  "project_id": null,
} satisfies ThreatModelBase

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ThreatModelBase
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


