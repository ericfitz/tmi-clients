# AuthorizeContentTokenRequest

Authorize request body.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_callback** | **str** | Client URL to redirect back to after the content-OAuth callback completes. Must match the server-side allow list. | 

## Example

```python
from tmi_client.models.authorize_content_token_request import AuthorizeContentTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizeContentTokenRequest from a JSON string
authorize_content_token_request_instance = AuthorizeContentTokenRequest.from_json(json)
# print the JSON string representation of the object
print(AuthorizeContentTokenRequest.to_json())

# convert the object into a dict
authorize_content_token_request_dict = authorize_content_token_request_instance.to_dict()
# create an instance of AuthorizeContentTokenRequest from a dict
authorize_content_token_request_from_dict = AuthorizeContentTokenRequest.from_dict(authorize_content_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


