# SystemSetting

A system-wide configuration setting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Unique setting identifier using dot notation (e.g., rate_limit.requests_per_minute) | 
**value** | **str** | Setting value as a string (interpreted based on type) | 
**type** | **str** | Data type of the setting value | 
**description** | **str** | Human-readable description of the setting | [optional] 
**modified_at** | **datetime** | When the setting was last modified | [optional] 
**modified_by** | **UUID** | UUID of the user who last modified the setting | [optional] 
**source** | **str** | Where the effective value of this setting comes from. Server-managed, not writable. | [optional] [readonly] 
**read_only** | **bool** | Whether this setting can be modified via the API. True when source is not database. | [optional] [readonly] 

## Example

```python
from tmi_client.models.system_setting import SystemSetting

# TODO update the JSON string below
json = "{}"
# create an instance of SystemSetting from a JSON string
system_setting_instance = SystemSetting.from_json(json)
# print the JSON string representation of the object
print(SystemSetting.to_json())

# convert the object into a dict
system_setting_dict = system_setting_instance.to_dict()
# create an instance of SystemSetting from a dict
system_setting_from_dict = SystemSetting.from_dict(system_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


