# EdgeConnectorOneOfArgs

Connector-specific arguments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**radius** | **float** | Radius for rounded connectors | [optional] 
**precision** | **float** | Precision for smooth connectors | [optional] 
**size** | **float** | Jump size for jumpover connectors | [optional] 
**jump** | **str** | Jump style for jumpover connectors | [optional] 

## Example

```python
from tmi_client.models.edge_connector_one_of_args import EdgeConnectorOneOfArgs

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeConnectorOneOfArgs from a JSON string
edge_connector_one_of_args_instance = EdgeConnectorOneOfArgs.from_json(json)
# print the JSON string representation of the object
print(EdgeConnectorOneOfArgs.to_json())

# convert the object into a dict
edge_connector_one_of_args_dict = edge_connector_one_of_args_instance.to_dict()
# create an instance of EdgeConnectorOneOfArgs from a dict
edge_connector_one_of_args_from_dict = EdgeConnectorOneOfArgs.from_dict(edge_connector_one_of_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


