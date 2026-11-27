# ClientConfigUi

UI configuration defaults

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_theme** | **str** | Default UI theme | [optional] 

## Example

```python
from tmi_client.models.client_config_ui import ClientConfigUi

# TODO update the JSON string below
json = "{}"
# create an instance of ClientConfigUi from a JSON string
client_config_ui_instance = ClientConfigUi.from_json(json)
# print the JSON string representation of the object
print(ClientConfigUi.to_json())

# convert the object into a dict
client_config_ui_dict = client_config_ui_instance.to_dict()
# create an instance of ClientConfigUi from a dict
client_config_ui_from_dict = ClientConfigUi.from_dict(client_config_ui_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


