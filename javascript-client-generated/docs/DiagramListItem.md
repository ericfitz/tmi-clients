# TmiJsClient.DiagramListItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Unique identifier of the diagram (UUID) | 
**name** | **String** | Name of the diagram | 
**type** | **String** | Type of the diagram | 
**description** | **String** | Optional description of the diagram | [optional] 
**createdAt** | **Date** | Creation timestamp (ISO3339) | 
**modifiedAt** | **Date** | Last modification timestamp (ISO3339) | 
**image** | [**DiagramListItemImage**](DiagramListItemImage.md) |  | [optional] 
**includeInReport** | **Boolean** | Whether this item should be included in generated reports | [optional] [default to true]

<a name="TypeEnum"></a>
## Enum: TypeEnum

* `dFD100` (value: `"DFD-1.0.0"`)

