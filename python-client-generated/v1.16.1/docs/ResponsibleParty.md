# ResponsibleParty

A responsible party for a team or project with their role

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **UUID** | UUID of the responsible party user | 
**user** | [**User**](User.md) | Resolved user details (read-only, populated by server) | [optional] [readonly] 
**role** | [**TeamMemberRole**](TeamMemberRole.md) |  | [optional] 
**custom_role** | **str** | Custom role description when role is &#39;other&#39; | [optional] 

## Example

```python
from tmi_client.models.responsible_party import ResponsibleParty

# TODO update the JSON string below
json = "{}"
# create an instance of ResponsibleParty from a JSON string
responsible_party_instance = ResponsibleParty.from_json(json)
# print the JSON string representation of the object
print(ResponsibleParty.to_json())

# convert the object into a dict
responsible_party_dict = responsible_party_instance.to_dict()
# create an instance of ResponsibleParty from a dict
responsible_party_from_dict = ResponsibleParty.from_dict(responsible_party_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


