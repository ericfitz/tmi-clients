# ClientConfigLimits

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**MaxFileUploadMb** | Pointer to **int32** | Maximum file upload size in megabytes | [optional] 
**MaxDiagramParticipants** | Pointer to **int32** | Maximum participants per collaboration session | [optional] 

## Methods

### NewClientConfigLimits

`func NewClientConfigLimits() *ClientConfigLimits`

NewClientConfigLimits instantiates a new ClientConfigLimits object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewClientConfigLimitsWithDefaults

`func NewClientConfigLimitsWithDefaults() *ClientConfigLimits`

NewClientConfigLimitsWithDefaults instantiates a new ClientConfigLimits object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMaxFileUploadMb

`func (o *ClientConfigLimits) GetMaxFileUploadMb() int32`

GetMaxFileUploadMb returns the MaxFileUploadMb field if non-nil, zero value otherwise.

### GetMaxFileUploadMbOk

`func (o *ClientConfigLimits) GetMaxFileUploadMbOk() (*int32, bool)`

GetMaxFileUploadMbOk returns a tuple with the MaxFileUploadMb field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxFileUploadMb

`func (o *ClientConfigLimits) SetMaxFileUploadMb(v int32)`

SetMaxFileUploadMb sets MaxFileUploadMb field to given value.

### HasMaxFileUploadMb

`func (o *ClientConfigLimits) HasMaxFileUploadMb() bool`

HasMaxFileUploadMb returns a boolean if a field has been set.

### GetMaxDiagramParticipants

`func (o *ClientConfigLimits) GetMaxDiagramParticipants() int32`

GetMaxDiagramParticipants returns the MaxDiagramParticipants field if non-nil, zero value otherwise.

### GetMaxDiagramParticipantsOk

`func (o *ClientConfigLimits) GetMaxDiagramParticipantsOk() (*int32, bool)`

GetMaxDiagramParticipantsOk returns a tuple with the MaxDiagramParticipants field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxDiagramParticipants

`func (o *ClientConfigLimits) SetMaxDiagramParticipants(v int32)`

SetMaxDiagramParticipants sets MaxDiagramParticipants field to given value.

### HasMaxDiagramParticipants

`func (o *ClientConfigLimits) HasMaxDiagramParticipants() bool`

HasMaxDiagramParticipants returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


