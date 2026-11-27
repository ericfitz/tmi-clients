# EdgeConnectorOneOf

Connector with custom configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Connector style name | 
**args** | [**EdgeConnectorOneOfArgs**](EdgeConnectorOneOfArgs.md) |  | [optional] 

## Example

```python
from tmi_client.models.edge_connector_one_of import EdgeConnectorOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeConnectorOneOf from a JSON string
edge_connector_one_of_instance = EdgeConnectorOneOf.from_json(json)
# print the JSON string representation of the object
print(EdgeConnectorOneOf.to_json())

# convert the object into a dict
edge_connector_one_of_dict = edge_connector_one_of_instance.to_dict()
# create an instance of EdgeConnectorOneOf from a dict
edge_connector_one_of_from_dict = EdgeConnectorOneOf.from_dict(edge_connector_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


