
# RelatedProject

A relationship entry linking to another project

## Properties

Name | Type
------------ | -------------
`related_project_id` | string
`relationship` | [RelationshipType](RelationshipType.md)
`custom_relationship` | string

## Example

```typescript
import type { RelatedProject } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "related_project_id": null,
  "relationship": null,
  "custom_relationship": null,
} satisfies RelatedProject

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as RelatedProject
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


