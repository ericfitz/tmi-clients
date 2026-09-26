# EdgeLabelAttrs

Label styling attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | [**EdgeLabelAttrsText**](EdgeLabelAttrsText.md) |  | [optional] 

## Example

```python
from tmi_client.models.edge_label_attrs import EdgeLabelAttrs

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeLabelAttrs from a JSON string
edge_label_attrs_instance = EdgeLabelAttrs.from_json(json)
# print the JSON string representation of the object
print(EdgeLabelAttrs.to_json())

# convert the object into a dict
edge_label_attrs_dict = edge_label_attrs_instance.to_dict()
# create an instance of EdgeLabelAttrs from a dict
edge_label_attrs_from_dict = EdgeLabelAttrs.from_dict(edge_label_attrs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


