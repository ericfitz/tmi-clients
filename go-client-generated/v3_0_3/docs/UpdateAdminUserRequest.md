# UpdateAdminUserRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Email** | Pointer to **string** | Updated email address | [optional] 
**Name** | Pointer to **string** | Updated display name | [optional] 
**EmailVerified** | Pointer to **bool** | Updated email verification status | [optional] 

## Methods

### NewUpdateAdminUserRequest

`func NewUpdateAdminUserRequest() *UpdateAdminUserRequest`

NewUpdateAdminUserRequest instantiates a new UpdateAdminUserRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateAdminUserRequestWithDefaults

`func NewUpdateAdminUserRequestWithDefaults() *UpdateAdminUserRequest`

NewUpdateAdminUserRequestWithDefaults instantiates a new UpdateAdminUserRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEmail

`func (o *UpdateAdminUserRequest) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *UpdateAdminUserRequest) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *UpdateAdminUserRequest) SetEmail(v string)`

SetEmail sets Email field to given value.

### HasEmail

`func (o *UpdateAdminUserRequest) HasEmail() bool`

HasEmail returns a boolean if a field has been set.

### GetName

`func (o *UpdateAdminUserRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *UpdateAdminUserRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *UpdateAdminUserRequest) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *UpdateAdminUserRequest) HasName() bool`

HasName returns a boolean if a field has been set.

### GetEmailVerified

`func (o *UpdateAdminUserRequest) GetEmailVerified() bool`

GetEmailVerified returns the EmailVerified field if non-nil, zero value otherwise.

### GetEmailVerifiedOk

`func (o *UpdateAdminUserRequest) GetEmailVerifiedOk() (*bool, bool)`

GetEmailVerifiedOk returns a tuple with the EmailVerified field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmailVerified

`func (o *UpdateAdminUserRequest) SetEmailVerified(v bool)`

SetEmailVerified sets EmailVerified field to given value.

### HasEmailVerified

`func (o *UpdateAdminUserRequest) HasEmailVerified() bool`

HasEmailVerified returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


