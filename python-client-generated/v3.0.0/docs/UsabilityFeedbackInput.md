# UsabilityFeedbackInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sentiment** | **str** | User sentiment | 
**verbatim** | **str** | Optional free-text comment from the user | [optional] 
**surface** | **str** | Logical UI-surface identifier (developer-supplied tag for analytics) | 
**client_id** | **str** | Identifier of the client emitting the feedback (e.g., &#39;tmi-ux&#39;) | 
**client_version** | **str** | Semver version string of the client | [optional] 
**client_build** | **str** | Short commit hash of the client build | [optional] 
**user_agent** | **str** | Browser User-Agent header value (when applicable) | [optional] 
**user_agent_data** | **Dict[str, object]** | Optional NavigatorUAData payload (≤ 4 KB serialized) | [optional] 
**viewport** | **str** | Viewport dimensions, e.g. &#39;1280x1024&#39; | [optional] 
**screenshot** | **str** | Optional viewport screenshot captured by the client at submission time. Data URL form (e.g. &#x60;data:image/jpeg;base64,...&#x60;). Used as support context. | [optional] 

## Example

```python
from tmi_client.models.usability_feedback_input import UsabilityFeedbackInput

# TODO update the JSON string below
json = "{}"
# create an instance of UsabilityFeedbackInput from a JSON string
usability_feedback_input_instance = UsabilityFeedbackInput.from_json(json)
# print the JSON string representation of the object
print(UsabilityFeedbackInput.to_json())

# convert the object into a dict
usability_feedback_input_dict = usability_feedback_input_instance.to_dict()
# create an instance of UsabilityFeedbackInput from a dict
usability_feedback_input_from_dict = UsabilityFeedbackInput.from_dict(usability_feedback_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


