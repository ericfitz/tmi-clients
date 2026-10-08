# DfdDiagramInput

Input schema for creating or updating a Data Flow Diagram

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the diagram | 
**type** | **str** | DFD diagram type with version | 
**metadata** | [**List[Metadata]**](Metadata.md) | Key-value pairs for additional diagram metadata | [optional] 
**image** | [**DfdDiagramImage**](DfdDiagramImage.md) |  | [optional] 
**description** | **str** | Optional description of the diagram | [optional] 
**include_in_report** | **bool** | Whether this item should be included in generated reports | [optional] [default to True]
**timmy_enabled** | **bool** | Whether the Timmy AI assistant is enabled for this entity | [optional] [default to True]
**color_palette** | [**List[ColorPaletteEntry]**](ColorPaletteEntry.md) | Custom color palette for diagram elements, ordered by position | [optional] 
**cells** | [**List[DfdDiagramCellsInner]**](DfdDiagramCellsInner.md) | List of diagram cells (nodes and edges) following X6 structure | 

## Example

```python
from tmi_client.models.dfd_diagram_input import DfdDiagramInput

# TODO update the JSON string below
json = "{}"
# create an instance of DfdDiagramInput from a JSON string
dfd_diagram_input_instance = DfdDiagramInput.from_json(json)
# print the JSON string representation of the object
print(DfdDiagramInput.to_json())

# convert the object into a dict
dfd_diagram_input_dict = dfd_diagram_input_instance.to_dict()
# create an instance of DfdDiagramInput from a dict
dfd_diagram_input_from_dict = DfdDiagramInput.from_dict(dfd_diagram_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


