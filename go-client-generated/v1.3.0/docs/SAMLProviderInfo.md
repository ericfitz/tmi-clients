# SAMLProviderInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Provider identifier | 
**Name** | **string** | Display name of the provider | 
**Icon** | **string** | Icon identifier for the provider (Font Awesome class, URL, or path) | 
**AuthUrl** | **string** | TMI SAML login endpoint URL | 
**MetadataUrl** | **string** | SAML service provider metadata URL | 
**EntityId** | **string** | Service Provider entity ID | 
**AcsUrl** | **string** | Assertion Consumer Service URL | 
**SloUrl** | Pointer to **string** | Single Logout URL | [optional] 
**Initialized** | **bool** | Whether the SAML provider was successfully initialized and is available for authentication | 

## Methods

### NewSAMLProviderInfo

`func NewSAMLProviderInfo(id string, name string, icon string, authUrl string, metadataUrl string, entityId string, acsUrl string, initialized bool, ) *SAMLProviderInfo`

NewSAMLProviderInfo instantiates a new SAMLProviderInfo object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSAMLProviderInfoWithDefaults

`func NewSAMLProviderInfoWithDefaults() *SAMLProviderInfo`

NewSAMLProviderInfoWithDefaults instantiates a new SAMLProviderInfo object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *SAMLProviderInfo) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *SAMLProviderInfo) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *SAMLProviderInfo) SetId(v string)`

SetId sets Id field to given value.


### GetName

`func (o *SAMLProviderInfo) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *SAMLProviderInfo) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *SAMLProviderInfo) SetName(v string)`

SetName sets Name field to given value.


### GetIcon

`func (o *SAMLProviderInfo) GetIcon() string`

GetIcon returns the Icon field if non-nil, zero value otherwise.

### GetIconOk

`func (o *SAMLProviderInfo) GetIconOk() (*string, bool)`

GetIconOk returns a tuple with the Icon field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIcon

`func (o *SAMLProviderInfo) SetIcon(v string)`

SetIcon sets Icon field to given value.


### GetAuthUrl

`func (o *SAMLProviderInfo) GetAuthUrl() string`

GetAuthUrl returns the AuthUrl field if non-nil, zero value otherwise.

### GetAuthUrlOk

`func (o *SAMLProviderInfo) GetAuthUrlOk() (*string, bool)`

GetAuthUrlOk returns a tuple with the AuthUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthUrl

`func (o *SAMLProviderInfo) SetAuthUrl(v string)`

SetAuthUrl sets AuthUrl field to given value.


### GetMetadataUrl

`func (o *SAMLProviderInfo) GetMetadataUrl() string`

GetMetadataUrl returns the MetadataUrl field if non-nil, zero value otherwise.

### GetMetadataUrlOk

`func (o *SAMLProviderInfo) GetMetadataUrlOk() (*string, bool)`

GetMetadataUrlOk returns a tuple with the MetadataUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadataUrl

`func (o *SAMLProviderInfo) SetMetadataUrl(v string)`

SetMetadataUrl sets MetadataUrl field to given value.


### GetEntityId

`func (o *SAMLProviderInfo) GetEntityId() string`

GetEntityId returns the EntityId field if non-nil, zero value otherwise.

### GetEntityIdOk

`func (o *SAMLProviderInfo) GetEntityIdOk() (*string, bool)`

GetEntityIdOk returns a tuple with the EntityId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEntityId

`func (o *SAMLProviderInfo) SetEntityId(v string)`

SetEntityId sets EntityId field to given value.


### GetAcsUrl

`func (o *SAMLProviderInfo) GetAcsUrl() string`

GetAcsUrl returns the AcsUrl field if non-nil, zero value otherwise.

### GetAcsUrlOk

`func (o *SAMLProviderInfo) GetAcsUrlOk() (*string, bool)`

GetAcsUrlOk returns a tuple with the AcsUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAcsUrl

`func (o *SAMLProviderInfo) SetAcsUrl(v string)`

SetAcsUrl sets AcsUrl field to given value.


### GetSloUrl

`func (o *SAMLProviderInfo) GetSloUrl() string`

GetSloUrl returns the SloUrl field if non-nil, zero value otherwise.

### GetSloUrlOk

`func (o *SAMLProviderInfo) GetSloUrlOk() (*string, bool)`

GetSloUrlOk returns a tuple with the SloUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSloUrl

`func (o *SAMLProviderInfo) SetSloUrl(v string)`

SetSloUrl sets SloUrl field to given value.

### HasSloUrl

`func (o *SAMLProviderInfo) HasSloUrl() bool`

HasSloUrl returns a boolean if a field has been set.

### GetInitialized

`func (o *SAMLProviderInfo) GetInitialized() bool`

GetInitialized returns the Initialized field if non-nil, zero value otherwise.

### GetInitializedOk

`func (o *SAMLProviderInfo) GetInitializedOk() (*bool, bool)`

GetInitializedOk returns a tuple with the Initialized field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInitialized

`func (o *SAMLProviderInfo) SetInitialized(v bool)`

SetInitialized sets Initialized field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


