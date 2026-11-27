# PendingIdentityLinkResponsePending


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | Identity provider of the second identity | 
**provider_user_id** | **str** | User identifier at the provider (first 8 chars + ellipsis) | 
**email** | **str** | Cached email from the second identity (display only) | [optional] 
**name** | **str** | Cached display name from the second identity | [optional] 

## Example

```python
from tmi_client.models.pending_identity_link_response_pending import PendingIdentityLinkResponsePending

# TODO update the JSON string below
json = "{}"
# create an instance of PendingIdentityLinkResponsePending from a JSON string
pending_identity_link_response_pending_instance = PendingIdentityLinkResponsePending.from_json(json)
# print the JSON string representation of the object
print(PendingIdentityLinkResponsePending.to_json())

# convert the object into a dict
pending_identity_link_response_pending_dict = pending_identity_link_response_pending_instance.to_dict()
# create an instance of PendingIdentityLinkResponsePending from a dict
pending_identity_link_response_pending_from_dict = PendingIdentityLinkResponsePending.from_dict(pending_identity_link_response_pending_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


