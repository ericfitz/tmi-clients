# Node

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodeShape** | [**ShapeEnum**](#ShapeEnum) | Node type determining its visual representation and behavior |  [optional]
**position** | [**NodePosition**](NodePosition.md) |  |  [optional]
**size** | [**NodeSize**](NodeSize.md) |  |  [optional]
**angle** | [**BigDecimal**](BigDecimal.md) | Rotation angle in degrees |  [optional]
**attrs** | **Object** | Visual styling attributes for the node |  [optional]
**ports** | **Object** | Port configuration for connections |  [optional]
**parent** | [**UUID**](UUID.md) | ID of the parent cell for nested/grouped nodes (UUID) |  [optional]
**x** | [**BigDecimal**](BigDecimal.md) | X coordinate (flat format). Use either this with y, width, height OR use position/size objects. |  [optional]
**y** | [**BigDecimal**](BigDecimal.md) | Y coordinate (flat format) |  [optional]
**width** | [**BigDecimal**](BigDecimal.md) | Width in pixels (flat format) |  [optional]
**height** | [**BigDecimal**](BigDecimal.md) | Height in pixels (flat format) |  [optional]

<a name="ShapeEnum"></a>
## Enum: ShapeEnum
Name | Value
---- | -----
ACTOR | &quot;actor&quot;
PROCESS | &quot;process&quot;
STORE | &quot;store&quot;
SECURITY_BOUNDARY | &quot;security-boundary&quot;
TEXT_BOX | &quot;text-box&quot;
