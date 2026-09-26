# CreateDiagramCollaborationSession409Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Error** | **string** | Error message indicating session already exists | 
**JoinUrl** | **string** | URL to join the existing collaboration session | 

## Methods

### NewCreateDiagramCollaborationSession409Response

`func NewCreateDiagramCollaborationSession409Response(error_ string, joinUrl string, ) *CreateDiagramCollaborationSession409Response`

NewCreateDiagramCollaborationSession409Response instantiates a new CreateDiagramCollaborationSession409Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateDiagramCollaborationSession409ResponseWithDefaults

`func NewCreateDiagramCollaborationSession409ResponseWithDefaults() *CreateDiagramCollaborationSession409Response`

NewCreateDiagramCollaborationSession409ResponseWithDefaults instantiates a new CreateDiagramCollaborationSession409Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetError

`func (o *CreateDiagramCollaborationSession409Response) GetError() string`

GetError returns the Error field if non-nil, zero value otherwise.

### GetErrorOk

`func (o *CreateDiagramCollaborationSession409Response) GetErrorOk() (*string, bool)`

GetErrorOk returns a tuple with the Error field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetError

`func (o *CreateDiagramCollaborationSession409Response) SetError(v string)`

SetError sets Error field to given value.


### GetJoinUrl

`func (o *CreateDiagramCollaborationSession409Response) GetJoinUrl() string`

GetJoinUrl returns the JoinUrl field if non-nil, zero value otherwise.

### GetJoinUrlOk

`func (o *CreateDiagramCollaborationSession409Response) GetJoinUrlOk() (*string, bool)`

GetJoinUrlOk returns a tuple with the JoinUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJoinUrl

`func (o *CreateDiagramCollaborationSession409Response) SetJoinUrl(v string)`

SetJoinUrl sets JoinUrl field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


