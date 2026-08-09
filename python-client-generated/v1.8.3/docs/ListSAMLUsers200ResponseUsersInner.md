# ListSAMLUsers200ResponseUsersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_uuid** | **UUID** | TMI-internal identifier for the user. | 
**email** | **str** | User&#39;s email address as asserted by the identity provider. | 
**name** | **str** | User&#39;s display name. | 
**last_login** | **datetime** | When the user last authenticated. Omitted if the user has never logged in. | [optional] 

## Example

```python
from tmi_client.models.list_saml_users200_response_users_inner import ListSAMLUsers200ResponseUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListSAMLUsers200ResponseUsersInner from a JSON string
list_saml_users200_response_users_inner_instance = ListSAMLUsers200ResponseUsersInner.from_json(json)
# print the JSON string representation of the object
print(ListSAMLUsers200ResponseUsersInner.to_json())

# convert the object into a dict
list_saml_users200_response_users_inner_dict = list_saml_users200_response_users_inner_instance.to_dict()
# create an instance of ListSAMLUsers200ResponseUsersInner from a dict
list_saml_users200_response_users_inner_from_dict = ListSAMLUsers200ResponseUsersInner.from_dict(list_saml_users200_response_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


