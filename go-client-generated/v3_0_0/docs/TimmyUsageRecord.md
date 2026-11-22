# TimmyUsageRecord

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**UserId** | Pointer to **string** | User identifier | [optional] 
**SessionId** | Pointer to **string** | Chat session identifier | [optional] 
**ThreatModelId** | Pointer to **string** | Threat model identifier | [optional] 
**MessageCount** | Pointer to **int32** | Number of messages in the period | [optional] 
**PromptTokens** | Pointer to **int32** | Number of prompt tokens consumed | [optional] 
**CompletionTokens** | Pointer to **int32** | Number of completion tokens consumed | [optional] 
**EmbeddingTokens** | Pointer to **int32** | Number of embedding tokens consumed | [optional] 
**PeriodStart** | Pointer to **time.Time** | Start of the usage period (RFC3339) | [optional] 
**PeriodEnd** | Pointer to **time.Time** | End of the usage period (RFC3339) | [optional] 

## Methods

### NewTimmyUsageRecord

`func NewTimmyUsageRecord() *TimmyUsageRecord`

NewTimmyUsageRecord instantiates a new TimmyUsageRecord object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTimmyUsageRecordWithDefaults

`func NewTimmyUsageRecordWithDefaults() *TimmyUsageRecord`

NewTimmyUsageRecordWithDefaults instantiates a new TimmyUsageRecord object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetUserId

`func (o *TimmyUsageRecord) GetUserId() string`

GetUserId returns the UserId field if non-nil, zero value otherwise.

### GetUserIdOk

`func (o *TimmyUsageRecord) GetUserIdOk() (*string, bool)`

GetUserIdOk returns a tuple with the UserId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserId

`func (o *TimmyUsageRecord) SetUserId(v string)`

SetUserId sets UserId field to given value.

### HasUserId

`func (o *TimmyUsageRecord) HasUserId() bool`

HasUserId returns a boolean if a field has been set.

### GetSessionId

`func (o *TimmyUsageRecord) GetSessionId() string`

GetSessionId returns the SessionId field if non-nil, zero value otherwise.

### GetSessionIdOk

`func (o *TimmyUsageRecord) GetSessionIdOk() (*string, bool)`

GetSessionIdOk returns a tuple with the SessionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSessionId

`func (o *TimmyUsageRecord) SetSessionId(v string)`

SetSessionId sets SessionId field to given value.

### HasSessionId

`func (o *TimmyUsageRecord) HasSessionId() bool`

HasSessionId returns a boolean if a field has been set.

### GetThreatModelId

`func (o *TimmyUsageRecord) GetThreatModelId() string`

GetThreatModelId returns the ThreatModelId field if non-nil, zero value otherwise.

### GetThreatModelIdOk

`func (o *TimmyUsageRecord) GetThreatModelIdOk() (*string, bool)`

GetThreatModelIdOk returns a tuple with the ThreatModelId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreatModelId

`func (o *TimmyUsageRecord) SetThreatModelId(v string)`

SetThreatModelId sets ThreatModelId field to given value.

### HasThreatModelId

`func (o *TimmyUsageRecord) HasThreatModelId() bool`

HasThreatModelId returns a boolean if a field has been set.

### GetMessageCount

`func (o *TimmyUsageRecord) GetMessageCount() int32`

GetMessageCount returns the MessageCount field if non-nil, zero value otherwise.

### GetMessageCountOk

`func (o *TimmyUsageRecord) GetMessageCountOk() (*int32, bool)`

GetMessageCountOk returns a tuple with the MessageCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessageCount

`func (o *TimmyUsageRecord) SetMessageCount(v int32)`

SetMessageCount sets MessageCount field to given value.

### HasMessageCount

`func (o *TimmyUsageRecord) HasMessageCount() bool`

HasMessageCount returns a boolean if a field has been set.

### GetPromptTokens

`func (o *TimmyUsageRecord) GetPromptTokens() int32`

GetPromptTokens returns the PromptTokens field if non-nil, zero value otherwise.

### GetPromptTokensOk

`func (o *TimmyUsageRecord) GetPromptTokensOk() (*int32, bool)`

GetPromptTokensOk returns a tuple with the PromptTokens field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPromptTokens

`func (o *TimmyUsageRecord) SetPromptTokens(v int32)`

SetPromptTokens sets PromptTokens field to given value.

### HasPromptTokens

`func (o *TimmyUsageRecord) HasPromptTokens() bool`

HasPromptTokens returns a boolean if a field has been set.

### GetCompletionTokens

`func (o *TimmyUsageRecord) GetCompletionTokens() int32`

GetCompletionTokens returns the CompletionTokens field if non-nil, zero value otherwise.

### GetCompletionTokensOk

`func (o *TimmyUsageRecord) GetCompletionTokensOk() (*int32, bool)`

GetCompletionTokensOk returns a tuple with the CompletionTokens field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompletionTokens

`func (o *TimmyUsageRecord) SetCompletionTokens(v int32)`

SetCompletionTokens sets CompletionTokens field to given value.

### HasCompletionTokens

`func (o *TimmyUsageRecord) HasCompletionTokens() bool`

HasCompletionTokens returns a boolean if a field has been set.

### GetEmbeddingTokens

`func (o *TimmyUsageRecord) GetEmbeddingTokens() int32`

GetEmbeddingTokens returns the EmbeddingTokens field if non-nil, zero value otherwise.

### GetEmbeddingTokensOk

`func (o *TimmyUsageRecord) GetEmbeddingTokensOk() (*int32, bool)`

GetEmbeddingTokensOk returns a tuple with the EmbeddingTokens field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmbeddingTokens

`func (o *TimmyUsageRecord) SetEmbeddingTokens(v int32)`

SetEmbeddingTokens sets EmbeddingTokens field to given value.

### HasEmbeddingTokens

`func (o *TimmyUsageRecord) HasEmbeddingTokens() bool`

HasEmbeddingTokens returns a boolean if a field has been set.

### GetPeriodStart

`func (o *TimmyUsageRecord) GetPeriodStart() time.Time`

GetPeriodStart returns the PeriodStart field if non-nil, zero value otherwise.

### GetPeriodStartOk

`func (o *TimmyUsageRecord) GetPeriodStartOk() (*time.Time, bool)`

GetPeriodStartOk returns a tuple with the PeriodStart field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPeriodStart

`func (o *TimmyUsageRecord) SetPeriodStart(v time.Time)`

SetPeriodStart sets PeriodStart field to given value.

### HasPeriodStart

`func (o *TimmyUsageRecord) HasPeriodStart() bool`

HasPeriodStart returns a boolean if a field has been set.

### GetPeriodEnd

`func (o *TimmyUsageRecord) GetPeriodEnd() time.Time`

GetPeriodEnd returns the PeriodEnd field if non-nil, zero value otherwise.

### GetPeriodEndOk

`func (o *TimmyUsageRecord) GetPeriodEndOk() (*time.Time, bool)`

GetPeriodEndOk returns a tuple with the PeriodEnd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPeriodEnd

`func (o *TimmyUsageRecord) SetPeriodEnd(v time.Time)`

SetPeriodEnd sets PeriodEnd field to given value.

### HasPeriodEnd

`func (o *TimmyUsageRecord) HasPeriodEnd() bool`

HasPeriodEnd returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


