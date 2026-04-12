# ApiInfoStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Code** | **string** | Status code indicating system health: OK (all components healthy), DEGRADED (server up but database or Redis unhealthy), ERROR (critical failure) | 
**Time** | **time.Time** | Current server time in UTC, formatted as RFC 3339 | 

## Methods

### NewApiInfoStatus

`func NewApiInfoStatus(code string, time time.Time, ) *ApiInfoStatus`

NewApiInfoStatus instantiates a new ApiInfoStatus object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewApiInfoStatusWithDefaults

`func NewApiInfoStatusWithDefaults() *ApiInfoStatus`

NewApiInfoStatusWithDefaults instantiates a new ApiInfoStatus object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCode

`func (o *ApiInfoStatus) GetCode() string`

GetCode returns the Code field if non-nil, zero value otherwise.

### GetCodeOk

`func (o *ApiInfoStatus) GetCodeOk() (*string, bool)`

GetCodeOk returns a tuple with the Code field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCode

`func (o *ApiInfoStatus) SetCode(v string)`

SetCode sets Code field to given value.


### GetTime

`func (o *ApiInfoStatus) GetTime() time.Time`

GetTime returns the Time field if non-nil, zero value otherwise.

### GetTimeOk

`func (o *ApiInfoStatus) GetTimeOk() (*time.Time, bool)`

GetTimeOk returns a tuple with the Time field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTime

`func (o *ApiInfoStatus) SetTime(v time.Time)`

SetTime sets Time field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


