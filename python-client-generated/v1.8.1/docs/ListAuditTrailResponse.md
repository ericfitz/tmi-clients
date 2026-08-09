# ListAuditTrailResponse

Paginated list of audit trail entries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audit_entries** | [**List[AuditEntry]**](AuditEntry.md) |  | 
**total** | **int** | Total number of matching audit entries | 
**limit** | **int** | Maximum number of entries returned | 
**offset** | **int** | Offset from the beginning of the result set | 

## Example

```python
from tmi_client.models.list_audit_trail_response import ListAuditTrailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAuditTrailResponse from a JSON string
list_audit_trail_response_instance = ListAuditTrailResponse.from_json(json)
# print the JSON string representation of the object
print(ListAuditTrailResponse.to_json())

# convert the object into a dict
list_audit_trail_response_dict = list_audit_trail_response_instance.to_dict()
# create an instance of ListAuditTrailResponse from a dict
list_audit_trail_response_from_dict = ListAuditTrailResponse.from_dict(list_audit_trail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


