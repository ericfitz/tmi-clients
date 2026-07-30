# EdgeRouter

Edge routing algorithm configuration for pathfinding

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Router algorithm name | 
**args** | [**EdgeRouterOneOfArgs**](EdgeRouterOneOfArgs.md) |  | [optional] 

## Example

```python
from tmi_client.models.edge_router import EdgeRouter

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeRouter from a JSON string
edge_router_instance = EdgeRouter.from_json(json)
# print the JSON string representation of the object
print(EdgeRouter.to_json())

# convert the object into a dict
edge_router_dict = edge_router_instance.to_dict()
# create an instance of EdgeRouter from a dict
edge_router_from_dict = EdgeRouter.from_dict(edge_router_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


