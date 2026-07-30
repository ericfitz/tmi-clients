# AdminGroup

Group object with administrative fields and enriched data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_uuid** | **UUID** | Internal system UUID for the group | 
**provider** | **str** | OAuth/SAML provider identifier, or \&quot;tmi\&quot; for TMI built-in groups | 
**group_name** | **str** | Provider-assigned group name | 
**name** | **str** | Human-readable group name | [optional] 
**description** | **str** | Group description | [optional] 
**first_used** | **datetime** | First time this group was referenced | 
**last_used** | **datetime** | Last time this group was referenced | 
**usage_count** | **int** | Number of times this group has been referenced | 
**used_in_authorizations** | **bool** | Whether this group is used in any authorizations (enriched) | [optional] [readonly] 
**used_in_admin_grants** | **bool** | Whether this group is used in any admin grants (enriched) | [optional] [readonly] 
**member_count** | **int** | Number of members in the group from IdP (enriched, if available) | [optional] [readonly] 

## Example

```python
from tmi_client.models.admin_group import AdminGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AdminGroup from a JSON string
admin_group_instance = AdminGroup.from_json(json)
# print the JSON string representation of the object
print(AdminGroup.to_json())

# convert the object into a dict
admin_group_dict = admin_group_instance.to_dict()
# create an instance of AdminGroup from a dict
admin_group_from_dict = AdminGroup.from_dict(admin_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


