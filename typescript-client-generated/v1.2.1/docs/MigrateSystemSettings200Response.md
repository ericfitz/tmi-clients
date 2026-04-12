
# MigrateSystemSettings200Response


## Properties

Name | Type
------------ | -------------
`migrated` | number
`skipped` | number
`settings` | [Array&lt;SystemSetting&gt;](SystemSetting.md)

## Example

```typescript
import type { MigrateSystemSettings200Response } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "migrated": 5,
  "skipped": 2,
  "settings": [{"key":"rate_limit.requests_per_minute","value":"60","type":"int","description":"Maximum API requests per minute","modified_at":"2024-01-15T10:00:00Z"}],
} satisfies MigrateSystemSettings200Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as MigrateSystemSettings200Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


