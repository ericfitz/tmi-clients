# ReencryptSystemSettings200ResponseErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The setting key that failed | 
**error** | **str** | Description of the failure | 

## Example

```python
from tmi_client.models.reencrypt_system_settings200_response_errors_inner import ReencryptSystemSettings200ResponseErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReencryptSystemSettings200ResponseErrorsInner from a JSON string
reencrypt_system_settings200_response_errors_inner_instance = ReencryptSystemSettings200ResponseErrorsInner.from_json(json)
# print the JSON string representation of the object
print(ReencryptSystemSettings200ResponseErrorsInner.to_json())

# convert the object into a dict
reencrypt_system_settings200_response_errors_inner_dict = reencrypt_system_settings200_response_errors_inner_instance.to_dict()
# create an instance of ReencryptSystemSettings200ResponseErrorsInner from a dict
reencrypt_system_settings200_response_errors_inner_from_dict = ReencryptSystemSettings200ResponseErrorsInner.from_dict(reencrypt_system_settings200_response_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


