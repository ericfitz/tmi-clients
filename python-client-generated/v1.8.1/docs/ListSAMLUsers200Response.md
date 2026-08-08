# ListSAMLUsers200Response

Lightweight SAML user list for UI autocomplete.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idp** | **str** | Identity provider the users belong to; always equals the {idp} path parameter. | 
**users** | [**List[ListSAMLUsers200ResponseUsersInner]**](ListSAMLUsers200ResponseUsersInner.md) | Users from this identity provider, most recently logged in first. | 
**total** | **int** | Total users matching the filter, ignoring limit/offset. | 

## Example

```python
from tmi_client.models.list_saml_users200_response import ListSAMLUsers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListSAMLUsers200Response from a JSON string
list_saml_users200_response_instance = ListSAMLUsers200Response.from_json(json)
# print the JSON string representation of the object
print(ListSAMLUsers200Response.to_json())

# convert the object into a dict
list_saml_users200_response_dict = list_saml_users200_response_instance.to_dict()
# create an instance of ListSAMLUsers200Response from a dict
list_saml_users200_response_from_dict = ListSAMLUsers200Response.from_dict(list_saml_users200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


