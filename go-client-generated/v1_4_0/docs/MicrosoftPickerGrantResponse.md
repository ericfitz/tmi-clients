# MicrosoftPickerGrantResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**PermissionId** | **string** | Microsoft Graph permission id created by the grant call. | 
**DriveId** | **string** | OneDrive or SharePoint drive identifier of the granted file. | 
**ItemId** | **string** | Drive item identifier of the granted file. | 

## Methods

### NewMicrosoftPickerGrantResponse

`func NewMicrosoftPickerGrantResponse(permissionId string, driveId string, itemId string, ) *MicrosoftPickerGrantResponse`

NewMicrosoftPickerGrantResponse instantiates a new MicrosoftPickerGrantResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMicrosoftPickerGrantResponseWithDefaults

`func NewMicrosoftPickerGrantResponseWithDefaults() *MicrosoftPickerGrantResponse`

NewMicrosoftPickerGrantResponseWithDefaults instantiates a new MicrosoftPickerGrantResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPermissionId

`func (o *MicrosoftPickerGrantResponse) GetPermissionId() string`

GetPermissionId returns the PermissionId field if non-nil, zero value otherwise.

### GetPermissionIdOk

`func (o *MicrosoftPickerGrantResponse) GetPermissionIdOk() (*string, bool)`

GetPermissionIdOk returns a tuple with the PermissionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPermissionId

`func (o *MicrosoftPickerGrantResponse) SetPermissionId(v string)`

SetPermissionId sets PermissionId field to given value.


### GetDriveId

`func (o *MicrosoftPickerGrantResponse) GetDriveId() string`

GetDriveId returns the DriveId field if non-nil, zero value otherwise.

### GetDriveIdOk

`func (o *MicrosoftPickerGrantResponse) GetDriveIdOk() (*string, bool)`

GetDriveIdOk returns a tuple with the DriveId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDriveId

`func (o *MicrosoftPickerGrantResponse) SetDriveId(v string)`

SetDriveId sets DriveId field to given value.


### GetItemId

`func (o *MicrosoftPickerGrantResponse) GetItemId() string`

GetItemId returns the ItemId field if non-nil, zero value otherwise.

### GetItemIdOk

`func (o *MicrosoftPickerGrantResponse) GetItemIdOk() (*string, bool)`

GetItemIdOk returns a tuple with the ItemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemId

`func (o *MicrosoftPickerGrantResponse) SetItemId(v string)`

SetItemId sets ItemId field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


