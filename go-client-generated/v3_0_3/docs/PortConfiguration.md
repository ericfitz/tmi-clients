# PortConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Groups** | Pointer to [**map[string]PortConfigurationGroupsValue**](PortConfigurationGroupsValue.md) | Port group definitions | [optional] 
**Items** | Pointer to [**[]PortConfigurationItemsInner**](PortConfigurationItemsInner.md) | Individual port instances | [optional] 

## Methods

### NewPortConfiguration

`func NewPortConfiguration() *PortConfiguration`

NewPortConfiguration instantiates a new PortConfiguration object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPortConfigurationWithDefaults

`func NewPortConfigurationWithDefaults() *PortConfiguration`

NewPortConfigurationWithDefaults instantiates a new PortConfiguration object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetGroups

`func (o *PortConfiguration) GetGroups() map[string]PortConfigurationGroupsValue`

GetGroups returns the Groups field if non-nil, zero value otherwise.

### GetGroupsOk

`func (o *PortConfiguration) GetGroupsOk() (*map[string]PortConfigurationGroupsValue, bool)`

GetGroupsOk returns a tuple with the Groups field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroups

`func (o *PortConfiguration) SetGroups(v map[string]PortConfigurationGroupsValue)`

SetGroups sets Groups field to given value.

### HasGroups

`func (o *PortConfiguration) HasGroups() bool`

HasGroups returns a boolean if a field has been set.

### GetItems

`func (o *PortConfiguration) GetItems() []PortConfigurationItemsInner`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *PortConfiguration) GetItemsOk() (*[]PortConfigurationItemsInner, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *PortConfiguration) SetItems(v []PortConfigurationItemsInner)`

SetItems sets Items field to given value.

### HasItems

`func (o *PortConfiguration) HasItems() bool`

HasItems returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


