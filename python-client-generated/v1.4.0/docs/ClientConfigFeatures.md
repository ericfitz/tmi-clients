# ClientConfigFeatures

Feature flags indicating enabled functionality

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**websocket_enabled** | **bool** | Whether WebSocket collaboration is enabled | [optional] 
**saml_enabled** | **bool** | Whether SAML authentication is enabled | [optional] 
**webhooks_enabled** | **bool** | Whether webhook subscriptions are enabled | [optional] 

## Example

```python
from tmi_client.models.client_config_features import ClientConfigFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of ClientConfigFeatures from a JSON string
client_config_features_instance = ClientConfigFeatures.from_json(json)
# print the JSON string representation of the object
print(ClientConfigFeatures.to_json())

# convert the object into a dict
client_config_features_dict = client_config_features_instance.to_dict()
# create an instance of ClientConfigFeatures from a dict
client_config_features_from_dict = ClientConfigFeatures.from_dict(client_config_features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


