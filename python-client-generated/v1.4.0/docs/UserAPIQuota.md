# UserAPIQuota

API rate limit and quota configuration for a user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **UUID** | User ID | 
**max_requests_per_minute** | **int** | Maximum API requests per minute | 
**max_requests_per_hour** | **int** | Maximum API requests per hour (optional) | [optional] 
**created_at** | **datetime** | Creation timestamp | 
**modified_at** | **datetime** | Last modification timestamp | 

## Example

```python
from tmi_client.models.user_api_quota import UserAPIQuota

# TODO update the JSON string below
json = "{}"
# create an instance of UserAPIQuota from a JSON string
user_api_quota_instance = UserAPIQuota.from_json(json)
# print the JSON string representation of the object
print(UserAPIQuota.to_json())

# convert the object into a dict
user_api_quota_dict = user_api_quota_instance.to_dict()
# create an instance of UserAPIQuota from a dict
user_api_quota_from_dict = UserAPIQuota.from_dict(user_api_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


