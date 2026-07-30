
# TeamInput

Client-writable fields for Team

## Properties

Name | Type
------------ | -------------
`name` | string
`description` | string
`related_teams` | [Array&lt;RelatedTeam&gt;](RelatedTeam.md)
`uri` | string
`email_address` | string
`status` | [TeamStatus](TeamStatus.md)
`members` | [Array&lt;TeamMemberInput&gt;](TeamMemberInput.md)
`responsible_parties` | [Array&lt;ResponsiblePartyInput&gt;](ResponsiblePartyInput.md)

## Example

```typescript
import type { TeamInput } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "name": Platform Engineering,
  "description": Core platform infrastructure team,
  "related_teams": [],
  "uri": https://wiki.example.com/teams/platform-engineering,
  "email_address": platform-eng@example.com,
  "status": active,
  "members": [{"user_id":"a1b2c3d4-e5f6-7890-abcd-ef1234567890","role":"engineering_lead"}],
  "responsible_parties": [],
} satisfies TeamInput

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as TeamInput
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


