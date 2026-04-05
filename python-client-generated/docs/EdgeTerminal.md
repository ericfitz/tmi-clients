# EdgeTerminal

Connection point for an edge (source or target)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cell** | **UUID** | ID of the connected node (UUID) | 
**port** | **str** | ID of the specific port on the node (optional) | [optional] 

## Example

```python
from tmi_client.models.edge_terminal import EdgeTerminal

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeTerminal from a JSON string
edge_terminal_instance = EdgeTerminal.from_json(json)
# print the JSON string representation of the object
print(EdgeTerminal.to_json())

# convert the object into a dict
edge_terminal_dict = edge_terminal_instance.to_dict()
# create an instance of EdgeTerminal from a dict
edge_terminal_from_dict = EdgeTerminal.from_dict(edge_terminal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


