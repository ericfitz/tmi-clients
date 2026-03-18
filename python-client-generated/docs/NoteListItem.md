# NoteListItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Note name | 
**description** | **str** | Description of note purpose or context | [optional] 
**metadata** | [**list[Metadata]**](Metadata.md) | Key-value pairs for additional note metadata | [optional] 
**id** | **str** | Unique identifier for the note | 
**created_at** | **datetime** | Creation timestamp (RFC3339) | [optional] 
**modified_at** | **datetime** | Last modification timestamp (RFC3339) | [optional] 
**include_in_report** | **bool** | Whether this item should be included in generated reports | [optional] [default to True]
**timmy_enabled** | **bool** | Whether the Timmy AI assistant is enabled for this entity | [optional] [default to True]
**deleted_at** | **datetime** | Deletion timestamp (RFC3339). Present only on soft-deleted entities within the tombstone retention period. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

