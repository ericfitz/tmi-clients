# ClientConfigLimits

System limits and quotas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_file_upload_mb** | **int** | Maximum file upload size in megabytes | [optional] 
**max_diagram_participants** | **int** | Maximum participants per collaboration session | [optional] 

## Example

```python
from tmi_client.models.client_config_limits import ClientConfigLimits

# TODO update the JSON string below
json = "{}"
# create an instance of ClientConfigLimits from a JSON string
client_config_limits_instance = ClientConfigLimits.from_json(json)
# print the JSON string representation of the object
print(ClientConfigLimits.to_json())

# convert the object into a dict
client_config_limits_dict = client_config_limits_instance.to_dict()
# create an instance of ClientConfigLimits from a dict
client_config_limits_from_dict = ClientConfigLimits.from_dict(client_config_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


