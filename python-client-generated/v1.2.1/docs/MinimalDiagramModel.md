# MinimalDiagramModel

Minimal diagram representation optimized for automated threat modeling, containing threat model context and simplified cell data without visual styling

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Threat model unique identifier | 
**name** | **str** | Threat model name | 
**description** | **str** | Threat model description | 
**metadata** | **Dict[str, str]** | Flattened metadata from threat model (converted from array format to key-value pairs) | 
**cells** | [**List[MinimalCell]**](MinimalCell.md) | Minimal cell data (nodes and edges) without visual styling | 
**assets** | [**List[Asset]**](Asset.md) | Asset objects referenced by cells in this diagram via dataAssetIds | 

## Example

```python
from tmi_client.models.minimal_diagram_model import MinimalDiagramModel

# TODO update the JSON string below
json = "{}"
# create an instance of MinimalDiagramModel from a JSON string
minimal_diagram_model_instance = MinimalDiagramModel.from_json(json)
# print the JSON string representation of the object
print(MinimalDiagramModel.to_json())

# convert the object into a dict
minimal_diagram_model_dict = minimal_diagram_model_instance.to_dict()
# create an instance of MinimalDiagramModel from a dict
minimal_diagram_model_from_dict = MinimalDiagramModel.from_dict(minimal_diagram_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


