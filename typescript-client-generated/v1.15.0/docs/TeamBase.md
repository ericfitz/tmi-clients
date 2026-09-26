
# TeamBase

Client-writable fields for a team

## Properties

Name | Type
------------ | -------------
`name` | string
`description` | string
`related_teams` | [Array&lt;RelatedTeam&gt;](RelatedTeam.md)
`uri` | string
`email_address` | string
`status` | [TeamStatus](TeamStatus.md)

## Example

```typescript
import type { TeamBase } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "name": Platform Engineering,
  "description": Core platform infrastructure team,
  "related_teams": [],
  "uri": https://wiki.example.com/teams/platform-engineering,
  "email_address": platform-eng@example.com,
  "status": active,
} satisfies TeamBase

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as TeamBase
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


