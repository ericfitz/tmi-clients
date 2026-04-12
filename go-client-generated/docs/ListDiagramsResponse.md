# ListDiagramsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Diagrams** | [**[]DiagramListItem**](DiagramListItem.md) |  | 
**Total** | **int32** | Total number of diagrams matching criteria | 
**Limit** | **int32** | Pagination limit | 
**Offset** | **int32** | Pagination offset | 

## Methods

### NewListDiagramsResponse

`func NewListDiagramsResponse(diagrams []DiagramListItem, total int32, limit int32, offset int32, ) *ListDiagramsResponse`

NewListDiagramsResponse instantiates a new ListDiagramsResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListDiagramsResponseWithDefaults

`func NewListDiagramsResponseWithDefaults() *ListDiagramsResponse`

NewListDiagramsResponseWithDefaults instantiates a new ListDiagramsResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDiagrams

`func (o *ListDiagramsResponse) GetDiagrams() []DiagramListItem`

GetDiagrams returns the Diagrams field if non-nil, zero value otherwise.

### GetDiagramsOk

`func (o *ListDiagramsResponse) GetDiagramsOk() (*[]DiagramListItem, bool)`

GetDiagramsOk returns a tuple with the Diagrams field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDiagrams

`func (o *ListDiagramsResponse) SetDiagrams(v []DiagramListItem)`

SetDiagrams sets Diagrams field to given value.


### GetTotal

`func (o *ListDiagramsResponse) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListDiagramsResponse) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListDiagramsResponse) SetTotal(v int32)`

SetTotal sets Total field to given value.


### GetLimit

`func (o *ListDiagramsResponse) GetLimit() int32`

GetLimit returns the Limit field if non-nil, zero value otherwise.

### GetLimitOk

`func (o *ListDiagramsResponse) GetLimitOk() (*int32, bool)`

GetLimitOk returns a tuple with the Limit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimit

`func (o *ListDiagramsResponse) SetLimit(v int32)`

SetLimit sets Limit field to given value.


### GetOffset

`func (o *ListDiagramsResponse) GetOffset() int32`

GetOffset returns the Offset field if non-nil, zero value otherwise.

### GetOffsetOk

`func (o *ListDiagramsResponse) GetOffsetOk() (*int32, bool)`

GetOffsetOk returns a tuple with the Offset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOffset

`func (o *ListDiagramsResponse) SetOffset(v int32)`

SetOffset sets Offset field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


