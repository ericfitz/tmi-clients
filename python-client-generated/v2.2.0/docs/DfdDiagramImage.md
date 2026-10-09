# DfdDiagramImage

Image data with version information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**svg** | **bytes** | BASE64 encoded SVG representation of the diagram, used for thumbnails and reports | [optional] 
**update_vector** | **int** | Version of the diagram when this SVG was generated. If not provided when svg is updated, will be auto-set to the diagram update_vector | [optional] 

## Example

```python
from tmi_client.models.dfd_diagram_image import DfdDiagramImage

# TODO update the JSON string below
json = "{}"
# create an instance of DfdDiagramImage from a JSON string
dfd_diagram_image_instance = DfdDiagramImage.from_json(json)
# print the JSON string representation of the object
print(DfdDiagramImage.to_json())

# convert the object into a dict
dfd_diagram_image_dict = dfd_diagram_image_instance.to_dict()
# create an instance of DfdDiagramImage from a dict
dfd_diagram_image_from_dict = DfdDiagramImage.from_dict(dfd_diagram_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


