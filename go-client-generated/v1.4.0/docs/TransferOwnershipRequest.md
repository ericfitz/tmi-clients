# TransferOwnershipRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TargetUserId** | **string** | Internal UUID of the user to receive ownership | 

## Methods

### NewTransferOwnershipRequest

`func NewTransferOwnershipRequest(targetUserId string, ) *TransferOwnershipRequest`

NewTransferOwnershipRequest instantiates a new TransferOwnershipRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTransferOwnershipRequestWithDefaults

`func NewTransferOwnershipRequestWithDefaults() *TransferOwnershipRequest`

NewTransferOwnershipRequestWithDefaults instantiates a new TransferOwnershipRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTargetUserId

`func (o *TransferOwnershipRequest) GetTargetUserId() string`

GetTargetUserId returns the TargetUserId field if non-nil, zero value otherwise.

### GetTargetUserIdOk

`func (o *TransferOwnershipRequest) GetTargetUserIdOk() (*string, bool)`

GetTargetUserIdOk returns a tuple with the TargetUserId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTargetUserId

`func (o *TransferOwnershipRequest) SetTargetUserId(v string)`

SetTargetUserId sets TargetUserId field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


