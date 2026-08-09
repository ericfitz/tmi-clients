# StepUpAuthenticate200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | 
**redirect_url** | **str** | Upstream IdP authorization URL (with fresh-prompt parameters appended) the client must top-level navigate to. Present only when result&#x3D;&#39;step_up_redirect&#39;. | [optional] 
**provider** | **str** | Present only when result&#x3D;&#39;step_up_weak_complete&#39;. | [optional] 
**auth_time** | **int** | Present only when result&#x3D;&#39;step_up_weak_complete&#39;. | [optional] 
**message** | **str** | Present only when result&#x3D;&#39;step_up_weak_complete&#39;. | [optional] 

## Example

```python
from tmi_client.models.step_up_authenticate200_response import StepUpAuthenticate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of StepUpAuthenticate200Response from a JSON string
step_up_authenticate200_response_instance = StepUpAuthenticate200Response.from_json(json)
# print the JSON string representation of the object
print(StepUpAuthenticate200Response.to_json())

# convert the object into a dict
step_up_authenticate200_response_dict = step_up_authenticate200_response_instance.to_dict()
# create an instance of StepUpAuthenticate200Response from a dict
step_up_authenticate200_response_from_dict = StepUpAuthenticate200Response.from_dict(step_up_authenticate200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


