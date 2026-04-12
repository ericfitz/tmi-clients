# MinimalCell

Minimal diagram cell data for WebSocket collaboration updates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Cell unique identifier | 
**shape** | **str** | Edge shape type | 
**parent** | **UUID** | Parent cell ID for nested nodes (null for top-level nodes) | [optional] 
**children** | **List[UUID]** | Child cell IDs (computed bidirectional relationship including reverse parent references) | 
**labels** | **List[str]** | Text labels extracted from edge labels array | 
**data_asset_ids** | **List[UUID]** | References to Asset IDs associated with this edge | [optional] 
**metadata** | **Dict[str, str]** | Flattened edge metadata (converted from _metadata array in edge.data) | 
**security_boundary** | **bool** | Indicates whether this node represents a security boundary. Always true for shape&#x3D;&#39;security-boundary&#39;, otherwise derived from cell data. | [default to False]
**source** | [**EdgeTerminal**](EdgeTerminal.md) | Source node connection details | 
**target** | [**EdgeTerminal**](EdgeTerminal.md) | Target node connection details | 

## Example

```python
from tmi_client.models.minimal_cell import MinimalCell

# TODO update the JSON string below
json = "{}"
# create an instance of MinimalCell from a JSON string
minimal_cell_instance = MinimalCell.from_json(json)
# print the JSON string representation of the object
print(MinimalCell.to_json())

# convert the object into a dict
minimal_cell_dict = minimal_cell_instance.to_dict()
# create an instance of MinimalCell from a dict
minimal_cell_from_dict = MinimalCell.from_dict(minimal_cell_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


