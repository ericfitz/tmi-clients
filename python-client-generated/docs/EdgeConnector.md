# EdgeConnector

Edge connector style configuration for visual appearance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Connector style name | 
**args** | [**EdgeConnectorOneOfArgs**](EdgeConnectorOneOfArgs.md) |  | [optional] 

## Example

```python
from tmi_client.models.edge_connector import EdgeConnector

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeConnector from a JSON string
edge_connector_instance = EdgeConnector.from_json(json)
# print the JSON string representation of the object
print(EdgeConnector.to_json())

# convert the object into a dict
edge_connector_dict = edge_connector_instance.to_dict()
# create an instance of EdgeConnector from a dict
edge_connector_from_dict = EdgeConnector.from_dict(edge_connector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


