# Node

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Shape** | **string** | Node type determining its visual representation and behavior | [default to null]
**Position** | [***NodePosition**](Node_position.md) |  | [optional] [default to null]
**Size** | [***NodeSize**](Node_size.md) |  | [optional] [default to null]
**Angle** | **float64** | Rotation angle in degrees | [optional] [default to 0]
**Attrs** | [***Object**](.md) | Visual styling attributes for the node | [optional] [default to null]
**Ports** | [***Object**](.md) | Port configuration for connections | [optional] [default to null]
**Parent** | **string** | ID of the parent cell for nested/grouped nodes (UUID) | [optional] [default to null]
**Children** | **[]string** | IDs of child cells contained within this node (UUIDs) | [optional] [default to null]
**X** | **float64** | X coordinate (flat format). Use either this with y, width, height OR use position/size objects. | [optional] [default to null]
**Y** | **float64** | Y coordinate (flat format) | [optional] [default to null]
**Width** | **float64** | Width in pixels (flat format) | [optional] [default to null]
**Height** | **float64** | Height in pixels (flat format) | [optional] [default to null]
**Id** | **string** | Unique identifier of the cell (UUID) | [default to null]
**Data** | [***CellData**](Cell_data.md) |  | [optional] [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

