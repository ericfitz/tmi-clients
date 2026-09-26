
# ProjectInput

Client-writable fields for Project

## Properties

Name | Type
------------ | -------------
`name` | string
`description` | string
`team_id` | string
`related_projects` | [Array&lt;RelatedProject&gt;](RelatedProject.md)
`uri` | string
`status` | [ProjectStatus](ProjectStatus.md)
`responsible_parties` | [Array&lt;ResponsiblePartyInput&gt;](ResponsiblePartyInput.md)

## Example

```typescript
import type { ProjectInput } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "name": API Gateway Modernization,
  "description": Migrate legacy API gateway to cloud-native architecture,
  "team_id": 550e8400-e29b-41d4-a716-446655440000,
  "related_projects": [],
  "uri": https://wiki.example.com/projects/api-gateway,
  "status": active,
  "responsible_parties": [],
} satisfies ProjectInput

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ProjectInput
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


