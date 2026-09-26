# CreateDiagramCollaborationSession409Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error message indicating session already exists | 
**join_url** | **str** | URL to join the existing collaboration session | 

## Example

```python
from tmi_client.models.create_diagram_collaboration_session409_response import CreateDiagramCollaborationSession409Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDiagramCollaborationSession409Response from a JSON string
create_diagram_collaboration_session409_response_instance = CreateDiagramCollaborationSession409Response.from_json(json)
# print the JSON string representation of the object
print(CreateDiagramCollaborationSession409Response.to_json())

# convert the object into a dict
create_diagram_collaboration_session409_response_dict = create_diagram_collaboration_session409_response_instance.to_dict()
# create an instance of CreateDiagramCollaborationSession409Response from a dict
create_diagram_collaboration_session409_response_from_dict = CreateDiagramCollaborationSession409Response.from_dict(create_diagram_collaboration_session409_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


