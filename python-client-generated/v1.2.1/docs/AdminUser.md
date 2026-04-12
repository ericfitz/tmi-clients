# AdminUser

User object with administrative fields and enriched data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_uuid** | **UUID** | Internal system UUID for the user | 
**provider** | **str** | OAuth/SAML provider identifier | 
**provider_user_id** | **str** | Provider-assigned user identifier | 
**email** | **str** | User email address | 
**name** | **str** | User display name | 
**email_verified** | **bool** | Whether the email has been verified | 
**created_at** | **datetime** | Account creation timestamp | 
**modified_at** | **datetime** | Last modification timestamp | 
**last_login** | **datetime** | Last login timestamp | [optional] 
**is_admin** | **bool** | Whether the user has administrator privileges (enriched) | [optional] [readonly] 
**groups** | **List[str]** | List of group names the user belongs to (enriched) | [optional] [readonly] 
**active_threat_models** | **int** | Number of active threat models owned by user (enriched) | [optional] [readonly] 

## Example

```python
from tmi_client.models.admin_user import AdminUser

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUser from a JSON string
admin_user_instance = AdminUser.from_json(json)
# print the JSON string representation of the object
print(AdminUser.to_json())

# convert the object into a dict
admin_user_dict = admin_user_instance.to_dict()
# create an instance of AdminUser from a dict
admin_user_from_dict = AdminUser.from_dict(admin_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


