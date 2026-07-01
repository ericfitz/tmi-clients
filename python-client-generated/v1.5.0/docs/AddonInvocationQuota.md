# AddonInvocationQuota

Addon invocation quota for a user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_id** | **UUID** | User ID | 
**max_active_invocations** | **int** | Maximum concurrent active addon invocations | 
**max_invocations_per_hour** | **int** | Maximum addon invocations per hour | 
**created_at** | **datetime** | Creation timestamp | 
**modified_at** | **datetime** | Last modification timestamp | 

## Example

```python
from tmi_client.models.addon_invocation_quota import AddonInvocationQuota

# TODO update the JSON string below
json = "{}"
# create an instance of AddonInvocationQuota from a JSON string
addon_invocation_quota_instance = AddonInvocationQuota.from_json(json)
# print the JSON string representation of the object
print(AddonInvocationQuota.to_json())

# convert the object into a dict
addon_invocation_quota_dict = addon_invocation_quota_instance.to_dict()
# create an instance of AddonInvocationQuota from a dict
addon_invocation_quota_from_dict = AddonInvocationQuota.from_dict(addon_invocation_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


