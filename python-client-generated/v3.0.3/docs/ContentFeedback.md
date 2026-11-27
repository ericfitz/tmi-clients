# ContentFeedback


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sentiment** | **str** |  | 
**target_type** | **str** | Type of artifact the feedback targets | 
**target_id** | **UUID** | ID of the targeted artifact (note/diagram/threat). For threat_classification, the threat ID. | 
**target_field** | **str** | Required iff target_type is &#39;threat_classification&#39;; identifies the field of the threat (e.g. &#39;cwe&#39;, &#39;severity&#39;) | [optional] 
**verbatim** | **str** |  | [optional] 
**false_positive_reason** | **str** | Allowed only when sentiment&#x3D;&#39;down&#39; and target_type&#x3D;&#39;threat&#39; | [optional] 
**false_positive_subreason** | **str** | Requires false_positive_reason; a subreason without a reason is rejected with 400. Allowed only when the chosen false_positive_reason has subreasons, and must be one of that reason&#39;s subreasons: detection_misfired (code_does_not_exist, trigger_conditions_not_met), out_of_scope (component_outside_threat_model), intended_behavior (sanctioned_by_design), detection_rule_flawed (not_a_real_risk, needs_tuning). | [optional] 
**client_id** | **str** |  | 
**client_version** | **str** |  | [optional] 
**screenshot** | **str** | Optional viewport screenshot captured by the client at submission time. Data URL form (e.g. &#x60;data:image/jpeg;base64,...&#x60;). Used as support context. | [optional] 
**id** | **UUID** |  | 
**threat_model_id** | **UUID** |  | 
**created_by** | **UUID** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from tmi_client.models.content_feedback import ContentFeedback

# TODO update the JSON string below
json = "{}"
# create an instance of ContentFeedback from a JSON string
content_feedback_instance = ContentFeedback.from_json(json)
# print the JSON string representation of the object
print(ContentFeedback.to_json())

# convert the object into a dict
content_feedback_dict = content_feedback_instance.to_dict()
# create an instance of ContentFeedback from a dict
content_feedback_from_dict = ContentFeedback.from_dict(content_feedback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


