# UserQuotaUpdate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**MaxRequestsPerMinute** | **int32** | Maximum API requests per minute | 
**MaxRequestsPerHour** | Pointer to **NullableInt32** | Maximum API requests per hour (optional) | [optional] 

## Methods

### NewUserQuotaUpdate

`func NewUserQuotaUpdate(maxRequestsPerMinute int32, ) *UserQuotaUpdate`

NewUserQuotaUpdate instantiates a new UserQuotaUpdate object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUserQuotaUpdateWithDefaults

`func NewUserQuotaUpdateWithDefaults() *UserQuotaUpdate`

NewUserQuotaUpdateWithDefaults instantiates a new UserQuotaUpdate object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMaxRequestsPerMinute

`func (o *UserQuotaUpdate) GetMaxRequestsPerMinute() int32`

GetMaxRequestsPerMinute returns the MaxRequestsPerMinute field if non-nil, zero value otherwise.

### GetMaxRequestsPerMinuteOk

`func (o *UserQuotaUpdate) GetMaxRequestsPerMinuteOk() (*int32, bool)`

GetMaxRequestsPerMinuteOk returns a tuple with the MaxRequestsPerMinute field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxRequestsPerMinute

`func (o *UserQuotaUpdate) SetMaxRequestsPerMinute(v int32)`

SetMaxRequestsPerMinute sets MaxRequestsPerMinute field to given value.


### GetMaxRequestsPerHour

`func (o *UserQuotaUpdate) GetMaxRequestsPerHour() int32`

GetMaxRequestsPerHour returns the MaxRequestsPerHour field if non-nil, zero value otherwise.

### GetMaxRequestsPerHourOk

`func (o *UserQuotaUpdate) GetMaxRequestsPerHourOk() (*int32, bool)`

GetMaxRequestsPerHourOk returns a tuple with the MaxRequestsPerHour field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxRequestsPerHour

`func (o *UserQuotaUpdate) SetMaxRequestsPerHour(v int32)`

SetMaxRequestsPerHour sets MaxRequestsPerHour field to given value.

### HasMaxRequestsPerHour

`func (o *UserQuotaUpdate) HasMaxRequestsPerHour() bool`

HasMaxRequestsPerHour returns a boolean if a field has been set.

### SetMaxRequestsPerHourNil

`func (o *UserQuotaUpdate) SetMaxRequestsPerHourNil(b bool)`

 SetMaxRequestsPerHourNil sets the value for MaxRequestsPerHour to be an explicit nil

### UnsetMaxRequestsPerHour
`func (o *UserQuotaUpdate) UnsetMaxRequestsPerHour()`

UnsetMaxRequestsPerHour ensures that no value is present for MaxRequestsPerHour, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


