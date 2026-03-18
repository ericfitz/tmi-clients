# BaseDiagram

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the diagram (UUID) | 
**name** | **str** | Name of the diagram | 
**type** | **str** | Type of diagram with version | 
**created_at** | **datetime** | Creation timestamp (ISO3339) | 
**modified_at** | **datetime** | Last modification timestamp (ISO3339) | 
**metadata** | [**list[Metadata]**](Metadata.md) | Key-value pairs for additional diagram metadata | [optional] 
**update_vector** | **int** | Server-managed monotonic version counter, incremented on each diagram update | [optional] 
**image** | [**BaseDiagramImage**](BaseDiagramImage.md) |  | [optional] 
**description** | **str** | Optional description of the diagram | [optional] 
**include_in_report** | **bool** | Whether this item should be included in generated reports | [optional] [default to True]
**timmy_enabled** | **bool** | Whether the Timmy AI assistant is enabled for this entity | [optional] [default to True]
**deleted_at** | **datetime** | Deletion timestamp (RFC3339). Present only on soft-deleted entities within the tombstone retention period. | [optional] 
**color_palette** | [**list[ColorPaletteEntry]**](ColorPaletteEntry.md) | Custom color palette for diagram elements, ordered by position | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

