# UserWithAdminStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**PrincipalType** | **string** | Always \&quot;user\&quot; for User objects | 
**Provider** | **string** | Identity provider name (e.g., \&quot;google\&quot;, \&quot;github\&quot;, \&quot;microsoft\&quot;, \&quot;tmi\&quot;). Use \&quot;*\&quot; for provider-independent groups. | 
**ProviderId** | **string** | Provider-assigned identifier. For users: provider_user_id (e.g., email or OAuth sub). For groups: group_name. | 
**DisplayName** | **string** | User full name for display | 
**Email** | **string** | User email address (required) | 
**IsAdmin** | **bool** | Whether the user has administrator privileges (computed dynamically based on Administrators group membership) | 
**IsSecurityReviewer** | **bool** | Whether the user is a security reviewer (computed dynamically based on Security Reviewers group membership) | 
**Groups** | [**[]UserGroupMembership**](UserGroupMembership.md) | TMI-managed groups that the user belongs to (direct membership only, excludes the implicit everyone pseudo-group) | 

## Methods

### NewUserWithAdminStatus

`func NewUserWithAdminStatus(principalType string, provider string, providerId string, displayName string, email string, isAdmin bool, isSecurityReviewer bool, groups []UserGroupMembership, ) *UserWithAdminStatus`

NewUserWithAdminStatus instantiates a new UserWithAdminStatus object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUserWithAdminStatusWithDefaults

`func NewUserWithAdminStatusWithDefaults() *UserWithAdminStatus`

NewUserWithAdminStatusWithDefaults instantiates a new UserWithAdminStatus object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPrincipalType

`func (o *UserWithAdminStatus) GetPrincipalType() string`

GetPrincipalType returns the PrincipalType field if non-nil, zero value otherwise.

### GetPrincipalTypeOk

`func (o *UserWithAdminStatus) GetPrincipalTypeOk() (*string, bool)`

GetPrincipalTypeOk returns a tuple with the PrincipalType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrincipalType

`func (o *UserWithAdminStatus) SetPrincipalType(v string)`

SetPrincipalType sets PrincipalType field to given value.


### GetProvider

`func (o *UserWithAdminStatus) GetProvider() string`

GetProvider returns the Provider field if non-nil, zero value otherwise.

### GetProviderOk

`func (o *UserWithAdminStatus) GetProviderOk() (*string, bool)`

GetProviderOk returns a tuple with the Provider field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProvider

`func (o *UserWithAdminStatus) SetProvider(v string)`

SetProvider sets Provider field to given value.


### GetProviderId

`func (o *UserWithAdminStatus) GetProviderId() string`

GetProviderId returns the ProviderId field if non-nil, zero value otherwise.

### GetProviderIdOk

`func (o *UserWithAdminStatus) GetProviderIdOk() (*string, bool)`

GetProviderIdOk returns a tuple with the ProviderId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderId

`func (o *UserWithAdminStatus) SetProviderId(v string)`

SetProviderId sets ProviderId field to given value.


### GetDisplayName

`func (o *UserWithAdminStatus) GetDisplayName() string`

GetDisplayName returns the DisplayName field if non-nil, zero value otherwise.

### GetDisplayNameOk

`func (o *UserWithAdminStatus) GetDisplayNameOk() (*string, bool)`

GetDisplayNameOk returns a tuple with the DisplayName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplayName

`func (o *UserWithAdminStatus) SetDisplayName(v string)`

SetDisplayName sets DisplayName field to given value.


### GetEmail

`func (o *UserWithAdminStatus) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *UserWithAdminStatus) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *UserWithAdminStatus) SetEmail(v string)`

SetEmail sets Email field to given value.


### GetIsAdmin

`func (o *UserWithAdminStatus) GetIsAdmin() bool`

GetIsAdmin returns the IsAdmin field if non-nil, zero value otherwise.

### GetIsAdminOk

`func (o *UserWithAdminStatus) GetIsAdminOk() (*bool, bool)`

GetIsAdminOk returns a tuple with the IsAdmin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsAdmin

`func (o *UserWithAdminStatus) SetIsAdmin(v bool)`

SetIsAdmin sets IsAdmin field to given value.


### GetIsSecurityReviewer

`func (o *UserWithAdminStatus) GetIsSecurityReviewer() bool`

GetIsSecurityReviewer returns the IsSecurityReviewer field if non-nil, zero value otherwise.

### GetIsSecurityReviewerOk

`func (o *UserWithAdminStatus) GetIsSecurityReviewerOk() (*bool, bool)`

GetIsSecurityReviewerOk returns a tuple with the IsSecurityReviewer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsSecurityReviewer

`func (o *UserWithAdminStatus) SetIsSecurityReviewer(v bool)`

SetIsSecurityReviewer sets IsSecurityReviewer field to given value.


### GetGroups

`func (o *UserWithAdminStatus) GetGroups() []UserGroupMembership`

GetGroups returns the Groups field if non-nil, zero value otherwise.

### GetGroupsOk

`func (o *UserWithAdminStatus) GetGroupsOk() (*[]UserGroupMembership, bool)`

GetGroupsOk returns a tuple with the Groups field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroups

`func (o *UserWithAdminStatus) SetGroups(v []UserGroupMembership)`

SetGroups sets Groups field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


