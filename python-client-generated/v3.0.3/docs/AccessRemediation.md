# AccessRemediation

A suggested client- or user-facing action to resolve a document access problem. Ordered list: the first remediation in `DocumentAccessDiagnostics.remediations` is the recommended next step.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**params** | **Dict[str, object]** | Action-specific parameters. Examples: &#x60;service_account_email&#x60;, &#x60;provider_id&#x60;, &#x60;user_email&#x60; (for &#x60;share_with_service_account&#x60;); &#x60;drive_id&#x60;, &#x60;item_id&#x60;, &#x60;app_object_id&#x60;, &#x60;graph_call&#x60;, &#x60;graph_body&#x60; (for &#x60;share_with_application&#x60;). | 

## Example

```python
from tmi_client.models.access_remediation import AccessRemediation

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRemediation from a JSON string
access_remediation_instance = AccessRemediation.from_json(json)
# print the JSON string representation of the object
print(AccessRemediation.to_json())

# convert the object into a dict
access_remediation_dict = access_remediation_instance.to_dict()
# create an instance of AccessRemediation from a dict
access_remediation_from_dict = AccessRemediation.from_dict(access_remediation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


