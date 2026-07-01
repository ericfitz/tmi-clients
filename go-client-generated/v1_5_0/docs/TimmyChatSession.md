# TimmyChatSession

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier for the chat session | [readonly] 
**ThreatModelId** | **string** | Identifier of the parent threat model | [readonly] 
**UserId** | **string** | Identifier of the user who created the session | [readonly] 
**Title** | Pointer to **string** | Optional session title | [optional] 
**SourceSnapshot** | Pointer to [**[]TimmyChatSessionSourceSnapshotInner**](TimmyChatSessionSourceSnapshotInner.md) | Snapshot of source entities used for context | [optional] 
**SystemPromptHash** | Pointer to **string** | Hash of the system prompt used for this session | [optional] [readonly] 
**Status** | **string** | Current status of the chat session | 
**CreatedAt** | **time.Time** | Creation timestamp (RFC3339) | [readonly] 
**ModifiedAt** | **time.Time** | Last modification timestamp (RFC3339) | [readonly] 

## Methods

### NewTimmyChatSession

`func NewTimmyChatSession(id string, threatModelId string, userId string, status string, createdAt time.Time, modifiedAt time.Time, ) *TimmyChatSession`

NewTimmyChatSession instantiates a new TimmyChatSession object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTimmyChatSessionWithDefaults

`func NewTimmyChatSessionWithDefaults() *TimmyChatSession`

NewTimmyChatSessionWithDefaults instantiates a new TimmyChatSession object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *TimmyChatSession) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *TimmyChatSession) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *TimmyChatSession) SetId(v string)`

SetId sets Id field to given value.


### GetThreatModelId

`func (o *TimmyChatSession) GetThreatModelId() string`

GetThreatModelId returns the ThreatModelId field if non-nil, zero value otherwise.

### GetThreatModelIdOk

`func (o *TimmyChatSession) GetThreatModelIdOk() (*string, bool)`

GetThreatModelIdOk returns a tuple with the ThreatModelId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreatModelId

`func (o *TimmyChatSession) SetThreatModelId(v string)`

SetThreatModelId sets ThreatModelId field to given value.


### GetUserId

`func (o *TimmyChatSession) GetUserId() string`

GetUserId returns the UserId field if non-nil, zero value otherwise.

### GetUserIdOk

`func (o *TimmyChatSession) GetUserIdOk() (*string, bool)`

GetUserIdOk returns a tuple with the UserId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserId

`func (o *TimmyChatSession) SetUserId(v string)`

SetUserId sets UserId field to given value.


### GetTitle

`func (o *TimmyChatSession) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *TimmyChatSession) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *TimmyChatSession) SetTitle(v string)`

SetTitle sets Title field to given value.

### HasTitle

`func (o *TimmyChatSession) HasTitle() bool`

HasTitle returns a boolean if a field has been set.

### GetSourceSnapshot

`func (o *TimmyChatSession) GetSourceSnapshot() []TimmyChatSessionSourceSnapshotInner`

GetSourceSnapshot returns the SourceSnapshot field if non-nil, zero value otherwise.

### GetSourceSnapshotOk

`func (o *TimmyChatSession) GetSourceSnapshotOk() (*[]TimmyChatSessionSourceSnapshotInner, bool)`

GetSourceSnapshotOk returns a tuple with the SourceSnapshot field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceSnapshot

`func (o *TimmyChatSession) SetSourceSnapshot(v []TimmyChatSessionSourceSnapshotInner)`

SetSourceSnapshot sets SourceSnapshot field to given value.

### HasSourceSnapshot

`func (o *TimmyChatSession) HasSourceSnapshot() bool`

HasSourceSnapshot returns a boolean if a field has been set.

### GetSystemPromptHash

`func (o *TimmyChatSession) GetSystemPromptHash() string`

GetSystemPromptHash returns the SystemPromptHash field if non-nil, zero value otherwise.

### GetSystemPromptHashOk

`func (o *TimmyChatSession) GetSystemPromptHashOk() (*string, bool)`

GetSystemPromptHashOk returns a tuple with the SystemPromptHash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemPromptHash

`func (o *TimmyChatSession) SetSystemPromptHash(v string)`

SetSystemPromptHash sets SystemPromptHash field to given value.

### HasSystemPromptHash

`func (o *TimmyChatSession) HasSystemPromptHash() bool`

HasSystemPromptHash returns a boolean if a field has been set.

### GetStatus

`func (o *TimmyChatSession) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *TimmyChatSession) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *TimmyChatSession) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetCreatedAt

`func (o *TimmyChatSession) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *TimmyChatSession) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *TimmyChatSession) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetModifiedAt

`func (o *TimmyChatSession) GetModifiedAt() time.Time`

GetModifiedAt returns the ModifiedAt field if non-nil, zero value otherwise.

### GetModifiedAtOk

`func (o *TimmyChatSession) GetModifiedAtOk() (*time.Time, bool)`

GetModifiedAtOk returns a tuple with the ModifiedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedAt

`func (o *TimmyChatSession) SetModifiedAt(v time.Time)`

SetModifiedAt sets ModifiedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


