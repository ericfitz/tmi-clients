# ContentProvider

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Source identifier (matches ContentSource.Name()) | 
**Name** | **string** | Display label for the provider | 
**Kind** | **string** | delegated: per-user OAuth (client must call /me/content_tokens/{id}/authorize); service: operator-credentialed (no per-user link); direct: no auth (e.g., HTTP fetch) | 
**Icon** | **string** | Font Awesome class string (matches OAuth IdP convention). Empty if no default and no override. | 
**PickerConfig** | Pointer to **map[string]string** | Browser-safe OAuth/picker bootstrap values for in-browser file pickers. Present only when the operator has configured a public Web OAuth client for this provider. All values are intended for browser use; never include client_secret or service-account material here. Per-provider keys are documented in the provider&#39;s section. | [optional] 

## Methods

### NewContentProvider

`func NewContentProvider(id string, name string, kind string, icon string, ) *ContentProvider`

NewContentProvider instantiates a new ContentProvider object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewContentProviderWithDefaults

`func NewContentProviderWithDefaults() *ContentProvider`

NewContentProviderWithDefaults instantiates a new ContentProvider object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *ContentProvider) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ContentProvider) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ContentProvider) SetId(v string)`

SetId sets Id field to given value.


### GetName

`func (o *ContentProvider) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ContentProvider) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ContentProvider) SetName(v string)`

SetName sets Name field to given value.


### GetKind

`func (o *ContentProvider) GetKind() string`

GetKind returns the Kind field if non-nil, zero value otherwise.

### GetKindOk

`func (o *ContentProvider) GetKindOk() (*string, bool)`

GetKindOk returns a tuple with the Kind field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKind

`func (o *ContentProvider) SetKind(v string)`

SetKind sets Kind field to given value.


### GetIcon

`func (o *ContentProvider) GetIcon() string`

GetIcon returns the Icon field if non-nil, zero value otherwise.

### GetIconOk

`func (o *ContentProvider) GetIconOk() (*string, bool)`

GetIconOk returns a tuple with the Icon field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIcon

`func (o *ContentProvider) SetIcon(v string)`

SetIcon sets Icon field to given value.


### GetPickerConfig

`func (o *ContentProvider) GetPickerConfig() map[string]string`

GetPickerConfig returns the PickerConfig field if non-nil, zero value otherwise.

### GetPickerConfigOk

`func (o *ContentProvider) GetPickerConfigOk() (*map[string]string, bool)`

GetPickerConfigOk returns a tuple with the PickerConfig field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPickerConfig

`func (o *ContentProvider) SetPickerConfig(v map[string]string)`

SetPickerConfig sets PickerConfig field to given value.

### HasPickerConfig

`func (o *ContentProvider) HasPickerConfig() bool`

HasPickerConfig returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


