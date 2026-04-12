# EdgeAttrsLine

Line styling attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stroke** | **str** | Line color | [optional] 
**stroke_width** | **float** | Line width in pixels | [optional] 
**stroke_dasharray** | **str** | Dash pattern for the line | [optional] 
**target_marker** | [**EdgeAttrsLineTargetMarker**](EdgeAttrsLineTargetMarker.md) |  | [optional] 
**source_marker** | [**EdgeAttrsLineSourceMarker**](EdgeAttrsLineSourceMarker.md) |  | [optional] 

## Example

```python
from tmi_client.models.edge_attrs_line import EdgeAttrsLine

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeAttrsLine from a JSON string
edge_attrs_line_instance = EdgeAttrsLine.from_json(json)
# print the JSON string representation of the object
print(EdgeAttrsLine.to_json())

# convert the object into a dict
edge_attrs_line_dict = edge_attrs_line_instance.to_dict()
# create an instance of EdgeAttrsLine from a dict
edge_attrs_line_from_dict = EdgeAttrsLine.from_dict(edge_attrs_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


