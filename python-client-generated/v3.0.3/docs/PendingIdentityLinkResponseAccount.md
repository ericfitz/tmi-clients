# PendingIdentityLinkResponseAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | Primary identity provider of this TMI account | 
**email** | **str** | Email address of this TMI account | 

## Example

```python
from tmi_client.models.pending_identity_link_response_account import PendingIdentityLinkResponseAccount

# TODO update the JSON string below
json = "{}"
# create an instance of PendingIdentityLinkResponseAccount from a JSON string
pending_identity_link_response_account_instance = PendingIdentityLinkResponseAccount.from_json(json)
# print the JSON string representation of the object
print(PendingIdentityLinkResponseAccount.to_json())

# convert the object into a dict
pending_identity_link_response_account_dict = pending_identity_link_response_account_instance.to_dict()
# create an instance of PendingIdentityLinkResponseAccount from a dict
pending_identity_link_response_account_from_dict = PendingIdentityLinkResponseAccount.from_dict(pending_identity_link_response_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


