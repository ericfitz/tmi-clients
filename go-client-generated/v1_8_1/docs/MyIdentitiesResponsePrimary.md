# MyIdentitiesResponsePrimary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Provider** | **string** | Primary identity provider ID | 
**Email** | **string** | Primary account email address | 
**Name** | Pointer to **string** | Primary account display name | [optional] 

## Methods

### NewMyIdentitiesResponsePrimary

`func NewMyIdentitiesResponsePrimary(provider string, email string, ) *MyIdentitiesResponsePrimary`

NewMyIdentitiesResponsePrimary instantiates a new MyIdentitiesResponsePrimary object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMyIdentitiesResponsePrimaryWithDefaults

`func NewMyIdentitiesResponsePrimaryWithDefaults() *MyIdentitiesResponsePrimary`

NewMyIdentitiesResponsePrimaryWithDefaults instantiates a new MyIdentitiesResponsePrimary object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetProvider

`func (o *MyIdentitiesResponsePrimary) GetProvider() string`

GetProvider returns the Provider field if non-nil, zero value otherwise.

### GetProviderOk

`func (o *MyIdentitiesResponsePrimary) GetProviderOk() (*string, bool)`

GetProviderOk returns a tuple with the Provider field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProvider

`func (o *MyIdentitiesResponsePrimary) SetProvider(v string)`

SetProvider sets Provider field to given value.


### GetEmail

`func (o *MyIdentitiesResponsePrimary) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *MyIdentitiesResponsePrimary) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *MyIdentitiesResponsePrimary) SetEmail(v string)`

SetEmail sets Email field to given value.


### GetName

`func (o *MyIdentitiesResponsePrimary) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *MyIdentitiesResponsePrimary) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *MyIdentitiesResponsePrimary) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *MyIdentitiesResponsePrimary) HasName() bool`

HasName returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


