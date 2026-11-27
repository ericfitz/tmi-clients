# EdgeAttrsLineSourceMarker

Source marker configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Marker type | [optional] 
**size** | **float** | Marker size in pixels | [optional] 

## Example

```python
from tmi_client.models.edge_attrs_line_source_marker import EdgeAttrsLineSourceMarker

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeAttrsLineSourceMarker from a JSON string
edge_attrs_line_source_marker_instance = EdgeAttrsLineSourceMarker.from_json(json)
# print the JSON string representation of the object
print(EdgeAttrsLineSourceMarker.to_json())

# convert the object into a dict
edge_attrs_line_source_marker_dict = edge_attrs_line_source_marker_instance.to_dict()
# create an instance of EdgeAttrsLineSourceMarker from a dict
edge_attrs_line_source_marker_from_dict = EdgeAttrsLineSourceMarker.from_dict(edge_attrs_line_source_marker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


