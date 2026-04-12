
# ThreatModel

A threat model containing diagrams, threats, documents, and other security analysis artifacts

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
`id` | string
`created_at` | Date
`modified_at` | Date
`created_by` | [User](User.md)
`documents` | [Array&lt;Document&gt;](Document.md)
`repositories` | [Array&lt;Repository&gt;](Repository.md)
`diagrams` | [Array&lt;DfdDiagram&gt;](DfdDiagram.md)
`threats` | [Array&lt;Threat&gt;](Threat.md)
`notes` | [Array&lt;Note&gt;](Note.md)
`assets` | [Array&lt;ExtendedAsset&gt;](ExtendedAsset.md)
`status_updated` | Date
`is_confidential` | boolean
`deleted_at` | Date

## Example

```typescript
import type { ThreatModel } from '@tmiclient/client'

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
  "id": null,
  "created_at": null,
  "modified_at": null,
  "created_by": null,
  "documents": null,
  "repositories": null,
  "diagrams": null,
  "threats": null,
  "notes": null,
  "assets": null,
  "status_updated": null,
  "is_confidential": null,
  "deleted_at": null,
} satisfies ThreatModel

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ThreatModel
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


