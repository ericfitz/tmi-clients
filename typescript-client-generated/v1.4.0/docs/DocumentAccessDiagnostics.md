
# DocumentAccessDiagnostics

Per-viewer diagnostics explaining why a document is currently not accessible and what the viewer (or the document owner) can do to restore access. Emitted on Document responses whenever `access_status` is not `accessible`.

## Properties

Name | Type
------------ | -------------
`reason_code` | string
`reason_detail` | string
`remediations` | [Array&lt;AccessRemediation&gt;](AccessRemediation.md)

## Example

```typescript
import type { DocumentAccessDiagnostics } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "reason_code": null,
  "reason_detail": null,
  "remediations": null,
} satisfies DocumentAccessDiagnostics

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DocumentAccessDiagnostics
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


