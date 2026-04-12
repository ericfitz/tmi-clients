
# Team

A team representing an organizational unit

## Properties

Name | Type
------------ | -------------
`name` | string
`description` | string
`members` | [Array&lt;TeamMember&gt;](TeamMember.md)
`responsible_parties` | [Array&lt;ResponsibleParty&gt;](ResponsibleParty.md)
`related_teams` | [Array&lt;RelatedTeam&gt;](RelatedTeam.md)
`uri` | string
`email_address` | string
`status` | string
`id` | string
`created_by` | object
`created_at` | Date
`modified_by` | object
`modified_at` | Date
`reviewed_by` | object
`reviewed_at` | Date
`metadata` | [Array&lt;Metadata&gt;](Metadata.md)

## Example

```typescript
import type { Team } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "name": Platform Engineering,
  "description": Core platform infrastructure team,
  "members": [{user_id=a1b2c3d4-e5f6-7890-abcd-ef1234567890, role=engineering_lead}],
  "responsible_parties": [],
  "related_teams": [],
  "uri": https://wiki.example.com/teams/platform-engineering,
  "email_address": platform-eng@example.com,
  "status": active,
  "id": null,
  "created_by": null,
  "created_at": null,
  "modified_by": null,
  "modified_at": null,
  "reviewed_by": null,
  "reviewed_at": null,
  "metadata": null,
} satisfies Team

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Team
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


