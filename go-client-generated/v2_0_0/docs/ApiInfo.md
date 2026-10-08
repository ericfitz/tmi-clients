# ApiInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Status** | [**ApiInfoStatus**](ApiInfoStatus.md) |  | 
**Service** | [**ApiInfoService**](ApiInfoService.md) |  | 
**Api** | [**ApiInfoApi**](ApiInfoApi.md) |  | 
**Operator** | Pointer to [**ApiInfoOperator**](ApiInfoOperator.md) |  | [optional] 
**Health** | Pointer to [**ApiInfoHealth**](ApiInfoHealth.md) |  | [optional] 

## Methods

### NewApiInfo

`func NewApiInfo(status ApiInfoStatus, service ApiInfoService, api ApiInfoApi, ) *ApiInfo`

NewApiInfo instantiates a new ApiInfo object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewApiInfoWithDefaults

`func NewApiInfoWithDefaults() *ApiInfo`

NewApiInfoWithDefaults instantiates a new ApiInfo object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetStatus

`func (o *ApiInfo) GetStatus() ApiInfoStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *ApiInfo) GetStatusOk() (*ApiInfoStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *ApiInfo) SetStatus(v ApiInfoStatus)`

SetStatus sets Status field to given value.


### GetService

`func (o *ApiInfo) GetService() ApiInfoService`

GetService returns the Service field if non-nil, zero value otherwise.

### GetServiceOk

`func (o *ApiInfo) GetServiceOk() (*ApiInfoService, bool)`

GetServiceOk returns a tuple with the Service field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetService

`func (o *ApiInfo) SetService(v ApiInfoService)`

SetService sets Service field to given value.


### GetApi

`func (o *ApiInfo) GetApi() ApiInfoApi`

GetApi returns the Api field if non-nil, zero value otherwise.

### GetApiOk

`func (o *ApiInfo) GetApiOk() (*ApiInfoApi, bool)`

GetApiOk returns a tuple with the Api field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApi

`func (o *ApiInfo) SetApi(v ApiInfoApi)`

SetApi sets Api field to given value.


### GetOperator

`func (o *ApiInfo) GetOperator() ApiInfoOperator`

GetOperator returns the Operator field if non-nil, zero value otherwise.

### GetOperatorOk

`func (o *ApiInfo) GetOperatorOk() (*ApiInfoOperator, bool)`

GetOperatorOk returns a tuple with the Operator field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOperator

`func (o *ApiInfo) SetOperator(v ApiInfoOperator)`

SetOperator sets Operator field to given value.

### HasOperator

`func (o *ApiInfo) HasOperator() bool`

HasOperator returns a boolean if a field has been set.

### GetHealth

`func (o *ApiInfo) GetHealth() ApiInfoHealth`

GetHealth returns the Health field if non-nil, zero value otherwise.

### GetHealthOk

`func (o *ApiInfo) GetHealthOk() (*ApiInfoHealth, bool)`

GetHealthOk returns a tuple with the Health field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHealth

`func (o *ApiInfo) SetHealth(v ApiInfoHealth)`

SetHealth sets Health field to given value.

### HasHealth

`func (o *ApiInfo) HasHealth() bool`

HasHealth returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


