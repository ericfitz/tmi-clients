# MigrateSystemSettings200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migrated** | **int** | Number of settings migrated (created or updated) | 
**skipped** | **int** | Number of settings skipped (already exist and overwrite&#x3D;false) | 
**settings** | [**List[SystemSetting]**](SystemSetting.md) | List of settings that were migrated | 

## Example

```python
from tmi_client.models.migrate_system_settings200_response import MigrateSystemSettings200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MigrateSystemSettings200Response from a JSON string
migrate_system_settings200_response_instance = MigrateSystemSettings200Response.from_json(json)
# print the JSON string representation of the object
print(MigrateSystemSettings200Response.to_json())

# convert the object into a dict
migrate_system_settings200_response_dict = migrate_system_settings200_response_instance.to_dict()
# create an instance of MigrateSystemSettings200Response from a dict
migrate_system_settings200_response_from_dict = MigrateSystemSettings200Response.from_dict(migrate_system_settings200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


