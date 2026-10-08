# MicrosoftPickerGrantRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DriveId** | **string** | OneDrive or SharePoint drive identifier returned by the Microsoft File Picker. | 
**ItemId** | **string** | Drive item identifier returned by the Microsoft File Picker. | 

## Methods

### NewMicrosoftPickerGrantRequest

`func NewMicrosoftPickerGrantRequest(driveId string, itemId string, ) *MicrosoftPickerGrantRequest`

NewMicrosoftPickerGrantRequest instantiates a new MicrosoftPickerGrantRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMicrosoftPickerGrantRequestWithDefaults

`func NewMicrosoftPickerGrantRequestWithDefaults() *MicrosoftPickerGrantRequest`

NewMicrosoftPickerGrantRequestWithDefaults instantiates a new MicrosoftPickerGrantRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDriveId

`func (o *MicrosoftPickerGrantRequest) GetDriveId() string`

GetDriveId returns the DriveId field if non-nil, zero value otherwise.

### GetDriveIdOk

`func (o *MicrosoftPickerGrantRequest) GetDriveIdOk() (*string, bool)`

GetDriveIdOk returns a tuple with the DriveId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDriveId

`func (o *MicrosoftPickerGrantRequest) SetDriveId(v string)`

SetDriveId sets DriveId field to given value.


### GetItemId

`func (o *MicrosoftPickerGrantRequest) GetItemId() string`

GetItemId returns the ItemId field if non-nil, zero value otherwise.

### GetItemIdOk

`func (o *MicrosoftPickerGrantRequest) GetItemIdOk() (*string, bool)`

GetItemIdOk returns a tuple with the ItemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemId

`func (o *MicrosoftPickerGrantRequest) SetItemId(v string)`

SetItemId sets ItemId field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


