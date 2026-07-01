
# ContentTokenList

List response wrapper for delegated content provider tokens.

## Properties

Name | Type
------------ | -------------
`content_tokens` | [Array&lt;ContentTokenInfo&gt;](ContentTokenInfo.md)

## Example

```typescript
import type { ContentTokenList } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "content_tokens": [],
} satisfies ContentTokenList

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ContentTokenList
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


