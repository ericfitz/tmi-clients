# BaseDiagramImage

Image data with version information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**svg** | **bytes** | BASE64 encoded SVG representation of the diagram, used for thumbnails and reports | [optional] 
**update_vector** | **int** | Version of the diagram when this SVG was generated. If not provided when svg is updated, will be auto-set to BaseDiagram.update_vector | [optional] 

## Example

```python
from tmi_client.models.base_diagram_image import BaseDiagramImage

# TODO update the JSON string below
json = "{}"
# create an instance of BaseDiagramImage from a JSON string
base_diagram_image_instance = BaseDiagramImage.from_json(json)
# print the JSON string representation of the object
print(BaseDiagramImage.to_json())

# convert the object into a dict
base_diagram_image_dict = base_diagram_image_instance.to_dict()
# create an instance of BaseDiagramImage from a dict
base_diagram_image_from_dict = BaseDiagramImage.from_dict(base_diagram_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


