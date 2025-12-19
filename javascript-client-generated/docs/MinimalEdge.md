# TmiJsClient.MinimalEdge

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Cell unique identifier | 
**shape** | **String** | Edge shape type | 
**source** | **AllOfMinimalEdgeSource** | Source node connection details | 
**target** | **AllOfMinimalEdgeTarget** | Target node connection details | 
**labels** | **[String]** | Text labels extracted from edge labels array | 
**dataAssetId** | **String** | Optional reference to a data asset entity | [optional] 
**metadata** | **{String: String}** | Flattened edge metadata (converted from _metadata array in edge.data) | 

<a name="ShapeEnum"></a>
## Enum: ShapeEnum

* `edge` (value: `"edge"`)

