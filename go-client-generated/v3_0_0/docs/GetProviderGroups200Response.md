# GetProviderGroups200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Idp** | **string** | Identity provider ID | 
**Groups** | [**[]GetProviderGroups200ResponseGroupsInner**](GetProviderGroups200ResponseGroupsInner.md) |  | 

## Methods

### NewGetProviderGroups200Response

`func NewGetProviderGroups200Response(idp string, groups []GetProviderGroups200ResponseGroupsInner, ) *GetProviderGroups200Response`

NewGetProviderGroups200Response instantiates a new GetProviderGroups200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetProviderGroups200ResponseWithDefaults

`func NewGetProviderGroups200ResponseWithDefaults() *GetProviderGroups200Response`

NewGetProviderGroups200ResponseWithDefaults instantiates a new GetProviderGroups200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetIdp

`func (o *GetProviderGroups200Response) GetIdp() string`

GetIdp returns the Idp field if non-nil, zero value otherwise.

### GetIdpOk

`func (o *GetProviderGroups200Response) GetIdpOk() (*string, bool)`

GetIdpOk returns a tuple with the Idp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIdp

`func (o *GetProviderGroups200Response) SetIdp(v string)`

SetIdp sets Idp field to given value.


### GetGroups

`func (o *GetProviderGroups200Response) GetGroups() []GetProviderGroups200ResponseGroupsInner`

GetGroups returns the Groups field if non-nil, zero value otherwise.

### GetGroupsOk

`func (o *GetProviderGroups200Response) GetGroupsOk() (*[]GetProviderGroups200ResponseGroupsInner, bool)`

GetGroupsOk returns a tuple with the Groups field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroups

`func (o *GetProviderGroups200Response) SetGroups(v []GetProviderGroups200ResponseGroupsInner)`

SetGroups sets Groups field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


