# ListUserQuotasResponseDefaults

Server default quota values applied when a user has no quota row

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_requests_per_minute** | **int** | Default requests-per-minute limit | 
**max_requests_per_hour** | **int** | Default requests-per-hour limit | 

## Example

```python
from tmi_client.models.list_user_quotas_response_defaults import ListUserQuotasResponseDefaults

# TODO update the JSON string below
json = "{}"
# create an instance of ListUserQuotasResponseDefaults from a JSON string
list_user_quotas_response_defaults_instance = ListUserQuotasResponseDefaults.from_json(json)
# print the JSON string representation of the object
print(ListUserQuotasResponseDefaults.to_json())

# convert the object into a dict
list_user_quotas_response_defaults_dict = list_user_quotas_response_defaults_instance.to_dict()
# create an instance of ListUserQuotasResponseDefaults from a dict
list_user_quotas_response_defaults_from_dict = ListUserQuotasResponseDefaults.from_dict(list_user_quotas_response_defaults_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


