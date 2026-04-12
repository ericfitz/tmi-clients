# CollaborationSession

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SessionId** | **string** | Unique identifier for the session (UUID) | [readonly] 
**Host** | [**User**](User.md) | User hosting the collaboration session | [readonly] 
**Presenter** | Pointer to [**User**](User.md) | User currently presenting (may be null if no active presenter) | [optional] [readonly] 
**ThreatModelId** | **string** | Unique identifier of the associated threat model (UUID) | 
**ThreatModelName** | **string** | Name of the associated threat model | 
**DiagramId** | **string** | Unique identifier of the associated diagram (UUID) | 
**DiagramName** | **string** | Name of the associated diagram | 
**Participants** | [**[]Participant**](Participant.md) | List of active participants | 
**WebsocketUrl** | **string** | WebSocket URL for real-time updates | 

## Methods

### NewCollaborationSession

`func NewCollaborationSession(sessionId string, host User, threatModelId string, threatModelName string, diagramId string, diagramName string, participants []Participant, websocketUrl string, ) *CollaborationSession`

NewCollaborationSession instantiates a new CollaborationSession object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCollaborationSessionWithDefaults

`func NewCollaborationSessionWithDefaults() *CollaborationSession`

NewCollaborationSessionWithDefaults instantiates a new CollaborationSession object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSessionId

`func (o *CollaborationSession) GetSessionId() string`

GetSessionId returns the SessionId field if non-nil, zero value otherwise.

### GetSessionIdOk

`func (o *CollaborationSession) GetSessionIdOk() (*string, bool)`

GetSessionIdOk returns a tuple with the SessionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSessionId

`func (o *CollaborationSession) SetSessionId(v string)`

SetSessionId sets SessionId field to given value.


### GetHost

`func (o *CollaborationSession) GetHost() User`

GetHost returns the Host field if non-nil, zero value otherwise.

### GetHostOk

`func (o *CollaborationSession) GetHostOk() (*User, bool)`

GetHostOk returns a tuple with the Host field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHost

`func (o *CollaborationSession) SetHost(v User)`

SetHost sets Host field to given value.


### GetPresenter

`func (o *CollaborationSession) GetPresenter() User`

GetPresenter returns the Presenter field if non-nil, zero value otherwise.

### GetPresenterOk

`func (o *CollaborationSession) GetPresenterOk() (*User, bool)`

GetPresenterOk returns a tuple with the Presenter field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPresenter

`func (o *CollaborationSession) SetPresenter(v User)`

SetPresenter sets Presenter field to given value.

### HasPresenter

`func (o *CollaborationSession) HasPresenter() bool`

HasPresenter returns a boolean if a field has been set.

### GetThreatModelId

`func (o *CollaborationSession) GetThreatModelId() string`

GetThreatModelId returns the ThreatModelId field if non-nil, zero value otherwise.

### GetThreatModelIdOk

`func (o *CollaborationSession) GetThreatModelIdOk() (*string, bool)`

GetThreatModelIdOk returns a tuple with the ThreatModelId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreatModelId

`func (o *CollaborationSession) SetThreatModelId(v string)`

SetThreatModelId sets ThreatModelId field to given value.


### GetThreatModelName

`func (o *CollaborationSession) GetThreatModelName() string`

GetThreatModelName returns the ThreatModelName field if non-nil, zero value otherwise.

### GetThreatModelNameOk

`func (o *CollaborationSession) GetThreatModelNameOk() (*string, bool)`

GetThreatModelNameOk returns a tuple with the ThreatModelName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreatModelName

`func (o *CollaborationSession) SetThreatModelName(v string)`

SetThreatModelName sets ThreatModelName field to given value.


### GetDiagramId

`func (o *CollaborationSession) GetDiagramId() string`

GetDiagramId returns the DiagramId field if non-nil, zero value otherwise.

### GetDiagramIdOk

`func (o *CollaborationSession) GetDiagramIdOk() (*string, bool)`

GetDiagramIdOk returns a tuple with the DiagramId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDiagramId

`func (o *CollaborationSession) SetDiagramId(v string)`

SetDiagramId sets DiagramId field to given value.


### GetDiagramName

`func (o *CollaborationSession) GetDiagramName() string`

GetDiagramName returns the DiagramName field if non-nil, zero value otherwise.

### GetDiagramNameOk

`func (o *CollaborationSession) GetDiagramNameOk() (*string, bool)`

GetDiagramNameOk returns a tuple with the DiagramName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDiagramName

`func (o *CollaborationSession) SetDiagramName(v string)`

SetDiagramName sets DiagramName field to given value.


### GetParticipants

`func (o *CollaborationSession) GetParticipants() []Participant`

GetParticipants returns the Participants field if non-nil, zero value otherwise.

### GetParticipantsOk

`func (o *CollaborationSession) GetParticipantsOk() (*[]Participant, bool)`

GetParticipantsOk returns a tuple with the Participants field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParticipants

`func (o *CollaborationSession) SetParticipants(v []Participant)`

SetParticipants sets Participants field to given value.


### GetWebsocketUrl

`func (o *CollaborationSession) GetWebsocketUrl() string`

GetWebsocketUrl returns the WebsocketUrl field if non-nil, zero value otherwise.

### GetWebsocketUrlOk

`func (o *CollaborationSession) GetWebsocketUrlOk() (*string, bool)`

GetWebsocketUrlOk returns a tuple with the WebsocketUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWebsocketUrl

`func (o *CollaborationSession) SetWebsocketUrl(v string)`

SetWebsocketUrl sets WebsocketUrl field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


