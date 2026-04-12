# ClientConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Features** | Pointer to [**ClientConfigFeatures**](ClientConfigFeatures.md) |  | [optional] 
**Operator** | Pointer to [**ClientConfigOperator**](ClientConfigOperator.md) |  | [optional] 
**Limits** | Pointer to [**ClientConfigLimits**](ClientConfigLimits.md) |  | [optional] 
**Ui** | Pointer to [**ClientConfigUi**](ClientConfigUi.md) |  | [optional] 

## Methods

### NewClientConfig

`func NewClientConfig() *ClientConfig`

NewClientConfig instantiates a new ClientConfig object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewClientConfigWithDefaults

`func NewClientConfigWithDefaults() *ClientConfig`

NewClientConfigWithDefaults instantiates a new ClientConfig object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFeatures

`func (o *ClientConfig) GetFeatures() ClientConfigFeatures`

GetFeatures returns the Features field if non-nil, zero value otherwise.

### GetFeaturesOk

`func (o *ClientConfig) GetFeaturesOk() (*ClientConfigFeatures, bool)`

GetFeaturesOk returns a tuple with the Features field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFeatures

`func (o *ClientConfig) SetFeatures(v ClientConfigFeatures)`

SetFeatures sets Features field to given value.

### HasFeatures

`func (o *ClientConfig) HasFeatures() bool`

HasFeatures returns a boolean if a field has been set.

### GetOperator

`func (o *ClientConfig) GetOperator() ClientConfigOperator`

GetOperator returns the Operator field if non-nil, zero value otherwise.

### GetOperatorOk

`func (o *ClientConfig) GetOperatorOk() (*ClientConfigOperator, bool)`

GetOperatorOk returns a tuple with the Operator field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOperator

`func (o *ClientConfig) SetOperator(v ClientConfigOperator)`

SetOperator sets Operator field to given value.

### HasOperator

`func (o *ClientConfig) HasOperator() bool`

HasOperator returns a boolean if a field has been set.

### GetLimits

`func (o *ClientConfig) GetLimits() ClientConfigLimits`

GetLimits returns the Limits field if non-nil, zero value otherwise.

### GetLimitsOk

`func (o *ClientConfig) GetLimitsOk() (*ClientConfigLimits, bool)`

GetLimitsOk returns a tuple with the Limits field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimits

`func (o *ClientConfig) SetLimits(v ClientConfigLimits)`

SetLimits sets Limits field to given value.

### HasLimits

`func (o *ClientConfig) HasLimits() bool`

HasLimits returns a boolean if a field has been set.

### GetUi

`func (o *ClientConfig) GetUi() ClientConfigUi`

GetUi returns the Ui field if non-nil, zero value otherwise.

### GetUiOk

`func (o *ClientConfig) GetUiOk() (*ClientConfigUi, bool)`

GetUiOk returns a tuple with the Ui field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUi

`func (o *ClientConfig) SetUi(v ClientConfigUi)`

SetUi sets Ui field to given value.

### HasUi

`func (o *ClientConfig) HasUi() bool`

HasUi returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


