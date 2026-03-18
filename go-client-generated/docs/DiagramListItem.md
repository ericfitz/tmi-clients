# DiagramListItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier of the diagram (UUID) | [default to null]
**Name** | **string** | Name of the diagram | [default to null]
**Type_** | **string** | Type of the diagram | [default to null]
**Description** | **string** | Optional description of the diagram | [optional] [default to null]
**CreatedAt** | [**time.Time**](time.Time.md) | Creation timestamp (ISO3339) | [default to null]
**ModifiedAt** | [**time.Time**](time.Time.md) | Last modification timestamp (ISO3339) | [default to null]
**Image** | [***DiagramListItemImage**](DiagramListItem_image.md) |  | [optional] [default to null]
**IncludeInReport** | **bool** | Whether this item should be included in generated reports | [optional] [default to true]
**TimmyEnabled** | **bool** | Whether the Timmy AI assistant is enabled for this entity | [optional] [default to true]
**DeletedAt** | [**time.Time**](time.Time.md) | Deletion timestamp (RFC3339). Present only on soft-deleted entities within the tombstone retention period. | [optional] [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

