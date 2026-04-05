# ClientCredentialInfo

Client credential information without the secret

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier for the credential | 
**client_id** | **str** | OAuth 2.0 client ID (format: tmi_cc_*) | 
**name** | **str** | Human-readable name for the credential | 
**description** | **str** | Optional description of the credential&#39;s purpose | [optional] 
**is_active** | **bool** | Whether the credential is active | 
**last_used_at** | **datetime** | Last time this credential was used (ISO 8601) | [optional] 
**created_at** | **datetime** | Creation timestamp (ISO 8601) | 
**modified_at** | **datetime** | Last modification timestamp (ISO 8601) | 
**expires_at** | **datetime** | Optional expiration timestamp (ISO 8601) | [optional] 

## Example

```python
from tmi_client.models.client_credential_info import ClientCredentialInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCredentialInfo from a JSON string
client_credential_info_instance = ClientCredentialInfo.from_json(json)
# print the JSON string representation of the object
print(ClientCredentialInfo.to_json())

# convert the object into a dict
client_credential_info_dict = client_credential_info_instance.to_dict()
# create an instance of ClientCredentialInfo from a dict
client_credential_info_from_dict = ClientCredentialInfo.from_dict(client_credential_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


