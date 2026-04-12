# ThreatModelInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Name of the threat model | 
**Description** | Pointer to **NullableString** | Description of the threat model and its purpose | [optional] 
**ThreatModelFramework** | Pointer to **NullableString** | The framework used for this threat model | [optional] 
**Authorization** | Pointer to [**[]Authorization**](Authorization.md) | List of users and their roles for this threat model | [optional] 
**Metadata** | Pointer to [**[]Metadata**](Metadata.md) | Key-value pairs for additional threat model metadata | [optional] 
**IssueUri** | Pointer to **NullableString** | URL to an issue in an issue tracking system for this threat model | [optional] 
**IsConfidential** | Pointer to **bool** | If true, threat model is marked as confidential. Can only be set at creation. | [optional] [default to false]

## Methods

### NewThreatModelInput

`func NewThreatModelInput(name string, ) *ThreatModelInput`

NewThreatModelInput instantiates a new ThreatModelInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewThreatModelInputWithDefaults

`func NewThreatModelInputWithDefaults() *ThreatModelInput`

NewThreatModelInputWithDefaults instantiates a new ThreatModelInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *ThreatModelInput) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ThreatModelInput) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ThreatModelInput) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *ThreatModelInput) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *ThreatModelInput) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *ThreatModelInput) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *ThreatModelInput) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *ThreatModelInput) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *ThreatModelInput) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetThreatModelFramework

`func (o *ThreatModelInput) GetThreatModelFramework() string`

GetThreatModelFramework returns the ThreatModelFramework field if non-nil, zero value otherwise.

### GetThreatModelFrameworkOk

`func (o *ThreatModelInput) GetThreatModelFrameworkOk() (*string, bool)`

GetThreatModelFrameworkOk returns a tuple with the ThreatModelFramework field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreatModelFramework

`func (o *ThreatModelInput) SetThreatModelFramework(v string)`

SetThreatModelFramework sets ThreatModelFramework field to given value.

### HasThreatModelFramework

`func (o *ThreatModelInput) HasThreatModelFramework() bool`

HasThreatModelFramework returns a boolean if a field has been set.

### SetThreatModelFrameworkNil

`func (o *ThreatModelInput) SetThreatModelFrameworkNil(b bool)`

 SetThreatModelFrameworkNil sets the value for ThreatModelFramework to be an explicit nil

### UnsetThreatModelFramework
`func (o *ThreatModelInput) UnsetThreatModelFramework()`

UnsetThreatModelFramework ensures that no value is present for ThreatModelFramework, not even an explicit nil
### GetAuthorization

`func (o *ThreatModelInput) GetAuthorization() []Authorization`

GetAuthorization returns the Authorization field if non-nil, zero value otherwise.

### GetAuthorizationOk

`func (o *ThreatModelInput) GetAuthorizationOk() (*[]Authorization, bool)`

GetAuthorizationOk returns a tuple with the Authorization field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthorization

`func (o *ThreatModelInput) SetAuthorization(v []Authorization)`

SetAuthorization sets Authorization field to given value.

### HasAuthorization

`func (o *ThreatModelInput) HasAuthorization() bool`

HasAuthorization returns a boolean if a field has been set.

### GetMetadata

`func (o *ThreatModelInput) GetMetadata() []Metadata`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *ThreatModelInput) GetMetadataOk() (*[]Metadata, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *ThreatModelInput) SetMetadata(v []Metadata)`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *ThreatModelInput) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### SetMetadataNil

`func (o *ThreatModelInput) SetMetadataNil(b bool)`

 SetMetadataNil sets the value for Metadata to be an explicit nil

### UnsetMetadata
`func (o *ThreatModelInput) UnsetMetadata()`

UnsetMetadata ensures that no value is present for Metadata, not even an explicit nil
### GetIssueUri

`func (o *ThreatModelInput) GetIssueUri() string`

GetIssueUri returns the IssueUri field if non-nil, zero value otherwise.

### GetIssueUriOk

`func (o *ThreatModelInput) GetIssueUriOk() (*string, bool)`

GetIssueUriOk returns a tuple with the IssueUri field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIssueUri

`func (o *ThreatModelInput) SetIssueUri(v string)`

SetIssueUri sets IssueUri field to given value.

### HasIssueUri

`func (o *ThreatModelInput) HasIssueUri() bool`

HasIssueUri returns a boolean if a field has been set.

### SetIssueUriNil

`func (o *ThreatModelInput) SetIssueUriNil(b bool)`

 SetIssueUriNil sets the value for IssueUri to be an explicit nil

### UnsetIssueUri
`func (o *ThreatModelInput) UnsetIssueUri()`

UnsetIssueUri ensures that no value is present for IssueUri, not even an explicit nil
### GetIsConfidential

`func (o *ThreatModelInput) GetIsConfidential() bool`

GetIsConfidential returns the IsConfidential field if non-nil, zero value otherwise.

### GetIsConfidentialOk

`func (o *ThreatModelInput) GetIsConfidentialOk() (*bool, bool)`

GetIsConfidentialOk returns a tuple with the IsConfidential field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsConfidential

`func (o *ThreatModelInput) SetIsConfidential(v bool)`

SetIsConfidential sets IsConfidential field to given value.

### HasIsConfidential

`func (o *ThreatModelInput) HasIsConfidential() bool`

HasIsConfidential returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


