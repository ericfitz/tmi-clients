# MinimalEdge

Minimal edge representation without visual styling or routing information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Cell unique identifier | 
**shape** | **str** | Edge shape type | 
**source** | [**EdgeTerminal**](EdgeTerminal.md) | Source node connection details | 
**target** | [**EdgeTerminal**](EdgeTerminal.md) | Target node connection details | 
**labels** | **List[str]** | Text labels extracted from edge labels array | 
**metadata** | **Dict[str, str]** | Flattened edge metadata (converted from _metadata array in edge.data) | 
**data_asset_ids** | **List[UUID]** | References to Asset IDs associated with this edge | [optional] 

## Example

```python
from tmi_client.models.minimal_edge import MinimalEdge

# TODO update the JSON string below
json = "{}"
# create an instance of MinimalEdge from a JSON string
minimal_edge_instance = MinimalEdge.from_json(json)
# print the JSON string representation of the object
print(MinimalEdge.to_json())

# convert the object into a dict
minimal_edge_dict = minimal_edge_instance.to_dict()
# create an instance of MinimalEdge from a dict
minimal_edge_from_dict = MinimalEdge.from_dict(minimal_edge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


