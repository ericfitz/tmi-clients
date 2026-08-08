# TimmyStatusResponse

Timmy AI assistant system status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory_used_bytes** | **int** | Current memory usage in bytes | 
**memory_budget_bytes** | **int** | Total memory budget in bytes | 
**memory_utilization_pct** | **float** | Memory utilization percentage | 
**loaded_indexes** | **int** | Number of currently loaded indexes | 
**active_sessions** | **int** | Number of active chat sessions | 
**evictions_total** | **int** | Total number of index evictions | 
**evictions_pressure** | **int** | Number of evictions due to memory pressure | 
**sessions_rejected_total** | **int** | Total number of sessions rejected due to resource constraints | 

## Example

```python
from tmi_client.models.timmy_status_response import TimmyStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TimmyStatusResponse from a JSON string
timmy_status_response_instance = TimmyStatusResponse.from_json(json)
# print the JSON string representation of the object
print(TimmyStatusResponse.to_json())

# convert the object into a dict
timmy_status_response_dict = timmy_status_response_instance.to_dict()
# create an instance of TimmyStatusResponse from a dict
timmy_status_response_from_dict = TimmyStatusResponse.from_dict(timmy_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


