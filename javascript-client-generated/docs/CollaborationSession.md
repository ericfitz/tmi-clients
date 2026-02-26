# TmiJsClient.CollaborationSession

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sessionId** | **String** | Unique identifier for the session (UUID) | 
**host** | **AllOfCollaborationSessionHost** | User hosting the collaboration session | 
**presenter** | **AllOfCollaborationSessionPresenter** | User currently presenting (may be null if no active presenter) | [optional] 
**threatModelId** | **String** | Unique identifier of the associated threat model (UUID) | 
**threatModelName** | **String** | Name of the associated threat model | 
**diagramId** | **String** | Unique identifier of the associated diagram (UUID) | 
**diagramName** | **String** | Name of the associated diagram | 
**participants** | [**[Participant]**](Participant.md) | List of active participants | 
**websocketUrl** | **String** | WebSocket URL for real-time updates | 
