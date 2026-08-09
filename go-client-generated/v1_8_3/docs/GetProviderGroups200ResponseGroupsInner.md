# GetProviderGroups200ResponseGroupsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Group name | 
**DisplayName** | Pointer to **string** | Display name for the group | [optional] 
**UsedInAuthorizations** | Pointer to **bool** | Whether this group is used in any threat model authorizations | [optional] 

## Methods

### NewGetProviderGroups200ResponseGroupsInner

`func NewGetProviderGroups200ResponseGroupsInner(name string, ) *GetProviderGroups200ResponseGroupsInner`

NewGetProviderGroups200ResponseGroupsInner instantiates a new GetProviderGroups200ResponseGroupsInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetProviderGroups200ResponseGroupsInnerWithDefaults

`func NewGetProviderGroups200ResponseGroupsInnerWithDefaults() *GetProviderGroups200ResponseGroupsInner`

NewGetProviderGroups200ResponseGroupsInnerWithDefaults instantiates a new GetProviderGroups200ResponseGroupsInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *GetProviderGroups200ResponseGroupsInner) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *GetProviderGroups200ResponseGroupsInner) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *GetProviderGroups200ResponseGroupsInner) SetName(v string)`

SetName sets Name field to given value.


### GetDisplayName

`func (o *GetProviderGroups200ResponseGroupsInner) GetDisplayName() string`

GetDisplayName returns the DisplayName field if non-nil, zero value otherwise.

### GetDisplayNameOk

`func (o *GetProviderGroups200ResponseGroupsInner) GetDisplayNameOk() (*string, bool)`

GetDisplayNameOk returns a tuple with the DisplayName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplayName

`func (o *GetProviderGroups200ResponseGroupsInner) SetDisplayName(v string)`

SetDisplayName sets DisplayName field to given value.

### HasDisplayName

`func (o *GetProviderGroups200ResponseGroupsInner) HasDisplayName() bool`

HasDisplayName returns a boolean if a field has been set.

### GetUsedInAuthorizations

`func (o *GetProviderGroups200ResponseGroupsInner) GetUsedInAuthorizations() bool`

GetUsedInAuthorizations returns the UsedInAuthorizations field if non-nil, zero value otherwise.

### GetUsedInAuthorizationsOk

`func (o *GetProviderGroups200ResponseGroupsInner) GetUsedInAuthorizationsOk() (*bool, bool)`

GetUsedInAuthorizationsOk returns a tuple with the UsedInAuthorizations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUsedInAuthorizations

`func (o *GetProviderGroups200ResponseGroupsInner) SetUsedInAuthorizations(v bool)`

SetUsedInAuthorizations sets UsedInAuthorizations field to given value.

### HasUsedInAuthorizations

`func (o *GetProviderGroups200ResponseGroupsInner) HasUsedInAuthorizations() bool`

HasUsedInAuthorizations returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


