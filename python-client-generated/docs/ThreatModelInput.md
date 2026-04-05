# ThreatModelInput

Input schema for creating/updating ThreatModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the threat model | 
**description** | **str** | Description of the threat model and its purpose | [optional] 
**threat_model_framework** | **str** | The framework used for this threat model | [optional] 
**authorization** | [**List[Authorization]**](Authorization.md) | List of users and their roles for this threat model | [optional] 
**metadata** | [**List[Metadata]**](Metadata.md) | Key-value pairs for additional threat model metadata | [optional] 
**issue_uri** | **str** | URL to an issue in an issue tracking system for this threat model | [optional] 
**is_confidential** | **bool** | If true, threat model is marked as confidential. Can only be set at creation. | [optional] [default to False]

## Example

```python
from tmi_client.models.threat_model_input import ThreatModelInput

# TODO update the JSON string below
json = "{}"
# create an instance of ThreatModelInput from a JSON string
threat_model_input_instance = ThreatModelInput.from_json(json)
# print the JSON string representation of the object
print(ThreatModelInput.to_json())

# convert the object into a dict
threat_model_input_dict = threat_model_input_instance.to_dict()
# create an instance of ThreatModelInput from a dict
threat_model_input_from_dict = ThreatModelInput.from_dict(threat_model_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


