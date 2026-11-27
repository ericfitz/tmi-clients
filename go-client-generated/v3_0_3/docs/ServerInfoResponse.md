# ServerInfoResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TlsEnabled** | **bool** | Whether the server itself terminates TLS | 
**TlsSubjectName** | Pointer to **string** | Subject name of the server TLS certificate; omitted when empty | [optional] 
**WebsocketBaseUrl** | **string** | WebSocket base URL derived from the host the client used and the client-facing scheme (wss when the request arrived over TLS directly or through a TLS-terminating proxy that sets X-Forwarded-Proto, otherwise ws) | 

## Methods

### NewServerInfoResponse

`func NewServerInfoResponse(tlsEnabled bool, websocketBaseUrl string, ) *ServerInfoResponse`

NewServerInfoResponse instantiates a new ServerInfoResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewServerInfoResponseWithDefaults

`func NewServerInfoResponseWithDefaults() *ServerInfoResponse`

NewServerInfoResponseWithDefaults instantiates a new ServerInfoResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTlsEnabled

`func (o *ServerInfoResponse) GetTlsEnabled() bool`

GetTlsEnabled returns the TlsEnabled field if non-nil, zero value otherwise.

### GetTlsEnabledOk

`func (o *ServerInfoResponse) GetTlsEnabledOk() (*bool, bool)`

GetTlsEnabledOk returns a tuple with the TlsEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTlsEnabled

`func (o *ServerInfoResponse) SetTlsEnabled(v bool)`

SetTlsEnabled sets TlsEnabled field to given value.


### GetTlsSubjectName

`func (o *ServerInfoResponse) GetTlsSubjectName() string`

GetTlsSubjectName returns the TlsSubjectName field if non-nil, zero value otherwise.

### GetTlsSubjectNameOk

`func (o *ServerInfoResponse) GetTlsSubjectNameOk() (*string, bool)`

GetTlsSubjectNameOk returns a tuple with the TlsSubjectName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTlsSubjectName

`func (o *ServerInfoResponse) SetTlsSubjectName(v string)`

SetTlsSubjectName sets TlsSubjectName field to given value.

### HasTlsSubjectName

`func (o *ServerInfoResponse) HasTlsSubjectName() bool`

HasTlsSubjectName returns a boolean if a field has been set.

### GetWebsocketBaseUrl

`func (o *ServerInfoResponse) GetWebsocketBaseUrl() string`

GetWebsocketBaseUrl returns the WebsocketBaseUrl field if non-nil, zero value otherwise.

### GetWebsocketBaseUrlOk

`func (o *ServerInfoResponse) GetWebsocketBaseUrlOk() (*string, bool)`

GetWebsocketBaseUrlOk returns a tuple with the WebsocketBaseUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWebsocketBaseUrl

`func (o *ServerInfoResponse) SetWebsocketBaseUrl(v string)`

SetWebsocketBaseUrl sets WebsocketBaseUrl field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


