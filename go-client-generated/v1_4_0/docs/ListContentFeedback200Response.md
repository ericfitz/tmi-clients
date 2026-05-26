# ListContentFeedback200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | [**[]ContentFeedback**](ContentFeedback.md) |  | 
**Total** | **int32** |  | 

## Methods

### NewListContentFeedback200Response

`func NewListContentFeedback200Response(items []ContentFeedback, total int32, ) *ListContentFeedback200Response`

NewListContentFeedback200Response instantiates a new ListContentFeedback200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListContentFeedback200ResponseWithDefaults

`func NewListContentFeedback200ResponseWithDefaults() *ListContentFeedback200Response`

NewListContentFeedback200ResponseWithDefaults instantiates a new ListContentFeedback200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *ListContentFeedback200Response) GetItems() []ContentFeedback`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *ListContentFeedback200Response) GetItemsOk() (*[]ContentFeedback, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *ListContentFeedback200Response) SetItems(v []ContentFeedback)`

SetItems sets Items field to given value.


### GetTotal

`func (o *ListContentFeedback200Response) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListContentFeedback200Response) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListContentFeedback200Response) SetTotal(v int32)`

SetTotal sets Total field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


