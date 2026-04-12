# EdgeLabel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Attrs** | Pointer to [**EdgeLabelAttrs**](EdgeLabelAttrs.md) |  | [optional] 
**Position** | Pointer to [**EdgeLabelPosition**](EdgeLabelPosition.md) |  | [optional] 

## Methods

### NewEdgeLabel

`func NewEdgeLabel() *EdgeLabel`

NewEdgeLabel instantiates a new EdgeLabel object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEdgeLabelWithDefaults

`func NewEdgeLabelWithDefaults() *EdgeLabel`

NewEdgeLabelWithDefaults instantiates a new EdgeLabel object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAttrs

`func (o *EdgeLabel) GetAttrs() EdgeLabelAttrs`

GetAttrs returns the Attrs field if non-nil, zero value otherwise.

### GetAttrsOk

`func (o *EdgeLabel) GetAttrsOk() (*EdgeLabelAttrs, bool)`

GetAttrsOk returns a tuple with the Attrs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttrs

`func (o *EdgeLabel) SetAttrs(v EdgeLabelAttrs)`

SetAttrs sets Attrs field to given value.

### HasAttrs

`func (o *EdgeLabel) HasAttrs() bool`

HasAttrs returns a boolean if a field has been set.

### GetPosition

`func (o *EdgeLabel) GetPosition() EdgeLabelPosition`

GetPosition returns the Position field if non-nil, zero value otherwise.

### GetPositionOk

`func (o *EdgeLabel) GetPositionOk() (*EdgeLabelPosition, bool)`

GetPositionOk returns a tuple with the Position field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPosition

`func (o *EdgeLabel) SetPosition(v EdgeLabelPosition)`

SetPosition sets Position field to given value.

### HasPosition

`func (o *EdgeLabel) HasPosition() bool`

HasPosition returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


