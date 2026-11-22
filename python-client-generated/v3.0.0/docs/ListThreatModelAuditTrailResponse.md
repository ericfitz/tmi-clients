# ListThreatModelAuditTrailResponse

Cursor-paginated list of audit trail entries for a threat model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audit_entries** | [**List[AuditEntry]**](AuditEntry.md) |  | 
**total** | **int** | Total number of matching audit entries | 
**limit** | **int** | Maximum number of entries returned | 
**next_cursor** | **str** | Cursor for the next (older) page; absent or null when exhausted. | [optional] 
**prev_cursor** | **str** | Cursor for the previous (newer) page; absent or null when at the newest end. | [optional] 

## Example

```python
from tmi_client.models.list_threat_model_audit_trail_response import ListThreatModelAuditTrailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListThreatModelAuditTrailResponse from a JSON string
list_threat_model_audit_trail_response_instance = ListThreatModelAuditTrailResponse.from_json(json)
# print the JSON string representation of the object
print(ListThreatModelAuditTrailResponse.to_json())

# convert the object into a dict
list_threat_model_audit_trail_response_dict = list_threat_model_audit_trail_response_instance.to_dict()
# create an instance of ListThreatModelAuditTrailResponse from a dict
list_threat_model_audit_trail_response_from_dict = ListThreatModelAuditTrailResponse.from_dict(list_threat_model_audit_trail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


