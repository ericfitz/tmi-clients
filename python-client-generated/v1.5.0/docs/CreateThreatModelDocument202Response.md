# CreateThreatModelDocument202Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document** | [**Document**](Document.md) |  | 
**job_id** | **UUID** | Identifier of the queued extraction job, for client correlation. The extraction result is surfaced via the document access_status and the document.extraction_* webhook events; there is no dedicated job-status endpoint. | 

## Example

```python
from tmi_client.models.create_threat_model_document202_response import CreateThreatModelDocument202Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateThreatModelDocument202Response from a JSON string
create_threat_model_document202_response_instance = CreateThreatModelDocument202Response.from_json(json)
# print the JSON string representation of the object
print(CreateThreatModelDocument202Response.to_json())

# convert the object into a dict
create_threat_model_document202_response_dict = create_threat_model_document202_response_instance.to_dict()
# create an instance of CreateThreatModelDocument202Response from a dict
create_threat_model_document202_response_from_dict = CreateThreatModelDocument202Response.from_dict(create_threat_model_document202_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


