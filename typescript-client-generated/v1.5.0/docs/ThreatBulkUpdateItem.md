
# ThreatBulkUpdateItem

Threat data for bulk update operations, including required ID field

## Properties

Name | Type
------------ | -------------
`name` | string
`description` | string
`mitigation` | string
`diagram_id` | string
`cell_id` | string
`severity` | string
`score` | number
`priority` | string
`mitigated` | boolean
`status` | string
`threat_type` | Set&lt;string&gt;
`metadata` | [Array&lt;Metadata&gt;](Metadata.md)
`issue_uri` | string
`asset_id` | string
`cwe_id` | Set&lt;string&gt;
`cvss` | [Array&lt;CVSSScore&gt;](CVSSScore.md)
`include_in_report` | boolean
`timmy_enabled` | boolean
`ssvc` | [SSVCScore](SSVCScore.md)
`id` | string

## Example

```typescript
import type { ThreatBulkUpdateItem } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "description": null,
  "mitigation": null,
  "diagram_id": null,
  "cell_id": null,
  "severity": null,
  "score": null,
  "priority": null,
  "mitigated": null,
  "status": null,
  "threat_type": null,
  "metadata": null,
  "issue_uri": null,
  "asset_id": null,
  "cwe_id": null,
  "cvss": null,
  "include_in_report": null,
  "timmy_enabled": null,
  "ssvc": null,
  "id": null,
} satisfies ThreatBulkUpdateItem

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ThreatBulkUpdateItem
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


