
# MinimalDiagramModel

Minimal diagram representation optimized for automated threat modeling, containing threat model context and simplified cell data without visual styling

## Properties

Name | Type
------------ | -------------
`id` | string
`name` | string
`description` | string
`metadata` | { [key: string]: string; }
`cells` | [Array&lt;MinimalCell&gt;](MinimalCell.md)
`assets` | [Array&lt;Asset&gt;](Asset.md)

## Example

```typescript
import type { MinimalDiagramModel } from '@tmiclient/client'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "name": null,
  "description": null,
  "metadata": null,
  "cells": null,
  "assets": null,
} satisfies MinimalDiagramModel

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as MinimalDiagramModel
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


