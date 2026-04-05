# EdgeLabel

Label positioned along an edge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attrs** | [**EdgeLabelAttrs**](EdgeLabelAttrs.md) |  | [optional] 
**position** | [**EdgeLabelPosition**](EdgeLabelPosition.md) |  | [optional] 

## Example

```python
from tmi_client.models.edge_label import EdgeLabel

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeLabel from a JSON string
edge_label_instance = EdgeLabel.from_json(json)
# print the JSON string representation of the object
print(EdgeLabel.to_json())

# convert the object into a dict
edge_label_dict = edge_label_instance.to_dict()
# create an instance of EdgeLabel from a dict
edge_label_from_dict = EdgeLabel.from_dict(edge_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


