# MinimalDiagramModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Threat model unique identifier | 
**name** | **str** | Threat model name | 
**description** | **str** | Threat model description | 
**metadata** | **dict(str, str)** | Flattened metadata from threat model (converted from array format to key-value pairs) | 
**cells** | [**list[MinimalCell]**](MinimalCell.md) | Minimal cell data (nodes and edges) without visual styling | 
**assets** | [**list[Asset]**](Asset.md) | Asset objects referenced by cells in this diagram via dataAssetIds | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

