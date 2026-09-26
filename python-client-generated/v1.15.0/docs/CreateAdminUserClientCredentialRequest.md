# CreateAdminUserClientCredentialRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable name for the credential | 
**description** | **str** | Optional description of the credential&#39;s purpose | [optional] 
**expires_at** | **datetime** | Optional expiration timestamp (ISO 8601) | [optional] 
**direct_write** | **bool** | Opt in to direct writes for this automation account: tokens from this credential may modify threat-model sub-resources, authorized by the automation user&#39;s roles. Omitting the field is the same as false. Rejected with 400 when the automation user is a member of the Administrators group. | [optional] [default to False]
**addon_id** | **UUID** | Optional addon to link this credential to (only valid with direct_write&#x3D;true; 400 otherwise, or if the addon does not exist). Events caused by writes made with tokens from this credential are not delivered to the linked addon&#39;s own webhook subscription, matching the suppression applied to delegation-token write-backs. Not a foreign key: deleting the addon leaves the credential intact and simply stops the suppression. | [optional] 

## Example

```python
from tmi_client.models.create_admin_user_client_credential_request import CreateAdminUserClientCredentialRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminUserClientCredentialRequest from a JSON string
create_admin_user_client_credential_request_instance = CreateAdminUserClientCredentialRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAdminUserClientCredentialRequest.to_json())

# convert the object into a dict
create_admin_user_client_credential_request_dict = create_admin_user_client_credential_request_instance.to_dict()
# create an instance of CreateAdminUserClientCredentialRequest from a dict
create_admin_user_client_credential_request_from_dict = CreateAdminUserClientCredentialRequest.from_dict(create_admin_user_client_credential_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


