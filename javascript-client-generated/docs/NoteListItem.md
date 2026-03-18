# TmiJsClient.NoteListItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Note name | 
**description** | **String** | Description of note purpose or context | [optional] 
**metadata** | [**[Metadata]**](Metadata.md) | Key-value pairs for additional note metadata | [optional] 
**id** | **String** | Unique identifier for the note | 
**createdAt** | **Date** | Creation timestamp (RFC3339) | [optional] 
**modifiedAt** | **Date** | Last modification timestamp (RFC3339) | [optional] 
**includeInReport** | **Boolean** | Whether this item should be included in generated reports | [optional] [default to true]
**timmyEnabled** | **Boolean** | Whether the Timmy AI assistant is enabled for this entity | [optional] [default to true]
**deletedAt** | **Date** | Deletion timestamp (RFC3339). Present only on soft-deleted entities within the tombstone retention period. | [optional] 
