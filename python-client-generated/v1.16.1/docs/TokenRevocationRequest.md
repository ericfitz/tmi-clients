# TokenRevocationRequest

OAuth 2.0 token revocation request per RFC 7009

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | The token to be revoked (access token or refresh token) | 
**token_type_hint** | **str** | A hint about the type of the token. If omitted, the server will attempt to determine the token type. | [optional] 
**client_id** | **str** | Client identifier for client credentials authentication (alternative to Bearer token) | [optional] 
**client_secret** | **str** | Client secret (required if client_id is provided) | [optional] 

## Example

```python
from tmi_client.models.token_revocation_request import TokenRevocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenRevocationRequest from a JSON string
token_revocation_request_instance = TokenRevocationRequest.from_json(json)
# print the JSON string representation of the object
print(TokenRevocationRequest.to_json())

# convert the object into a dict
token_revocation_request_dict = token_revocation_request_instance.to_dict()
# create an instance of TokenRevocationRequest from a dict
token_revocation_request_from_dict = TokenRevocationRequest.from_dict(token_revocation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


