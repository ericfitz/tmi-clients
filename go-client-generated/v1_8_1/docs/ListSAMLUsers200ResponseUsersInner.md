# ListSAMLUsers200ResponseUsersInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**InternalUuid** | **string** | TMI-internal identifier for the user. | 
**Email** | **string** | User&#39;s email address as asserted by the identity provider. | 
**Name** | **string** | User&#39;s display name. | 
**LastLogin** | Pointer to **time.Time** | When the user last authenticated. Omitted if the user has never logged in. | [optional] 

## Methods

### NewListSAMLUsers200ResponseUsersInner

`func NewListSAMLUsers200ResponseUsersInner(internalUuid string, email string, name string, ) *ListSAMLUsers200ResponseUsersInner`

NewListSAMLUsers200ResponseUsersInner instantiates a new ListSAMLUsers200ResponseUsersInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListSAMLUsers200ResponseUsersInnerWithDefaults

`func NewListSAMLUsers200ResponseUsersInnerWithDefaults() *ListSAMLUsers200ResponseUsersInner`

NewListSAMLUsers200ResponseUsersInnerWithDefaults instantiates a new ListSAMLUsers200ResponseUsersInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetInternalUuid

`func (o *ListSAMLUsers200ResponseUsersInner) GetInternalUuid() string`

GetInternalUuid returns the InternalUuid field if non-nil, zero value otherwise.

### GetInternalUuidOk

`func (o *ListSAMLUsers200ResponseUsersInner) GetInternalUuidOk() (*string, bool)`

GetInternalUuidOk returns a tuple with the InternalUuid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInternalUuid

`func (o *ListSAMLUsers200ResponseUsersInner) SetInternalUuid(v string)`

SetInternalUuid sets InternalUuid field to given value.


### GetEmail

`func (o *ListSAMLUsers200ResponseUsersInner) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *ListSAMLUsers200ResponseUsersInner) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *ListSAMLUsers200ResponseUsersInner) SetEmail(v string)`

SetEmail sets Email field to given value.


### GetName

`func (o *ListSAMLUsers200ResponseUsersInner) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ListSAMLUsers200ResponseUsersInner) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ListSAMLUsers200ResponseUsersInner) SetName(v string)`

SetName sets Name field to given value.


### GetLastLogin

`func (o *ListSAMLUsers200ResponseUsersInner) GetLastLogin() time.Time`

GetLastLogin returns the LastLogin field if non-nil, zero value otherwise.

### GetLastLoginOk

`func (o *ListSAMLUsers200ResponseUsersInner) GetLastLoginOk() (*time.Time, bool)`

GetLastLoginOk returns a tuple with the LastLogin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastLogin

`func (o *ListSAMLUsers200ResponseUsersInner) SetLastLogin(v time.Time)`

SetLastLogin sets LastLogin field to given value.

### HasLastLogin

`func (o *ListSAMLUsers200ResponseUsersInner) HasLastLogin() bool`

HasLastLogin returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


