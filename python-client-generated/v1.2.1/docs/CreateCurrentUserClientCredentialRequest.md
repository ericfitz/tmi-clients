# CreateCurrentUserClientCredentialRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable name for the credential | 
**description** | **str** | Optional description of the credential&#39;s purpose | [optional] 
**expires_at** | **datetime** | Optional expiration timestamp (ISO 8601) | [optional] 

## Example

```python
from tmi_client.models.create_current_user_client_credential_request import CreateCurrentUserClientCredentialRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCurrentUserClientCredentialRequest from a JSON string
create_current_user_client_credential_request_instance = CreateCurrentUserClientCredentialRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCurrentUserClientCredentialRequest.to_json())

# convert the object into a dict
create_current_user_client_credential_request_dict = create_current_user_client_credential_request_instance.to_dict()
# create an instance of CreateCurrentUserClientCredentialRequest from a dict
create_current_user_client_credential_request_from_dict = CreateCurrentUserClientCredentialRequest.from_dict(create_current_user_client_credential_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


