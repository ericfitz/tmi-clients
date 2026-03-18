# TmiJsClient.BaseDiagram

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Unique identifier for the diagram (UUID) | 
**name** | **String** | Name of the diagram | 
**type** | **String** | Type of diagram with version | 
**createdAt** | **Date** | Creation timestamp (ISO3339) | 
**modifiedAt** | **Date** | Last modification timestamp (ISO3339) | 
**metadata** | [**[Metadata]**](Metadata.md) | Key-value pairs for additional diagram metadata | [optional] 
**updateVector** | **Number** | Server-managed monotonic version counter, incremented on each diagram update | [optional] 
**image** | [**BaseDiagramImage**](BaseDiagramImage.md) |  | [optional] 
**description** | **String** | Optional description of the diagram | [optional] 
**includeInReport** | **Boolean** | Whether this item should be included in generated reports | [optional] [default to true]
**timmyEnabled** | **Boolean** | Whether the Timmy AI assistant is enabled for this entity | [optional] [default to true]
**deletedAt** | **Date** | Deletion timestamp (RFC3339). Present only on soft-deleted entities within the tombstone retention period. | [optional] 
**colorPalette** | [**[ColorPaletteEntry]**](ColorPaletteEntry.md) | Custom color palette for diagram elements, ordered by position | [optional] 

<a name="TypeEnum"></a>
## Enum: TypeEnum

* `dFD100` (value: `"DFD-1.0.0"`)

