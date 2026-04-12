# ThreatModelBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Name of the threat model | 
**Description** | Pointer to **string** | Description of the threat model | [optional] 
**Owner** | [**User**](User.md) | User who owns the threat model (can be null for orphaned models) | 
**ThreatModelFramework** | **string** | The framework used for this threat model | 
**Authorization** | [**[]Authorization**](Authorization.md) | List of users and their roles for this threat model | 
**Metadata** | Pointer to [**[]Metadata**](Metadata.md) | Key-value pairs for additional threat model metadata | [optional] 
**IssueUri** | Pointer to **string** | URL to an issue in an issue tracking system for this threat model | [optional] 
**Status** | Pointer to **NullableString** | Status of the threat model in the organization&#39;s threat modeling or SDLC process. Examples: \&quot;Not started\&quot;, \&quot;In progress\&quot;, \&quot;Review\&quot;, \&quot;Approved\&quot;, \&quot;Closed\&quot; | [optional] 
**Alias** | Pointer to **[]string** | Alternative names or identifiers for the threat model | [optional] 
**SecurityReviewer** | Pointer to [**NullableUser**](User.md) | Security reviewer assigned to this threat model. When set, the security reviewer is automatically added to the authorization list with the owner role. The security reviewer&#39;s owner role cannot be removed via authorization changes while they remain assigned as security reviewer. To change the security reviewer&#39;s authorization, first unassign them as security reviewer. | [optional] 
**ProjectId** | Pointer to **NullableString** | Optional reference to the project this threat model belongs to | [optional] 

## Methods

### NewThreatModelBase

`func NewThreatModelBase(name string, owner User, threatModelFramework string, authorization []Authorization, ) *ThreatModelBase`

NewThreatModelBase instantiates a new ThreatModelBase object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewThreatModelBaseWithDefaults

`func NewThreatModelBaseWithDefaults() *ThreatModelBase`

NewThreatModelBaseWithDefaults instantiates a new ThreatModelBase object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *ThreatModelBase) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ThreatModelBase) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ThreatModelBase) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *ThreatModelBase) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *ThreatModelBase) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *ThreatModelBase) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *ThreatModelBase) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetOwner

`func (o *ThreatModelBase) GetOwner() User`

GetOwner returns the Owner field if non-nil, zero value otherwise.

### GetOwnerOk

`func (o *ThreatModelBase) GetOwnerOk() (*User, bool)`

GetOwnerOk returns a tuple with the Owner field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOwner

`func (o *ThreatModelBase) SetOwner(v User)`

SetOwner sets Owner field to given value.


### GetThreatModelFramework

`func (o *ThreatModelBase) GetThreatModelFramework() string`

GetThreatModelFramework returns the ThreatModelFramework field if non-nil, zero value otherwise.

### GetThreatModelFrameworkOk

`func (o *ThreatModelBase) GetThreatModelFrameworkOk() (*string, bool)`

GetThreatModelFrameworkOk returns a tuple with the ThreatModelFramework field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreatModelFramework

`func (o *ThreatModelBase) SetThreatModelFramework(v string)`

SetThreatModelFramework sets ThreatModelFramework field to given value.


### GetAuthorization

`func (o *ThreatModelBase) GetAuthorization() []Authorization`

GetAuthorization returns the Authorization field if non-nil, zero value otherwise.

### GetAuthorizationOk

`func (o *ThreatModelBase) GetAuthorizationOk() (*[]Authorization, bool)`

GetAuthorizationOk returns a tuple with the Authorization field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthorization

`func (o *ThreatModelBase) SetAuthorization(v []Authorization)`

SetAuthorization sets Authorization field to given value.


### GetMetadata

`func (o *ThreatModelBase) GetMetadata() []Metadata`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *ThreatModelBase) GetMetadataOk() (*[]Metadata, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *ThreatModelBase) SetMetadata(v []Metadata)`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *ThreatModelBase) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### SetMetadataNil

`func (o *ThreatModelBase) SetMetadataNil(b bool)`

 SetMetadataNil sets the value for Metadata to be an explicit nil

### UnsetMetadata
`func (o *ThreatModelBase) UnsetMetadata()`

UnsetMetadata ensures that no value is present for Metadata, not even an explicit nil
### GetIssueUri

`func (o *ThreatModelBase) GetIssueUri() string`

GetIssueUri returns the IssueUri field if non-nil, zero value otherwise.

### GetIssueUriOk

`func (o *ThreatModelBase) GetIssueUriOk() (*string, bool)`

GetIssueUriOk returns a tuple with the IssueUri field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIssueUri

`func (o *ThreatModelBase) SetIssueUri(v string)`

SetIssueUri sets IssueUri field to given value.

### HasIssueUri

`func (o *ThreatModelBase) HasIssueUri() bool`

HasIssueUri returns a boolean if a field has been set.

### GetStatus

`func (o *ThreatModelBase) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *ThreatModelBase) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *ThreatModelBase) SetStatus(v string)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *ThreatModelBase) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### SetStatusNil

`func (o *ThreatModelBase) SetStatusNil(b bool)`

 SetStatusNil sets the value for Status to be an explicit nil

### UnsetStatus
`func (o *ThreatModelBase) UnsetStatus()`

UnsetStatus ensures that no value is present for Status, not even an explicit nil
### GetAlias

`func (o *ThreatModelBase) GetAlias() []string`

GetAlias returns the Alias field if non-nil, zero value otherwise.

### GetAliasOk

`func (o *ThreatModelBase) GetAliasOk() (*[]string, bool)`

GetAliasOk returns a tuple with the Alias field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAlias

`func (o *ThreatModelBase) SetAlias(v []string)`

SetAlias sets Alias field to given value.

### HasAlias

`func (o *ThreatModelBase) HasAlias() bool`

HasAlias returns a boolean if a field has been set.

### GetSecurityReviewer

`func (o *ThreatModelBase) GetSecurityReviewer() User`

GetSecurityReviewer returns the SecurityReviewer field if non-nil, zero value otherwise.

### GetSecurityReviewerOk

`func (o *ThreatModelBase) GetSecurityReviewerOk() (*User, bool)`

GetSecurityReviewerOk returns a tuple with the SecurityReviewer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSecurityReviewer

`func (o *ThreatModelBase) SetSecurityReviewer(v User)`

SetSecurityReviewer sets SecurityReviewer field to given value.

### HasSecurityReviewer

`func (o *ThreatModelBase) HasSecurityReviewer() bool`

HasSecurityReviewer returns a boolean if a field has been set.

### SetSecurityReviewerNil

`func (o *ThreatModelBase) SetSecurityReviewerNil(b bool)`

 SetSecurityReviewerNil sets the value for SecurityReviewer to be an explicit nil

### UnsetSecurityReviewer
`func (o *ThreatModelBase) UnsetSecurityReviewer()`

UnsetSecurityReviewer ensures that no value is present for SecurityReviewer, not even an explicit nil
### GetProjectId

`func (o *ThreatModelBase) GetProjectId() string`

GetProjectId returns the ProjectId field if non-nil, zero value otherwise.

### GetProjectIdOk

`func (o *ThreatModelBase) GetProjectIdOk() (*string, bool)`

GetProjectIdOk returns a tuple with the ProjectId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectId

`func (o *ThreatModelBase) SetProjectId(v string)`

SetProjectId sets ProjectId field to given value.

### HasProjectId

`func (o *ThreatModelBase) HasProjectId() bool`

HasProjectId returns a boolean if a field has been set.

### SetProjectIdNil

`func (o *ThreatModelBase) SetProjectIdNil(b bool)`

 SetProjectIdNil sets the value for ProjectId to be an explicit nil

### UnsetProjectId
`func (o *ThreatModelBase) UnsetProjectId()`

UnsetProjectId ensures that no value is present for ProjectId, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


