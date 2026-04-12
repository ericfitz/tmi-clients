# ApiInfoHealth

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Database** | Pointer to [**ComponentHealth**](ComponentHealth.md) |  | [optional] 
**Redis** | Pointer to [**ComponentHealth**](ComponentHealth.md) |  | [optional] 

## Methods

### NewApiInfoHealth

`func NewApiInfoHealth() *ApiInfoHealth`

NewApiInfoHealth instantiates a new ApiInfoHealth object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewApiInfoHealthWithDefaults

`func NewApiInfoHealthWithDefaults() *ApiInfoHealth`

NewApiInfoHealthWithDefaults instantiates a new ApiInfoHealth object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDatabase

`func (o *ApiInfoHealth) GetDatabase() ComponentHealth`

GetDatabase returns the Database field if non-nil, zero value otherwise.

### GetDatabaseOk

`func (o *ApiInfoHealth) GetDatabaseOk() (*ComponentHealth, bool)`

GetDatabaseOk returns a tuple with the Database field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDatabase

`func (o *ApiInfoHealth) SetDatabase(v ComponentHealth)`

SetDatabase sets Database field to given value.

### HasDatabase

`func (o *ApiInfoHealth) HasDatabase() bool`

HasDatabase returns a boolean if a field has been set.

### GetRedis

`func (o *ApiInfoHealth) GetRedis() ComponentHealth`

GetRedis returns the Redis field if non-nil, zero value otherwise.

### GetRedisOk

`func (o *ApiInfoHealth) GetRedisOk() (*ComponentHealth, bool)`

GetRedisOk returns a tuple with the Redis field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRedis

`func (o *ApiInfoHealth) SetRedis(v ComponentHealth)`

SetRedis sets Redis field to given value.

### HasRedis

`func (o *ApiInfoHealth) HasRedis() bool`

HasRedis returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


