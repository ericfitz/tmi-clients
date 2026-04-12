# AdminUser

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**InternalUuid** | **string** | Internal system UUID for the user | 
**Provider** | **string** | OAuth/SAML provider identifier | 
**ProviderUserId** | **string** | Provider-assigned user identifier | 
**Email** | **string** | User email address | 
**Name** | **string** | User display name | 
**EmailVerified** | **bool** | Whether the email has been verified | 
**CreatedAt** | **time.Time** | Account creation timestamp | 
**ModifiedAt** | **time.Time** | Last modification timestamp | 
**LastLogin** | Pointer to **NullableTime** | Last login timestamp | [optional] 
**IsAdmin** | Pointer to **bool** | Whether the user has administrator privileges (enriched) | [optional] [readonly] 
**Groups** | Pointer to **[]string** | List of group names the user belongs to (enriched) | [optional] [readonly] 
**ActiveThreatModels** | Pointer to **int32** | Number of active threat models owned by user (enriched) | [optional] [readonly] 

## Methods

### NewAdminUser

`func NewAdminUser(internalUuid string, provider string, providerUserId string, email string, name string, emailVerified bool, createdAt time.Time, modifiedAt time.Time, ) *AdminUser`

NewAdminUser instantiates a new AdminUser object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAdminUserWithDefaults

`func NewAdminUserWithDefaults() *AdminUser`

NewAdminUserWithDefaults instantiates a new AdminUser object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetInternalUuid

`func (o *AdminUser) GetInternalUuid() string`

GetInternalUuid returns the InternalUuid field if non-nil, zero value otherwise.

### GetInternalUuidOk

`func (o *AdminUser) GetInternalUuidOk() (*string, bool)`

GetInternalUuidOk returns a tuple with the InternalUuid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInternalUuid

`func (o *AdminUser) SetInternalUuid(v string)`

SetInternalUuid sets InternalUuid field to given value.


### GetProvider

`func (o *AdminUser) GetProvider() string`

GetProvider returns the Provider field if non-nil, zero value otherwise.

### GetProviderOk

`func (o *AdminUser) GetProviderOk() (*string, bool)`

GetProviderOk returns a tuple with the Provider field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProvider

`func (o *AdminUser) SetProvider(v string)`

SetProvider sets Provider field to given value.


### GetProviderUserId

`func (o *AdminUser) GetProviderUserId() string`

GetProviderUserId returns the ProviderUserId field if non-nil, zero value otherwise.

### GetProviderUserIdOk

`func (o *AdminUser) GetProviderUserIdOk() (*string, bool)`

GetProviderUserIdOk returns a tuple with the ProviderUserId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderUserId

`func (o *AdminUser) SetProviderUserId(v string)`

SetProviderUserId sets ProviderUserId field to given value.


### GetEmail

`func (o *AdminUser) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *AdminUser) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *AdminUser) SetEmail(v string)`

SetEmail sets Email field to given value.


### GetName

`func (o *AdminUser) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *AdminUser) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *AdminUser) SetName(v string)`

SetName sets Name field to given value.


### GetEmailVerified

`func (o *AdminUser) GetEmailVerified() bool`

GetEmailVerified returns the EmailVerified field if non-nil, zero value otherwise.

### GetEmailVerifiedOk

`func (o *AdminUser) GetEmailVerifiedOk() (*bool, bool)`

GetEmailVerifiedOk returns a tuple with the EmailVerified field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmailVerified

`func (o *AdminUser) SetEmailVerified(v bool)`

SetEmailVerified sets EmailVerified field to given value.


### GetCreatedAt

`func (o *AdminUser) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *AdminUser) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *AdminUser) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetModifiedAt

`func (o *AdminUser) GetModifiedAt() time.Time`

GetModifiedAt returns the ModifiedAt field if non-nil, zero value otherwise.

### GetModifiedAtOk

`func (o *AdminUser) GetModifiedAtOk() (*time.Time, bool)`

GetModifiedAtOk returns a tuple with the ModifiedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedAt

`func (o *AdminUser) SetModifiedAt(v time.Time)`

SetModifiedAt sets ModifiedAt field to given value.


### GetLastLogin

`func (o *AdminUser) GetLastLogin() time.Time`

GetLastLogin returns the LastLogin field if non-nil, zero value otherwise.

### GetLastLoginOk

`func (o *AdminUser) GetLastLoginOk() (*time.Time, bool)`

GetLastLoginOk returns a tuple with the LastLogin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastLogin

`func (o *AdminUser) SetLastLogin(v time.Time)`

SetLastLogin sets LastLogin field to given value.

### HasLastLogin

`func (o *AdminUser) HasLastLogin() bool`

HasLastLogin returns a boolean if a field has been set.

### SetLastLoginNil

`func (o *AdminUser) SetLastLoginNil(b bool)`

 SetLastLoginNil sets the value for LastLogin to be an explicit nil

### UnsetLastLogin
`func (o *AdminUser) UnsetLastLogin()`

UnsetLastLogin ensures that no value is present for LastLogin, not even an explicit nil
### GetIsAdmin

`func (o *AdminUser) GetIsAdmin() bool`

GetIsAdmin returns the IsAdmin field if non-nil, zero value otherwise.

### GetIsAdminOk

`func (o *AdminUser) GetIsAdminOk() (*bool, bool)`

GetIsAdminOk returns a tuple with the IsAdmin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsAdmin

`func (o *AdminUser) SetIsAdmin(v bool)`

SetIsAdmin sets IsAdmin field to given value.

### HasIsAdmin

`func (o *AdminUser) HasIsAdmin() bool`

HasIsAdmin returns a boolean if a field has been set.

### GetGroups

`func (o *AdminUser) GetGroups() []string`

GetGroups returns the Groups field if non-nil, zero value otherwise.

### GetGroupsOk

`func (o *AdminUser) GetGroupsOk() (*[]string, bool)`

GetGroupsOk returns a tuple with the Groups field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroups

`func (o *AdminUser) SetGroups(v []string)`

SetGroups sets Groups field to given value.

### HasGroups

`func (o *AdminUser) HasGroups() bool`

HasGroups returns a boolean if a field has been set.

### GetActiveThreatModels

`func (o *AdminUser) GetActiveThreatModels() int32`

GetActiveThreatModels returns the ActiveThreatModels field if non-nil, zero value otherwise.

### GetActiveThreatModelsOk

`func (o *AdminUser) GetActiveThreatModelsOk() (*int32, bool)`

GetActiveThreatModelsOk returns a tuple with the ActiveThreatModels field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActiveThreatModels

`func (o *AdminUser) SetActiveThreatModels(v int32)`

SetActiveThreatModels sets ActiveThreatModels field to given value.

### HasActiveThreatModels

`func (o *AdminUser) HasActiveThreatModels() bool`

HasActiveThreatModels returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


