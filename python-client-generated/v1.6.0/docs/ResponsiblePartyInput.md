# ResponsiblePartyInput

Client-writable fields of ResponsibleParty (excludes the server-resolved user).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **UUID** | UUID of the responsible party user | 
**role** | [**TeamMemberRole**](TeamMemberRole.md) |  | [optional] 
**custom_role** | **str** | Custom role description when role is &#39;other&#39; | [optional] 

## Example

```python
from tmi_client.models.responsible_party_input import ResponsiblePartyInput

# TODO update the JSON string below
json = "{}"
# create an instance of ResponsiblePartyInput from a JSON string
responsible_party_input_instance = ResponsiblePartyInput.from_json(json)
# print the JSON string representation of the object
print(ResponsiblePartyInput.to_json())

# convert the object into a dict
responsible_party_input_dict = responsible_party_input_instance.to_dict()
# create an instance of ResponsiblePartyInput from a dict
responsible_party_input_from_dict = ResponsiblePartyInput.from_dict(responsible_party_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


