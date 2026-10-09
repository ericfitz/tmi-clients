# SystemAuditEntry

An immutable system-level audit record of a successful /admin/* write (T7 evidence). Old/new values are redacted at write time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Entry identifier. | 
**actor** | [**AuditActor**](AuditActor.md) |  | 
**http_method** | **str** | HTTP method of the audited request. | 
**http_path** | **str** | Request path of the audited request. | 
**field_path** | **str** | Dotted path of the changed field. | 
**old_value_redacted** | **str** | Previous value, redacted at write time. | [optional] 
**new_value_redacted** | **str** | New value, redacted at write time. | [optional] 
**change_summary** | **str** | Human-readable change summary. | [optional] 
**created_at** | **datetime** | When the audited write completed. | 

## Example

```python
from tmi_client.models.system_audit_entry import SystemAuditEntry

# TODO update the JSON string below
json = "{}"
# create an instance of SystemAuditEntry from a JSON string
system_audit_entry_instance = SystemAuditEntry.from_json(json)
# print the JSON string representation of the object
print(SystemAuditEntry.to_json())

# convert the object into a dict
system_audit_entry_dict = system_audit_entry_instance.to_dict()
# create an instance of SystemAuditEntry from a dict
system_audit_entry_from_dict = SystemAuditEntry.from_dict(system_audit_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


