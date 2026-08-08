
# ApiInfo

API information response for the root endpoint

## Properties

Name | Type
------------ | -------------
`status` | [ApiInfoStatus](ApiInfoStatus.md)
`service` | [ApiInfoService](ApiInfoService.md)
`api` | [ApiInfoApi](ApiInfoApi.md)
`operator` | [ApiInfoOperator](ApiInfoOperator.md)
`health` | [ApiInfoHealth](ApiInfoHealth.md)

## Example

```typescript
import type { ApiInfo } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "status": null,
  "service": null,
  "api": null,
  "operator": null,
  "health": null,
} satisfies ApiInfo

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ApiInfo
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


