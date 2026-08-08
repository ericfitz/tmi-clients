# ListAddonQuotasResponseDefaults

Server default quota values applied when a user has no quota row

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_active_invocations** | **int** | Default max active invocations limit | 
**max_invocations_per_hour** | **int** | Default max invocations-per-hour limit | 

## Example

```python
from tmi_client.models.list_addon_quotas_response_defaults import ListAddonQuotasResponseDefaults

# TODO update the JSON string below
json = "{}"
# create an instance of ListAddonQuotasResponseDefaults from a JSON string
list_addon_quotas_response_defaults_instance = ListAddonQuotasResponseDefaults.from_json(json)
# print the JSON string representation of the object
print(ListAddonQuotasResponseDefaults.to_json())

# convert the object into a dict
list_addon_quotas_response_defaults_dict = list_addon_quotas_response_defaults_instance.to_dict()
# create an instance of ListAddonQuotasResponseDefaults from a dict
list_addon_quotas_response_defaults_from_dict = ListAddonQuotasResponseDefaults.from_dict(list_addon_quotas_response_defaults_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


