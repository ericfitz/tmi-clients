# ClientConfigOperator

Operator information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the service operator | [optional] 
**contact** | **str** | Contact information for the operator | [optional] 

## Example

```python
from tmi_client.models.client_config_operator import ClientConfigOperator

# TODO update the JSON string below
json = "{}"
# create an instance of ClientConfigOperator from a JSON string
client_config_operator_instance = ClientConfigOperator.from_json(json)
# print the JSON string representation of the object
print(ClientConfigOperator.to_json())

# convert the object into a dict
client_config_operator_dict = client_config_operator_instance.to_dict()
# create an instance of ClientConfigOperator from a dict
client_config_operator_from_dict = ClientConfigOperator.from_dict(client_config_operator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


