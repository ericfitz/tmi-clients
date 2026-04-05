# EdgeRouterOneOf

Router with custom configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Router algorithm name | 
**args** | [**EdgeRouterOneOfArgs**](EdgeRouterOneOfArgs.md) |  | [optional] 

## Example

```python
from tmi_client.models.edge_router_one_of import EdgeRouterOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeRouterOneOf from a JSON string
edge_router_one_of_instance = EdgeRouterOneOf.from_json(json)
# print the JSON string representation of the object
print(EdgeRouterOneOf.to_json())

# convert the object into a dict
edge_router_one_of_dict = edge_router_one_of_instance.to_dict()
# create an instance of EdgeRouterOneOf from a dict
edge_router_one_of_from_dict = EdgeRouterOneOf.from_dict(edge_router_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


