# ThreatModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Name of the threat model | 
**Description** | Pointer to **NullableString** | Description of the threat model | [optional] 
**Owner** | [**User**](User.md) | User who owns the threat model (can be null for orphaned models) | 
**ThreatModelFramework** | **string** | The framework used for this threat model | 
**Authorization** | [**[]Authorization**](Authorization.md) | List of users and their roles for this threat model | 
**Metadata** | Pointer to [**[]Metadata**](Metadata.md) | Key-value pairs for additional threat model metadata | [optional] 
**IssueUri** | Pointer to **NullableString** | URL to an issue in an issue tracking system for this threat model | [optional] 
**Status** | Pointer to **NullableString** | Status of the threat model in the organization&#39;s threat modeling or SDLC process. Examples: \&quot;Not started\&quot;, \&quot;In progress\&quot;, \&quot;Review\&quot;, \&quot;Approved\&quot;, \&quot;Closed\&quot; | [optional] 
**Alias** | Pointer to **[]string** | Alternative names or identifiers for the threat model | [optional] 
**SecurityReviewer** | Pointer to [**NullableUser**](User.md) | Security reviewer assigned to this threat model. When set, the security reviewer is automatically added to the authorization list with the owner role. The security reviewer&#39;s owner role cannot be removed via authorization changes while they remain assigned as security reviewer. To change the security reviewer&#39;s authorization, first unassign them as security reviewer. | [optional] 
**ProjectId** | Pointer to **NullableString** | Optional reference to the project this threat model belongs to | [optional] 
**Id** | Pointer to **string** | Unique identifier for the threat model (UUID) | [optional] [readonly] 
**CreatedAt** | Pointer to **time.Time** | Creation timestamp (RFC3339) | [optional] [readonly] 
**ModifiedAt** | Pointer to **time.Time** | Last modification timestamp (RFC3339) | [optional] [readonly] 
**CreatedBy** | Pointer to [**User**](User.md) | User who created the threat model | [optional] [readonly] 
**Documents** | Pointer to [**[]Document**](Document.md) | List of documents related to the threat model | [optional] [readonly] 
**Repositories** | Pointer to [**[]Repository**](Repository.md) | List of source code repositories related to the threat model | [optional] [readonly] 
**Diagrams** | Pointer to [**[]DfdDiagram**](DfdDiagram.md) | List of diagram objects associated with this threat model | [optional] [readonly] 
**Threats** | Pointer to [**[]Threat**](Threat.md) | List of threats within the threat model | [optional] [readonly] 
**Notes** | Pointer to [**[]Note**](Note.md) | List of notes associated with the threat model | [optional] [readonly] 
**Assets** | Pointer to [**[]ExtendedAsset**](ExtendedAsset.md) | List of assets associated with the threat model | [optional] [readonly] 
**StatusUpdated** | Pointer to **NullableTime** | Timestamp when the status field was last modified (RFC3339). Automatically updated by the server when status changes. | [optional] [readonly] 
**IsConfidential** | Pointer to **bool** | Whether this threat model is confidential (set at creation, read-only after) | [optional] [readonly] 
**DeletedAt** | Pointer to **NullableTime** | Deletion timestamp (RFC3339). Present only on soft-deleted entities within the tombstone retention period. | [optional] [readonly] 

## Methods

### NewThreatModel

`func NewThreatModel(name string, owner User, threatModelFramework string, authorization []Authorization, ) *ThreatModel`

NewThreatModel instantiates a new ThreatModel object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewThreatModelWithDefaults

`func NewThreatModelWithDefaults() *ThreatModel`

NewThreatModelWithDefaults instantiates a new ThreatModel object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *ThreatModel) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ThreatModel) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ThreatModel) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *ThreatModel) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *ThreatModel) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *ThreatModel) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *ThreatModel) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *ThreatModel) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *ThreatModel) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetOwner

`func (o *ThreatModel) GetOwner() User`

GetOwner returns the Owner field if non-nil, zero value otherwise.

### GetOwnerOk

`func (o *ThreatModel) GetOwnerOk() (*User, bool)`

GetOwnerOk returns a tuple with the Owner field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOwner

`func (o *ThreatModel) SetOwner(v User)`

SetOwner sets Owner field to given value.


### GetThreatModelFramework

`func (o *ThreatModel) GetThreatModelFramework() string`

GetThreatModelFramework returns the ThreatModelFramework field if non-nil, zero value otherwise.

### GetThreatModelFrameworkOk

`func (o *ThreatModel) GetThreatModelFrameworkOk() (*string, bool)`

GetThreatModelFrameworkOk returns a tuple with the ThreatModelFramework field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreatModelFramework

`func (o *ThreatModel) SetThreatModelFramework(v string)`

SetThreatModelFramework sets ThreatModelFramework field to given value.


### GetAuthorization

`func (o *ThreatModel) GetAuthorization() []Authorization`

GetAuthorization returns the Authorization field if non-nil, zero value otherwise.

### GetAuthorizationOk

`func (o *ThreatModel) GetAuthorizationOk() (*[]Authorization, bool)`

GetAuthorizationOk returns a tuple with the Authorization field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthorization

`func (o *ThreatModel) SetAuthorization(v []Authorization)`

SetAuthorization sets Authorization field to given value.


### GetMetadata

`func (o *ThreatModel) GetMetadata() []Metadata`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *ThreatModel) GetMetadataOk() (*[]Metadata, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *ThreatModel) SetMetadata(v []Metadata)`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *ThreatModel) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### SetMetadataNil

`func (o *ThreatModel) SetMetadataNil(b bool)`

 SetMetadataNil sets the value for Metadata to be an explicit nil

### UnsetMetadata
`func (o *ThreatModel) UnsetMetadata()`

UnsetMetadata ensures that no value is present for Metadata, not even an explicit nil
### GetIssueUri

`func (o *ThreatModel) GetIssueUri() string`

GetIssueUri returns the IssueUri field if non-nil, zero value otherwise.

### GetIssueUriOk

`func (o *ThreatModel) GetIssueUriOk() (*string, bool)`

GetIssueUriOk returns a tuple with the IssueUri field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIssueUri

`func (o *ThreatModel) SetIssueUri(v string)`

SetIssueUri sets IssueUri field to given value.

### HasIssueUri

`func (o *ThreatModel) HasIssueUri() bool`

HasIssueUri returns a boolean if a field has been set.

### SetIssueUriNil

`func (o *ThreatModel) SetIssueUriNil(b bool)`

 SetIssueUriNil sets the value for IssueUri to be an explicit nil

### UnsetIssueUri
`func (o *ThreatModel) UnsetIssueUri()`

UnsetIssueUri ensures that no value is present for IssueUri, not even an explicit nil
### GetStatus

`func (o *ThreatModel) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *ThreatModel) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *ThreatModel) SetStatus(v string)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *ThreatModel) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### SetStatusNil

`func (o *ThreatModel) SetStatusNil(b bool)`

 SetStatusNil sets the value for Status to be an explicit nil

### UnsetStatus
`func (o *ThreatModel) UnsetStatus()`

UnsetStatus ensures that no value is present for Status, not even an explicit nil
### GetAlias

`func (o *ThreatModel) GetAlias() []string`

GetAlias returns the Alias field if non-nil, zero value otherwise.

### GetAliasOk

`func (o *ThreatModel) GetAliasOk() (*[]string, bool)`

GetAliasOk returns a tuple with the Alias field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAlias

`func (o *ThreatModel) SetAlias(v []string)`

SetAlias sets Alias field to given value.

### HasAlias

`func (o *ThreatModel) HasAlias() bool`

HasAlias returns a boolean if a field has been set.

### GetSecurityReviewer

`func (o *ThreatModel) GetSecurityReviewer() User`

GetSecurityReviewer returns the SecurityReviewer field if non-nil, zero value otherwise.

### GetSecurityReviewerOk

`func (o *ThreatModel) GetSecurityReviewerOk() (*User, bool)`

GetSecurityReviewerOk returns a tuple with the SecurityReviewer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSecurityReviewer

`func (o *ThreatModel) SetSecurityReviewer(v User)`

SetSecurityReviewer sets SecurityReviewer field to given value.

### HasSecurityReviewer

`func (o *ThreatModel) HasSecurityReviewer() bool`

HasSecurityReviewer returns a boolean if a field has been set.

### SetSecurityReviewerNil

`func (o *ThreatModel) SetSecurityReviewerNil(b bool)`

 SetSecurityReviewerNil sets the value for SecurityReviewer to be an explicit nil

### UnsetSecurityReviewer
`func (o *ThreatModel) UnsetSecurityReviewer()`

UnsetSecurityReviewer ensures that no value is present for SecurityReviewer, not even an explicit nil
### GetProjectId

`func (o *ThreatModel) GetProjectId() string`

GetProjectId returns the ProjectId field if non-nil, zero value otherwise.

### GetProjectIdOk

`func (o *ThreatModel) GetProjectIdOk() (*string, bool)`

GetProjectIdOk returns a tuple with the ProjectId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectId

`func (o *ThreatModel) SetProjectId(v string)`

SetProjectId sets ProjectId field to given value.

### HasProjectId

`func (o *ThreatModel) HasProjectId() bool`

HasProjectId returns a boolean if a field has been set.

### SetProjectIdNil

`func (o *ThreatModel) SetProjectIdNil(b bool)`

 SetProjectIdNil sets the value for ProjectId to be an explicit nil

### UnsetProjectId
`func (o *ThreatModel) UnsetProjectId()`

UnsetProjectId ensures that no value is present for ProjectId, not even an explicit nil
### GetId

`func (o *ThreatModel) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ThreatModel) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ThreatModel) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *ThreatModel) HasId() bool`

HasId returns a boolean if a field has been set.

### GetCreatedAt

`func (o *ThreatModel) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *ThreatModel) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *ThreatModel) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *ThreatModel) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetModifiedAt

`func (o *ThreatModel) GetModifiedAt() time.Time`

GetModifiedAt returns the ModifiedAt field if non-nil, zero value otherwise.

### GetModifiedAtOk

`func (o *ThreatModel) GetModifiedAtOk() (*time.Time, bool)`

GetModifiedAtOk returns a tuple with the ModifiedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedAt

`func (o *ThreatModel) SetModifiedAt(v time.Time)`

SetModifiedAt sets ModifiedAt field to given value.

### HasModifiedAt

`func (o *ThreatModel) HasModifiedAt() bool`

HasModifiedAt returns a boolean if a field has been set.

### GetCreatedBy

`func (o *ThreatModel) GetCreatedBy() User`

GetCreatedBy returns the CreatedBy field if non-nil, zero value otherwise.

### GetCreatedByOk

`func (o *ThreatModel) GetCreatedByOk() (*User, bool)`

GetCreatedByOk returns a tuple with the CreatedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedBy

`func (o *ThreatModel) SetCreatedBy(v User)`

SetCreatedBy sets CreatedBy field to given value.

### HasCreatedBy

`func (o *ThreatModel) HasCreatedBy() bool`

HasCreatedBy returns a boolean if a field has been set.

### GetDocuments

`func (o *ThreatModel) GetDocuments() []Document`

GetDocuments returns the Documents field if non-nil, zero value otherwise.

### GetDocumentsOk

`func (o *ThreatModel) GetDocumentsOk() (*[]Document, bool)`

GetDocumentsOk returns a tuple with the Documents field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDocuments

`func (o *ThreatModel) SetDocuments(v []Document)`

SetDocuments sets Documents field to given value.

### HasDocuments

`func (o *ThreatModel) HasDocuments() bool`

HasDocuments returns a boolean if a field has been set.

### GetRepositories

`func (o *ThreatModel) GetRepositories() []Repository`

GetRepositories returns the Repositories field if non-nil, zero value otherwise.

### GetRepositoriesOk

`func (o *ThreatModel) GetRepositoriesOk() (*[]Repository, bool)`

GetRepositoriesOk returns a tuple with the Repositories field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRepositories

`func (o *ThreatModel) SetRepositories(v []Repository)`

SetRepositories sets Repositories field to given value.

### HasRepositories

`func (o *ThreatModel) HasRepositories() bool`

HasRepositories returns a boolean if a field has been set.

### GetDiagrams

`func (o *ThreatModel) GetDiagrams() []DfdDiagram`

GetDiagrams returns the Diagrams field if non-nil, zero value otherwise.

### GetDiagramsOk

`func (o *ThreatModel) GetDiagramsOk() (*[]DfdDiagram, bool)`

GetDiagramsOk returns a tuple with the Diagrams field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDiagrams

`func (o *ThreatModel) SetDiagrams(v []DfdDiagram)`

SetDiagrams sets Diagrams field to given value.

### HasDiagrams

`func (o *ThreatModel) HasDiagrams() bool`

HasDiagrams returns a boolean if a field has been set.

### GetThreats

`func (o *ThreatModel) GetThreats() []Threat`

GetThreats returns the Threats field if non-nil, zero value otherwise.

### GetThreatsOk

`func (o *ThreatModel) GetThreatsOk() (*[]Threat, bool)`

GetThreatsOk returns a tuple with the Threats field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreats

`func (o *ThreatModel) SetThreats(v []Threat)`

SetThreats sets Threats field to given value.

### HasThreats

`func (o *ThreatModel) HasThreats() bool`

HasThreats returns a boolean if a field has been set.

### GetNotes

`func (o *ThreatModel) GetNotes() []Note`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *ThreatModel) GetNotesOk() (*[]Note, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNotes

`func (o *ThreatModel) SetNotes(v []Note)`

SetNotes sets Notes field to given value.

### HasNotes

`func (o *ThreatModel) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### GetAssets

`func (o *ThreatModel) GetAssets() []ExtendedAsset`

GetAssets returns the Assets field if non-nil, zero value otherwise.

### GetAssetsOk

`func (o *ThreatModel) GetAssetsOk() (*[]ExtendedAsset, bool)`

GetAssetsOk returns a tuple with the Assets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssets

`func (o *ThreatModel) SetAssets(v []ExtendedAsset)`

SetAssets sets Assets field to given value.

### HasAssets

`func (o *ThreatModel) HasAssets() bool`

HasAssets returns a boolean if a field has been set.

### GetStatusUpdated

`func (o *ThreatModel) GetStatusUpdated() time.Time`

GetStatusUpdated returns the StatusUpdated field if non-nil, zero value otherwise.

### GetStatusUpdatedOk

`func (o *ThreatModel) GetStatusUpdatedOk() (*time.Time, bool)`

GetStatusUpdatedOk returns a tuple with the StatusUpdated field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatusUpdated

`func (o *ThreatModel) SetStatusUpdated(v time.Time)`

SetStatusUpdated sets StatusUpdated field to given value.

### HasStatusUpdated

`func (o *ThreatModel) HasStatusUpdated() bool`

HasStatusUpdated returns a boolean if a field has been set.

### SetStatusUpdatedNil

`func (o *ThreatModel) SetStatusUpdatedNil(b bool)`

 SetStatusUpdatedNil sets the value for StatusUpdated to be an explicit nil

### UnsetStatusUpdated
`func (o *ThreatModel) UnsetStatusUpdated()`

UnsetStatusUpdated ensures that no value is present for StatusUpdated, not even an explicit nil
### GetIsConfidential

`func (o *ThreatModel) GetIsConfidential() bool`

GetIsConfidential returns the IsConfidential field if non-nil, zero value otherwise.

### GetIsConfidentialOk

`func (o *ThreatModel) GetIsConfidentialOk() (*bool, bool)`

GetIsConfidentialOk returns a tuple with the IsConfidential field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsConfidential

`func (o *ThreatModel) SetIsConfidential(v bool)`

SetIsConfidential sets IsConfidential field to given value.

### HasIsConfidential

`func (o *ThreatModel) HasIsConfidential() bool`

HasIsConfidential returns a boolean if a field has been set.

### GetDeletedAt

`func (o *ThreatModel) GetDeletedAt() time.Time`

GetDeletedAt returns the DeletedAt field if non-nil, zero value otherwise.

### GetDeletedAtOk

`func (o *ThreatModel) GetDeletedAtOk() (*time.Time, bool)`

GetDeletedAtOk returns a tuple with the DeletedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeletedAt

`func (o *ThreatModel) SetDeletedAt(v time.Time)`

SetDeletedAt sets DeletedAt field to given value.

### HasDeletedAt

`func (o *ThreatModel) HasDeletedAt() bool`

HasDeletedAt returns a boolean if a field has been set.

### SetDeletedAtNil

`func (o *ThreatModel) SetDeletedAtNil(b bool)`

 SetDeletedAtNil sets the value for DeletedAt to be an explicit nil

### UnsetDeletedAt
`func (o *ThreatModel) UnsetDeletedAt()`

UnsetDeletedAt ensures that no value is present for DeletedAt, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


