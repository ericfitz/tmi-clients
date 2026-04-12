# ReencryptSystemSettings200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reencrypted** | **int** | Number of settings successfully re-encrypted | 
**errors** | [**List[ReencryptSystemSettings200ResponseErrorsInner]**](ReencryptSystemSettings200ResponseErrorsInner.md) | Settings that failed re-encryption | 
**total** | **int** | Total number of settings processed | 

## Example

```python
from tmi_client.models.reencrypt_system_settings200_response import ReencryptSystemSettings200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReencryptSystemSettings200Response from a JSON string
reencrypt_system_settings200_response_instance = ReencryptSystemSettings200Response.from_json(json)
# print the JSON string representation of the object
print(ReencryptSystemSettings200Response.to_json())

# convert the object into a dict
reencrypt_system_settings200_response_dict = reencrypt_system_settings200_response_instance.to_dict()
# create an instance of ReencryptSystemSettings200Response from a dict
reencrypt_system_settings200_response_from_dict = ReencryptSystemSettings200Response.from_dict(reencrypt_system_settings200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


