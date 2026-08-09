
# TeamSummary

Minimal team reference embedded in other resources. Only the identifying fields are resolved; fetch /teams/{team_id} for the complete team.

## Properties

Name | Type
------------ | -------------
`id` | string
`name` | string
`description` | string

## Example

```typescript
import type { TeamSummary } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "name": Platform Engineering,
  "description": Core platform infrastructure team,
} satisfies TeamSummary

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as TeamSummary
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


