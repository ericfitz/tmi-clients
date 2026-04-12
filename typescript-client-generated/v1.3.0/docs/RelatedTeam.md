
# RelatedTeam

A relationship entry linking to another team

## Properties

Name | Type
------------ | -------------
`related_team_id` | string
`relationship` | [RelationshipType](RelationshipType.md)
`custom_relationship` | string

## Example

```typescript
import type { RelatedTeam } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "related_team_id": null,
  "relationship": null,
  "custom_relationship": null,
} satisfies RelatedTeam

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as RelatedTeam
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


