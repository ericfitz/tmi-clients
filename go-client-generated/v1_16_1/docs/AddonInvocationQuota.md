# AddonInvocationQuota

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**OwnerId** | **string** | User ID | 
**MaxActiveInvocations** | **int32** | Maximum concurrent active addon invocations | 
**MaxInvocationsPerHour** | **int32** | Maximum addon invocations per hour | 
**CreatedAt** | **time.Time** | Creation timestamp | 
**ModifiedAt** | **time.Time** | Last modification timestamp | 

## Methods

### NewAddonInvocationQuota

`func NewAddonInvocationQuota(ownerId string, maxActiveInvocations int32, maxInvocationsPerHour int32, createdAt time.Time, modifiedAt time.Time, ) *AddonInvocationQuota`

NewAddonInvocationQuota instantiates a new AddonInvocationQuota object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAddonInvocationQuotaWithDefaults

`func NewAddonInvocationQuotaWithDefaults() *AddonInvocationQuota`

NewAddonInvocationQuotaWithDefaults instantiates a new AddonInvocationQuota object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOwnerId

`func (o *AddonInvocationQuota) GetOwnerId() string`

GetOwnerId returns the OwnerId field if non-nil, zero value otherwise.

### GetOwnerIdOk

`func (o *AddonInvocationQuota) GetOwnerIdOk() (*string, bool)`

GetOwnerIdOk returns a tuple with the OwnerId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOwnerId

`func (o *AddonInvocationQuota) SetOwnerId(v string)`

SetOwnerId sets OwnerId field to given value.


### GetMaxActiveInvocations

`func (o *AddonInvocationQuota) GetMaxActiveInvocations() int32`

GetMaxActiveInvocations returns the MaxActiveInvocations field if non-nil, zero value otherwise.

### GetMaxActiveInvocationsOk

`func (o *AddonInvocationQuota) GetMaxActiveInvocationsOk() (*int32, bool)`

GetMaxActiveInvocationsOk returns a tuple with the MaxActiveInvocations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxActiveInvocations

`func (o *AddonInvocationQuota) SetMaxActiveInvocations(v int32)`

SetMaxActiveInvocations sets MaxActiveInvocations field to given value.


### GetMaxInvocationsPerHour

`func (o *AddonInvocationQuota) GetMaxInvocationsPerHour() int32`

GetMaxInvocationsPerHour returns the MaxInvocationsPerHour field if non-nil, zero value otherwise.

### GetMaxInvocationsPerHourOk

`func (o *AddonInvocationQuota) GetMaxInvocationsPerHourOk() (*int32, bool)`

GetMaxInvocationsPerHourOk returns a tuple with the MaxInvocationsPerHour field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxInvocationsPerHour

`func (o *AddonInvocationQuota) SetMaxInvocationsPerHour(v int32)`

SetMaxInvocationsPerHour sets MaxInvocationsPerHour field to given value.


### GetCreatedAt

`func (o *AddonInvocationQuota) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *AddonInvocationQuota) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *AddonInvocationQuota) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetModifiedAt

`func (o *AddonInvocationQuota) GetModifiedAt() time.Time`

GetModifiedAt returns the ModifiedAt field if non-nil, zero value otherwise.

### GetModifiedAtOk

`func (o *AddonInvocationQuota) GetModifiedAtOk() (*time.Time, bool)`

GetModifiedAtOk returns a tuple with the ModifiedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedAt

`func (o *AddonInvocationQuota) SetModifiedAt(v time.Time)`

SetModifiedAt sets ModifiedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


