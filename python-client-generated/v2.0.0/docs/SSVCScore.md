# SSVCScore

SSVC (Stakeholder-Specific Vulnerability Categorization) assessment result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vector** | **str** | SSVC vector string following CERT/CC convention (e.g., SSVCv2/E:A/U:S/T:T/P:S/2026-04-08/) | 
**decision** | **str** | SSVC decision outcome | 
**methodology** | **str** | The SSVC stakeholder perspective used for assessment | 

## Example

```python
from tmi_client.models.ssvc_score import SSVCScore

# TODO update the JSON string below
json = "{}"
# create an instance of SSVCScore from a JSON string
ssvc_score_instance = SSVCScore.from_json(json)
# print the JSON string representation of the object
print(SSVCScore.to_json())

# convert the object into a dict
ssvc_score_dict = ssvc_score_instance.to_dict()
# create an instance of SSVCScore from a dict
ssvc_score_from_dict = SSVCScore.from_dict(ssvc_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


