# TransferOwnershipRequest

Request to transfer ownership of all owned threat models and survey responses to another user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_user_id** | **UUID** | Internal UUID of the user to receive ownership | 

## Example

```python
from tmi_client.models.transfer_ownership_request import TransferOwnershipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransferOwnershipRequest from a JSON string
transfer_ownership_request_instance = TransferOwnershipRequest.from_json(json)
# print the JSON string representation of the object
print(TransferOwnershipRequest.to_json())

# convert the object into a dict
transfer_ownership_request_dict = transfer_ownership_request_instance.to_dict()
# create an instance of TransferOwnershipRequest from a dict
transfer_ownership_request_from_dict = TransferOwnershipRequest.from_dict(transfer_ownership_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


