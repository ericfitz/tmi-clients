# Node

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shape** | **str** | Node type determining its visual representation and behavior | [optional] 
**position** | [**NodePosition**](NodePosition.md) |  | [optional] 
**size** | [**NodeSize**](NodeSize.md) |  | [optional] 
**angle** | **float** | Rotation angle in degrees | [optional] [default to 0]
**attrs** | **object** | Visual styling attributes for the node | [optional] 
**ports** | **object** | Port configuration for connections | [optional] 
**parent** | **str** | ID of the parent cell for nested/grouped nodes (UUID) | [optional] 
**children** | **list[str]** | IDs of child cells contained within this node (UUIDs) | [optional] 
**x** | **float** | X coordinate (flat format). Use either this with y, width, height OR use position/size objects. | [optional] 
**y** | **float** | Y coordinate (flat format) | [optional] 
**width** | **float** | Width in pixels (flat format) | [optional] 
**height** | **float** | Height in pixels (flat format) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

