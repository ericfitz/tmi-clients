# SystemSettingUpdate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Value** | **string** | Setting value as a string (interpreted based on type) | 
**Type** | **string** | Data type of the setting value | 
**Description** | Pointer to **string** | Human-readable description of the setting | [optional] 

## Methods

### NewSystemSettingUpdate

`func NewSystemSettingUpdate(value string, type_ string, ) *SystemSettingUpdate`

NewSystemSettingUpdate instantiates a new SystemSettingUpdate object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSystemSettingUpdateWithDefaults

`func NewSystemSettingUpdateWithDefaults() *SystemSettingUpdate`

NewSystemSettingUpdateWithDefaults instantiates a new SystemSettingUpdate object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetValue

`func (o *SystemSettingUpdate) GetValue() string`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *SystemSettingUpdate) GetValueOk() (*string, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *SystemSettingUpdate) SetValue(v string)`

SetValue sets Value field to given value.


### GetType

`func (o *SystemSettingUpdate) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *SystemSettingUpdate) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *SystemSettingUpdate) SetType(v string)`

SetType sets Type field to given value.


### GetDescription

`func (o *SystemSettingUpdate) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *SystemSettingUpdate) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *SystemSettingUpdate) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *SystemSettingUpdate) HasDescription() bool`

HasDescription returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


