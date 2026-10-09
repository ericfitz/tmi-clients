# CreateAdminGroupRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**GroupName** | **string** | Group identifier (alphanumeric, hyphens, underscores only) | 
**Name** | **string** | Human-readable group name | 
**Description** | Pointer to **string** | Optional group description | [optional] 

## Methods

### NewCreateAdminGroupRequest

`func NewCreateAdminGroupRequest(groupName string, name string, ) *CreateAdminGroupRequest`

NewCreateAdminGroupRequest instantiates a new CreateAdminGroupRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateAdminGroupRequestWithDefaults

`func NewCreateAdminGroupRequestWithDefaults() *CreateAdminGroupRequest`

NewCreateAdminGroupRequestWithDefaults instantiates a new CreateAdminGroupRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetGroupName

`func (o *CreateAdminGroupRequest) GetGroupName() string`

GetGroupName returns the GroupName field if non-nil, zero value otherwise.

### GetGroupNameOk

`func (o *CreateAdminGroupRequest) GetGroupNameOk() (*string, bool)`

GetGroupNameOk returns a tuple with the GroupName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroupName

`func (o *CreateAdminGroupRequest) SetGroupName(v string)`

SetGroupName sets GroupName field to given value.


### GetName

`func (o *CreateAdminGroupRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateAdminGroupRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CreateAdminGroupRequest) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *CreateAdminGroupRequest) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *CreateAdminGroupRequest) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *CreateAdminGroupRequest) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *CreateAdminGroupRequest) HasDescription() bool`

HasDescription returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


