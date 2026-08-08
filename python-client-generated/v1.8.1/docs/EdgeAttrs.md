# EdgeAttrs

Visual attributes for an edge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line** | [**EdgeAttrsLine**](EdgeAttrsLine.md) |  | [optional] 

## Example

```python
from tmi_client.models.edge_attrs import EdgeAttrs

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeAttrs from a JSON string
edge_attrs_instance = EdgeAttrs.from_json(json)
# print the JSON string representation of the object
print(EdgeAttrs.to_json())

# convert the object into a dict
edge_attrs_dict = edge_attrs_instance.to_dict()
# create an instance of EdgeAttrs from a dict
edge_attrs_from_dict = EdgeAttrs.from_dict(edge_attrs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


