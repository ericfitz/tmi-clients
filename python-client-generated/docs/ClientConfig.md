# ClientConfig

Client configuration for tmi-ux and other client applications

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | [**ClientConfigFeatures**](ClientConfigFeatures.md) |  | [optional] 
**operator** | [**ClientConfigOperator**](ClientConfigOperator.md) |  | [optional] 
**limits** | [**ClientConfigLimits**](ClientConfigLimits.md) |  | [optional] 
**ui** | [**ClientConfigUi**](ClientConfigUi.md) |  | [optional] 

## Example

```python
from tmi_client.models.client_config import ClientConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ClientConfig from a JSON string
client_config_instance = ClientConfig.from_json(json)
# print the JSON string representation of the object
print(ClientConfig.to_json())

# convert the object into a dict
client_config_dict = client_config_instance.to_dict()
# create an instance of ClientConfig from a dict
client_config_from_dict = ClientConfig.from_dict(client_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


