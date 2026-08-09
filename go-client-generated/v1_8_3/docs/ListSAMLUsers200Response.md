# ListSAMLUsers200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Idp** | **string** | Identity provider the users belong to; always equals the {idp} path parameter. | 
**Users** | [**[]ListSAMLUsers200ResponseUsersInner**](ListSAMLUsers200ResponseUsersInner.md) | Users from this identity provider, most recently logged in first. | 
**Total** | **int32** | Total users matching the filter, ignoring limit/offset. | 

## Methods

### NewListSAMLUsers200Response

`func NewListSAMLUsers200Response(idp string, users []ListSAMLUsers200ResponseUsersInner, total int32, ) *ListSAMLUsers200Response`

NewListSAMLUsers200Response instantiates a new ListSAMLUsers200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListSAMLUsers200ResponseWithDefaults

`func NewListSAMLUsers200ResponseWithDefaults() *ListSAMLUsers200Response`

NewListSAMLUsers200ResponseWithDefaults instantiates a new ListSAMLUsers200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetIdp

`func (o *ListSAMLUsers200Response) GetIdp() string`

GetIdp returns the Idp field if non-nil, zero value otherwise.

### GetIdpOk

`func (o *ListSAMLUsers200Response) GetIdpOk() (*string, bool)`

GetIdpOk returns a tuple with the Idp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIdp

`func (o *ListSAMLUsers200Response) SetIdp(v string)`

SetIdp sets Idp field to given value.


### GetUsers

`func (o *ListSAMLUsers200Response) GetUsers() []ListSAMLUsers200ResponseUsersInner`

GetUsers returns the Users field if non-nil, zero value otherwise.

### GetUsersOk

`func (o *ListSAMLUsers200Response) GetUsersOk() (*[]ListSAMLUsers200ResponseUsersInner, bool)`

GetUsersOk returns a tuple with the Users field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUsers

`func (o *ListSAMLUsers200Response) SetUsers(v []ListSAMLUsers200ResponseUsersInner)`

SetUsers sets Users field to given value.


### GetTotal

`func (o *ListSAMLUsers200Response) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListSAMLUsers200Response) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListSAMLUsers200Response) SetTotal(v int32)`

SetTotal sets Total field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


