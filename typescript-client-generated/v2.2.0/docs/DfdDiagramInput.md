
# DfdDiagramInput

Input schema for creating or updating a Data Flow Diagram

## Properties

Name | Type
------------ | -------------
`name` | string
`type` | string
`metadata` | [Array&lt;Metadata&gt;](Metadata.md)
`image` | [DfdDiagramImage](DfdDiagramImage.md)
`description` | string
`include_in_report` | boolean
`timmy_enabled` | boolean
`color_palette` | [Array&lt;ColorPaletteEntry&gt;](ColorPaletteEntry.md)
`cells` | [Array&lt;DfdDiagramCellsInner&gt;](DfdDiagramCellsInner.md)

## Example

```typescript
import type { DfdDiagramInput } from '@tmi-dev/client'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "type": null,
  "metadata": null,
  "image": null,
  "description": null,
  "include_in_report": null,
  "timmy_enabled": null,
  "color_palette": null,
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


