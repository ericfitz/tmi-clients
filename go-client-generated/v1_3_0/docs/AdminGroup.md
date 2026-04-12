# AdminGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**InternalUuid** | **string** | Internal system UUID for the group | 
**Provider** | **string** | OAuth/SAML provider identifier, or \&quot;*\&quot; for provider-independent groups | 
**GroupName** | **string** | Provider-assigned group name | 
**Name** | Pointer to **string** | Human-readable group name | [optional] 
**Description** | Pointer to **string** | Group description | [optional] 
**FirstUsed** | **time.Time** | First time this group was referenced | 
**LastUsed** | **time.Time** | Last time this group was referenced | 
**UsageCount** | **int32** | Number of times this group has been referenced | 
**UsedInAuthorizations** | Pointer to **bool** | Whether this group is used in any authorizations (enriched) | [optional] [readonly] 
**UsedInAdminGrants** | Pointer to **bool** | Whether this group is used in any admin grants (enriched) | [optional] [readonly] 
**MemberCount** | Pointer to **int32** | Number of members in the group from IdP (enriched, if available) | [optional] [readonly] 

## Methods

### NewAdminGroup

`func NewAdminGroup(internalUuid string, provider string, groupName string, firstUsed time.Time, lastUsed time.Time, usageCount int32, ) *AdminGroup`

NewAdminGroup instantiates a new AdminGroup object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAdminGroupWithDefaults

`func NewAdminGroupWithDefaults() *AdminGroup`

NewAdminGroupWithDefaults instantiates a new AdminGroup object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetInternalUuid

`func (o *AdminGroup) GetInternalUuid() string`

GetInternalUuid returns the InternalUuid field if non-nil, zero value otherwise.

### GetInternalUuidOk

`func (o *AdminGroup) GetInternalUuidOk() (*string, bool)`

GetInternalUuidOk returns a tuple with the InternalUuid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInternalUuid

`func (o *AdminGroup) SetInternalUuid(v string)`

SetInternalUuid sets InternalUuid field to given value.


### GetProvider

`func (o *AdminGroup) GetProvider() string`

GetProvider returns the Provider field if non-nil, zero value otherwise.

### GetProviderOk

`func (o *AdminGroup) GetProviderOk() (*string, bool)`

GetProviderOk returns a tuple with the Provider field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProvider

`func (o *AdminGroup) SetProvider(v string)`

SetProvider sets Provider field to given value.


### GetGroupName

`func (o *AdminGroup) GetGroupName() string`

GetGroupName returns the GroupName field if non-nil, zero value otherwise.

### GetGroupNameOk

`func (o *AdminGroup) GetGroupNameOk() (*string, bool)`

GetGroupNameOk returns a tuple with the GroupName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroupName

`func (o *AdminGroup) SetGroupName(v string)`

SetGroupName sets GroupName field to given value.


### GetName

`func (o *AdminGroup) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *AdminGroup) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *AdminGroup) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *AdminGroup) HasName() bool`

HasName returns a boolean if a field has been set.

### GetDescription

`func (o *AdminGroup) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *AdminGroup) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *AdminGroup) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *AdminGroup) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetFirstUsed

`func (o *AdminGroup) GetFirstUsed() time.Time`

GetFirstUsed returns the FirstUsed field if non-nil, zero value otherwise.

### GetFirstUsedOk

`func (o *AdminGroup) GetFirstUsedOk() (*time.Time, bool)`

GetFirstUsedOk returns a tuple with the FirstUsed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFirstUsed

`func (o *AdminGroup) SetFirstUsed(v time.Time)`

SetFirstUsed sets FirstUsed field to given value.


### GetLastUsed

`func (o *AdminGroup) GetLastUsed() time.Time`

GetLastUsed returns the LastUsed field if non-nil, zero value otherwise.

### GetLastUsedOk

`func (o *AdminGroup) GetLastUsedOk() (*time.Time, bool)`

GetLastUsedOk returns a tuple with the LastUsed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastUsed

`func (o *AdminGroup) SetLastUsed(v time.Time)`

SetLastUsed sets LastUsed field to given value.


### GetUsageCount

`func (o *AdminGroup) GetUsageCount() int32`

GetUsageCount returns the UsageCount field if non-nil, zero value otherwise.

### GetUsageCountOk

`func (o *AdminGroup) GetUsageCountOk() (*int32, bool)`

GetUsageCountOk returns a tuple with the UsageCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUsageCount

`func (o *AdminGroup) SetUsageCount(v int32)`

SetUsageCount sets UsageCount field to given value.


### GetUsedInAuthorizations

`func (o *AdminGroup) GetUsedInAuthorizations() bool`

GetUsedInAuthorizations returns the UsedInAuthorizations field if non-nil, zero value otherwise.

### GetUsedInAuthorizationsOk

`func (o *AdminGroup) GetUsedInAuthorizationsOk() (*bool, bool)`

GetUsedInAuthorizationsOk returns a tuple with the UsedInAuthorizations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUsedInAuthorizations

`func (o *AdminGroup) SetUsedInAuthorizations(v bool)`

SetUsedInAuthorizations sets UsedInAuthorizations field to given value.

### HasUsedInAuthorizations

`func (o *AdminGroup) HasUsedInAuthorizations() bool`

HasUsedInAuthorizations returns a boolean if a field has been set.

### GetUsedInAdminGrants

`func (o *AdminGroup) GetUsedInAdminGrants() bool`

GetUsedInAdminGrants returns the UsedInAdminGrants field if non-nil, zero value otherwise.

### GetUsedInAdminGrantsOk

`func (o *AdminGroup) GetUsedInAdminGrantsOk() (*bool, bool)`

GetUsedInAdminGrantsOk returns a tuple with the UsedInAdminGrants field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUsedInAdminGrants

`func (o *AdminGroup) SetUsedInAdminGrants(v bool)`

SetUsedInAdminGrants sets UsedInAdminGrants field to given value.

### HasUsedInAdminGrants

`func (o *AdminGroup) HasUsedInAdminGrants() bool`

HasUsedInAdminGrants returns a boolean if a field has been set.

### GetMemberCount

`func (o *AdminGroup) GetMemberCount() int32`

GetMemberCount returns the MemberCount field if non-nil, zero value otherwise.

### GetMemberCountOk

`func (o *AdminGroup) GetMemberCountOk() (*int32, bool)`

GetMemberCountOk returns a tuple with the MemberCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMemberCount

`func (o *AdminGroup) SetMemberCount(v int32)`

SetMemberCount sets MemberCount field to given value.

### HasMemberCount

`func (o *AdminGroup) HasMemberCount() bool`

HasMemberCount returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


