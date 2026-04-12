# SurveyResponse

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
**Id** | Pointer to **string** | Unique identifier for the response (UUID) | [optional] [readonly] 
**Status** | Pointer to **string** | Current status of the survey response in the triage workflow | [optional] 
**IsConfidential** | Pointer to **bool** | Whether Security Reviewers group was excluded (set at creation, read-only after) | [optional] [readonly] 
**RevisionNotes** | Pointer to **NullableString** | Notes from security reviewer when returning for revision | [optional] [readonly] 
**CreatedThreatModelId** | Pointer to **NullableString** | ID of threat model created from this response | [optional] [readonly] 
**Owner** | Pointer to **map[string]interface{}** | User who created the response | [optional] [readonly] 
**CreatedAt** | Pointer to **time.Time** | Creation timestamp (RFC3339) | [optional] [readonly] 
**ModifiedAt** | Pointer to **time.Time** | Last modification timestamp (RFC3339) | [optional] [readonly] 
**SubmittedAt** | Pointer to **NullableTime** | When the response was submitted for review | [optional] [readonly] 
**ReviewedAt** | Pointer to **NullableTime** | When the response was last reviewed | [optional] [readonly] 
**ReviewedBy** | Pointer to **map[string]interface{}** | Security engineer who last reviewed the response | [optional] [readonly] 
**SurveyJson** | Pointer to **map[string]interface{}** | Snapshot of the survey survey_json at the time this response was created. Used to render historical responses against the correct survey version. | [optional] [readonly] 
**Metadata** | Pointer to [**[]Metadata**](Metadata.md) | Optional metadata key-value pairs | [optional] 
**CreatedBy** | Pointer to **map[string]interface{}** | User who created the response | [optional] [readonly] 

## Methods

### NewSurveyResponse

`func NewSurveyResponse(surveyId string, ) *SurveyResponse`

NewSurveyResponse instantiates a new SurveyResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSurveyResponseWithDefaults

`func NewSurveyResponseWithDefaults() *SurveyResponse`

NewSurveyResponseWithDefaults instantiates a new SurveyResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAnswers

`func (o *SurveyResponse) GetAnswers() map[string]interface{}`

GetAnswers returns the Answers field if non-nil, zero value otherwise.

### GetAnswersOk

`func (o *SurveyResponse) GetAnswersOk() (*map[string]interface{}, bool)`

GetAnswersOk returns a tuple with the Answers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAnswers

`func (o *SurveyResponse) SetAnswers(v map[string]interface{})`

SetAnswers sets Answers field to given value.

### HasAnswers

`func (o *SurveyResponse) HasAnswers() bool`

HasAnswers returns a boolean if a field has been set.

### GetLinkedThreatModelId

`func (o *SurveyResponse) GetLinkedThreatModelId() string`

GetLinkedThreatModelId returns the LinkedThreatModelId field if non-nil, zero value otherwise.

### GetLinkedThreatModelIdOk

`func (o *SurveyResponse) GetLinkedThreatModelIdOk() (*string, bool)`

GetLinkedThreatModelIdOk returns a tuple with the LinkedThreatModelId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinkedThreatModelId

`func (o *SurveyResponse) SetLinkedThreatModelId(v string)`

SetLinkedThreatModelId sets LinkedThreatModelId field to given value.

### HasLinkedThreatModelId

`func (o *SurveyResponse) HasLinkedThreatModelId() bool`

HasLinkedThreatModelId returns a boolean if a field has been set.

### SetLinkedThreatModelIdNil

`func (o *SurveyResponse) SetLinkedThreatModelIdNil(b bool)`

 SetLinkedThreatModelIdNil sets the value for LinkedThreatModelId to be an explicit nil

### UnsetLinkedThreatModelId
`func (o *SurveyResponse) UnsetLinkedThreatModelId()`

UnsetLinkedThreatModelId ensures that no value is present for LinkedThreatModelId, not even an explicit nil
### GetAuthorization

`func (o *SurveyResponse) GetAuthorization() []Authorization`

GetAuthorization returns the Authorization field if non-nil, zero value otherwise.

### GetAuthorizationOk

`func (o *SurveyResponse) GetAuthorizationOk() (*[]Authorization, bool)`

GetAuthorizationOk returns a tuple with the Authorization field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthorization

`func (o *SurveyResponse) SetAuthorization(v []Authorization)`

SetAuthorization sets Authorization field to given value.

### HasAuthorization

`func (o *SurveyResponse) HasAuthorization() bool`

HasAuthorization returns a boolean if a field has been set.

### GetUiState

`func (o *SurveyResponse) GetUiState() map[string]interface{}`

GetUiState returns the UiState field if non-nil, zero value otherwise.

### GetUiStateOk

`func (o *SurveyResponse) GetUiStateOk() (*map[string]interface{}, bool)`

GetUiStateOk returns a tuple with the UiState field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUiState

`func (o *SurveyResponse) SetUiState(v map[string]interface{})`

SetUiState sets UiState field to given value.

### HasUiState

`func (o *SurveyResponse) HasUiState() bool`

HasUiState returns a boolean if a field has been set.

### SetUiStateNil

`func (o *SurveyResponse) SetUiStateNil(b bool)`

 SetUiStateNil sets the value for UiState to be an explicit nil

### UnsetUiState
`func (o *SurveyResponse) UnsetUiState()`

UnsetUiState ensures that no value is present for UiState, not even an explicit nil
### GetSurveyId

`func (o *SurveyResponse) GetSurveyId() string`

GetSurveyId returns the SurveyId field if non-nil, zero value otherwise.

### GetSurveyIdOk

`func (o *SurveyResponse) GetSurveyIdOk() (*string, bool)`

GetSurveyIdOk returns a tuple with the SurveyId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSurveyId

`func (o *SurveyResponse) SetSurveyId(v string)`

SetSurveyId sets SurveyId field to given value.


### GetSurveyVersion

`func (o *SurveyResponse) GetSurveyVersion() string`

GetSurveyVersion returns the SurveyVersion field if non-nil, zero value otherwise.

### GetSurveyVersionOk

`func (o *SurveyResponse) GetSurveyVersionOk() (*string, bool)`

GetSurveyVersionOk returns a tuple with the SurveyVersion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSurveyVersion

`func (o *SurveyResponse) SetSurveyVersion(v string)`

SetSurveyVersion sets SurveyVersion field to given value.

### HasSurveyVersion

`func (o *SurveyResponse) HasSurveyVersion() bool`

HasSurveyVersion returns a boolean if a field has been set.

### GetProjectId

`func (o *SurveyResponse) GetProjectId() string`

GetProjectId returns the ProjectId field if non-nil, zero value otherwise.

### GetProjectIdOk

`func (o *SurveyResponse) GetProjectIdOk() (*string, bool)`

GetProjectIdOk returns a tuple with the ProjectId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectId

`func (o *SurveyResponse) SetProjectId(v string)`

SetProjectId sets ProjectId field to given value.

### HasProjectId

`func (o *SurveyResponse) HasProjectId() bool`

HasProjectId returns a boolean if a field has been set.

### SetProjectIdNil

`func (o *SurveyResponse) SetProjectIdNil(b bool)`

 SetProjectIdNil sets the value for ProjectId to be an explicit nil

### UnsetProjectId
`func (o *SurveyResponse) UnsetProjectId()`

UnsetProjectId ensures that no value is present for ProjectId, not even an explicit nil
### GetId

`func (o *SurveyResponse) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *SurveyResponse) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *SurveyResponse) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *SurveyResponse) HasId() bool`

HasId returns a boolean if a field has been set.

### GetStatus

`func (o *SurveyResponse) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *SurveyResponse) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *SurveyResponse) SetStatus(v string)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *SurveyResponse) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetIsConfidential

`func (o *SurveyResponse) GetIsConfidential() bool`

GetIsConfidential returns the IsConfidential field if non-nil, zero value otherwise.

### GetIsConfidentialOk

`func (o *SurveyResponse) GetIsConfidentialOk() (*bool, bool)`

GetIsConfidentialOk returns a tuple with the IsConfidential field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsConfidential

`func (o *SurveyResponse) SetIsConfidential(v bool)`

SetIsConfidential sets IsConfidential field to given value.

### HasIsConfidential

`func (o *SurveyResponse) HasIsConfidential() bool`

HasIsConfidential returns a boolean if a field has been set.

### GetRevisionNotes

`func (o *SurveyResponse) GetRevisionNotes() string`

GetRevisionNotes returns the RevisionNotes field if non-nil, zero value otherwise.

### GetRevisionNotesOk

`func (o *SurveyResponse) GetRevisionNotesOk() (*string, bool)`

GetRevisionNotesOk returns a tuple with the RevisionNotes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRevisionNotes

`func (o *SurveyResponse) SetRevisionNotes(v string)`

SetRevisionNotes sets RevisionNotes field to given value.

### HasRevisionNotes

`func (o *SurveyResponse) HasRevisionNotes() bool`

HasRevisionNotes returns a boolean if a field has been set.

### SetRevisionNotesNil

`func (o *SurveyResponse) SetRevisionNotesNil(b bool)`

 SetRevisionNotesNil sets the value for RevisionNotes to be an explicit nil

### UnsetRevisionNotes
`func (o *SurveyResponse) UnsetRevisionNotes()`

UnsetRevisionNotes ensures that no value is present for RevisionNotes, not even an explicit nil
### GetCreatedThreatModelId

`func (o *SurveyResponse) GetCreatedThreatModelId() string`

GetCreatedThreatModelId returns the CreatedThreatModelId field if non-nil, zero value otherwise.

### GetCreatedThreatModelIdOk

`func (o *SurveyResponse) GetCreatedThreatModelIdOk() (*string, bool)`

GetCreatedThreatModelIdOk returns a tuple with the CreatedThreatModelId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedThreatModelId

`func (o *SurveyResponse) SetCreatedThreatModelId(v string)`

SetCreatedThreatModelId sets CreatedThreatModelId field to given value.

### HasCreatedThreatModelId

`func (o *SurveyResponse) HasCreatedThreatModelId() bool`

HasCreatedThreatModelId returns a boolean if a field has been set.

### SetCreatedThreatModelIdNil

`func (o *SurveyResponse) SetCreatedThreatModelIdNil(b bool)`

 SetCreatedThreatModelIdNil sets the value for CreatedThreatModelId to be an explicit nil

### UnsetCreatedThreatModelId
`func (o *SurveyResponse) UnsetCreatedThreatModelId()`

UnsetCreatedThreatModelId ensures that no value is present for CreatedThreatModelId, not even an explicit nil
### GetOwner

`func (o *SurveyResponse) GetOwner() map[string]interface{}`

GetOwner returns the Owner field if non-nil, zero value otherwise.

### GetOwnerOk

`func (o *SurveyResponse) GetOwnerOk() (*map[string]interface{}, bool)`

GetOwnerOk returns a tuple with the Owner field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOwner

`func (o *SurveyResponse) SetOwner(v map[string]interface{})`

SetOwner sets Owner field to given value.

### HasOwner

`func (o *SurveyResponse) HasOwner() bool`

HasOwner returns a boolean if a field has been set.

### SetOwnerNil

`func (o *SurveyResponse) SetOwnerNil(b bool)`

 SetOwnerNil sets the value for Owner to be an explicit nil

### UnsetOwner
`func (o *SurveyResponse) UnsetOwner()`

UnsetOwner ensures that no value is present for Owner, not even an explicit nil
### GetCreatedAt

`func (o *SurveyResponse) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *SurveyResponse) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *SurveyResponse) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *SurveyResponse) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetModifiedAt

`func (o *SurveyResponse) GetModifiedAt() time.Time`

GetModifiedAt returns the ModifiedAt field if non-nil, zero value otherwise.

### GetModifiedAtOk

`func (o *SurveyResponse) GetModifiedAtOk() (*time.Time, bool)`

GetModifiedAtOk returns a tuple with the ModifiedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedAt

`func (o *SurveyResponse) SetModifiedAt(v time.Time)`

SetModifiedAt sets ModifiedAt field to given value.

### HasModifiedAt

`func (o *SurveyResponse) HasModifiedAt() bool`

HasModifiedAt returns a boolean if a field has been set.

### GetSubmittedAt

`func (o *SurveyResponse) GetSubmittedAt() time.Time`

GetSubmittedAt returns the SubmittedAt field if non-nil, zero value otherwise.

### GetSubmittedAtOk

`func (o *SurveyResponse) GetSubmittedAtOk() (*time.Time, bool)`

GetSubmittedAtOk returns a tuple with the SubmittedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubmittedAt

`func (o *SurveyResponse) SetSubmittedAt(v time.Time)`

SetSubmittedAt sets SubmittedAt field to given value.

### HasSubmittedAt

`func (o *SurveyResponse) HasSubmittedAt() bool`

HasSubmittedAt returns a boolean if a field has been set.

### SetSubmittedAtNil

`func (o *SurveyResponse) SetSubmittedAtNil(b bool)`

 SetSubmittedAtNil sets the value for SubmittedAt to be an explicit nil

### UnsetSubmittedAt
`func (o *SurveyResponse) UnsetSubmittedAt()`

UnsetSubmittedAt ensures that no value is present for SubmittedAt, not even an explicit nil
### GetReviewedAt

`func (o *SurveyResponse) GetReviewedAt() time.Time`

GetReviewedAt returns the ReviewedAt field if non-nil, zero value otherwise.

### GetReviewedAtOk

`func (o *SurveyResponse) GetReviewedAtOk() (*time.Time, bool)`

GetReviewedAtOk returns a tuple with the ReviewedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReviewedAt

`func (o *SurveyResponse) SetReviewedAt(v time.Time)`

SetReviewedAt sets ReviewedAt field to given value.

### HasReviewedAt

`func (o *SurveyResponse) HasReviewedAt() bool`

HasReviewedAt returns a boolean if a field has been set.

### SetReviewedAtNil

`func (o *SurveyResponse) SetReviewedAtNil(b bool)`

 SetReviewedAtNil sets the value for ReviewedAt to be an explicit nil

### UnsetReviewedAt
`func (o *SurveyResponse) UnsetReviewedAt()`

UnsetReviewedAt ensures that no value is present for ReviewedAt, not even an explicit nil
### GetReviewedBy

`func (o *SurveyResponse) GetReviewedBy() map[string]interface{}`

GetReviewedBy returns the ReviewedBy field if non-nil, zero value otherwise.

### GetReviewedByOk

`func (o *SurveyResponse) GetReviewedByOk() (*map[string]interface{}, bool)`

GetReviewedByOk returns a tuple with the ReviewedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReviewedBy

`func (o *SurveyResponse) SetReviewedBy(v map[string]interface{})`

SetReviewedBy sets ReviewedBy field to given value.

### HasReviewedBy

`func (o *SurveyResponse) HasReviewedBy() bool`

HasReviewedBy returns a boolean if a field has been set.

### SetReviewedByNil

`func (o *SurveyResponse) SetReviewedByNil(b bool)`

 SetReviewedByNil sets the value for ReviewedBy to be an explicit nil

### UnsetReviewedBy
`func (o *SurveyResponse) UnsetReviewedBy()`

UnsetReviewedBy ensures that no value is present for ReviewedBy, not even an explicit nil
### GetSurveyJson

`func (o *SurveyResponse) GetSurveyJson() map[string]interface{}`

GetSurveyJson returns the SurveyJson field if non-nil, zero value otherwise.

### GetSurveyJsonOk

`func (o *SurveyResponse) GetSurveyJsonOk() (*map[string]interface{}, bool)`

GetSurveyJsonOk returns a tuple with the SurveyJson field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSurveyJson

`func (o *SurveyResponse) SetSurveyJson(v map[string]interface{})`

SetSurveyJson sets SurveyJson field to given value.

### HasSurveyJson

`func (o *SurveyResponse) HasSurveyJson() bool`

HasSurveyJson returns a boolean if a field has been set.

### GetMetadata

`func (o *SurveyResponse) GetMetadata() []Metadata`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *SurveyResponse) GetMetadataOk() (*[]Metadata, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *SurveyResponse) SetMetadata(v []Metadata)`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *SurveyResponse) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### SetMetadataNil

`func (o *SurveyResponse) SetMetadataNil(b bool)`

 SetMetadataNil sets the value for Metadata to be an explicit nil

### UnsetMetadata
`func (o *SurveyResponse) UnsetMetadata()`

UnsetMetadata ensures that no value is present for Metadata, not even an explicit nil
### GetCreatedBy

`func (o *SurveyResponse) GetCreatedBy() map[string]interface{}`

GetCreatedBy returns the CreatedBy field if non-nil, zero value otherwise.

### GetCreatedByOk

`func (o *SurveyResponse) GetCreatedByOk() (*map[string]interface{}, bool)`

GetCreatedByOk returns a tuple with the CreatedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedBy

`func (o *SurveyResponse) SetCreatedBy(v map[string]interface{})`

SetCreatedBy sets CreatedBy field to given value.

### HasCreatedBy

`func (o *SurveyResponse) HasCreatedBy() bool`

HasCreatedBy returns a boolean if a field has been set.

### SetCreatedByNil

`func (o *SurveyResponse) SetCreatedByNil(b bool)`

 SetCreatedByNil sets the value for CreatedBy to be an explicit nil

### UnsetCreatedBy
`func (o *SurveyResponse) UnsetCreatedBy()`

UnsetCreatedBy ensures that no value is present for CreatedBy, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


