# EdgeLabelPositionOneOf

Advanced position with offset and angle (X6 LabelPositionObject format)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distance** | **float** | Position along the edge: 0-1 for percentage, &gt;1 for pixels from start, &lt;0 for pixels from end | 
**offset** | [**EdgeLabelPositionOneOfOffset**](EdgeLabelPositionOneOfOffset.md) |  | [optional] 
**angle** | **float** | Rotation angle in degrees (clockwise) | [optional] 
**options** | [**EdgeLabelPositionOneOfOptions**](EdgeLabelPositionOneOfOptions.md) |  | [optional] 

## Example

```python
from tmi_client.models.edge_label_position_one_of import EdgeLabelPositionOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeLabelPositionOneOf from a JSON string
edge_label_position_one_of_instance = EdgeLabelPositionOneOf.from_json(json)
# print the JSON string representation of the object
print(EdgeLabelPositionOneOf.to_json())

# convert the object into a dict
edge_label_position_one_of_dict = edge_label_position_one_of_instance.to_dict()
# create an instance of EdgeLabelPositionOneOf from a dict
edge_label_position_one_of_from_dict = EdgeLabelPositionOneOf.from_dict(edge_label_position_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


