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
