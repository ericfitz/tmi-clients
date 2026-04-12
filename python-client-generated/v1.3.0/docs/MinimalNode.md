# MinimalNode

Minimal node representation without visual styling or layout information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Cell unique identifier | 
**shape** | **str** | Node shape type determining its semantic role in the diagram | 
**parent** | **UUID** | Parent cell ID for nested nodes (null for top-level nodes) | [optional] 
**children** | **List[UUID]** | Child cell IDs (computed bidirectional relationship including reverse parent references) | 
**labels** | **List[str]** | Text labels extracted from node attrs and embedded text-box children | 
**data_asset_ids** | **List[UUID]** | References to Asset IDs associated with this node | [optional] 
**metadata** | **Dict[str, str]** | Flattened cell metadata (converted from _metadata array in cell.data) | 
**security_boundary** | **bool** | Indicates whether this node represents a security boundary. Always true for shape&#x3D;&#39;security-boundary&#39;, otherwise derived from cell data. | [default to False]

## Example

```python
from tmi_client.models.minimal_node import MinimalNode

# TODO update the JSON string below
json = "{}"
# create an instance of MinimalNode from a JSON string
minimal_node_instance = MinimalNode.from_json(json)
# print the JSON string representation of the object
print(MinimalNode.to_json())

# convert the object into a dict
minimal_node_dict = minimal_node_instance.to_dict()
# create an instance of MinimalNode from a dict
minimal_node_from_dict = MinimalNode.from_dict(minimal_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


