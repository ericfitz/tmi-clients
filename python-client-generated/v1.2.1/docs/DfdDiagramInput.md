# DfdDiagramInput

Input schema for creating or updating a Data Flow Diagram

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DFD diagram type with version | [optional] 
**cells** | [**List[DfdDiagramInputAllOfCells]**](DfdDiagramInputAllOfCells.md) | List of diagram cells (nodes and edges) following X6 structure | 

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


