# MinimalEdge

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Cell unique identifier | [default to null]
**Shape** | **string** | Edge shape type | [default to null]
**Source** | [***AllOfMinimalEdgeSource**](AllOfMinimalEdgeSource.md) | Source node connection details | [default to null]
**Target** | [***AllOfMinimalEdgeTarget**](AllOfMinimalEdgeTarget.md) | Target node connection details | [default to null]
**Labels** | **[]string** | Text labels extracted from edge labels array | [default to null]
**DataAssetId** | **string** | Optional reference to a data asset entity | [optional] [default to null]
**Metadata** | **map[string]string** | Flattened edge metadata (converted from _metadata array in edge.data) | [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

