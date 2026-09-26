# GetCurrentUser200Response

OIDC-compliant userinfo response per OpenID Connect Core 1.0 Section 5.1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub** | **str** | Subject identifier - unique identifier for the user (required per OIDC) | 
**email** | **str** | User email address | [optional] 
**name** | **str** | User display name | [optional] 
**idp** | **str** | Identity provider that authenticated the user | [optional] 
**groups** | **List[str]** | Groups the user belongs to | [optional] 

## Example

```python
from tmi_client.models.get_current_user200_response import GetCurrentUser200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCurrentUser200Response from a JSON string
get_current_user200_response_instance = GetCurrentUser200Response.from_json(json)
# print the JSON string representation of the object
print(GetCurrentUser200Response.to_json())

# convert the object into a dict
get_current_user200_response_dict = get_current_user200_response_instance.to_dict()
# create an instance of GetCurrentUser200Response from a dict
get_current_user200_response_from_dict = GetCurrentUser200Response.from_dict(get_current_user200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


