# AuditEntry

An entry in the audit trail recording a mutation to an entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier for the audit entry | 
**threat_model_id** | **UUID** | ID of the threat model this audit entry belongs to | 
**object_type** | **str** | Type of the entity that was mutated | 
**object_id** | **UUID** | ID of the entity that was mutated | 
**version** | **int** | Version number. Null if the version snapshot has been pruned and rollback is no longer available. | [optional] 
**change_type** | **str** | Type of mutation | 
**actor** | [**AuditActor**](AuditActor.md) |  | 
**change_summary** | **str** | Human-readable summary of what changed | [optional] 
**created_at** | **datetime** | When the mutation occurred | 

## Example

```python
from tmi_client.models.audit_entry import AuditEntry

# TODO update the JSON string below
json = "{}"
# create an instance of AuditEntry from a JSON string
audit_entry_instance = AuditEntry.from_json(json)
# print the JSON string representation of the object
print(AuditEntry.to_json())

# convert the object into a dict
audit_entry_dict = audit_entry_instance.to_dict()
# create an instance of AuditEntry from a dict
audit_entry_from_dict = AuditEntry.from_dict(audit_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


