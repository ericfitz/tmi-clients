# ListSystemAuditEntriesResponse

Cursor-paginated list of system audit entries.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[SystemAuditEntry]**](SystemAuditEntry.md) |  | 
**total** | **int** | Total entries matching the filter. | 
**limit** | **int** | Page size used. | 
**next_cursor** | **str** | Cursor for the next page; absent or null when exhausted. | [optional] 
**prev_cursor** | **str** | Cursor for the previous (newer) page; absent or null when at the newest end. | [optional] 

## Example

```python
from tmi_client.models.list_system_audit_entries_response import ListSystemAuditEntriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListSystemAuditEntriesResponse from a JSON string
list_system_audit_entries_response_instance = ListSystemAuditEntriesResponse.from_json(json)
# print the JSON string representation of the object
print(ListSystemAuditEntriesResponse.to_json())

# convert the object into a dict
list_system_audit_entries_response_dict = list_system_audit_entries_response_instance.to_dict()
# create an instance of ListSystemAuditEntriesResponse from a dict
list_system_audit_entries_response_from_dict = ListSystemAuditEntriesResponse.from_dict(list_system_audit_entries_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


