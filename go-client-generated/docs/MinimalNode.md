# MinimalNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Cell unique identifier | [default to null]
**Shape** | **string** | Node shape type determining its semantic role in the diagram | [default to null]
**Parent** | **string** | Parent cell ID for nested nodes (null for top-level nodes) | [optional] [default to null]
**Children** | **[]string** | Child cell IDs (computed bidirectional relationship including reverse parent references) | [default to null]
**Labels** | **[]string** | Text labels extracted from node attrs and embedded text-box children | [default to null]
**DataAssetId** | **string** | Optional reference to a data asset entity | [optional] [default to null]
**Metadata** | **map[string]string** | Flattened cell metadata (converted from _metadata array in cell.data) | [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

