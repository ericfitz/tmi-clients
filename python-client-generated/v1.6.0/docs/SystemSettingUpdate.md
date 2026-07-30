# SystemSettingUpdate

Request body for creating or updating a system setting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Setting value as a string (interpreted based on type) | 
**type** | **str** | Data type of the setting value | 
**description** | **str** | Human-readable description of the setting | [optional] 

## Example

```python
from tmi_client.models.system_setting_update import SystemSettingUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SystemSettingUpdate from a JSON string
system_setting_update_instance = SystemSettingUpdate.from_json(json)
# print the JSON string representation of the object
print(SystemSettingUpdate.to_json())

# convert the object into a dict
system_setting_update_dict = system_setting_update_instance.to_dict()
# create an instance of SystemSettingUpdate from a dict
system_setting_update_from_dict = SystemSettingUpdate.from_dict(system_setting_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


