# EdgeAttrsLineTargetMarker

Arrowhead marker configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Marker type | [optional] 
**size** | **float** | Marker size in pixels | [optional] 

## Example

```python
from tmi_client.models.edge_attrs_line_target_marker import EdgeAttrsLineTargetMarker

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeAttrsLineTargetMarker from a JSON string
edge_attrs_line_target_marker_instance = EdgeAttrsLineTargetMarker.from_json(json)
# print the JSON string representation of the object
print(EdgeAttrsLineTargetMarker.to_json())

# convert the object into a dict
edge_attrs_line_target_marker_dict = edge_attrs_line_target_marker_instance.to_dict()
# create an instance of EdgeAttrsLineTargetMarker from a dict
edge_attrs_line_target_marker_from_dict = EdgeAttrsLineTargetMarker.from_dict(edge_attrs_line_target_marker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


