# TmiJsClient.CollaborationApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createDiagramCollaborationSession**](CollaborationApi.md#createDiagramCollaborationSession) | **POST** /threat_models/{threat_model_id}/diagrams/{diagram_id}/collaborate | Create diagram collaboration session
[**endDiagramCollaborationSession**](CollaborationApi.md#endDiagramCollaborationSession) | **DELETE** /threat_models/{threat_model_id}/diagrams/{diagram_id}/collaborate | End diagram collaboration session
[**getCurrentUserSessions**](CollaborationApi.md#getCurrentUserSessions) | **GET** /me/sessions | List active collaboration sessions
[**getDiagramCollaborationSession**](CollaborationApi.md#getDiagramCollaborationSession) | **GET** /threat_models/{threat_model_id}/diagrams/{diagram_id}/collaborate | Get diagram collaboration session

<a name="createDiagramCollaborationSession"></a>
# **createDiagramCollaborationSession**
> CollaborationSession createDiagramCollaborationSession(threatModelId, diagramId)

Create diagram collaboration session

Creates a new collaboration session for real-time diagram editing. Only one collaboration session can exist per diagram at a time. If a session already exists, returns 409 with a link to join the existing session.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.CollaborationApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let diagramId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Diagram identifier

apiInstance.createDiagramCollaborationSession(threatModelId, diagramId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **diagramId** | [**String**](.md)| Diagram identifier | 

### Return type

[**CollaborationSession**](CollaborationSession.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="endDiagramCollaborationSession"></a>
# **endDiagramCollaborationSession**
> endDiagramCollaborationSession(threatModelId, diagramId)

End diagram collaboration session

Terminates the active collaboration session for a diagram

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.CollaborationApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let diagramId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Diagram identifier

apiInstance.endDiagramCollaborationSession(threatModelId, diagramId).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **diagramId** | [**String**](.md)| Diagram identifier | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getCurrentUserSessions"></a>
# **getCurrentUserSessions**
> Object getCurrentUserSessions()

List active collaboration sessions

Returns all currently active collaboration sessions for diagrams. Clients can use this endpoint to discover existing sessions before connecting via WebSocket.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.CollaborationApi();
apiInstance.getCurrentUserSessions().then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters
This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getDiagramCollaborationSession"></a>
# **getDiagramCollaborationSession**
> CollaborationSession getDiagramCollaborationSession(threatModelId, diagramId)

Get diagram collaboration session

Retrieves the current collaboration session details for a diagram. The session payload indicates who has been authorized to the session, not who is currently active in the WebSocket session. The 200 status indicates successful retrieval - clients must NOT evaluate the payload to determine session status.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.CollaborationApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let diagramId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Diagram identifier

apiInstance.getDiagramCollaborationSession(threatModelId, diagramId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **diagramId** | [**String**](.md)| Diagram identifier | 

### Return type

[**CollaborationSession**](CollaborationSession.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

