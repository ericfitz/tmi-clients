# ListAddonsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Addons** | [**[]AddonResponse**](AddonResponse.md) |  | 
**Total** | **int32** | Total number of add-ons matching criteria | 
**Limit** | **int32** | Pagination limit | 
**Offset** | **int32** | Pagination offset | 

## Methods

### NewListAddonsResponse

`func NewListAddonsResponse(addons []AddonResponse, total int32, limit int32, offset int32, ) *ListAddonsResponse`

NewListAddonsResponse instantiates a new ListAddonsResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListAddonsResponseWithDefaults

`func NewListAddonsResponseWithDefaults() *ListAddonsResponse`

NewListAddonsResponseWithDefaults instantiates a new ListAddonsResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAddons

`func (o *ListAddonsResponse) GetAddons() []AddonResponse`

GetAddons returns the Addons field if non-nil, zero value otherwise.

### GetAddonsOk

`func (o *ListAddonsResponse) GetAddonsOk() (*[]AddonResponse, bool)`

GetAddonsOk returns a tuple with the Addons field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAddons

`func (o *ListAddonsResponse) SetAddons(v []AddonResponse)`

SetAddons sets Addons field to given value.


### GetTotal

`func (o *ListAddonsResponse) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListAddonsResponse) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListAddonsResponse) SetTotal(v int32)`

SetTotal sets Total field to given value.


### GetLimit

`func (o *ListAddonsResponse) GetLimit() int32`

GetLimit returns the Limit field if non-nil, zero value otherwise.

### GetLimitOk

`func (o *ListAddonsResponse) GetLimitOk() (*int32, bool)`

GetLimitOk returns a tuple with the Limit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimit

`func (o *ListAddonsResponse) SetLimit(v int32)`

SetLimit sets Limit field to given value.


### GetOffset

`func (o *ListAddonsResponse) GetOffset() int32`

GetOffset returns the Offset field if non-nil, zero value otherwise.

### GetOffsetOk

`func (o *ListAddonsResponse) GetOffsetOk() (*int32, bool)`

GetOffsetOk returns a tuple with the Offset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOffset

`func (o *ListAddonsResponse) SetOffset(v int32)`

SetOffset sets Offset field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


