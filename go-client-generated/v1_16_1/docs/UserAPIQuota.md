# UserAPIQuota

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**UserId** | **string** | User ID | 
**MaxRequestsPerMinute** | **int32** | Maximum API requests per minute | 
**MaxRequestsPerHour** | Pointer to **NullableInt32** | Maximum API requests per hour (optional) | [optional] 
**CreatedAt** | **time.Time** | Creation timestamp | 
**ModifiedAt** | **time.Time** | Last modification timestamp | 

## Methods

### NewUserAPIQuota

`func NewUserAPIQuota(userId string, maxRequestsPerMinute int32, createdAt time.Time, modifiedAt time.Time, ) *UserAPIQuota`

NewUserAPIQuota instantiates a new UserAPIQuota object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUserAPIQuotaWithDefaults

`func NewUserAPIQuotaWithDefaults() *UserAPIQuota`

NewUserAPIQuotaWithDefaults instantiates a new UserAPIQuota object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetUserId

`func (o *UserAPIQuota) GetUserId() string`

GetUserId returns the UserId field if non-nil, zero value otherwise.

### GetUserIdOk

`func (o *UserAPIQuota) GetUserIdOk() (*string, bool)`

GetUserIdOk returns a tuple with the UserId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserId

`func (o *UserAPIQuota) SetUserId(v string)`

SetUserId sets UserId field to given value.


### GetMaxRequestsPerMinute

`func (o *UserAPIQuota) GetMaxRequestsPerMinute() int32`

GetMaxRequestsPerMinute returns the MaxRequestsPerMinute field if non-nil, zero value otherwise.

### GetMaxRequestsPerMinuteOk

`func (o *UserAPIQuota) GetMaxRequestsPerMinuteOk() (*int32, bool)`

GetMaxRequestsPerMinuteOk returns a tuple with the MaxRequestsPerMinute field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxRequestsPerMinute

`func (o *UserAPIQuota) SetMaxRequestsPerMinute(v int32)`

SetMaxRequestsPerMinute sets MaxRequestsPerMinute field to given value.


### GetMaxRequestsPerHour

`func (o *UserAPIQuota) GetMaxRequestsPerHour() int32`

GetMaxRequestsPerHour returns the MaxRequestsPerHour field if non-nil, zero value otherwise.

### GetMaxRequestsPerHourOk

`func (o *UserAPIQuota) GetMaxRequestsPerHourOk() (*int32, bool)`

GetMaxRequestsPerHourOk returns a tuple with the MaxRequestsPerHour field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxRequestsPerHour

`func (o *UserAPIQuota) SetMaxRequestsPerHour(v int32)`

SetMaxRequestsPerHour sets MaxRequestsPerHour field to given value.

### HasMaxRequestsPerHour

`func (o *UserAPIQuota) HasMaxRequestsPerHour() bool`

HasMaxRequestsPerHour returns a boolean if a field has been set.

### SetMaxRequestsPerHourNil

`func (o *UserAPIQuota) SetMaxRequestsPerHourNil(b bool)`

 SetMaxRequestsPerHourNil sets the value for MaxRequestsPerHour to be an explicit nil

### UnsetMaxRequestsPerHour
`func (o *UserAPIQuota) UnsetMaxRequestsPerHour()`

UnsetMaxRequestsPerHour ensures that no value is present for MaxRequestsPerHour, not even an explicit nil
### GetCreatedAt

`func (o *UserAPIQuota) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *UserAPIQuota) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *UserAPIQuota) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetModifiedAt

`func (o *UserAPIQuota) GetModifiedAt() time.Time`

GetModifiedAt returns the ModifiedAt field if non-nil, zero value otherwise.

### GetModifiedAtOk

`func (o *UserAPIQuota) GetModifiedAtOk() (*time.Time, bool)`

GetModifiedAtOk returns a tuple with the ModifiedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedAt

`func (o *UserAPIQuota) SetModifiedAt(v time.Time)`

SetModifiedAt sets ModifiedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


