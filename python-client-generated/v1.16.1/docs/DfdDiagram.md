# DfdDiagram


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DFD diagram type with version | [optional] 
**cells** | [**List[DfdDiagramAllOfCells]**](DfdDiagramAllOfCells.md) | List of diagram cells (nodes and edges) following X6 structure | 
**version** | **int** | Server-managed monotonically-increasing optimistic-locking version. Returned on reads and bumped by every successful PUT/PATCH. Clients echo this back via the If-Match request header (preferred) or the body &#39;version&#39; field on the next mutation. A mismatch returns 409 Conflict. See issue #385. | [optional] [readonly] 

## Example

```python
from tmi_client.models.dfd_diagram import DfdDiagram

# TODO update the JSON string below
json = "{}"
# create an instance of DfdDiagram from a JSON string
dfd_diagram_instance = DfdDiagram.from_json(json)
# print the JSON string representation of the object
print(DfdDiagram.to_json())

# convert the object into a dict
dfd_diagram_dict = dfd_diagram_instance.to_dict()
# create an instance of DfdDiagram from a dict
dfd_diagram_from_dict = DfdDiagram.from_dict(dfd_diagram_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


