# NodeAttrsText

Text/label styling attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Label text content | [optional] 
**font_size** | **float** | Font size in pixels | [optional] 
**fill** | **str** | Text color | [optional] 
**font_family** | **str** | Font family | [optional] 
**ref_x** | [**NodeAttrsTextRefX**](NodeAttrsTextRefX.md) |  | [optional] 
**ref_y** | [**NodeAttrsTextRefY**](NodeAttrsTextRefY.md) |  | [optional] 
**ref_dx** | **float** | Horizontal offset from refX (corner-based, retained for back-compat; client uses refX2) | [optional] 
**ref_dy** | **float** | Vertical offset from refY (corner-based, retained for back-compat; client uses refY2) | [optional] 
**ref_x2** | [**NodeAttrsTextRefX2**](NodeAttrsTextRefX2.md) |  | [optional] 
**ref_y2** | [**NodeAttrsTextRefY2**](NodeAttrsTextRefY2.md) |  | [optional] 
**text_anchor** | **str** | Horizontal text alignment anchor point | [optional] 
**text_vertical_anchor** | **str** | Vertical text alignment anchor point | [optional] 

## Example

```python
from tmi_client.models.node_attrs_text import NodeAttrsText

# TODO update the JSON string below
json = "{}"
# create an instance of NodeAttrsText from a JSON string
node_attrs_text_instance = NodeAttrsText.from_json(json)
# print the JSON string representation of the object
print(NodeAttrsText.to_json())

# convert the object into a dict
node_attrs_text_dict = node_attrs_text_instance.to_dict()
# create an instance of NodeAttrsText from a dict
node_attrs_text_from_dict = NodeAttrsText.from_dict(node_attrs_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


