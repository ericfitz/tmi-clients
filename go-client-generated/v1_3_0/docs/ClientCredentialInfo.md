# ClientCredentialInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier for the credential | 
**ClientId** | **string** | OAuth 2.0 client ID (format: tmi_cc_*) | 
**Name** | **string** | Human-readable name for the credential | 
**Description** | Pointer to **string** | Optional description of the credential&#39;s purpose | [optional] 
**IsActive** | **bool** | Whether the credential is active | 
**LastUsedAt** | Pointer to **time.Time** | Last time this credential was used (ISO 8601) | [optional] 
**CreatedAt** | **time.Time** | Creation timestamp (ISO 8601) | 
**ModifiedAt** | **time.Time** | Last modification timestamp (ISO 8601) | 
**ExpiresAt** | Pointer to **time.Time** | Optional expiration timestamp (ISO 8601) | [optional] 

## Methods

### NewClientCredentialInfo

`func NewClientCredentialInfo(id string, clientId string, name string, isActive bool, createdAt time.Time, modifiedAt time.Time, ) *ClientCredentialInfo`

NewClientCredentialInfo instantiates a new ClientCredentialInfo object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewClientCredentialInfoWithDefaults

`func NewClientCredentialInfoWithDefaults() *ClientCredentialInfo`

NewClientCredentialInfoWithDefaults instantiates a new ClientCredentialInfo object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *ClientCredentialInfo) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ClientCredentialInfo) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ClientCredentialInfo) SetId(v string)`

SetId sets Id field to given value.


### GetClientId

`func (o *ClientCredentialInfo) GetClientId() string`

GetClientId returns the ClientId field if non-nil, zero value otherwise.

### GetClientIdOk

`func (o *ClientCredentialInfo) GetClientIdOk() (*string, bool)`

GetClientIdOk returns a tuple with the ClientId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClientId

`func (o *ClientCredentialInfo) SetClientId(v string)`

SetClientId sets ClientId field to given value.


### GetName

`func (o *ClientCredentialInfo) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ClientCredentialInfo) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ClientCredentialInfo) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *ClientCredentialInfo) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *ClientCredentialInfo) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *ClientCredentialInfo) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *ClientCredentialInfo) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetIsActive

`func (o *ClientCredentialInfo) GetIsActive() bool`

GetIsActive returns the IsActive field if non-nil, zero value otherwise.

### GetIsActiveOk

`func (o *ClientCredentialInfo) GetIsActiveOk() (*bool, bool)`

GetIsActiveOk returns a tuple with the IsActive field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsActive

`func (o *ClientCredentialInfo) SetIsActive(v bool)`

SetIsActive sets IsActive field to given value.


### GetLastUsedAt

`func (o *ClientCredentialInfo) GetLastUsedAt() time.Time`

GetLastUsedAt returns the LastUsedAt field if non-nil, zero value otherwise.

### GetLastUsedAtOk

`func (o *ClientCredentialInfo) GetLastUsedAtOk() (*time.Time, bool)`

GetLastUsedAtOk returns a tuple with the LastUsedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastUsedAt

`func (o *ClientCredentialInfo) SetLastUsedAt(v time.Time)`

SetLastUsedAt sets LastUsedAt field to given value.

### HasLastUsedAt

`func (o *ClientCredentialInfo) HasLastUsedAt() bool`

HasLastUsedAt returns a boolean if a field has been set.

### GetCreatedAt

`func (o *ClientCredentialInfo) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *ClientCredentialInfo) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *ClientCredentialInfo) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetModifiedAt

`func (o *ClientCredentialInfo) GetModifiedAt() time.Time`

GetModifiedAt returns the ModifiedAt field if non-nil, zero value otherwise.

### GetModifiedAtOk

`func (o *ClientCredentialInfo) GetModifiedAtOk() (*time.Time, bool)`

GetModifiedAtOk returns a tuple with the ModifiedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedAt

`func (o *ClientCredentialInfo) SetModifiedAt(v time.Time)`

SetModifiedAt sets ModifiedAt field to given value.


### GetExpiresAt

`func (o *ClientCredentialInfo) GetExpiresAt() time.Time`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *ClientCredentialInfo) GetExpiresAtOk() (*time.Time, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *ClientCredentialInfo) SetExpiresAt(v time.Time)`

SetExpiresAt sets ExpiresAt field to given value.

### HasExpiresAt

`func (o *ClientCredentialInfo) HasExpiresAt() bool`

HasExpiresAt returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


