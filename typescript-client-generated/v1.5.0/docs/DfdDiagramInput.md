
# DfdDiagramInput

Input schema for creating or updating a Data Flow Diagram

## Properties

Name | Type
------------ | -------------
`type` | string
`cells` | [Array&lt;DfdDiagramInputAllOfCells&gt;](DfdDiagramInputAllOfCells.md)

## Example

```typescript
import type { DfdDiagramInput } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "type": null,
  "cells": null,
} satisfies DfdDiagramInput

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DfdDiagramInput
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


