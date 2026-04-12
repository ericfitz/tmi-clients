# AddonQuotaUpdate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**MaxActiveInvocations** | **int32** | Maximum concurrent active addon invocations | 
**MaxInvocationsPerHour** | **int32** | Maximum addon invocations per hour | 

## Methods

### NewAddonQuotaUpdate

`func NewAddonQuotaUpdate(maxActiveInvocations int32, maxInvocationsPerHour int32, ) *AddonQuotaUpdate`

NewAddonQuotaUpdate instantiates a new AddonQuotaUpdate object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAddonQuotaUpdateWithDefaults

`func NewAddonQuotaUpdateWithDefaults() *AddonQuotaUpdate`

NewAddonQuotaUpdateWithDefaults instantiates a new AddonQuotaUpdate object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMaxActiveInvocations

`func (o *AddonQuotaUpdate) GetMaxActiveInvocations() int32`

GetMaxActiveInvocations returns the MaxActiveInvocations field if non-nil, zero value otherwise.

### GetMaxActiveInvocationsOk

`func (o *AddonQuotaUpdate) GetMaxActiveInvocationsOk() (*int32, bool)`

GetMaxActiveInvocationsOk returns a tuple with the MaxActiveInvocations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxActiveInvocations

`func (o *AddonQuotaUpdate) SetMaxActiveInvocations(v int32)`

SetMaxActiveInvocations sets MaxActiveInvocations field to given value.


### GetMaxInvocationsPerHour

`func (o *AddonQuotaUpdate) GetMaxInvocationsPerHour() int32`

GetMaxInvocationsPerHour returns the MaxInvocationsPerHour field if non-nil, zero value otherwise.

### GetMaxInvocationsPerHourOk

`func (o *AddonQuotaUpdate) GetMaxInvocationsPerHourOk() (*int32, bool)`

GetMaxInvocationsPerHourOk returns a tuple with the MaxInvocationsPerHour field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxInvocationsPerHour

`func (o *AddonQuotaUpdate) SetMaxInvocationsPerHour(v int32)`

SetMaxInvocationsPerHour sets MaxInvocationsPerHour field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


