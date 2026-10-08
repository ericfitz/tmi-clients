# IdentityLinkStartResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_state** | **str** | Opaque state identifier for the link flow | 
**authorization_url** | **str** | URL to redirect the user to for identity provider authorization (prompt&#x3D;select_account) | 
**expires_at** | **datetime** | When the link state expires (10 minutes from creation) | 

## Example

```python
from tmi_client.models.identity_link_start_response import IdentityLinkStartResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityLinkStartResponse from a JSON string
identity_link_start_response_instance = IdentityLinkStartResponse.from_json(json)
# print the JSON string representation of the object
print(IdentityLinkStartResponse.to_json())

# convert the object into a dict
identity_link_start_response_dict = identity_link_start_response_instance.to_dict()
# create an instance of IdentityLinkStartResponse from a dict
identity_link_start_response_from_dict = IdentityLinkStartResponse.from_dict(identity_link_start_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


