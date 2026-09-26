# EdgeConnector

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Connector style name | 
**Args** | Pointer to [**EdgeConnectorOneOfArgs**](EdgeConnectorOneOfArgs.md) |  | [optional] 

## Methods

### NewEdgeConnector

`func NewEdgeConnector(name string, ) *EdgeConnector`

NewEdgeConnector instantiates a new EdgeConnector object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEdgeConnectorWithDefaults

`func NewEdgeConnectorWithDefaults() *EdgeConnector`

NewEdgeConnectorWithDefaults instantiates a new EdgeConnector object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *EdgeConnector) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *EdgeConnector) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *EdgeConnector) SetName(v string)`

SetName sets Name field to given value.


### GetArgs

`func (o *EdgeConnector) GetArgs() EdgeConnectorOneOfArgs`

GetArgs returns the Args field if non-nil, zero value otherwise.

### GetArgsOk

`func (o *EdgeConnector) GetArgsOk() (*EdgeConnectorOneOfArgs, bool)`

GetArgsOk returns a tuple with the Args field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArgs

`func (o *EdgeConnector) SetArgs(v EdgeConnectorOneOfArgs)`

SetArgs sets Args field to given value.

### HasArgs

`func (o *EdgeConnector) HasArgs() bool`

HasArgs returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


