# PendingIdentityLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pending** | [**PendingIdentityLinkResponsePending**](PendingIdentityLinkResponsePending.md) |  | 
**account** | [**PendingIdentityLinkResponseAccount**](PendingIdentityLinkResponseAccount.md) |  | 

## Example

```python
from tmi_client.models.pending_identity_link_response import PendingIdentityLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PendingIdentityLinkResponse from a JSON string
pending_identity_link_response_instance = PendingIdentityLinkResponse.from_json(json)
# print the JSON string representation of the object
print(PendingIdentityLinkResponse.to_json())

# convert the object into a dict
pending_identity_link_response_dict = pending_identity_link_response_instance.to_dict()
# create an instance of PendingIdentityLinkResponse from a dict
pending_identity_link_response_from_dict = PendingIdentityLinkResponse.from_dict(pending_identity_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


