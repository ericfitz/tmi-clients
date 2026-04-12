# PortConfigurationGroupsValue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Position** | Pointer to **string** | Port position on the node | [optional] 
**Attrs** | Pointer to **map[string]interface{}** | Visual attributes for port group rendering (e.g., circle styling) | [optional] 

## Methods

### NewPortConfigurationGroupsValue

`func NewPortConfigurationGroupsValue() *PortConfigurationGroupsValue`

NewPortConfigurationGroupsValue instantiates a new PortConfigurationGroupsValue object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPortConfigurationGroupsValueWithDefaults

`func NewPortConfigurationGroupsValueWithDefaults() *PortConfigurationGroupsValue`

NewPortConfigurationGroupsValueWithDefaults instantiates a new PortConfigurationGroupsValue object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPosition

`func (o *PortConfigurationGroupsValue) GetPosition() string`

GetPosition returns the Position field if non-nil, zero value otherwise.

### GetPositionOk

`func (o *PortConfigurationGroupsValue) GetPositionOk() (*string, bool)`

GetPositionOk returns a tuple with the Position field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPosition

`func (o *PortConfigurationGroupsValue) SetPosition(v string)`

SetPosition sets Position field to given value.

### HasPosition

`func (o *PortConfigurationGroupsValue) HasPosition() bool`

HasPosition returns a boolean if a field has been set.

### GetAttrs

`func (o *PortConfigurationGroupsValue) GetAttrs() map[string]interface{}`

GetAttrs returns the Attrs field if non-nil, zero value otherwise.

### GetAttrsOk

`func (o *PortConfigurationGroupsValue) GetAttrsOk() (*map[string]interface{}, bool)`

GetAttrsOk returns a tuple with the Attrs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttrs

`func (o *PortConfigurationGroupsValue) SetAttrs(v map[string]interface{})`

SetAttrs sets Attrs field to given value.

### HasAttrs

`func (o *PortConfigurationGroupsValue) HasAttrs() bool`

HasAttrs returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


