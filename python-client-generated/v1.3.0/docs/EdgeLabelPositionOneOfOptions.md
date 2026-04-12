# EdgeLabelPositionOneOfOptions

Advanced positioning options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**absolute_distance** | **bool** | Forces absolute coordinates for distance | [optional] 
**reverse_distance** | **bool** | Forces reverse absolute coordinates | [optional] 
**absolute_offset** | **bool** | Forces absolute coordinates for offset | [optional] 
**keep_gradient** | **bool** | Auto-adjusts angle to match path gradient | [optional] 
**ensure_legibility** | **bool** | Rotates labels to avoid upside-down text | [optional] 

## Example

```python
from tmi_client.models.edge_label_position_one_of_options import EdgeLabelPositionOneOfOptions

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeLabelPositionOneOfOptions from a JSON string
edge_label_position_one_of_options_instance = EdgeLabelPositionOneOfOptions.from_json(json)
# print the JSON string representation of the object
print(EdgeLabelPositionOneOfOptions.to_json())

# convert the object into a dict
edge_label_position_one_of_options_dict = edge_label_position_one_of_options_instance.to_dict()
# create an instance of EdgeLabelPositionOneOfOptions from a dict
edge_label_position_one_of_options_from_dict = EdgeLabelPositionOneOfOptions.from_dict(edge_label_position_one_of_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


