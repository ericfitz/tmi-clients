
# Project

A project representing a product, service, or application

## Properties

Name | Type
------------ | -------------
`name` | string
`description` | string
`team_id` | string
`responsible_parties` | [Array&lt;ResponsibleParty&gt;](ResponsibleParty.md)
`related_projects` | [Array&lt;RelatedProject&gt;](RelatedProject.md)
`uri` | string
`status` | [ProjectStatus](ProjectStatus.md)
`id` | string
`team` | object
`created_by` | object
`created_at` | Date
`modified_by` | object
`modified_at` | Date
`reviewed_by` | object
`reviewed_at` | Date
`metadata` | [Array&lt;Metadata&gt;](Metadata.md)
`notes` | [Array&lt;ProjectNoteListItem&gt;](ProjectNoteListItem.md)

## Example

```typescript
import type { Project } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "name": API Gateway Modernization,
  "description": Migrate legacy API gateway to cloud-native architecture,
  "team_id": 550e8400-e29b-41d4-a716-446655440000,
  "responsible_parties": [],
  "related_projects": [],
  "uri": https://wiki.example.com/projects/api-gateway,
  "status": null,
  "id": null,
  "team": null,
  "created_by": null,
  "created_at": null,
  "modified_by": null,
  "modified_at": null,
  "reviewed_by": null,
  "reviewed_at": null,
  "metadata": null,
  "notes": null,
} satisfies Project

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Project
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


