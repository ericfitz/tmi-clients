# NoteListItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Note name | [default to null]
**Description** | **string** | Description of note purpose or context | [optional] [default to null]
**Metadata** | [**[]Metadata**](Metadata.md) | Key-value pairs for additional note metadata | [optional] [default to null]
**Id** | **string** | Unique identifier for the note | [default to null]
**CreatedAt** | [**time.Time**](time.Time.md) | Creation timestamp (RFC3339) | [optional] [default to null]
**ModifiedAt** | [**time.Time**](time.Time.md) | Last modification timestamp (RFC3339) | [optional] [default to null]
**IncludeInReport** | **bool** | Whether this item should be included in generated reports | [optional] [default to true]
**TimmyEnabled** | **bool** | Whether the Timmy AI assistant is enabled for this entity | [optional] [default to true]
**DeletedAt** | [**time.Time**](time.Time.md) | Deletion timestamp (RFC3339). Present only on soft-deleted entities within the tombstone retention period. | [optional] [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

