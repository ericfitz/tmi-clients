# CreateCurrentUserClientCredentialRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Human-readable name for the credential | 
**Description** | Pointer to **string** | Optional description of the credential&#39;s purpose | [optional] 
**ExpiresAt** | Pointer to **time.Time** | Optional expiration timestamp (ISO 8601) | [optional] 

## Methods

### NewCreateCurrentUserClientCredentialRequest

`func NewCreateCurrentUserClientCredentialRequest(name string, ) *CreateCurrentUserClientCredentialRequest`

NewCreateCurrentUserClientCredentialRequest instantiates a new CreateCurrentUserClientCredentialRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateCurrentUserClientCredentialRequestWithDefaults

`func NewCreateCurrentUserClientCredentialRequestWithDefaults() *CreateCurrentUserClientCredentialRequest`

NewCreateCurrentUserClientCredentialRequestWithDefaults instantiates a new CreateCurrentUserClientCredentialRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *CreateCurrentUserClientCredentialRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateCurrentUserClientCredentialRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CreateCurrentUserClientCredentialRequest) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *CreateCurrentUserClientCredentialRequest) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *CreateCurrentUserClientCredentialRequest) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *CreateCurrentUserClientCredentialRequest) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *CreateCurrentUserClientCredentialRequest) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetExpiresAt

`func (o *CreateCurrentUserClientCredentialRequest) GetExpiresAt() time.Time`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *CreateCurrentUserClientCredentialRequest) GetExpiresAtOk() (*time.Time, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *CreateCurrentUserClientCredentialRequest) SetExpiresAt(v time.Time)`

SetExpiresAt sets ExpiresAt field to given value.

### HasExpiresAt

`func (o *CreateCurrentUserClientCredentialRequest) HasExpiresAt() bool`

HasExpiresAt returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


