# EdgeLabelAttrsText

Text styling

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Label text content | [optional] 
**font_size** | **float** | Font size in pixels | [optional] 
**fill** | **str** | Text color | [optional] 
**font_family** | **str** | Font family | [optional] 

## Example

```python
from tmi_client.models.edge_label_attrs_text import EdgeLabelAttrsText

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeLabelAttrsText from a JSON string
edge_label_attrs_text_instance = EdgeLabelAttrsText.from_json(json)
# print the JSON string representation of the object
print(EdgeLabelAttrsText.to_json())

# convert the object into a dict
edge_label_attrs_text_dict = edge_label_attrs_text_instance.to_dict()
# create an instance of EdgeLabelAttrsText from a dict
edge_label_attrs_text_from_dict = EdgeLabelAttrsText.from_dict(edge_label_attrs_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


