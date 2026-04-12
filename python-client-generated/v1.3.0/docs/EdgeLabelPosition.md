# EdgeLabelPosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distance** | **float** | Position along the edge: 0-1 for percentage, &gt;1 for pixels from start, &lt;0 for pixels from end | 
**offset** | [**EdgeLabelPositionOneOfOffset**](EdgeLabelPositionOneOfOffset.md) |  | [optional] 
**angle** | **float** | Rotation angle in degrees (clockwise) | [optional] 
**options** | [**EdgeLabelPositionOneOfOptions**](EdgeLabelPositionOneOfOptions.md) |  | [optional] 

## Example

```python
from tmi_client.models.edge_label_position import EdgeLabelPosition

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeLabelPosition from a JSON string
edge_label_position_instance = EdgeLabelPosition.from_json(json)
# print the JSON string representation of the object
print(EdgeLabelPosition.to_json())

# convert the object into a dict
edge_label_position_dict = edge_label_position_instance.to_dict()
# create an instance of EdgeLabelPosition from a dict
edge_label_position_from_dict = EdgeLabelPosition.from_dict(edge_label_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


