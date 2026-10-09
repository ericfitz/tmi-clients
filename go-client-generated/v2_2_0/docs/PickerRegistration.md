# PickerRegistration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ProviderId** | **string** | Content OAuth provider that issued the picker grant | 
**FileId** | **string** | Provider-native file identifier from the picker (e.g. Google Drive file ID, or Microsoft \&quot;{driveId}:{itemId}\&quot;) | 
**MimeType** | **string** | MIME type returned by the picker | 

## Methods

### NewPickerRegistration

`func NewPickerRegistration(providerId string, fileId string, mimeType string, ) *PickerRegistration`

NewPickerRegistration instantiates a new PickerRegistration object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPickerRegistrationWithDefaults

`func NewPickerRegistrationWithDefaults() *PickerRegistration`

NewPickerRegistrationWithDefaults instantiates a new PickerRegistration object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetProviderId

`func (o *PickerRegistration) GetProviderId() string`

GetProviderId returns the ProviderId field if non-nil, zero value otherwise.

### GetProviderIdOk

`func (o *PickerRegistration) GetProviderIdOk() (*string, bool)`

GetProviderIdOk returns a tuple with the ProviderId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderId

`func (o *PickerRegistration) SetProviderId(v string)`

SetProviderId sets ProviderId field to given value.


### GetFileId

`func (o *PickerRegistration) GetFileId() string`

GetFileId returns the FileId field if non-nil, zero value otherwise.

### GetFileIdOk

`func (o *PickerRegistration) GetFileIdOk() (*string, bool)`

GetFileIdOk returns a tuple with the FileId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFileId

`func (o *PickerRegistration) SetFileId(v string)`

SetFileId sets FileId field to given value.


### GetMimeType

`func (o *PickerRegistration) GetMimeType() string`

GetMimeType returns the MimeType field if non-nil, zero value otherwise.

### GetMimeTypeOk

`func (o *PickerRegistration) GetMimeTypeOk() (*string, bool)`

GetMimeTypeOk returns a tuple with the MimeType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMimeType

`func (o *PickerRegistration) SetMimeType(v string)`

SetMimeType sets MimeType field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


