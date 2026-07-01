# AuthTokenResponse

JWT token response for authentication endpoints

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | JWT access token | 
**refresh_token** | **str** | Refresh token for obtaining new access tokens | 
**token_type** | **str** | Token type | 
**expires_in** | **int** | Access token expiration time in seconds | 

## Example

```python
from tmi_client.models.auth_token_response import AuthTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthTokenResponse from a JSON string
auth_token_response_instance = AuthTokenResponse.from_json(json)
# print the JSON string representation of the object
print(AuthTokenResponse.to_json())

# convert the object into a dict
auth_token_response_dict = auth_token_response_instance.to_dict()
# create an instance of AuthTokenResponse from a dict
auth_token_response_from_dict = AuthTokenResponse.from_dict(auth_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


