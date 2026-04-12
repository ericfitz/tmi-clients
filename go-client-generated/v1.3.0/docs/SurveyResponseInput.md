# SurveyResponseInput

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

### NewSurveyResponseInput

`func NewSurveyResponseInput(surveyId string, ) *SurveyResponseInput`

NewSurveyResponseInput instantiates a new SurveyResponseInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSurveyResponseInputWithDefaults

`func NewSurveyResponseInputWithDefaults() *SurveyResponseInput`

NewSurveyResponseInputWithDefaults instantiates a new SurveyResponseInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAnswers

`func (o *SurveyResponseInput) GetAnswers() map[string]interface{}`

GetAnswers returns the Answers field if non-nil, zero value otherwise.

### GetAnswersOk

`func (o *SurveyResponseInput) GetAnswersOk() (*map[string]interface{}, bool)`

GetAnswersOk returns a tuple with the Answers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAnswers

`func (o *SurveyResponseInput) SetAnswers(v map[string]interface{})`

SetAnswers sets Answers field to given value.

### HasAnswers

`func (o *SurveyResponseInput) HasAnswers() bool`

HasAnswers returns a boolean if a field has been set.

### GetLinkedThreatModelId

`func (o *SurveyResponseInput) GetLinkedThreatModelId() string`

GetLinkedThreatModelId returns the LinkedThreatModelId field if non-nil, zero value otherwise.

### GetLinkedThreatModelIdOk

`func (o *SurveyResponseInput) GetLinkedThreatModelIdOk() (*string, bool)`

GetLinkedThreatModelIdOk returns a tuple with the LinkedThreatModelId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinkedThreatModelId

`func (o *SurveyResponseInput) SetLinkedThreatModelId(v string)`

SetLinkedThreatModelId sets LinkedThreatModelId field to given value.

### HasLinkedThreatModelId

`func (o *SurveyResponseInput) HasLinkedThreatModelId() bool`

HasLinkedThreatModelId returns a boolean if a field has been set.

### SetLinkedThreatModelIdNil

`func (o *SurveyResponseInput) SetLinkedThreatModelIdNil(b bool)`

 SetLinkedThreatModelIdNil sets the value for LinkedThreatModelId to be an explicit nil

### UnsetLinkedThreatModelId
`func (o *SurveyResponseInput) UnsetLinkedThreatModelId()`

UnsetLinkedThreatModelId ensures that no value is present for LinkedThreatModelId, not even an explicit nil
### GetAuthorization

`func (o *SurveyResponseInput) GetAuthorization() []Authorization`

GetAuthorization returns the Authorization field if non-nil, zero value otherwise.

### GetAuthorizationOk

`func (o *SurveyResponseInput) GetAuthorizationOk() (*[]Authorization, bool)`

GetAuthorizationOk returns a tuple with the Authorization field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthorization

`func (o *SurveyResponseInput) SetAuthorization(v []Authorization)`

SetAuthorization sets Authorization field to given value.

### HasAuthorization

`func (o *SurveyResponseInput) HasAuthorization() bool`

HasAuthorization returns a boolean if a field has been set.

### GetUiState

`func (o *SurveyResponseInput) GetUiState() map[string]interface{}`

GetUiState returns the UiState field if non-nil, zero value otherwise.

### GetUiStateOk

`func (o *SurveyResponseInput) GetUiStateOk() (*map[string]interface{}, bool)`

GetUiStateOk returns a tuple with the UiState field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUiState

`func (o *SurveyResponseInput) SetUiState(v map[string]interface{})`

SetUiState sets UiState field to given value.

### HasUiState

`func (o *SurveyResponseInput) HasUiState() bool`

HasUiState returns a boolean if a field has been set.

### SetUiStateNil

`func (o *SurveyResponseInput) SetUiStateNil(b bool)`

 SetUiStateNil sets the value for UiState to be an explicit nil

### UnsetUiState
`func (o *SurveyResponseInput) UnsetUiState()`

UnsetUiState ensures that no value is present for UiState, not even an explicit nil
### GetSurveyId

`func (o *SurveyResponseInput) GetSurveyId() string`

GetSurveyId returns the SurveyId field if non-nil, zero value otherwise.

### GetSurveyIdOk

`func (o *SurveyResponseInput) GetSurveyIdOk() (*string, bool)`

GetSurveyIdOk returns a tuple with the SurveyId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSurveyId

`func (o *SurveyResponseInput) SetSurveyId(v string)`

SetSurveyId sets SurveyId field to given value.


### GetSurveyVersion

`func (o *SurveyResponseInput) GetSurveyVersion() string`

GetSurveyVersion returns the SurveyVersion field if non-nil, zero value otherwise.

### GetSurveyVersionOk

`func (o *SurveyResponseInput) GetSurveyVersionOk() (*string, bool)`

GetSurveyVersionOk returns a tuple with the SurveyVersion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSurveyVersion

`func (o *SurveyResponseInput) SetSurveyVersion(v string)`

SetSurveyVersion sets SurveyVersion field to given value.

### HasSurveyVersion

`func (o *SurveyResponseInput) HasSurveyVersion() bool`

HasSurveyVersion returns a boolean if a field has been set.

### GetProjectId

`func (o *SurveyResponseInput) GetProjectId() string`

GetProjectId returns the ProjectId field if non-nil, zero value otherwise.

### GetProjectIdOk

`func (o *SurveyResponseInput) GetProjectIdOk() (*string, bool)`

GetProjectIdOk returns a tuple with the ProjectId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectId

`func (o *SurveyResponseInput) SetProjectId(v string)`

SetProjectId sets ProjectId field to given value.

### HasProjectId

`func (o *SurveyResponseInput) HasProjectId() bool`

HasProjectId returns a boolean if a field has been set.

### SetProjectIdNil

`func (o *SurveyResponseInput) SetProjectIdNil(b bool)`

 SetProjectIdNil sets the value for ProjectId to be an explicit nil

### UnsetProjectId
`func (o *SurveyResponseInput) UnsetProjectId()`

UnsetProjectId ensures that no value is present for ProjectId, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


