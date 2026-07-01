# ClientCredentialResponse

Response from creating a client credential. WARNING: The client_secret is ONLY returned once and cannot be retrieved later.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier for the credential | 
**client_id** | **str** | OAuth 2.0 client ID (format: tmi_cc_*) | 
**client_secret** | **str** | OAuth 2.0 client secret - ONLY returned at creation time, cannot be retrieved later | 
**name** | **str** | Human-readable name for the credential | 
**description** | **str** | Optional description of the credential&#39;s purpose | [optional] 
**created_at** | **datetime** | Creation timestamp (ISO 8601) | 
**expires_at** | **datetime** | Optional expiration timestamp (ISO 8601) | [optional] 

## Example

```python
from tmi_client.models.client_credential_response import ClientCredentialResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCredentialResponse from a JSON string
client_credential_response_instance = ClientCredentialResponse.from_json(json)
# print the JSON string representation of the object
print(ClientCredentialResponse.to_json())

# convert the object into a dict
client_credential_response_dict = client_credential_response_instance.to_dict()
# create an instance of ClientCredentialResponse from a dict
client_credential_response_from_dict = ClientCredentialResponse.from_dict(client_credential_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


