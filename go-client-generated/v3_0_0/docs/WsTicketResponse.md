# WsTicketResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Ticket** | **string** | Short-lived, single-use authentication ticket for WebSocket connection | 

## Methods

### NewWsTicketResponse

`func NewWsTicketResponse(ticket string, ) *WsTicketResponse`

NewWsTicketResponse instantiates a new WsTicketResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWsTicketResponseWithDefaults

`func NewWsTicketResponseWithDefaults() *WsTicketResponse`

NewWsTicketResponseWithDefaults instantiates a new WsTicketResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTicket

`func (o *WsTicketResponse) GetTicket() string`

GetTicket returns the Ticket field if non-nil, zero value otherwise.

### GetTicketOk

`func (o *WsTicketResponse) GetTicketOk() (*string, bool)`

GetTicketOk returns a tuple with the Ticket field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTicket

`func (o *WsTicketResponse) SetTicket(v string)`

SetTicket sets Ticket field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


