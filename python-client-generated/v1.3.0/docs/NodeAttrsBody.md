# NodeAttrsBody

Body/shape styling attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fill** | **str** | Fill color | [optional] 
**stroke** | **str** | Stroke color | [optional] 
**stroke_width** | **float** | Stroke width in pixels | [optional] 
**stroke_dasharray** | **str** | Dash pattern for strokes | [optional] 

## Example

```python
from tmi_client.models.node_attrs_body import NodeAttrsBody

# TODO update the JSON string below
json = "{}"
# create an instance of NodeAttrsBody from a JSON string
node_attrs_body_instance = NodeAttrsBody.from_json(json)
# print the JSON string representation of the object
print(NodeAttrsBody.to_json())

# convert the object into a dict
node_attrs_body_dict = node_attrs_body_instance.to_dict()
# create an instance of NodeAttrsBody from a dict
node_attrs_body_from_dict = NodeAttrsBody.from_dict(node_attrs_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


