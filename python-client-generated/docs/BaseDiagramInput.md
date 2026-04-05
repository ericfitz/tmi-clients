# BaseDiagramInput

Base diagram input for PUT/PATCH requests - excludes readOnly server-managed fields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the diagram | 
**type** | **str** | Type of diagram with version | 
**metadata** | [**List[Metadata]**](Metadata.md) | Key-value pairs for additional diagram metadata | [optional] 
**image** | [**BaseDiagramImage**](BaseDiagramImage.md) |  | [optional] 
**description** | **str** | Optional description of the diagram | [optional] 
**include_in_report** | **bool** | Whether this item should be included in generated reports | [optional] [default to True]
**timmy_enabled** | **bool** | Whether the Timmy AI assistant is enabled for this entity | [optional] [default to True]
**color_palette** | [**List[ColorPaletteEntry]**](ColorPaletteEntry.md) | Custom color palette for diagram elements, ordered by position | [optional] 

## Example

```python
from tmi_client.models.base_diagram_input import BaseDiagramInput

# TODO update the JSON string below
json = "{}"
# create an instance of BaseDiagramInput from a JSON string
base_diagram_input_instance = BaseDiagramInput.from_json(json)
# print the JSON string representation of the object
print(BaseDiagramInput.to_json())

# convert the object into a dict
base_diagram_input_dict = base_diagram_input_instance.to_dict()
# create an instance of BaseDiagramInput from a dict
base_diagram_input_from_dict = BaseDiagramInput.from_dict(base_diagram_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


