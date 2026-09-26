# CreateAdminUserClientCredentialRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Human-readable name for the credential | 
**Description** | Pointer to **string** | Optional description of the credential&#39;s purpose | [optional] 
**ExpiresAt** | Pointer to **time.Time** | Optional expiration timestamp (ISO 8601) | [optional] 
**DirectWrite** | Pointer to **bool** | Opt in to direct writes for this automation account: tokens from this credential may modify threat-model sub-resources, authorized by the automation user&#39;s roles. Omitting the field is the same as false. Rejected with 400 when the automation user is a member of the Administrators group. | [optional] [default to false]
**AddonId** | Pointer to **string** | Optional addon to link this credential to (only valid with direct_write&#x3D;true; 400 otherwise, or if the addon does not exist). Events caused by writes made with tokens from this credential are not delivered to the linked addon&#39;s own webhook subscription, matching the suppression applied to delegation-token write-backs. Not a foreign key: deleting the addon leaves the credential intact and simply stops the suppression. | [optional] 

## Methods

### NewCreateAdminUserClientCredentialRequest

`func NewCreateAdminUserClientCredentialRequest(name string, ) *CreateAdminUserClientCredentialRequest`

NewCreateAdminUserClientCredentialRequest instantiates a new CreateAdminUserClientCredentialRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateAdminUserClientCredentialRequestWithDefaults

`func NewCreateAdminUserClientCredentialRequestWithDefaults() *CreateAdminUserClientCredentialRequest`

NewCreateAdminUserClientCredentialRequestWithDefaults instantiates a new CreateAdminUserClientCredentialRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *CreateAdminUserClientCredentialRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateAdminUserClientCredentialRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CreateAdminUserClientCredentialRequest) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *CreateAdminUserClientCredentialRequest) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *CreateAdminUserClientCredentialRequest) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *CreateAdminUserClientCredentialRequest) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *CreateAdminUserClientCredentialRequest) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetExpiresAt

`func (o *CreateAdminUserClientCredentialRequest) GetExpiresAt() time.Time`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *CreateAdminUserClientCredentialRequest) GetExpiresAtOk() (*time.Time, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *CreateAdminUserClientCredentialRequest) SetExpiresAt(v time.Time)`

SetExpiresAt sets ExpiresAt field to given value.

### HasExpiresAt

`func (o *CreateAdminUserClientCredentialRequest) HasExpiresAt() bool`

HasExpiresAt returns a boolean if a field has been set.

### GetDirectWrite

`func (o *CreateAdminUserClientCredentialRequest) GetDirectWrite() bool`

GetDirectWrite returns the DirectWrite field if non-nil, zero value otherwise.

### GetDirectWriteOk

`func (o *CreateAdminUserClientCredentialRequest) GetDirectWriteOk() (*bool, bool)`

GetDirectWriteOk returns a tuple with the DirectWrite field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDirectWrite

`func (o *CreateAdminUserClientCredentialRequest) SetDirectWrite(v bool)`

SetDirectWrite sets DirectWrite field to given value.

### HasDirectWrite

`func (o *CreateAdminUserClientCredentialRequest) HasDirectWrite() bool`

HasDirectWrite returns a boolean if a field has been set.

### GetAddonId

`func (o *CreateAdminUserClientCredentialRequest) GetAddonId() string`

GetAddonId returns the AddonId field if non-nil, zero value otherwise.

### GetAddonIdOk

`func (o *CreateAdminUserClientCredentialRequest) GetAddonIdOk() (*string, bool)`

GetAddonIdOk returns a tuple with the AddonId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAddonId

`func (o *CreateAdminUserClientCredentialRequest) SetAddonId(v string)`

SetAddonId sets AddonId field to given value.

### HasAddonId

`func (o *CreateAdminUserClientCredentialRequest) HasAddonId() bool`

HasAddonId returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


