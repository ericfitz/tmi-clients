# MinimalNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Cell unique identifier | 
**shape** | **str** | Node shape type determining its semantic role in the diagram | 
**parent** | **str** | Parent cell ID for nested nodes (null for top-level nodes) | [optional] 
**children** | **list[str]** | Child cell IDs (computed bidirectional relationship including reverse parent references) | 
**labels** | **list[str]** | Text labels extracted from node attrs and embedded text-box children | 
**data_asset_ids** | **list[str]** | References to Asset IDs associated with this node | [optional] 
**metadata** | **dict(str, str)** | Flattened cell metadata (converted from _metadata array in cell.data) | 
**security_boundary** | **bool** | Indicates whether this node represents a security boundary. Always true for shape&#x3D;&#x27;security-boundary&#x27;, otherwise derived from cell data. | [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

