# TMListItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier of the threat model (UUID) | [readonly] 
**Name** | **string** | Name of the threat model | 
**Description** | Pointer to **string** | Description of the threat model | [optional] 
**CreatedAt** | **time.Time** | Creation timestamp (RFC3339) | 
**ModifiedAt** | **time.Time** | Last modification timestamp (RFC3339) | 
**Owner** | [**User**](User.md) | User who owns the threat model | 
**CreatedBy** | [**User**](User.md) | User who created the threat model | 
**ThreatModelFramework** | **string** | The framework used for this threat model | 
**DocumentCount** | **int32** | Number of documents associated with this threat model | 
**RepoCount** | **int32** | Number of source code repository entries associated with this threat model | 
**DiagramCount** | **int32** | Number of diagrams associated with this threat model | 
**ThreatCount** | **int32** | Number of threats defined in this threat model | 
**IssueUri** | Pointer to **string** | URL to an issue in an issue tracking system | [optional] 
**AssetCount** | **int32** | Number of assets associated with this threat model | 
**NoteCount** | **int32** | Number of notes associated with this threat model | 
**Status** | Pointer to **NullableString** | Status of the threat model in the organization&#39;s threat modeling or SDLC process. Examples: \&quot;Not started\&quot;, \&quot;In progress\&quot;, \&quot;Review\&quot;, \&quot;Approved\&quot;, \&quot;Closed\&quot; | [optional] 
**StatusUpdated** | Pointer to **NullableTime** | Timestamp when the status field was last modified (RFC3339). Automatically updated by the server when status changes. | [optional] [readonly] 
**SecurityReviewer** | Pointer to [**NullableUser**](User.md) | Security reviewer assigned to this threat model. The assigned security reviewer automatically has the owner role on this threat model. | [optional] 

## Methods

### NewTMListItem

`func NewTMListItem(id string, name string, createdAt time.Time, modifiedAt time.Time, owner User, createdBy User, threatModelFramework string, documentCount int32, repoCount int32, diagramCount int32, threatCount int32, assetCount int32, noteCount int32, ) *TMListItem`

NewTMListItem instantiates a new TMListItem object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTMListItemWithDefaults

`func NewTMListItemWithDefaults() *TMListItem`

NewTMListItemWithDefaults instantiates a new TMListItem object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *TMListItem) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *TMListItem) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *TMListItem) SetId(v string)`

SetId sets Id field to given value.


### GetName

`func (o *TMListItem) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *TMListItem) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *TMListItem) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *TMListItem) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *TMListItem) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *TMListItem) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *TMListItem) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetCreatedAt

`func (o *TMListItem) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *TMListItem) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *TMListItem) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetModifiedAt

`func (o *TMListItem) GetModifiedAt() time.Time`

GetModifiedAt returns the ModifiedAt field if non-nil, zero value otherwise.

### GetModifiedAtOk

`func (o *TMListItem) GetModifiedAtOk() (*time.Time, bool)`

GetModifiedAtOk returns a tuple with the ModifiedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedAt

`func (o *TMListItem) SetModifiedAt(v time.Time)`

SetModifiedAt sets ModifiedAt field to given value.


### GetOwner

`func (o *TMListItem) GetOwner() User`

GetOwner returns the Owner field if non-nil, zero value otherwise.

### GetOwnerOk

`func (o *TMListItem) GetOwnerOk() (*User, bool)`

GetOwnerOk returns a tuple with the Owner field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOwner

`func (o *TMListItem) SetOwner(v User)`

SetOwner sets Owner field to given value.


### GetCreatedBy

`func (o *TMListItem) GetCreatedBy() User`

GetCreatedBy returns the CreatedBy field if non-nil, zero value otherwise.

### GetCreatedByOk

`func (o *TMListItem) GetCreatedByOk() (*User, bool)`

GetCreatedByOk returns a tuple with the CreatedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedBy

`func (o *TMListItem) SetCreatedBy(v User)`

SetCreatedBy sets CreatedBy field to given value.


### GetThreatModelFramework

`func (o *TMListItem) GetThreatModelFramework() string`

GetThreatModelFramework returns the ThreatModelFramework field if non-nil, zero value otherwise.

### GetThreatModelFrameworkOk

`func (o *TMListItem) GetThreatModelFrameworkOk() (*string, bool)`

GetThreatModelFrameworkOk returns a tuple with the ThreatModelFramework field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreatModelFramework

`func (o *TMListItem) SetThreatModelFramework(v string)`

SetThreatModelFramework sets ThreatModelFramework field to given value.


### GetDocumentCount

`func (o *TMListItem) GetDocumentCount() int32`

GetDocumentCount returns the DocumentCount field if non-nil, zero value otherwise.

### GetDocumentCountOk

`func (o *TMListItem) GetDocumentCountOk() (*int32, bool)`

GetDocumentCountOk returns a tuple with the DocumentCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDocumentCount

`func (o *TMListItem) SetDocumentCount(v int32)`

SetDocumentCount sets DocumentCount field to given value.


### GetRepoCount

`func (o *TMListItem) GetRepoCount() int32`

GetRepoCount returns the RepoCount field if non-nil, zero value otherwise.

### GetRepoCountOk

`func (o *TMListItem) GetRepoCountOk() (*int32, bool)`

GetRepoCountOk returns a tuple with the RepoCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRepoCount

`func (o *TMListItem) SetRepoCount(v int32)`

SetRepoCount sets RepoCount field to given value.


### GetDiagramCount

`func (o *TMListItem) GetDiagramCount() int32`

GetDiagramCount returns the DiagramCount field if non-nil, zero value otherwise.

### GetDiagramCountOk

`func (o *TMListItem) GetDiagramCountOk() (*int32, bool)`

GetDiagramCountOk returns a tuple with the DiagramCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDiagramCount

`func (o *TMListItem) SetDiagramCount(v int32)`

SetDiagramCount sets DiagramCount field to given value.


### GetThreatCount

`func (o *TMListItem) GetThreatCount() int32`

GetThreatCount returns the ThreatCount field if non-nil, zero value otherwise.

### GetThreatCountOk

`func (o *TMListItem) GetThreatCountOk() (*int32, bool)`

GetThreatCountOk returns a tuple with the ThreatCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreatCount

`func (o *TMListItem) SetThreatCount(v int32)`

SetThreatCount sets ThreatCount field to given value.


### GetIssueUri

`func (o *TMListItem) GetIssueUri() string`

GetIssueUri returns the IssueUri field if non-nil, zero value otherwise.

### GetIssueUriOk

`func (o *TMListItem) GetIssueUriOk() (*string, bool)`

GetIssueUriOk returns a tuple with the IssueUri field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIssueUri

`func (o *TMListItem) SetIssueUri(v string)`

SetIssueUri sets IssueUri field to given value.

### HasIssueUri

`func (o *TMListItem) HasIssueUri() bool`

HasIssueUri returns a boolean if a field has been set.

### GetAssetCount

`func (o *TMListItem) GetAssetCount() int32`

GetAssetCount returns the AssetCount field if non-nil, zero value otherwise.

### GetAssetCountOk

`func (o *TMListItem) GetAssetCountOk() (*int32, bool)`

GetAssetCountOk returns a tuple with the AssetCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssetCount

`func (o *TMListItem) SetAssetCount(v int32)`

SetAssetCount sets AssetCount field to given value.


### GetNoteCount

`func (o *TMListItem) GetNoteCount() int32`

GetNoteCount returns the NoteCount field if non-nil, zero value otherwise.

### GetNoteCountOk

`func (o *TMListItem) GetNoteCountOk() (*int32, bool)`

GetNoteCountOk returns a tuple with the NoteCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNoteCount

`func (o *TMListItem) SetNoteCount(v int32)`

SetNoteCount sets NoteCount field to given value.


### GetStatus

`func (o *TMListItem) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *TMListItem) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *TMListItem) SetStatus(v string)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *TMListItem) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### SetStatusNil

`func (o *TMListItem) SetStatusNil(b bool)`

 SetStatusNil sets the value for Status to be an explicit nil

### UnsetStatus
`func (o *TMListItem) UnsetStatus()`

UnsetStatus ensures that no value is present for Status, not even an explicit nil
### GetStatusUpdated

`func (o *TMListItem) GetStatusUpdated() time.Time`

GetStatusUpdated returns the StatusUpdated field if non-nil, zero value otherwise.

### GetStatusUpdatedOk

`func (o *TMListItem) GetStatusUpdatedOk() (*time.Time, bool)`

GetStatusUpdatedOk returns a tuple with the StatusUpdated field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatusUpdated

`func (o *TMListItem) SetStatusUpdated(v time.Time)`

SetStatusUpdated sets StatusUpdated field to given value.

### HasStatusUpdated

`func (o *TMListItem) HasStatusUpdated() bool`

HasStatusUpdated returns a boolean if a field has been set.

### SetStatusUpdatedNil

`func (o *TMListItem) SetStatusUpdatedNil(b bool)`

 SetStatusUpdatedNil sets the value for StatusUpdated to be an explicit nil

### UnsetStatusUpdated
`func (o *TMListItem) UnsetStatusUpdated()`

UnsetStatusUpdated ensures that no value is present for StatusUpdated, not even an explicit nil
### GetSecurityReviewer

`func (o *TMListItem) GetSecurityReviewer() User`

GetSecurityReviewer returns the SecurityReviewer field if non-nil, zero value otherwise.

### GetSecurityReviewerOk

`func (o *TMListItem) GetSecurityReviewerOk() (*User, bool)`

GetSecurityReviewerOk returns a tuple with the SecurityReviewer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSecurityReviewer

`func (o *TMListItem) SetSecurityReviewer(v User)`

SetSecurityReviewer sets SecurityReviewer field to given value.

### HasSecurityReviewer

`func (o *TMListItem) HasSecurityReviewer() bool`

HasSecurityReviewer returns a boolean if a field has been set.

### SetSecurityReviewerNil

`func (o *TMListItem) SetSecurityReviewerNil(b bool)`

 SetSecurityReviewerNil sets the value for SecurityReviewer to be an explicit nil

### UnsetSecurityReviewer
`func (o *TMListItem) UnsetSecurityReviewer()`

UnsetSecurityReviewer ensures that no value is present for SecurityReviewer, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


