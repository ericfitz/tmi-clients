# ConfirmIdentityLink429Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**retry_after** | **int** |  | [optional] 

## Example

```python
from tmi_client.models.confirm_identity_link429_response import ConfirmIdentityLink429Response

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmIdentityLink429Response from a JSON string
confirm_identity_link429_response_instance = ConfirmIdentityLink429Response.from_json(json)
# print the JSON string representation of the object
print(ConfirmIdentityLink429Response.to_json())

# convert the object into a dict
confirm_identity_link429_response_dict = confirm_identity_link429_response_instance.to_dict()
# create an instance of ConfirmIdentityLink429Response from a dict
confirm_identity_link429_response_from_dict = ConfirmIdentityLink429Response.from_dict(confirm_identity_link429_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


