
# StepUpAuthenticate200Response


## Properties

Name | Type
------------ | -------------
`result` | string
`provider` | string
`auth_time` | number
`message` | string

## Example

```typescript
import type { StepUpAuthenticate200Response } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "result": null,
  "provider": null,
  "auth_time": null,
  "message": null,
} satisfies StepUpAuthenticate200Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as StepUpAuthenticate200Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


