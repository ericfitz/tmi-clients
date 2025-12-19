# TmiJsClient.Node

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shape** | **String** | Node type determining its visual representation and behavior | [optional] 
**position** | [**NodePosition**](NodePosition.md) |  | [optional] 
**size** | [**NodeSize**](NodeSize.md) |  | [optional] 
**angle** | **Number** | Rotation angle in degrees | [optional] [default to 0]
**attrs** | **Object** | Visual styling attributes for the node | [optional] 
**ports** | **Object** | Port configuration for connections | [optional] 
**parent** | **String** | ID of the parent cell for nested/grouped nodes (UUID) | [optional] 
**x** | **Number** | X coordinate (flat format). Use either this with y, width, height OR use position/size objects. | [optional] 
**y** | **Number** | Y coordinate (flat format) | [optional] 
**width** | **Number** | Width in pixels (flat format) | [optional] 
**height** | **Number** | Height in pixels (flat format) | [optional] 

<a name="ShapeEnum"></a>
## Enum: ShapeEnum

* `actor` (value: `"actor"`)
* `process` (value: `"process"`)
* `store` (value: `"store"`)
* `securityBoundary` (value: `"security-boundary"`)
* `textBox` (value: `"text-box"`)

