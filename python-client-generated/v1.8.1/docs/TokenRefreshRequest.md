# TokenRefreshRequest

OAuth 2.0 refresh token request. The refresh token may be supplied either in this body or via the HttpOnly refresh cookie (browser SPA flow); at least one must be present.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refresh_token** | **str** | Refresh token. Optional: browser SPA clients may omit it and send an empty body, in which case the server reads the refresh token from the HttpOnly refresh cookie. Non-browser clients should supply it in the body. | [optional] 

## Example

```python
from tmi_client.models.token_refresh_request import TokenRefreshRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenRefreshRequest from a JSON string
token_refresh_request_instance = TokenRefreshRequest.from_json(json)
# print the JSON string representation of the object
print(TokenRefreshRequest.to_json())

# convert the object into a dict
token_refresh_request_dict = token_refresh_request_instance.to_dict()
# create an instance of TokenRefreshRequest from a dict
token_refresh_request_from_dict = TokenRefreshRequest.from_dict(token_refresh_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


