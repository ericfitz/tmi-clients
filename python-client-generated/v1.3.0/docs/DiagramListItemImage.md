# DiagramListItemImage

Image data with version information for thumbnail rendering

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**svg** | **bytes** | BASE64 encoded SVG representation of the diagram, used for thumbnails and reports | [optional] 
**update_vector** | **int** | Version of the diagram when this SVG was generated | [optional] 

## Example

```python
from tmi_client.models.diagram_list_item_image import DiagramListItemImage

# TODO update the JSON string below
json = "{}"
# create an instance of DiagramListItemImage from a JSON string
diagram_list_item_image_instance = DiagramListItemImage.from_json(json)
# print the JSON string representation of the object
print(DiagramListItemImage.to_json())

# convert the object into a dict
diagram_list_item_image_dict = diagram_list_item_image_instance.to_dict()
# create an instance of DiagramListItemImage from a dict
diagram_list_item_image_from_dict = DiagramListItemImage.from_dict(diagram_list_item_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


