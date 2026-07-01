# CVSSScore

CVSS vector and score pair

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vector** | **str** | CVSS vector string (e.g., CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | 
**score** | **float** | CVSS score (0.0-10.0) | 

## Example

```python
from tmi_client.models.cvss_score import CVSSScore

# TODO update the JSON string below
json = "{}"
# create an instance of CVSSScore from a JSON string
cvss_score_instance = CVSSScore.from_json(json)
# print the JSON string representation of the object
print(CVSSScore.to_json())

# convert the object into a dict
cvss_score_dict = cvss_score_instance.to_dict()
# create an instance of CVSSScore from a dict
cvss_score_from_dict = CVSSScore.from_dict(cvss_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


