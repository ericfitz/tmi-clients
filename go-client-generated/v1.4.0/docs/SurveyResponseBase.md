# SurveyResponseBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Answers** | Pointer to **map[string]interface{}** | Question answers keyed by question name. Values can be any JSON type to support all SurveyJS question types including dynamic panels (arrays of objects), matrix questions (objects of objects), and scalar values (strings, numbers, booleans). | [optional] 
**LinkedThreatModelId** | Pointer to **NullableString** | Optional link to existing threat model for re-reviews | [optional] 
**Authorization** | Pointer to [**[]Authorization**](Authorization.md) | List of users and groups with access to this response | [optional] 
**UiState** | Pointer to **map[string]interface{}** | Client-managed UI state for draft resumption (e.g., current page, scroll position). Cleared on submission. | [optional] 
**SurveyId** | **string** | ID of the survey this response is based on | 
**SurveyVersion** | Pointer to **string** | Survey version captured at creation time - responses always complete on the original version | [optional] [readonly] 
**ProjectId** | Pointer to **NullableString** | Optional reference to the project this survey response belongs to | [optional] 

## Methods

### NewSurveyResponseBase

`func NewSurveyResponseBase(surveyId string, ) *SurveyResponseBase`

NewSurveyResponseBase instantiates a new SurveyResponseBase object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSurveyResponseBaseWithDefaults

`func NewSurveyResponseBaseWithDefaults() *SurveyResponseBase`

NewSurveyResponseBaseWithDefaults instantiates a new SurveyResponseBase object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAnswers

`func (o *SurveyResponseBase) GetAnswers() map[string]interface{}`

GetAnswers returns the Answers field if non-nil, zero value otherwise.

### GetAnswersOk

`func (o *SurveyResponseBase) GetAnswersOk() (*map[string]interface{}, bool)`

GetAnswersOk returns a tuple with the Answers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAnswers

`func (o *SurveyResponseBase) SetAnswers(v map[string]interface{})`

SetAnswers sets Answers field to given value.

### HasAnswers

`func (o *SurveyResponseBase) HasAnswers() bool`

HasAnswers returns a boolean if a field has been set.

### GetLinkedThreatModelId

`func (o *SurveyResponseBase) GetLinkedThreatModelId() string`

GetLinkedThreatModelId returns the LinkedThreatModelId field if non-nil, zero value otherwise.

### GetLinkedThreatModelIdOk

`func (o *SurveyResponseBase) GetLinkedThreatModelIdOk() (*string, bool)`

GetLinkedThreatModelIdOk returns a tuple with the LinkedThreatModelId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinkedThreatModelId

`func (o *SurveyResponseBase) SetLinkedThreatModelId(v string)`

SetLinkedThreatModelId sets LinkedThreatModelId field to given value.

### HasLinkedThreatModelId

`func (o *SurveyResponseBase) HasLinkedThreatModelId() bool`

HasLinkedThreatModelId returns a boolean if a field has been set.

### SetLinkedThreatModelIdNil

`func (o *SurveyResponseBase) SetLinkedThreatModelIdNil(b bool)`

 SetLinkedThreatModelIdNil sets the value for LinkedThreatModelId to be an explicit nil

### UnsetLinkedThreatModelId
`func (o *SurveyResponseBase) UnsetLinkedThreatModelId()`

UnsetLinkedThreatModelId ensures that no value is present for LinkedThreatModelId, not even an explicit nil
### GetAuthorization

`func (o *SurveyResponseBase) GetAuthorization() []Authorization`

GetAuthorization returns the Authorization field if non-nil, zero value otherwise.

### GetAuthorizationOk

`func (o *SurveyResponseBase) GetAuthorizationOk() (*[]Authorization, bool)`

GetAuthorizationOk returns a tuple with the Authorization field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthorization

`func (o *SurveyResponseBase) SetAuthorization(v []Authorization)`

SetAuthorization sets Authorization field to given value.

### HasAuthorization

`func (o *SurveyResponseBase) HasAuthorization() bool`

HasAuthorization returns a boolean if a field has been set.

### GetUiState

`func (o *SurveyResponseBase) GetUiState() map[string]interface{}`

GetUiState returns the UiState field if non-nil, zero value otherwise.

### GetUiStateOk

`func (o *SurveyResponseBase) GetUiStateOk() (*map[string]interface{}, bool)`

GetUiStateOk returns a tuple with the UiState field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUiState

`func (o *SurveyResponseBase) SetUiState(v map[string]interface{})`

SetUiState sets UiState field to given value.

### HasUiState

`func (o *SurveyResponseBase) HasUiState() bool`

HasUiState returns a boolean if a field has been set.

### SetUiStateNil

`func (o *SurveyResponseBase) SetUiStateNil(b bool)`

 SetUiStateNil sets the value for UiState to be an explicit nil

### UnsetUiState
`func (o *SurveyResponseBase) UnsetUiState()`

UnsetUiState ensures that no value is present for UiState, not even an explicit nil
### GetSurveyId

`func (o *SurveyResponseBase) GetSurveyId() string`

GetSurveyId returns the SurveyId field if non-nil, zero value otherwise.

### GetSurveyIdOk

`func (o *SurveyResponseBase) GetSurveyIdOk() (*string, bool)`

GetSurveyIdOk returns a tuple with the SurveyId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSurveyId

`func (o *SurveyResponseBase) SetSurveyId(v string)`

SetSurveyId sets SurveyId field to given value.


### GetSurveyVersion

`func (o *SurveyResponseBase) GetSurveyVersion() string`

GetSurveyVersion returns the SurveyVersion field if non-nil, zero value otherwise.

### GetSurveyVersionOk

`func (o *SurveyResponseBase) GetSurveyVersionOk() (*string, bool)`

GetSurveyVersionOk returns a tuple with the SurveyVersion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSurveyVersion

`func (o *SurveyResponseBase) SetSurveyVersion(v string)`

SetSurveyVersion sets SurveyVersion field to given value.

### HasSurveyVersion

`func (o *SurveyResponseBase) HasSurveyVersion() bool`

HasSurveyVersion returns a boolean if a field has been set.

### GetProjectId

`func (o *SurveyResponseBase) GetProjectId() string`

GetProjectId returns the ProjectId field if non-nil, zero value otherwise.

### GetProjectIdOk

`func (o *SurveyResponseBase) GetProjectIdOk() (*string, bool)`

GetProjectIdOk returns a tuple with the ProjectId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectId

`func (o *SurveyResponseBase) SetProjectId(v string)`

SetProjectId sets ProjectId field to given value.

### HasProjectId

`func (o *SurveyResponseBase) HasProjectId() bool`

HasProjectId returns a boolean if a field has been set.

### SetProjectIdNil

`func (o *SurveyResponseBase) SetProjectIdNil(b bool)`

 SetProjectIdNil sets the value for ProjectId to be an explicit nil

### UnsetProjectId
`func (o *SurveyResponseBase) UnsetProjectId()`

UnsetProjectId ensures that no value is present for ProjectId, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


