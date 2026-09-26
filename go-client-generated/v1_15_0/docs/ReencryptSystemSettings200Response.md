# ReencryptSystemSettings200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Reencrypted** | **int32** | Number of settings successfully re-encrypted | 
**Errors** | [**[]ReencryptSystemSettings200ResponseErrorsInner**](ReencryptSystemSettings200ResponseErrorsInner.md) | Settings that failed re-encryption | 
**Total** | **int32** | Total number of settings processed | 

## Methods

### NewReencryptSystemSettings200Response

`func NewReencryptSystemSettings200Response(reencrypted int32, errors []ReencryptSystemSettings200ResponseErrorsInner, total int32, ) *ReencryptSystemSettings200Response`

NewReencryptSystemSettings200Response instantiates a new ReencryptSystemSettings200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewReencryptSystemSettings200ResponseWithDefaults

`func NewReencryptSystemSettings200ResponseWithDefaults() *ReencryptSystemSettings200Response`

NewReencryptSystemSettings200ResponseWithDefaults instantiates a new ReencryptSystemSettings200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetReencrypted

`func (o *ReencryptSystemSettings200Response) GetReencrypted() int32`

GetReencrypted returns the Reencrypted field if non-nil, zero value otherwise.

### GetReencryptedOk

`func (o *ReencryptSystemSettings200Response) GetReencryptedOk() (*int32, bool)`

GetReencryptedOk returns a tuple with the Reencrypted field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReencrypted

`func (o *ReencryptSystemSettings200Response) SetReencrypted(v int32)`

SetReencrypted sets Reencrypted field to given value.


### GetErrors

`func (o *ReencryptSystemSettings200Response) GetErrors() []ReencryptSystemSettings200ResponseErrorsInner`

GetErrors returns the Errors field if non-nil, zero value otherwise.

### GetErrorsOk

`func (o *ReencryptSystemSettings200Response) GetErrorsOk() (*[]ReencryptSystemSettings200ResponseErrorsInner, bool)`

GetErrorsOk returns a tuple with the Errors field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrors

`func (o *ReencryptSystemSettings200Response) SetErrors(v []ReencryptSystemSettings200ResponseErrorsInner)`

SetErrors sets Errors field to given value.


### GetTotal

`func (o *ReencryptSystemSettings200Response) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ReencryptSystemSettings200Response) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ReencryptSystemSettings200Response) SetTotal(v int32)`

SetTotal sets Total field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


