# NodeAttrs

Visual attributes for a node

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**NodeAttrsBody**](NodeAttrsBody.md) |  | [optional] 
**text** | [**NodeAttrsText**](NodeAttrsText.md) |  | [optional] 

## Example

```python
from tmi_client.models.node_attrs import NodeAttrs

# TODO update the JSON string below
json = "{}"
# create an instance of NodeAttrs from a JSON string
node_attrs_instance = NodeAttrs.from_json(json)
# print the JSON string representation of the object
print(NodeAttrs.to_json())

# convert the object into a dict
node_attrs_dict = node_attrs_instance.to_dict()
# create an instance of NodeAttrs from a dict
node_attrs_from_dict = NodeAttrs.from_dict(node_attrs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


