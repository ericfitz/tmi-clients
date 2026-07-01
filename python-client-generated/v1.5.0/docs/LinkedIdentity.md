# LinkedIdentity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Linked identity unique identifier | 
**provider** | **str** | Identity provider ID | 
**provider_user_id** | **str** | User identifier at the provider (truncated for display) | 
**email** | **str** | Cached email address from provider (display only) | [optional] 
**name** | **str** | Cached display name from provider | [optional] 
**linked_at** | **datetime** | When this identity was linked | 
**last_used_at** | **datetime** | When this identity was last used to sign in | [optional] 

## Example

```python
from tmi_client.models.linked_identity import LinkedIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedIdentity from a JSON string
linked_identity_instance = LinkedIdentity.from_json(json)
# print the JSON string representation of the object
print(LinkedIdentity.to_json())

# convert the object into a dict
linked_identity_dict = linked_identity_instance.to_dict()
# create an instance of LinkedIdentity from a dict
linked_identity_from_dict = LinkedIdentity.from_dict(linked_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


