# RollbackResponse

Result of a rollback operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**restored_entity** | **object** | The entity restored to its previous state | [optional] 
**audit_entry** | [**AuditEntry**](AuditEntry.md) | The new audit entry recording the rollback | 

## Example

```python
from tmi_client.models.rollback_response import RollbackResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RollbackResponse from a JSON string
rollback_response_instance = RollbackResponse.from_json(json)
# print the JSON string representation of the object
print(RollbackResponse.to_json())

# convert the object into a dict
rollback_response_dict = rollback_response_instance.to_dict()
# create an instance of RollbackResponse from a dict
rollback_response_from_dict = RollbackResponse.from_dict(rollback_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


