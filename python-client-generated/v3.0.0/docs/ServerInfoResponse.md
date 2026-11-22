# ServerInfoResponse

Server TLS and WebSocket connection information for clients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tls_enabled** | **bool** | Whether the server itself terminates TLS | 
**tls_subject_name** | **str** | Subject name of the server TLS certificate; omitted when empty | [optional] 
**websocket_base_url** | **str** | WebSocket base URL derived from the host the client used and the client-facing scheme (wss when the request arrived over TLS directly or through a TLS-terminating proxy that sets X-Forwarded-Proto, otherwise ws) | 

## Example

```python
from tmi_client.models.server_info_response import ServerInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServerInfoResponse from a JSON string
server_info_response_instance = ServerInfoResponse.from_json(json)
# print the JSON string representation of the object
print(ServerInfoResponse.to_json())

# convert the object into a dict
server_info_response_dict = server_info_response_instance.to_dict()
# create an instance of ServerInfoResponse from a dict
server_info_response_from_dict = ServerInfoResponse.from_dict(server_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


