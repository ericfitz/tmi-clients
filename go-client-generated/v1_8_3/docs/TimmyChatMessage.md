# TimmyChatMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier for the message | [readonly] 
**SessionId** | **string** | Identifier of the parent chat session | [readonly] 
**Role** | **string** | Role of the message sender | 
**Content** | **string** | Message content | 
**TokenCount** | Pointer to **int32** | Number of tokens in the message | [optional] [readonly] 
**Sequence** | **int32** | Message sequence number within the session | [readonly] 
**CreatedAt** | **time.Time** | Creation timestamp (RFC3339) | [readonly] 

## Methods

### NewTimmyChatMessage

`func NewTimmyChatMessage(id string, sessionId string, role string, content string, sequence int32, createdAt time.Time, ) *TimmyChatMessage`

NewTimmyChatMessage instantiates a new TimmyChatMessage object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTimmyChatMessageWithDefaults

`func NewTimmyChatMessageWithDefaults() *TimmyChatMessage`

NewTimmyChatMessageWithDefaults instantiates a new TimmyChatMessage object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *TimmyChatMessage) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *TimmyChatMessage) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *TimmyChatMessage) SetId(v string)`

SetId sets Id field to given value.


### GetSessionId

`func (o *TimmyChatMessage) GetSessionId() string`

GetSessionId returns the SessionId field if non-nil, zero value otherwise.

### GetSessionIdOk

`func (o *TimmyChatMessage) GetSessionIdOk() (*string, bool)`

GetSessionIdOk returns a tuple with the SessionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSessionId

`func (o *TimmyChatMessage) SetSessionId(v string)`

SetSessionId sets SessionId field to given value.


### GetRole

`func (o *TimmyChatMessage) GetRole() string`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *TimmyChatMessage) GetRoleOk() (*string, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *TimmyChatMessage) SetRole(v string)`

SetRole sets Role field to given value.


### GetContent

`func (o *TimmyChatMessage) GetContent() string`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *TimmyChatMessage) GetContentOk() (*string, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *TimmyChatMessage) SetContent(v string)`

SetContent sets Content field to given value.


### GetTokenCount

`func (o *TimmyChatMessage) GetTokenCount() int32`

GetTokenCount returns the TokenCount field if non-nil, zero value otherwise.

### GetTokenCountOk

`func (o *TimmyChatMessage) GetTokenCountOk() (*int32, bool)`

GetTokenCountOk returns a tuple with the TokenCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTokenCount

`func (o *TimmyChatMessage) SetTokenCount(v int32)`

SetTokenCount sets TokenCount field to given value.

### HasTokenCount

`func (o *TimmyChatMessage) HasTokenCount() bool`

HasTokenCount returns a boolean if a field has been set.

### GetSequence

`func (o *TimmyChatMessage) GetSequence() int32`

GetSequence returns the Sequence field if non-nil, zero value otherwise.

### GetSequenceOk

`func (o *TimmyChatMessage) GetSequenceOk() (*int32, bool)`

GetSequenceOk returns a tuple with the Sequence field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSequence

`func (o *TimmyChatMessage) SetSequence(v int32)`

SetSequence sets Sequence field to given value.


### GetCreatedAt

`func (o *TimmyChatMessage) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *TimmyChatMessage) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *TimmyChatMessage) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


