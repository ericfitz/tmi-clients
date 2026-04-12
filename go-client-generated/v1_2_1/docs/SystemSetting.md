# SystemSetting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Key** | **string** | Unique setting identifier using dot notation (e.g., rate_limit.requests_per_minute) | 
**Value** | **string** | Setting value as a string (interpreted based on type) | 
**Type** | **string** | Data type of the setting value | 
**Description** | Pointer to **string** | Human-readable description of the setting | [optional] 
**ModifiedAt** | Pointer to **time.Time** | When the setting was last modified | [optional] 
**ModifiedBy** | Pointer to **string** | UUID of the user who last modified the setting | [optional] 

## Methods

### NewSystemSetting

`func NewSystemSetting(key string, value string, type_ string, ) *SystemSetting`

NewSystemSetting instantiates a new SystemSetting object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSystemSettingWithDefaults

`func NewSystemSettingWithDefaults() *SystemSetting`

NewSystemSettingWithDefaults instantiates a new SystemSetting object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetKey

`func (o *SystemSetting) GetKey() string`

GetKey returns the Key field if non-nil, zero value otherwise.

### GetKeyOk

`func (o *SystemSetting) GetKeyOk() (*string, bool)`

GetKeyOk returns a tuple with the Key field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKey

`func (o *SystemSetting) SetKey(v string)`

SetKey sets Key field to given value.


### GetValue

`func (o *SystemSetting) GetValue() string`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *SystemSetting) GetValueOk() (*string, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *SystemSetting) SetValue(v string)`

SetValue sets Value field to given value.


### GetType

`func (o *SystemSetting) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *SystemSetting) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *SystemSetting) SetType(v string)`

SetType sets Type field to given value.


### GetDescription

`func (o *SystemSetting) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *SystemSetting) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *SystemSetting) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *SystemSetting) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetModifiedAt

`func (o *SystemSetting) GetModifiedAt() time.Time`

GetModifiedAt returns the ModifiedAt field if non-nil, zero value otherwise.

### GetModifiedAtOk

`func (o *SystemSetting) GetModifiedAtOk() (*time.Time, bool)`

GetModifiedAtOk returns a tuple with the ModifiedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedAt

`func (o *SystemSetting) SetModifiedAt(v time.Time)`

SetModifiedAt sets ModifiedAt field to given value.

### HasModifiedAt

`func (o *SystemSetting) HasModifiedAt() bool`

HasModifiedAt returns a boolean if a field has been set.

### GetModifiedBy

`func (o *SystemSetting) GetModifiedBy() string`

GetModifiedBy returns the ModifiedBy field if non-nil, zero value otherwise.

### GetModifiedByOk

`func (o *SystemSetting) GetModifiedByOk() (*string, bool)`

GetModifiedByOk returns a tuple with the ModifiedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedBy

`func (o *SystemSetting) SetModifiedBy(v string)`

SetModifiedBy sets ModifiedBy field to given value.

### HasModifiedBy

`func (o *SystemSetting) HasModifiedBy() bool`

HasModifiedBy returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


