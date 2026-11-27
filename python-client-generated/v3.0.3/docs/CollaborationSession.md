# CollaborationSession

Details of an active collaboration session for a diagram

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **UUID** | Unique identifier for the session (UUID) | [readonly] 
**host** | [**User**](User.md) | User hosting the collaboration session | [readonly] 
**presenter** | [**User**](User.md) | User currently presenting (may be null if no active presenter) | [optional] [readonly] 
**threat_model_id** | **UUID** | Unique identifier of the associated threat model (UUID) | 
**threat_model_name** | **str** | Name of the associated threat model | 
**diagram_id** | **UUID** | Unique identifier of the associated diagram (UUID) | 
**diagram_name** | **str** | Name of the associated diagram | 
**participants** | [**List[Participant]**](Participant.md) | Users authorized to take part in the session: the threat model owner and each user in its authorization list, each with their session permission, plus any connected user not otherwise listed. This is not the set of currently connected users. Group authorization entries are not expanded. For users who are not currently connected, last_activity is the session last-activity time. For users who are not connected, permissions come from the threat model authorization role (owner and writer map to writer, reader to reader); roles elevated through group membership are not reflected. | 
**websocket_url** | **str** | WebSocket URL for real-time updates | 

## Example

```python
from tmi_client.models.collaboration_session import CollaborationSession

# TODO update the JSON string below
json = "{}"
# create an instance of CollaborationSession from a JSON string
collaboration_session_instance = CollaborationSession.from_json(json)
# print the JSON string representation of the object
print(CollaborationSession.to_json())

# convert the object into a dict
collaboration_session_dict = collaboration_session_instance.to_dict()
# create an instance of CollaborationSession from a dict
collaboration_session_from_dict = CollaborationSession.from_dict(collaboration_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


