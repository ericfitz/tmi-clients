# InvocationResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Invocation identifier | 
**AddonId** | **string** | Add-on that was invoked | 
**ThreatModelId** | **string** | Threat model context | 
**ObjectType** | Pointer to **string** | Object type (if specified) | [optional] 
**ObjectId** | Pointer to **string** | Object ID (if specified) | [optional] 
**InvokedBy** | [**User**](User.md) | User who triggered the invocation | 
**Payload** | Pointer to **string** | JSON-encoded payload | [optional] 
**Status** | **string** | Current status | 
**StatusPercent** | **int32** | Progress percentage (0-100) | 
**StatusMessage** | Pointer to **string** | Optional status description | [optional] 
**CreatedAt** | **time.Time** | Creation timestamp | 
**StatusUpdatedAt** | **time.Time** | Last status update timestamp | 

## Methods

### NewInvocationResponse

`func NewInvocationResponse(id string, addonId string, threatModelId string, invokedBy User, status string, statusPercent int32, createdAt time.Time, statusUpdatedAt time.Time, ) *InvocationResponse`

NewInvocationResponse instantiates a new InvocationResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewInvocationResponseWithDefaults

`func NewInvocationResponseWithDefaults() *InvocationResponse`

NewInvocationResponseWithDefaults instantiates a new InvocationResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *InvocationResponse) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *InvocationResponse) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *InvocationResponse) SetId(v string)`

SetId sets Id field to given value.


### GetAddonId

`func (o *InvocationResponse) GetAddonId() string`

GetAddonId returns the AddonId field if non-nil, zero value otherwise.

### GetAddonIdOk

`func (o *InvocationResponse) GetAddonIdOk() (*string, bool)`

GetAddonIdOk returns a tuple with the AddonId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAddonId

`func (o *InvocationResponse) SetAddonId(v string)`

SetAddonId sets AddonId field to given value.


### GetThreatModelId

`func (o *InvocationResponse) GetThreatModelId() string`

GetThreatModelId returns the ThreatModelId field if non-nil, zero value otherwise.

### GetThreatModelIdOk

`func (o *InvocationResponse) GetThreatModelIdOk() (*string, bool)`

GetThreatModelIdOk returns a tuple with the ThreatModelId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreatModelId

`func (o *InvocationResponse) SetThreatModelId(v string)`

SetThreatModelId sets ThreatModelId field to given value.


### GetObjectType

`func (o *InvocationResponse) GetObjectType() string`

GetObjectType returns the ObjectType field if non-nil, zero value otherwise.

### GetObjectTypeOk

`func (o *InvocationResponse) GetObjectTypeOk() (*string, bool)`

GetObjectTypeOk returns a tuple with the ObjectType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjectType

`func (o *InvocationResponse) SetObjectType(v string)`

SetObjectType sets ObjectType field to given value.

### HasObjectType

`func (o *InvocationResponse) HasObjectType() bool`

HasObjectType returns a boolean if a field has been set.

### GetObjectId

`func (o *InvocationResponse) GetObjectId() string`

GetObjectId returns the ObjectId field if non-nil, zero value otherwise.

### GetObjectIdOk

`func (o *InvocationResponse) GetObjectIdOk() (*string, bool)`

GetObjectIdOk returns a tuple with the ObjectId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjectId

`func (o *InvocationResponse) SetObjectId(v string)`

SetObjectId sets ObjectId field to given value.

### HasObjectId

`func (o *InvocationResponse) HasObjectId() bool`

HasObjectId returns a boolean if a field has been set.

### GetInvokedBy

`func (o *InvocationResponse) GetInvokedBy() User`

GetInvokedBy returns the InvokedBy field if non-nil, zero value otherwise.

### GetInvokedByOk

`func (o *InvocationResponse) GetInvokedByOk() (*User, bool)`

GetInvokedByOk returns a tuple with the InvokedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInvokedBy

`func (o *InvocationResponse) SetInvokedBy(v User)`

SetInvokedBy sets InvokedBy field to given value.


### GetPayload

`func (o *InvocationResponse) GetPayload() string`

GetPayload returns the Payload field if non-nil, zero value otherwise.

### GetPayloadOk

`func (o *InvocationResponse) GetPayloadOk() (*string, bool)`

GetPayloadOk returns a tuple with the Payload field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPayload

`func (o *InvocationResponse) SetPayload(v string)`

SetPayload sets Payload field to given value.

### HasPayload

`func (o *InvocationResponse) HasPayload() bool`

HasPayload returns a boolean if a field has been set.

### GetStatus

`func (o *InvocationResponse) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *InvocationResponse) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *InvocationResponse) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetStatusPercent

`func (o *InvocationResponse) GetStatusPercent() int32`

GetStatusPercent returns the StatusPercent field if non-nil, zero value otherwise.

### GetStatusPercentOk

`func (o *InvocationResponse) GetStatusPercentOk() (*int32, bool)`

GetStatusPercentOk returns a tuple with the StatusPercent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatusPercent

`func (o *InvocationResponse) SetStatusPercent(v int32)`

SetStatusPercent sets StatusPercent field to given value.


### GetStatusMessage

`func (o *InvocationResponse) GetStatusMessage() string`

GetStatusMessage returns the StatusMessage field if non-nil, zero value otherwise.

### GetStatusMessageOk

`func (o *InvocationResponse) GetStatusMessageOk() (*string, bool)`

GetStatusMessageOk returns a tuple with the StatusMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatusMessage

`func (o *InvocationResponse) SetStatusMessage(v string)`

SetStatusMessage sets StatusMessage field to given value.

### HasStatusMessage

`func (o *InvocationResponse) HasStatusMessage() bool`

HasStatusMessage returns a boolean if a field has been set.

### GetCreatedAt

`func (o *InvocationResponse) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *InvocationResponse) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *InvocationResponse) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetStatusUpdatedAt

`func (o *InvocationResponse) GetStatusUpdatedAt() time.Time`

GetStatusUpdatedAt returns the StatusUpdatedAt field if non-nil, zero value otherwise.

### GetStatusUpdatedAtOk

`func (o *InvocationResponse) GetStatusUpdatedAtOk() (*time.Time, bool)`

GetStatusUpdatedAtOk returns a tuple with the StatusUpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatusUpdatedAt

`func (o *InvocationResponse) SetStatusUpdatedAt(v time.Time)`

SetStatusUpdatedAt sets StatusUpdatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


