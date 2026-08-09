# AdminUserIdentitiesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Primary** | [**AdminUserIdentitiesResponsePrimary**](AdminUserIdentitiesResponsePrimary.md) |  | 
**Linked** | Pointer to [**[]LinkedIdentity**](LinkedIdentity.md) | Linked sign-in identities; the primary identity is not deletable and does not appear here | [optional] 

## Methods

### NewAdminUserIdentitiesResponse

`func NewAdminUserIdentitiesResponse(primary AdminUserIdentitiesResponsePrimary, ) *AdminUserIdentitiesResponse`

NewAdminUserIdentitiesResponse instantiates a new AdminUserIdentitiesResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAdminUserIdentitiesResponseWithDefaults

`func NewAdminUserIdentitiesResponseWithDefaults() *AdminUserIdentitiesResponse`

NewAdminUserIdentitiesResponseWithDefaults instantiates a new AdminUserIdentitiesResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPrimary

`func (o *AdminUserIdentitiesResponse) GetPrimary() AdminUserIdentitiesResponsePrimary`

GetPrimary returns the Primary field if non-nil, zero value otherwise.

### GetPrimaryOk

`func (o *AdminUserIdentitiesResponse) GetPrimaryOk() (*AdminUserIdentitiesResponsePrimary, bool)`

GetPrimaryOk returns a tuple with the Primary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrimary

`func (o *AdminUserIdentitiesResponse) SetPrimary(v AdminUserIdentitiesResponsePrimary)`

SetPrimary sets Primary field to given value.


### GetLinked

`func (o *AdminUserIdentitiesResponse) GetLinked() []LinkedIdentity`

GetLinked returns the Linked field if non-nil, zero value otherwise.

### GetLinkedOk

`func (o *AdminUserIdentitiesResponse) GetLinkedOk() (*[]LinkedIdentity, bool)`

GetLinkedOk returns a tuple with the Linked field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinked

`func (o *AdminUserIdentitiesResponse) SetLinked(v []LinkedIdentity)`

SetLinked sets Linked field to given value.

### HasLinked

`func (o *AdminUserIdentitiesResponse) HasLinked() bool`

HasLinked returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


