# Node

Diagram node representing a process, data store, external entity, or trust boundary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shape** | **str** | Node type determining its visual representation and behavior | [optional] 
**position** | [**NodeAllOfPosition**](NodeAllOfPosition.md) |  | [optional] 
**size** | [**NodeAllOfSize**](NodeAllOfSize.md) |  | [optional] 
**angle** | **float** | Rotation angle in degrees | [optional] [default to 0]
**attrs** | [**NodeAttrs**](NodeAttrs.md) | Visual styling attributes for the node | [optional] 
**ports** | [**PortConfiguration**](PortConfiguration.md) | Port configuration for connections | [optional] 
**parent** | **UUID** | ID of the parent cell for nested/grouped nodes (UUID) | [optional] 
**children** | **List[UUID]** | IDs of child cells contained within this node (UUIDs) | [optional] 
**x** | **float** | X coordinate (flat format). Use either this with y, width, height OR use position/size objects. | [optional] 
**y** | **float** | Y coordinate (flat format) | [optional] 
**width** | **float** | Width in pixels (flat format) | [optional] 
**height** | **float** | Height in pixels (flat format) | [optional] 

## Example

```python
from tmi_client.models.node import Node

# TODO update the JSON string below
json = "{}"
# create an instance of Node from a JSON string
node_instance = Node.from_json(json)
# print the JSON string representation of the object
print(Node.to_json())

# convert the object into a dict
node_dict = node_instance.to_dict()
# create an instance of Node from a dict
node_from_dict = Node.from_dict(node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


