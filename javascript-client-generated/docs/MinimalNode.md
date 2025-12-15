# TmiThreatModelingImprovedApi.MinimalNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Cell unique identifier | 
**shape** | **String** | Node shape type determining its semantic role in the diagram | 
**parent** | **String** | Parent cell ID for nested nodes (null for top-level nodes) | [optional] 
**children** | **[String]** | Child cell IDs (computed bidirectional relationship including reverse parent references) | 
**labels** | **[String]** | Text labels extracted from node attrs and embedded text-box children | 
**dataAssetId** | **String** | Optional reference to a data asset entity | [optional] 
**metadata** | **{String: String}** | Flattened cell metadata (converted from _metadata array in cell.data) | 

<a name="ShapeEnum"></a>
## Enum: ShapeEnum

* `actor` (value: `"actor"`)
* `process` (value: `"process"`)
* `store` (value: `"store"`)
* `securityBoundary` (value: `"security-boundary"`)
* `textBox` (value: `"text-box"`)

