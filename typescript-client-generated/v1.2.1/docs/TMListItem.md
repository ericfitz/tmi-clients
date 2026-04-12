
# TMListItem

Enhanced item for threat model list endpoints with key metadata and counts

## Properties

Name | Type
------------ | -------------
`id` | string
`name` | string
`description` | string
`created_at` | Date
`modified_at` | Date
`owner` | [User](User.md)
`created_by` | [User](User.md)
`threat_model_framework` | string
`document_count` | number
`repo_count` | number
`diagram_count` | number
`threat_count` | number
`issue_uri` | string
`asset_count` | number
`note_count` | number
`status` | string
`status_updated` | Date
`security_reviewer` | [User](User.md)

## Example

```typescript
import type { TMListItem } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "name": null,
  "description": null,
  "created_at": null,
  "modified_at": null,
  "owner": null,
  "created_by": null,
  "threat_model_framework": null,
  "document_count": null,
  "repo_count": null,
  "diagram_count": null,
  "threat_count": null,
  "issue_uri": null,
  "asset_count": null,
  "note_count": null,
  "status": null,
  "status_updated": null,
  "security_reviewer": null,
} satisfies TMListItem

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as TMListItem
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


