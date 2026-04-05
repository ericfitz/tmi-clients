# Edge

Diagram edge representing a data flow connection between nodes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shape** | **str** | Edge type identifier | [optional] 
**source** | [**EdgeTerminal**](EdgeTerminal.md) | Source connection point | 
**target** | [**EdgeTerminal**](EdgeTerminal.md) | Target connection point | 
**attrs** | [**EdgeAttrs**](EdgeAttrs.md) | Visual styling attributes for the edge | [optional] 
**labels** | [**List[EdgeLabel]**](EdgeLabel.md) | Text labels positioned along the edge | [optional] 
**vertices** | [**List[Point]**](Point.md) | Intermediate waypoints for edge routing | [optional] 
**router** | [**EdgeRouter**](EdgeRouter.md) | Edge routing algorithm configuration for path calculation | [optional] 
**connector** | [**EdgeConnector**](EdgeConnector.md) | Edge connector style configuration for visual appearance | [optional] 
**default_label** | [**EdgeLabel**](EdgeLabel.md) | Default label configuration applied to edges without explicit labels | [optional] 

## Example

```python
from tmi_client.models.edge import Edge

# TODO update the JSON string below
json = "{}"
# create an instance of Edge from a JSON string
edge_instance = Edge.from_json(json)
# print the JSON string representation of the object
print(Edge.to_json())

# convert the object into a dict
edge_dict = edge_instance.to_dict()
# create an instance of Edge from a dict
edge_from_dict = Edge.from_dict(edge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


