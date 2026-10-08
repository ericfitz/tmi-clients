# UserQuotaUpdate

Configuration update for user API quotas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_requests_per_minute** | **int** | Maximum API requests per minute | 
**max_requests_per_hour** | **int** | Maximum API requests per hour (optional) | [optional] 

## Example

```python
from tmi_client.models.user_quota_update import UserQuotaUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of UserQuotaUpdate from a JSON string
user_quota_update_instance = UserQuotaUpdate.from_json(json)
# print the JSON string representation of the object
print(UserQuotaUpdate.to_json())

# convert the object into a dict
user_quota_update_dict = user_quota_update_instance.to_dict()
# create an instance of UserQuotaUpdate from a dict
user_quota_update_from_dict = UserQuotaUpdate.from_dict(user_quota_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


