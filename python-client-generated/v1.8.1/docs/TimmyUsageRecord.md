# TimmyUsageRecord

Usage record for Timmy AI assistant

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **UUID** | User identifier | [optional] 
**session_id** | **UUID** | Chat session identifier | [optional] 
**threat_model_id** | **UUID** | Threat model identifier | [optional] 
**message_count** | **int** | Number of messages in the period | [optional] 
**prompt_tokens** | **int** | Number of prompt tokens consumed | [optional] 
**completion_tokens** | **int** | Number of completion tokens consumed | [optional] 
**embedding_tokens** | **int** | Number of embedding tokens consumed | [optional] 
**period_start** | **datetime** | Start of the usage period (RFC3339) | [optional] 
**period_end** | **datetime** | End of the usage period (RFC3339) | [optional] 

## Example

```python
from tmi_client.models.timmy_usage_record import TimmyUsageRecord

# TODO update the JSON string below
json = "{}"
# create an instance of TimmyUsageRecord from a JSON string
timmy_usage_record_instance = TimmyUsageRecord.from_json(json)
# print the JSON string representation of the object
print(TimmyUsageRecord.to_json())

# convert the object into a dict
timmy_usage_record_dict = timmy_usage_record_instance.to_dict()
# create an instance of TimmyUsageRecord from a dict
timmy_usage_record_from_dict = TimmyUsageRecord.from_dict(timmy_usage_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


