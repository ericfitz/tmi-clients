# GetCurrentUser200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Sub** | **string** | Subject identifier - unique identifier for the user (required per OIDC) | 
**Email** | Pointer to **string** | User email address | [optional] 
**Name** | Pointer to **string** | User display name | [optional] 
**Idp** | Pointer to **string** | Identity provider that authenticated the user | [optional] 
**Groups** | Pointer to **[]string** | Groups the user belongs to | [optional] 

## Methods

### NewGetCurrentUser200Response

`func NewGetCurrentUser200Response(sub string, ) *GetCurrentUser200Response`

NewGetCurrentUser200Response instantiates a new GetCurrentUser200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetCurrentUser200ResponseWithDefaults

`func NewGetCurrentUser200ResponseWithDefaults() *GetCurrentUser200Response`

NewGetCurrentUser200ResponseWithDefaults instantiates a new GetCurrentUser200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSub

`func (o *GetCurrentUser200Response) GetSub() string`

GetSub returns the Sub field if non-nil, zero value otherwise.

### GetSubOk

`func (o *GetCurrentUser200Response) GetSubOk() (*string, bool)`

GetSubOk returns a tuple with the Sub field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSub

`func (o *GetCurrentUser200Response) SetSub(v string)`

SetSub sets Sub field to given value.


### GetEmail

`func (o *GetCurrentUser200Response) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *GetCurrentUser200Response) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *GetCurrentUser200Response) SetEmail(v string)`

SetEmail sets Email field to given value.

### HasEmail

`func (o *GetCurrentUser200Response) HasEmail() bool`

HasEmail returns a boolean if a field has been set.

### GetName

`func (o *GetCurrentUser200Response) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *GetCurrentUser200Response) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *GetCurrentUser200Response) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *GetCurrentUser200Response) HasName() bool`

HasName returns a boolean if a field has been set.

### GetIdp

`func (o *GetCurrentUser200Response) GetIdp() string`

GetIdp returns the Idp field if non-nil, zero value otherwise.

### GetIdpOk

`func (o *GetCurrentUser200Response) GetIdpOk() (*string, bool)`

GetIdpOk returns a tuple with the Idp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIdp

`func (o *GetCurrentUser200Response) SetIdp(v string)`

SetIdp sets Idp field to given value.

### HasIdp

`func (o *GetCurrentUser200Response) HasIdp() bool`

HasIdp returns a boolean if a field has been set.

### GetGroups

`func (o *GetCurrentUser200Response) GetGroups() []string`

GetGroups returns the Groups field if non-nil, zero value otherwise.

### GetGroupsOk

`func (o *GetCurrentUser200Response) GetGroupsOk() (*[]string, bool)`

GetGroupsOk returns a tuple with the Groups field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroups

`func (o *GetCurrentUser200Response) SetGroups(v []string)`

SetGroups sets Groups field to given value.

### HasGroups

`func (o *GetCurrentUser200Response) HasGroups() bool`

HasGroups returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


