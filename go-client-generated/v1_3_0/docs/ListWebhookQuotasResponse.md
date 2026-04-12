# ListWebhookQuotasResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Quotas** | [**[]WebhookQuota**](WebhookQuota.md) |  | 
**Total** | **int32** | Total number of quotas matching criteria | 
**Limit** | **int32** | Pagination limit | 
**Offset** | **int32** | Pagination offset | 

## Methods

### NewListWebhookQuotasResponse

`func NewListWebhookQuotasResponse(quotas []WebhookQuota, total int32, limit int32, offset int32, ) *ListWebhookQuotasResponse`

NewListWebhookQuotasResponse instantiates a new ListWebhookQuotasResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListWebhookQuotasResponseWithDefaults

`func NewListWebhookQuotasResponseWithDefaults() *ListWebhookQuotasResponse`

NewListWebhookQuotasResponseWithDefaults instantiates a new ListWebhookQuotasResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetQuotas

`func (o *ListWebhookQuotasResponse) GetQuotas() []WebhookQuota`

GetQuotas returns the Quotas field if non-nil, zero value otherwise.

### GetQuotasOk

`func (o *ListWebhookQuotasResponse) GetQuotasOk() (*[]WebhookQuota, bool)`

GetQuotasOk returns a tuple with the Quotas field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQuotas

`func (o *ListWebhookQuotasResponse) SetQuotas(v []WebhookQuota)`

SetQuotas sets Quotas field to given value.


### GetTotal

`func (o *ListWebhookQuotasResponse) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListWebhookQuotasResponse) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListWebhookQuotasResponse) SetTotal(v int32)`

SetTotal sets Total field to given value.


### GetLimit

`func (o *ListWebhookQuotasResponse) GetLimit() int32`

GetLimit returns the Limit field if non-nil, zero value otherwise.

### GetLimitOk

`func (o *ListWebhookQuotasResponse) GetLimitOk() (*int32, bool)`

GetLimitOk returns a tuple with the Limit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimit

`func (o *ListWebhookQuotasResponse) SetLimit(v int32)`

SetLimit sets Limit field to given value.


### GetOffset

`func (o *ListWebhookQuotasResponse) GetOffset() int32`

GetOffset returns the Offset field if non-nil, zero value otherwise.

### GetOffsetOk

`func (o *ListWebhookQuotasResponse) GetOffsetOk() (*int32, bool)`

GetOffsetOk returns a tuple with the Offset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOffset

`func (o *ListWebhookQuotasResponse) SetOffset(v int32)`

SetOffset sets Offset field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


