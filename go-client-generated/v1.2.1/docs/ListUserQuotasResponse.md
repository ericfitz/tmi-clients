# ListUserQuotasResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Quotas** | [**[]UserAPIQuota**](UserAPIQuota.md) |  | 
**Total** | **int32** | Total number of quotas matching criteria | 
**Limit** | **int32** | Pagination limit | 
**Offset** | **int32** | Pagination offset | 

## Methods

### NewListUserQuotasResponse

`func NewListUserQuotasResponse(quotas []UserAPIQuota, total int32, limit int32, offset int32, ) *ListUserQuotasResponse`

NewListUserQuotasResponse instantiates a new ListUserQuotasResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListUserQuotasResponseWithDefaults

`func NewListUserQuotasResponseWithDefaults() *ListUserQuotasResponse`

NewListUserQuotasResponseWithDefaults instantiates a new ListUserQuotasResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetQuotas

`func (o *ListUserQuotasResponse) GetQuotas() []UserAPIQuota`

GetQuotas returns the Quotas field if non-nil, zero value otherwise.

### GetQuotasOk

`func (o *ListUserQuotasResponse) GetQuotasOk() (*[]UserAPIQuota, bool)`

GetQuotasOk returns a tuple with the Quotas field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQuotas

`func (o *ListUserQuotasResponse) SetQuotas(v []UserAPIQuota)`

SetQuotas sets Quotas field to given value.


### GetTotal

`func (o *ListUserQuotasResponse) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListUserQuotasResponse) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListUserQuotasResponse) SetTotal(v int32)`

SetTotal sets Total field to given value.


### GetLimit

`func (o *ListUserQuotasResponse) GetLimit() int32`

GetLimit returns the Limit field if non-nil, zero value otherwise.

### GetLimitOk

`func (o *ListUserQuotasResponse) GetLimitOk() (*int32, bool)`

GetLimitOk returns a tuple with the Limit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimit

`func (o *ListUserQuotasResponse) SetLimit(v int32)`

SetLimit sets Limit field to given value.


### GetOffset

`func (o *ListUserQuotasResponse) GetOffset() int32`

GetOffset returns the Offset field if non-nil, zero value otherwise.

### GetOffsetOk

`func (o *ListUserQuotasResponse) GetOffsetOk() (*int32, bool)`

GetOffsetOk returns a tuple with the Offset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOffset

`func (o *ListUserQuotasResponse) SetOffset(v int32)`

SetOffset sets Offset field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


