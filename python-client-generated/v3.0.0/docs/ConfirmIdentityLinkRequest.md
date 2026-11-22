# ConfirmIdentityLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Pending identity link token from the callback redirect | 

## Example

```python
from tmi_client.models.confirm_identity_link_request import ConfirmIdentityLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmIdentityLinkRequest from a JSON string
confirm_identity_link_request_instance = ConfirmIdentityLinkRequest.from_json(json)
# print the JSON string representation of the object
print(ConfirmIdentityLinkRequest.to_json())

# convert the object into a dict
confirm_identity_link_request_dict = confirm_identity_link_request_instance.to_dict()
# create an instance of ConfirmIdentityLinkRequest from a dict
confirm_identity_link_request_from_dict = ConfirmIdentityLinkRequest.from_dict(confirm_identity_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


