# EdgeRouterOneOfArgs

Router-specific arguments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**padding** | **float** | Padding around obstacles for routing | [optional] 
**step** | **float** | Grid step size for orthogonal routing | [optional] 
**directions** | **List[str]** | Allowed routing directions | [optional] 

## Example

```python
from tmi_client.models.edge_router_one_of_args import EdgeRouterOneOfArgs

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeRouterOneOfArgs from a JSON string
edge_router_one_of_args_instance = EdgeRouterOneOfArgs.from_json(json)
# print the JSON string representation of the object
print(EdgeRouterOneOfArgs.to_json())

# convert the object into a dict
edge_router_one_of_args_dict = edge_router_one_of_args_instance.to_dict()
# create an instance of EdgeRouterOneOfArgs from a dict
edge_router_one_of_args_from_dict = EdgeRouterOneOfArgs.from_dict(edge_router_one_of_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


