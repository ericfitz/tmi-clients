# AddonQuotaUpdate

Configuration update for addon invocation quotas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_active_invocations** | **int** | Maximum concurrent active addon invocations | 
**max_invocations_per_hour** | **int** | Maximum addon invocations per hour | 

## Example

```python
from tmi_client.models.addon_quota_update import AddonQuotaUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AddonQuotaUpdate from a JSON string
addon_quota_update_instance = AddonQuotaUpdate.from_json(json)
# print the JSON string representation of the object
print(AddonQuotaUpdate.to_json())

# convert the object into a dict
addon_quota_update_dict = addon_quota_update_instance.to_dict()
# create an instance of AddonQuotaUpdate from a dict
addon_quota_update_from_dict = AddonQuotaUpdate.from_dict(addon_quota_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


