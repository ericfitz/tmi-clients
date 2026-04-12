# EdgeLabelPosition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Distance** | **float32** | Position along the edge: 0-1 for percentage, &gt;1 for pixels from start, &lt;0 for pixels from end | 
**Offset** | Pointer to [**EdgeLabelPositionOneOfOffset**](EdgeLabelPositionOneOfOffset.md) |  | [optional] 
**Angle** | Pointer to **float32** | Rotation angle in degrees (clockwise) | [optional] 
**Options** | Pointer to [**EdgeLabelPositionOneOfOptions**](EdgeLabelPositionOneOfOptions.md) |  | [optional] 

## Methods

### NewEdgeLabelPosition

`func NewEdgeLabelPosition(distance float32, ) *EdgeLabelPosition`

NewEdgeLabelPosition instantiates a new EdgeLabelPosition object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEdgeLabelPositionWithDefaults

`func NewEdgeLabelPositionWithDefaults() *EdgeLabelPosition`

NewEdgeLabelPositionWithDefaults instantiates a new EdgeLabelPosition object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDistance

`func (o *EdgeLabelPosition) GetDistance() float32`

GetDistance returns the Distance field if non-nil, zero value otherwise.

### GetDistanceOk

`func (o *EdgeLabelPosition) GetDistanceOk() (*float32, bool)`

GetDistanceOk returns a tuple with the Distance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDistance

`func (o *EdgeLabelPosition) SetDistance(v float32)`

SetDistance sets Distance field to given value.


### GetOffset

`func (o *EdgeLabelPosition) GetOffset() EdgeLabelPositionOneOfOffset`

GetOffset returns the Offset field if non-nil, zero value otherwise.

### GetOffsetOk

`func (o *EdgeLabelPosition) GetOffsetOk() (*EdgeLabelPositionOneOfOffset, bool)`

GetOffsetOk returns a tuple with the Offset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOffset

`func (o *EdgeLabelPosition) SetOffset(v EdgeLabelPositionOneOfOffset)`

SetOffset sets Offset field to given value.

### HasOffset

`func (o *EdgeLabelPosition) HasOffset() bool`

HasOffset returns a boolean if a field has been set.

### GetAngle

`func (o *EdgeLabelPosition) GetAngle() float32`

GetAngle returns the Angle field if non-nil, zero value otherwise.

### GetAngleOk

`func (o *EdgeLabelPosition) GetAngleOk() (*float32, bool)`

GetAngleOk returns a tuple with the Angle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAngle

`func (o *EdgeLabelPosition) SetAngle(v float32)`

SetAngle sets Angle field to given value.

### HasAngle

`func (o *EdgeLabelPosition) HasAngle() bool`

HasAngle returns a boolean if a field has been set.

### GetOptions

`func (o *EdgeLabelPosition) GetOptions() EdgeLabelPositionOneOfOptions`

GetOptions returns the Options field if non-nil, zero value otherwise.

### GetOptionsOk

`func (o *EdgeLabelPosition) GetOptionsOk() (*EdgeLabelPositionOneOfOptions, bool)`

GetOptionsOk returns a tuple with the Options field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOptions

`func (o *EdgeLabelPosition) SetOptions(v EdgeLabelPositionOneOfOptions)`

SetOptions sets Options field to given value.

### HasOptions

`func (o *EdgeLabelPosition) HasOptions() bool`

HasOptions returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


