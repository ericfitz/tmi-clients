# DiagramListItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the diagram (UUID) | 
**name** | **str** | Name of the diagram | 
**type** | **str** | Type of the diagram | 
**description** | **str** | Optional description of the diagram | [optional] 
**created_at** | **datetime** | Creation timestamp (ISO3339) | 
**modified_at** | **datetime** | Last modification timestamp (ISO3339) | 
**image** | [**DiagramListItemImage**](DiagramListItemImage.md) |  | [optional] 
**include_in_report** | **bool** | Whether this item should be included in generated reports | [optional] [default to True]
**timmy_enabled** | **bool** | Whether the Timmy AI assistant is enabled for this entity | [optional] [default to True]
**deleted_at** | **datetime** | Deletion timestamp (RFC3339). Present only on soft-deleted entities within the tombstone retention period. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

