# AddonParameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Parameter name (used as key in invocation data payload) | 
**Type** | **string** | Parameter type determining client UI control | 
**Description** | Pointer to **string** | Human-readable description for UI display | [optional] 
**Required** | Pointer to **bool** | Whether the parameter must be provided on invocation | [optional] [default to false]
**EnumValues** | Pointer to **[]string** | Allowed values (applicable when type is &#39;enum&#39;) | [optional] 
**DefaultValue** | Pointer to **string** | Default value if not provided by user | [optional] 
**MetadataKey** | Pointer to **string** | Metadata key name to auto-populate from TMI object (applicable when type is &#39;metadata_key&#39;) | [optional] 
**NumberMin** | Pointer to **float32** | Minimum allowed value (applicable when type is &#39;number&#39;) | [optional] 
**NumberMax** | Pointer to **float32** | Maximum allowed value (applicable when type is &#39;number&#39;) | [optional] 
**StringMaxLength** | Pointer to **int32** | Maximum string length (applicable when type is &#39;string&#39;) | [optional] 
**StringValidationRegex** | Pointer to **string** | Regular expression for string validation (applicable when type is &#39;string&#39;) | [optional] 

## Methods

### NewAddonParameter

`func NewAddonParameter(name string, type_ string, ) *AddonParameter`

NewAddonParameter instantiates a new AddonParameter object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAddonParameterWithDefaults

`func NewAddonParameterWithDefaults() *AddonParameter`

NewAddonParameterWithDefaults instantiates a new AddonParameter object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *AddonParameter) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *AddonParameter) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *AddonParameter) SetName(v string)`

SetName sets Name field to given value.


### GetType

`func (o *AddonParameter) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *AddonParameter) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *AddonParameter) SetType(v string)`

SetType sets Type field to given value.


### GetDescription

`func (o *AddonParameter) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *AddonParameter) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *AddonParameter) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *AddonParameter) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetRequired

`func (o *AddonParameter) GetRequired() bool`

GetRequired returns the Required field if non-nil, zero value otherwise.

### GetRequiredOk

`func (o *AddonParameter) GetRequiredOk() (*bool, bool)`

GetRequiredOk returns a tuple with the Required field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequired

`func (o *AddonParameter) SetRequired(v bool)`

SetRequired sets Required field to given value.

### HasRequired

`func (o *AddonParameter) HasRequired() bool`

HasRequired returns a boolean if a field has been set.

### GetEnumValues

`func (o *AddonParameter) GetEnumValues() []string`

GetEnumValues returns the EnumValues field if non-nil, zero value otherwise.

### GetEnumValuesOk

`func (o *AddonParameter) GetEnumValuesOk() (*[]string, bool)`

GetEnumValuesOk returns a tuple with the EnumValues field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnumValues

`func (o *AddonParameter) SetEnumValues(v []string)`

SetEnumValues sets EnumValues field to given value.

### HasEnumValues

`func (o *AddonParameter) HasEnumValues() bool`

HasEnumValues returns a boolean if a field has been set.

### GetDefaultValue

`func (o *AddonParameter) GetDefaultValue() string`

GetDefaultValue returns the DefaultValue field if non-nil, zero value otherwise.

### GetDefaultValueOk

`func (o *AddonParameter) GetDefaultValueOk() (*string, bool)`

GetDefaultValueOk returns a tuple with the DefaultValue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefaultValue

`func (o *AddonParameter) SetDefaultValue(v string)`

SetDefaultValue sets DefaultValue field to given value.

### HasDefaultValue

`func (o *AddonParameter) HasDefaultValue() bool`

HasDefaultValue returns a boolean if a field has been set.

### GetMetadataKey

`func (o *AddonParameter) GetMetadataKey() string`

GetMetadataKey returns the MetadataKey field if non-nil, zero value otherwise.

### GetMetadataKeyOk

`func (o *AddonParameter) GetMetadataKeyOk() (*string, bool)`

GetMetadataKeyOk returns a tuple with the MetadataKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadataKey

`func (o *AddonParameter) SetMetadataKey(v string)`

SetMetadataKey sets MetadataKey field to given value.

### HasMetadataKey

`func (o *AddonParameter) HasMetadataKey() bool`

HasMetadataKey returns a boolean if a field has been set.

### GetNumberMin

`func (o *AddonParameter) GetNumberMin() float32`

GetNumberMin returns the NumberMin field if non-nil, zero value otherwise.

### GetNumberMinOk

`func (o *AddonParameter) GetNumberMinOk() (*float32, bool)`

GetNumberMinOk returns a tuple with the NumberMin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNumberMin

`func (o *AddonParameter) SetNumberMin(v float32)`

SetNumberMin sets NumberMin field to given value.

### HasNumberMin

`func (o *AddonParameter) HasNumberMin() bool`

HasNumberMin returns a boolean if a field has been set.

### GetNumberMax

`func (o *AddonParameter) GetNumberMax() float32`

GetNumberMax returns the NumberMax field if non-nil, zero value otherwise.

### GetNumberMaxOk

`func (o *AddonParameter) GetNumberMaxOk() (*float32, bool)`

GetNumberMaxOk returns a tuple with the NumberMax field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNumberMax

`func (o *AddonParameter) SetNumberMax(v float32)`

SetNumberMax sets NumberMax field to given value.

### HasNumberMax

`func (o *AddonParameter) HasNumberMax() bool`

HasNumberMax returns a boolean if a field has been set.

### GetStringMaxLength

`func (o *AddonParameter) GetStringMaxLength() int32`

GetStringMaxLength returns the StringMaxLength field if non-nil, zero value otherwise.

### GetStringMaxLengthOk

`func (o *AddonParameter) GetStringMaxLengthOk() (*int32, bool)`

GetStringMaxLengthOk returns a tuple with the StringMaxLength field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStringMaxLength

`func (o *AddonParameter) SetStringMaxLength(v int32)`

SetStringMaxLength sets StringMaxLength field to given value.

### HasStringMaxLength

`func (o *AddonParameter) HasStringMaxLength() bool`

HasStringMaxLength returns a boolean if a field has been set.

### GetStringValidationRegex

`func (o *AddonParameter) GetStringValidationRegex() string`

GetStringValidationRegex returns the StringValidationRegex field if non-nil, zero value otherwise.

### GetStringValidationRegexOk

`func (o *AddonParameter) GetStringValidationRegexOk() (*string, bool)`

GetStringValidationRegexOk returns a tuple with the StringValidationRegex field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStringValidationRegex

`func (o *AddonParameter) SetStringValidationRegex(v string)`

SetStringValidationRegex sets StringValidationRegex field to given value.

### HasStringValidationRegex

`func (o *AddonParameter) HasStringValidationRegex() bool`

HasStringValidationRegex returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


