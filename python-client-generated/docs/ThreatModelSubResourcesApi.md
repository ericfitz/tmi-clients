# tmi_client.ThreatModelSubResourcesApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_create_diagram_metadata**](ThreatModelSubResourcesApi.md#bulk_create_diagram_metadata) | **POST** /threat_models/{threat_model_id}/diagrams/{diagram_id}/metadata/bulk | Bulk create diagram metadata
[**bulk_create_document_metadata**](ThreatModelSubResourcesApi.md#bulk_create_document_metadata) | **POST** /threat_models/{threat_model_id}/documents/{document_id}/metadata/bulk | Bulk create document metadata
[**bulk_create_note_metadata**](ThreatModelSubResourcesApi.md#bulk_create_note_metadata) | **POST** /threat_models/{threat_model_id}/notes/{note_id}/metadata/bulk | Bulk create note metadata
[**bulk_create_repository_metadata**](ThreatModelSubResourcesApi.md#bulk_create_repository_metadata) | **POST** /threat_models/{threat_model_id}/repositories/{repository_id}/metadata/bulk | Bulk create source metadata
[**bulk_create_threat_metadata**](ThreatModelSubResourcesApi.md#bulk_create_threat_metadata) | **POST** /threat_models/{threat_model_id}/threats/{threat_id}/metadata/bulk | Bulk create threat metadata
[**bulk_create_threat_model_asset_metadata**](ThreatModelSubResourcesApi.md#bulk_create_threat_model_asset_metadata) | **POST** /threat_models/{threat_model_id}/assets/{asset_id}/metadata/bulk | Bulk create asset metadata
[**bulk_create_threat_model_assets**](ThreatModelSubResourcesApi.md#bulk_create_threat_model_assets) | **POST** /threat_models/{threat_model_id}/assets/bulk | Bulk create assets
[**bulk_create_threat_model_documents**](ThreatModelSubResourcesApi.md#bulk_create_threat_model_documents) | **POST** /threat_models/{threat_model_id}/documents/bulk | Bulk create documents
[**bulk_create_threat_model_metadata**](ThreatModelSubResourcesApi.md#bulk_create_threat_model_metadata) | **POST** /threat_models/{threat_model_id}/metadata/bulk | Bulk create threat model metadata
[**bulk_create_threat_model_repositories**](ThreatModelSubResourcesApi.md#bulk_create_threat_model_repositories) | **POST** /threat_models/{threat_model_id}/repositories/bulk | Bulk create sources
[**bulk_create_threat_model_threats**](ThreatModelSubResourcesApi.md#bulk_create_threat_model_threats) | **POST** /threat_models/{threat_model_id}/threats/bulk | Bulk create threats
[**bulk_replace_diagram_metadata**](ThreatModelSubResourcesApi.md#bulk_replace_diagram_metadata) | **PUT** /threat_models/{threat_model_id}/diagrams/{diagram_id}/metadata/bulk | Bulk replace diagram metadata
[**bulk_replace_document_metadata**](ThreatModelSubResourcesApi.md#bulk_replace_document_metadata) | **PUT** /threat_models/{threat_model_id}/documents/{document_id}/metadata/bulk | Bulk replace document metadata
[**bulk_replace_note_metadata**](ThreatModelSubResourcesApi.md#bulk_replace_note_metadata) | **PUT** /threat_models/{threat_model_id}/notes/{note_id}/metadata/bulk | Bulk replace note metadata
[**bulk_replace_repository_metadata**](ThreatModelSubResourcesApi.md#bulk_replace_repository_metadata) | **PUT** /threat_models/{threat_model_id}/repositories/{repository_id}/metadata/bulk | Bulk replace repository metadata
[**bulk_replace_threat_metadata**](ThreatModelSubResourcesApi.md#bulk_replace_threat_metadata) | **PUT** /threat_models/{threat_model_id}/threats/{threat_id}/metadata/bulk | Bulk replace threat metadata
[**bulk_replace_threat_model_asset_metadata**](ThreatModelSubResourcesApi.md#bulk_replace_threat_model_asset_metadata) | **PUT** /threat_models/{threat_model_id}/assets/{asset_id}/metadata/bulk | Bulk replace asset metadata
[**bulk_replace_threat_model_metadata**](ThreatModelSubResourcesApi.md#bulk_replace_threat_model_metadata) | **PUT** /threat_models/{threat_model_id}/metadata/bulk | Bulk replace threat model metadata
[**bulk_update_threat_model_threats**](ThreatModelSubResourcesApi.md#bulk_update_threat_model_threats) | **PUT** /threat_models/{threat_model_id}/threats/bulk | Bulk update threats
[**bulk_upsert_diagram_metadata**](ThreatModelSubResourcesApi.md#bulk_upsert_diagram_metadata) | **PATCH** /threat_models/{threat_model_id}/diagrams/{diagram_id}/metadata/bulk | Bulk upsert diagram metadata
[**bulk_upsert_document_metadata**](ThreatModelSubResourcesApi.md#bulk_upsert_document_metadata) | **PATCH** /threat_models/{threat_model_id}/documents/{document_id}/metadata/bulk | Bulk upsert document metadata
[**bulk_upsert_note_metadata**](ThreatModelSubResourcesApi.md#bulk_upsert_note_metadata) | **PATCH** /threat_models/{threat_model_id}/notes/{note_id}/metadata/bulk | Bulk upsert note metadata
[**bulk_upsert_repository_metadata**](ThreatModelSubResourcesApi.md#bulk_upsert_repository_metadata) | **PATCH** /threat_models/{threat_model_id}/repositories/{repository_id}/metadata/bulk | Bulk upsert repository metadata
[**bulk_upsert_threat_metadata**](ThreatModelSubResourcesApi.md#bulk_upsert_threat_metadata) | **PATCH** /threat_models/{threat_model_id}/threats/{threat_id}/metadata/bulk | Bulk upsert threat metadata
[**bulk_upsert_threat_model_asset_metadata**](ThreatModelSubResourcesApi.md#bulk_upsert_threat_model_asset_metadata) | **PATCH** /threat_models/{threat_model_id}/assets/{asset_id}/metadata/bulk | Bulk upsert asset metadata
[**bulk_upsert_threat_model_assets**](ThreatModelSubResourcesApi.md#bulk_upsert_threat_model_assets) | **PUT** /threat_models/{threat_model_id}/assets/bulk | Bulk upsert assets
[**bulk_upsert_threat_model_documents**](ThreatModelSubResourcesApi.md#bulk_upsert_threat_model_documents) | **PUT** /threat_models/{threat_model_id}/documents/bulk | Bulk upsert documents
[**bulk_upsert_threat_model_metadata**](ThreatModelSubResourcesApi.md#bulk_upsert_threat_model_metadata) | **PATCH** /threat_models/{threat_model_id}/metadata/bulk | Bulk upsert threat model metadata
[**bulk_upsert_threat_model_repositories**](ThreatModelSubResourcesApi.md#bulk_upsert_threat_model_repositories) | **PUT** /threat_models/{threat_model_id}/repositories/bulk | Bulk upsert repositories
[**create_diagram_metadata**](ThreatModelSubResourcesApi.md#create_diagram_metadata) | **POST** /threat_models/{threat_model_id}/diagrams/{diagram_id}/metadata | Create diagram metadata
[**create_document_metadata**](ThreatModelSubResourcesApi.md#create_document_metadata) | **POST** /threat_models/{threat_model_id}/documents/{document_id}/metadata | Create document metadata
[**create_note_metadata**](ThreatModelSubResourcesApi.md#create_note_metadata) | **POST** /threat_models/{threat_model_id}/notes/{note_id}/metadata | Create note metadata
[**create_repository_metadata**](ThreatModelSubResourcesApi.md#create_repository_metadata) | **POST** /threat_models/{threat_model_id}/repositories/{repository_id}/metadata | Create source metadata
[**create_threat_metadata**](ThreatModelSubResourcesApi.md#create_threat_metadata) | **POST** /threat_models/{threat_model_id}/threats/{threat_id}/metadata | Create threat metadata
[**create_threat_model_asset**](ThreatModelSubResourcesApi.md#create_threat_model_asset) | **POST** /threat_models/{threat_model_id}/assets | Create a new asset
[**create_threat_model_asset_metadata**](ThreatModelSubResourcesApi.md#create_threat_model_asset_metadata) | **POST** /threat_models/{threat_model_id}/assets/{asset_id}/metadata | Add metadata to an asset
[**create_threat_model_diagram**](ThreatModelSubResourcesApi.md#create_threat_model_diagram) | **POST** /threat_models/{threat_model_id}/diagrams | Create a new diagram
[**create_threat_model_document**](ThreatModelSubResourcesApi.md#create_threat_model_document) | **POST** /threat_models/{threat_model_id}/documents | Create a new document
[**create_threat_model_metadata**](ThreatModelSubResourcesApi.md#create_threat_model_metadata) | **POST** /threat_models/{threat_model_id}/metadata | Create threat model metadata
[**create_threat_model_note**](ThreatModelSubResourcesApi.md#create_threat_model_note) | **POST** /threat_models/{threat_model_id}/notes | Create a new note
[**create_threat_model_repository**](ThreatModelSubResourcesApi.md#create_threat_model_repository) | **POST** /threat_models/{threat_model_id}/repositories | Create a new source reference
[**create_threat_model_threat**](ThreatModelSubResourcesApi.md#create_threat_model_threat) | **POST** /threat_models/{threat_model_id}/threats | Create a new threat
[**delete_diagram_metadata_by_key**](ThreatModelSubResourcesApi.md#delete_diagram_metadata_by_key) | **DELETE** /threat_models/{threat_model_id}/diagrams/{diagram_id}/metadata/{key} | Delete diagram metadata by key
[**delete_document_metadata_by_key**](ThreatModelSubResourcesApi.md#delete_document_metadata_by_key) | **DELETE** /threat_models/{threat_model_id}/documents/{document_id}/metadata/{key} | Delete document metadata by key
[**delete_note_metadata_by_key**](ThreatModelSubResourcesApi.md#delete_note_metadata_by_key) | **DELETE** /threat_models/{threat_model_id}/notes/{note_id}/metadata/{key} | Delete note metadata by key
[**delete_repository_metadata_by_key**](ThreatModelSubResourcesApi.md#delete_repository_metadata_by_key) | **DELETE** /threat_models/{threat_model_id}/repositories/{repository_id}/metadata/{key} | Delete source metadata by key
[**delete_threat_metadata_by_key**](ThreatModelSubResourcesApi.md#delete_threat_metadata_by_key) | **DELETE** /threat_models/{threat_model_id}/threats/{threat_id}/metadata/{key} | Delete threat metadata by key
[**delete_threat_model_asset**](ThreatModelSubResourcesApi.md#delete_threat_model_asset) | **DELETE** /threat_models/{threat_model_id}/assets/{asset_id} | Delete an asset
[**delete_threat_model_asset_metadata**](ThreatModelSubResourcesApi.md#delete_threat_model_asset_metadata) | **DELETE** /threat_models/{threat_model_id}/assets/{asset_id}/metadata/{key} | Delete asset metadata
[**delete_threat_model_diagram**](ThreatModelSubResourcesApi.md#delete_threat_model_diagram) | **DELETE** /threat_models/{threat_model_id}/diagrams/{diagram_id} | Delete a diagram
[**delete_threat_model_document**](ThreatModelSubResourcesApi.md#delete_threat_model_document) | **DELETE** /threat_models/{threat_model_id}/documents/{document_id} | Delete a document
[**delete_threat_model_metadata_by_key**](ThreatModelSubResourcesApi.md#delete_threat_model_metadata_by_key) | **DELETE** /threat_models/{threat_model_id}/metadata/{key} | Delete threat model metadata by key
[**delete_threat_model_note**](ThreatModelSubResourcesApi.md#delete_threat_model_note) | **DELETE** /threat_models/{threat_model_id}/notes/{note_id} | Delete a note
[**delete_threat_model_repository**](ThreatModelSubResourcesApi.md#delete_threat_model_repository) | **DELETE** /threat_models/{threat_model_id}/repositories/{repository_id} | Delete a source reference
[**delete_threat_model_threat**](ThreatModelSubResourcesApi.md#delete_threat_model_threat) | **DELETE** /threat_models/{threat_model_id}/threats/{threat_id} | Delete a threat
[**get_diagram_metadata**](ThreatModelSubResourcesApi.md#get_diagram_metadata) | **GET** /threat_models/{threat_model_id}/diagrams/{diagram_id}/metadata | Get diagram metadata
[**get_diagram_metadata_by_key**](ThreatModelSubResourcesApi.md#get_diagram_metadata_by_key) | **GET** /threat_models/{threat_model_id}/diagrams/{diagram_id}/metadata/{key} | Get diagram metadata by key
[**get_diagram_model**](ThreatModelSubResourcesApi.md#get_diagram_model) | **GET** /threat_models/{threat_model_id}/diagrams/{diagram_id}/model | Get minimal diagram model for automated analysis
[**get_document_metadata**](ThreatModelSubResourcesApi.md#get_document_metadata) | **GET** /threat_models/{threat_model_id}/documents/{document_id}/metadata | Get document metadata
[**get_document_metadata_by_key**](ThreatModelSubResourcesApi.md#get_document_metadata_by_key) | **GET** /threat_models/{threat_model_id}/documents/{document_id}/metadata/{key} | Get document metadata by key
[**get_note_metadata**](ThreatModelSubResourcesApi.md#get_note_metadata) | **GET** /threat_models/{threat_model_id}/notes/{note_id}/metadata | Get note metadata
[**get_note_metadata_by_key**](ThreatModelSubResourcesApi.md#get_note_metadata_by_key) | **GET** /threat_models/{threat_model_id}/notes/{note_id}/metadata/{key} | Get note metadata by key
[**get_repository_metadata**](ThreatModelSubResourcesApi.md#get_repository_metadata) | **GET** /threat_models/{threat_model_id}/repositories/{repository_id}/metadata | Get source metadata
[**get_repository_metadata_by_key**](ThreatModelSubResourcesApi.md#get_repository_metadata_by_key) | **GET** /threat_models/{threat_model_id}/repositories/{repository_id}/metadata/{key} | Get source metadata by key
[**get_threat_metadata**](ThreatModelSubResourcesApi.md#get_threat_metadata) | **GET** /threat_models/{threat_model_id}/threats/{threat_id}/metadata | Get threat metadata
[**get_threat_metadata_by_key**](ThreatModelSubResourcesApi.md#get_threat_metadata_by_key) | **GET** /threat_models/{threat_model_id}/threats/{threat_id}/metadata/{key} | Get threat metadata by key
[**get_threat_model_asset**](ThreatModelSubResourcesApi.md#get_threat_model_asset) | **GET** /threat_models/{threat_model_id}/assets/{asset_id} | Get a specific asset
[**get_threat_model_asset_metadata**](ThreatModelSubResourcesApi.md#get_threat_model_asset_metadata) | **GET** /threat_models/{threat_model_id}/assets/{asset_id}/metadata | Get all metadata for an asset
[**get_threat_model_asset_metadata_by_key**](ThreatModelSubResourcesApi.md#get_threat_model_asset_metadata_by_key) | **GET** /threat_models/{threat_model_id}/assets/{asset_id}/metadata/{key} | Get specific metadata for an asset
[**get_threat_model_assets**](ThreatModelSubResourcesApi.md#get_threat_model_assets) | **GET** /threat_models/{threat_model_id}/assets | List assets in a threat model
[**get_threat_model_diagram**](ThreatModelSubResourcesApi.md#get_threat_model_diagram) | **GET** /threat_models/{threat_model_id}/diagrams/{diagram_id} | Get a specific diagram
[**get_threat_model_diagrams**](ThreatModelSubResourcesApi.md#get_threat_model_diagrams) | **GET** /threat_models/{threat_model_id}/diagrams | List threat model diagrams
[**get_threat_model_document**](ThreatModelSubResourcesApi.md#get_threat_model_document) | **GET** /threat_models/{threat_model_id}/documents/{document_id} | Get a specific document
[**get_threat_model_documents**](ThreatModelSubResourcesApi.md#get_threat_model_documents) | **GET** /threat_models/{threat_model_id}/documents | List documents in a threat model
[**get_threat_model_metadata**](ThreatModelSubResourcesApi.md#get_threat_model_metadata) | **GET** /threat_models/{threat_model_id}/metadata | Get threat model metadata
[**get_threat_model_metadata_by_key**](ThreatModelSubResourcesApi.md#get_threat_model_metadata_by_key) | **GET** /threat_models/{threat_model_id}/metadata/{key} | Get threat model metadata by key
[**get_threat_model_note**](ThreatModelSubResourcesApi.md#get_threat_model_note) | **GET** /threat_models/{threat_model_id}/notes/{note_id} | Get a specific note
[**get_threat_model_notes**](ThreatModelSubResourcesApi.md#get_threat_model_notes) | **GET** /threat_models/{threat_model_id}/notes | List notes in a threat model
[**get_threat_model_repositories**](ThreatModelSubResourcesApi.md#get_threat_model_repositories) | **GET** /threat_models/{threat_model_id}/repositories | List sources in a threat model
[**get_threat_model_repository**](ThreatModelSubResourcesApi.md#get_threat_model_repository) | **GET** /threat_models/{threat_model_id}/repositories/{repository_id} | Get a specific source reference
[**get_threat_model_threat**](ThreatModelSubResourcesApi.md#get_threat_model_threat) | **GET** /threat_models/{threat_model_id}/threats/{threat_id} | Get a specific threat
[**get_threat_model_threats**](ThreatModelSubResourcesApi.md#get_threat_model_threats) | **GET** /threat_models/{threat_model_id}/threats | List threats in a threat model
[**patch_threat_model_diagram**](ThreatModelSubResourcesApi.md#patch_threat_model_diagram) | **PATCH** /threat_models/{threat_model_id}/diagrams/{diagram_id} | Partially update a diagram
[**patch_threat_model_threat**](ThreatModelSubResourcesApi.md#patch_threat_model_threat) | **PATCH** /threat_models/{threat_model_id}/threats/{threat_id} | Partially update a threat
[**restore_asset**](ThreatModelSubResourcesApi.md#restore_asset) | **POST** /threat_models/{threat_model_id}/assets/{asset_id}/restore | Restore a soft-deleted asset
[**restore_diagram**](ThreatModelSubResourcesApi.md#restore_diagram) | **POST** /threat_models/{threat_model_id}/diagrams/{diagram_id}/restore | Restore a soft-deleted diagram
[**restore_document**](ThreatModelSubResourcesApi.md#restore_document) | **POST** /threat_models/{threat_model_id}/documents/{document_id}/restore | Restore a soft-deleted document
[**restore_note**](ThreatModelSubResourcesApi.md#restore_note) | **POST** /threat_models/{threat_model_id}/notes/{note_id}/restore | Restore a soft-deleted note
[**restore_repository**](ThreatModelSubResourcesApi.md#restore_repository) | **POST** /threat_models/{threat_model_id}/repositories/{repository_id}/restore | Restore a soft-deleted repository
[**restore_threat**](ThreatModelSubResourcesApi.md#restore_threat) | **POST** /threat_models/{threat_model_id}/threats/{threat_id}/restore | Restore a soft-deleted threat
[**update_diagram_metadata_by_key**](ThreatModelSubResourcesApi.md#update_diagram_metadata_by_key) | **PUT** /threat_models/{threat_model_id}/diagrams/{diagram_id}/metadata/{key} | Update diagram metadata by key
[**update_document_metadata_by_key**](ThreatModelSubResourcesApi.md#update_document_metadata_by_key) | **PUT** /threat_models/{threat_model_id}/documents/{document_id}/metadata/{key} | Update document metadata by key
[**update_note_metadata_by_key**](ThreatModelSubResourcesApi.md#update_note_metadata_by_key) | **PUT** /threat_models/{threat_model_id}/notes/{note_id}/metadata/{key} | Update note metadata by key
[**update_repository_metadata_by_key**](ThreatModelSubResourcesApi.md#update_repository_metadata_by_key) | **PUT** /threat_models/{threat_model_id}/repositories/{repository_id}/metadata/{key} | Update source metadata by key
[**update_threat_metadata_by_key**](ThreatModelSubResourcesApi.md#update_threat_metadata_by_key) | **PUT** /threat_models/{threat_model_id}/threats/{threat_id}/metadata/{key} | Update threat metadata by key
[**update_threat_model_asset**](ThreatModelSubResourcesApi.md#update_threat_model_asset) | **PUT** /threat_models/{threat_model_id}/assets/{asset_id} | Update an asset
[**update_threat_model_asset_metadata**](ThreatModelSubResourcesApi.md#update_threat_model_asset_metadata) | **PUT** /threat_models/{threat_model_id}/assets/{asset_id}/metadata/{key} | Update asset metadata
[**update_threat_model_diagram**](ThreatModelSubResourcesApi.md#update_threat_model_diagram) | **PUT** /threat_models/{threat_model_id}/diagrams/{diagram_id} | Update a diagram
[**update_threat_model_document**](ThreatModelSubResourcesApi.md#update_threat_model_document) | **PUT** /threat_models/{threat_model_id}/documents/{document_id} | Update a document
[**update_threat_model_metadata_by_key**](ThreatModelSubResourcesApi.md#update_threat_model_metadata_by_key) | **PUT** /threat_models/{threat_model_id}/metadata/{key} | Update threat model metadata by key
[**update_threat_model_note**](ThreatModelSubResourcesApi.md#update_threat_model_note) | **PUT** /threat_models/{threat_model_id}/notes/{note_id} | Update a note
[**update_threat_model_repository**](ThreatModelSubResourcesApi.md#update_threat_model_repository) | **PUT** /threat_models/{threat_model_id}/repositories/{repository_id} | Update a source reference
[**update_threat_model_threat**](ThreatModelSubResourcesApi.md#update_threat_model_threat) | **PUT** /threat_models/{threat_model_id}/threats/{threat_id} | Update a threat


# **bulk_create_diagram_metadata**
> List[Metadata] bulk_create_diagram_metadata(threat_model_id, diagram_id, metadata)

Bulk create diagram metadata

Creates multiple metadata entries in a single operation for the specified diagram. Returns 409 Conflict if any of the specified keys already exist.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    diagram_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Diagram identifier
    metadata = [tmi_client.Metadata()] # List[Metadata] | Bulk metadata key-value pairs to create

    try:
        # Bulk create diagram metadata
        api_response = api_instance.bulk_create_diagram_metadata(threat_model_id, diagram_id, metadata)
        print("The response of ThreatModelSubResourcesApi->bulk_create_diagram_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->bulk_create_diagram_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **diagram_id** | **UUID**| Diagram identifier | 
 **metadata** | [**List[Metadata]**](Metadata.md)| Bulk metadata key-value pairs to create | 

### Return type

[**List[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Metadata entries created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**409** | Conflict - One or more metadata keys already exist for this entity |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_create_document_metadata**
> List[Metadata] bulk_create_document_metadata(threat_model_id, document_id, metadata)

Bulk create document metadata

Creates multiple metadata entries in a single operation for the specified document. Returns 409 Conflict if any of the specified keys already exist.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    document_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Document identifier
    metadata = [tmi_client.Metadata()] # List[Metadata] | Bulk metadata key-value pairs to create

    try:
        # Bulk create document metadata
        api_response = api_instance.bulk_create_document_metadata(threat_model_id, document_id, metadata)
        print("The response of ThreatModelSubResourcesApi->bulk_create_document_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->bulk_create_document_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **document_id** | **UUID**| Document identifier | 
 **metadata** | [**List[Metadata]**](Metadata.md)| Bulk metadata key-value pairs to create | 

### Return type

[**List[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Metadata entries created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**409** | Conflict - One or more metadata keys already exist for this entity |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_create_note_metadata**
> List[Metadata] bulk_create_note_metadata(threat_model_id, note_id, metadata)

Bulk create note metadata

Creates multiple metadata key-value pairs for the specified note. Returns 409 Conflict if any of the specified keys already exist.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    note_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Note identifier
    metadata = [tmi_client.Metadata()] # List[Metadata] | Bulk metadata key-value pairs to create

    try:
        # Bulk create note metadata
        api_response = api_instance.bulk_create_note_metadata(threat_model_id, note_id, metadata)
        print("The response of ThreatModelSubResourcesApi->bulk_create_note_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->bulk_create_note_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **note_id** | **UUID**| Note identifier | 
 **metadata** | [**List[Metadata]**](Metadata.md)| Bulk metadata key-value pairs to create | 

### Return type

[**List[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Metadata created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**409** | Conflict - One or more metadata keys already exist for this entity |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_create_repository_metadata**
> List[Metadata] bulk_create_repository_metadata(threat_model_id, repository_id, metadata)

Bulk create source metadata

Creates multiple metadata entries in a single operation for the specified source reference. Returns 409 Conflict if any of the specified keys already exist.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    repository_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Repository identifier
    metadata = [tmi_client.Metadata()] # List[Metadata] | Bulk metadata key-value pairs to create

    try:
        # Bulk create source metadata
        api_response = api_instance.bulk_create_repository_metadata(threat_model_id, repository_id, metadata)
        print("The response of ThreatModelSubResourcesApi->bulk_create_repository_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->bulk_create_repository_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **repository_id** | **UUID**| Repository identifier | 
 **metadata** | [**List[Metadata]**](Metadata.md)| Bulk metadata key-value pairs to create | 

### Return type

[**List[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Metadata entries created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**409** | Conflict - One or more metadata keys already exist for this entity |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_create_threat_metadata**
> List[Metadata] bulk_create_threat_metadata(threat_model_id, threat_id, metadata)

Bulk create threat metadata

Creates multiple metadata entries in a single operation for the specified threat. Returns 409 Conflict if any of the specified keys already exist.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    threat_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat identifier
    metadata = [tmi_client.Metadata()] # List[Metadata] | Bulk metadata key-value pairs to create

    try:
        # Bulk create threat metadata
        api_response = api_instance.bulk_create_threat_metadata(threat_model_id, threat_id, metadata)
        print("The response of ThreatModelSubResourcesApi->bulk_create_threat_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->bulk_create_threat_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **threat_id** | **UUID**| Threat identifier | 
 **metadata** | [**List[Metadata]**](Metadata.md)| Bulk metadata key-value pairs to create | 

### Return type

[**List[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Metadata entries created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**409** | Conflict - One or more metadata keys already exist for this entity |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_create_threat_model_asset_metadata**
> List[Metadata] bulk_create_threat_model_asset_metadata(threat_model_id, asset_id, metadata)

Bulk create asset metadata

Creates multiple metadata key-value pairs for the specified asset. Returns 409 Conflict if any of the specified keys already exist.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    asset_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Asset identifier
    metadata = [tmi_client.Metadata()] # List[Metadata] | Bulk metadata key-value pairs to create

    try:
        # Bulk create asset metadata
        api_response = api_instance.bulk_create_threat_model_asset_metadata(threat_model_id, asset_id, metadata)
        print("The response of ThreatModelSubResourcesApi->bulk_create_threat_model_asset_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->bulk_create_threat_model_asset_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **asset_id** | **UUID**| Asset identifier | 
 **metadata** | [**List[Metadata]**](Metadata.md)| Bulk metadata key-value pairs to create | 

### Return type

[**List[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Metadata created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**409** | Conflict - One or more metadata keys already exist for this entity |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_create_threat_model_assets**
> List[Asset] bulk_create_threat_model_assets(threat_model_id, asset_base)

Bulk create assets

Creates multiple assets within the specified threat model (maximum 50 per request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.asset import Asset
from tmi_client.models.asset_base import AssetBase
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    asset_base = [{"name":"API Gateway","type":"software","description":"Main API gateway service"},{"name":"Redis Cache","type":"infrastructure","description":"Caching layer"}] # List[AssetBase] | Array of assets to create in bulk

    try:
        # Bulk create assets
        api_response = api_instance.bulk_create_threat_model_assets(threat_model_id, asset_base)
        print("The response of ThreatModelSubResourcesApi->bulk_create_threat_model_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->bulk_create_threat_model_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **asset_base** | [**List[AssetBase]**](AssetBase.md)| Array of assets to create in bulk | 

### Return type

[**List[Asset]**](Asset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Assets created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_create_threat_model_documents**
> List[Document] bulk_create_threat_model_documents(threat_model_id, document)

Bulk create documents

Creates multiple documents in a single operation for the specified threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.document import Document
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    document = [{"id":"770e8400-e29b-41d4-a716-446655440009","name":"Threat Model Report","uri":"https://docs.example.com/threat-report-v1.pdf","description":"Comprehensive threat assessment document","threat_model_id":"550e8400-e29b-41d4-a716-446655440000","created_at":"2025-01-10T09:00:00Z","modified_at":"2025-01-10T09:00:00Z"},{"name":"Security Requirements","description":"Security requirements and compliance standards","metadata":[{"key":"classification","value":"internal"},{"key":"department","value":"security"}],"uri":"https://docs.company.com/security.pdf","id":"550e8400-e29b-41d4-a716-446655440001"}] # List[Document] | Array of documents to create in bulk

    try:
        # Bulk create documents
        api_response = api_instance.bulk_create_threat_model_documents(threat_model_id, document)
        print("The response of ThreatModelSubResourcesApi->bulk_create_threat_model_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->bulk_create_threat_model_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **document** | [**List[Document]**](Document.md)| Array of documents to create in bulk | 

### Return type

[**List[Document]**](Document.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Documents created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_create_threat_model_metadata**
> List[Metadata] bulk_create_threat_model_metadata(threat_model_id, metadata)

Bulk create threat model metadata

Creates multiple metadata entries in a single operation for the specified threat model. Returns 409 Conflict if any of the specified keys already exist.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    metadata = [tmi_client.Metadata()] # List[Metadata] | Bulk metadata key-value pairs to create

    try:
        # Bulk create threat model metadata
        api_response = api_instance.bulk_create_threat_model_metadata(threat_model_id, metadata)
        print("The response of ThreatModelSubResourcesApi->bulk_create_threat_model_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->bulk_create_threat_model_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **metadata** | [**List[Metadata]**](Metadata.md)| Bulk metadata key-value pairs to create | 

### Return type

[**List[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Metadata entries created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**409** | Conflict - One or more metadata keys already exist for this entity |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_create_threat_model_repositories**
> List[Repository] bulk_create_threat_model_repositories(threat_model_id, repository)

Bulk create sources

Creates multiple source references in a single operation for the specified threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.repository import Repository
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    repository = [{"id":"990e8400-e29b-41d4-a716-446655440012","name":"API Repository","uri":"https://github.com/example/api","description":"Backend API source code","threat_model_id":"550e8400-e29b-41d4-a716-446655440000","created_at":"2025-01-12T08:00:00Z","modified_at":"2025-01-12T08:00:00Z"},{"name":"Database Connection Pool","description":"Database connection management","metadata":[{"key":"type","value":"infrastructure"},{"key":"criticality","value":"high"}],"uri":"https://github.com/company/repo/blob/main/db/pool.go","id":"550e8400-e29b-41d4-a716-446655440001"}] # List[Repository] | Array of repositorys to create in bulk

    try:
        # Bulk create sources
        api_response = api_instance.bulk_create_threat_model_repositories(threat_model_id, repository)
        print("The response of ThreatModelSubResourcesApi->bulk_create_threat_model_repositories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->bulk_create_threat_model_repositories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **repository** | [**List[Repository]**](Repository.md)| Array of repositorys to create in bulk | 

### Return type

[**List[Repository]**](Repository.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Sources created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_create_threat_model_threats**
> List[Threat] bulk_create_threat_model_threats(threat_model_id, threat)

Bulk create threats

Creates multiple threats in a single operation for the specified threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.threat import Threat
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    threat = [{"name":"SQL Injection Attack","description":"Attacker injects malicious SQL code through user input","metadata":[{"key":"category","value":"injection"},{"key":"stride","value":"tampering"}],"threat_type":["spoofing"]},{"name":"Cross-Site Scripting (XSS)","threat_type":["information-disclosure"],"description":"Malicious scripts executed in user's browser","severity":"Medium","status":"identified"}] # List[Threat] | Array of threats to create in bulk

    try:
        # Bulk create threats
        api_response = api_instance.bulk_create_threat_model_threats(threat_model_id, threat)
        print("The response of ThreatModelSubResourcesApi->bulk_create_threat_model_threats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->bulk_create_threat_model_threats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **threat** | [**List[Threat]**](Threat.md)| Array of threats to create in bulk | 

### Return type

[**List[Threat]**](Threat.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Threats created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_replace_diagram_metadata**
> List[Metadata] bulk_replace_diagram_metadata(threat_model_id, diagram_id, metadata)

Bulk replace diagram metadata

Replaces all metadata for the entity. All existing metadata is deleted and replaced with the provided set. To clear all metadata, send an empty array.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    diagram_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Diagram identifier
    metadata = [tmi_client.Metadata()] # List[Metadata] | Complete set of metadata key-value pairs to replace existing metadata

    try:
        # Bulk replace diagram metadata
        api_response = api_instance.bulk_replace_diagram_metadata(threat_model_id, diagram_id, metadata)
        print("The response of ThreatModelSubResourcesApi->bulk_replace_diagram_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->bulk_replace_diagram_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **diagram_id** | **UUID**| Diagram identifier | 
 **metadata** | [**List[Metadata]**](Metadata.md)| Complete set of metadata key-value pairs to replace existing metadata | 

### Return type

[**List[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata replaced successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_replace_document_metadata**
> List[Metadata] bulk_replace_document_metadata(threat_model_id, document_id, metadata)

Bulk replace document metadata

Replaces all metadata for the entity. All existing metadata is deleted and replaced with the provided set. To clear all metadata, send an empty array.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    document_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Document identifier
    metadata = [tmi_client.Metadata()] # List[Metadata] | Complete set of metadata key-value pairs to replace existing metadata

    try:
        # Bulk replace document metadata
        api_response = api_instance.bulk_replace_document_metadata(threat_model_id, document_id, metadata)
        print("The response of ThreatModelSubResourcesApi->bulk_replace_document_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->bulk_replace_document_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **document_id** | **UUID**| Document identifier | 
 **metadata** | [**List[Metadata]**](Metadata.md)| Complete set of metadata key-value pairs to replace existing metadata | 

### Return type

[**List[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata replaced successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_replace_note_metadata**
> List[Metadata] bulk_replace_note_metadata(threat_model_id, note_id, metadata)

Bulk replace note metadata

Replaces all metadata for the entity. All existing metadata is deleted and replaced with the provided set. To clear all metadata, send an empty array.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    note_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Note identifier
    metadata = [tmi_client.Metadata()] # List[Metadata] | Complete set of metadata key-value pairs to replace existing metadata

    try:
        # Bulk replace note metadata
        api_response = api_instance.bulk_replace_note_metadata(threat_model_id, note_id, metadata)
        print("The response of ThreatModelSubResourcesApi->bulk_replace_note_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->bulk_replace_note_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **note_id** | **UUID**| Note identifier | 
 **metadata** | [**List[Metadata]**](Metadata.md)| Complete set of metadata key-value pairs to replace existing metadata | 

### Return type

[**List[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata replaced successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_replace_repository_metadata**
> List[Metadata] bulk_replace_repository_metadata(threat_model_id, repository_id, metadata)

Bulk replace repository metadata

Replaces all metadata for the entity. All existing metadata is deleted and replaced with the provided set. To clear all metadata, send an empty array.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    repository_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Repository identifier
    metadata = [tmi_client.Metadata()] # List[Metadata] | Complete set of metadata key-value pairs to replace existing metadata

    try:
        # Bulk replace repository metadata
        api_response = api_instance.bulk_replace_repository_metadata(threat_model_id, repository_id, metadata)
        print("The response of ThreatModelSubResourcesApi->bulk_replace_repository_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->bulk_replace_repository_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **repository_id** | **UUID**| Repository identifier | 
 **metadata** | [**List[Metadata]**](Metadata.md)| Complete set of metadata key-value pairs to replace existing metadata | 

### Return type

[**List[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata replaced successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_replace_threat_metadata**
> List[Metadata] bulk_replace_threat_metadata(threat_model_id, threat_id, metadata)

Bulk replace threat metadata

Replaces all metadata for the entity. All existing metadata is deleted and replaced with the provided set. To clear all metadata, send an empty array.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    threat_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat identifier
    metadata = [tmi_client.Metadata()] # List[Metadata] | Complete set of metadata key-value pairs to replace existing metadata

    try:
        # Bulk replace threat metadata
        api_response = api_instance.bulk_replace_threat_metadata(threat_model_id, threat_id, metadata)
        print("The response of ThreatModelSubResourcesApi->bulk_replace_threat_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->bulk_replace_threat_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **threat_id** | **UUID**| Threat identifier | 
 **metadata** | [**List[Metadata]**](Metadata.md)| Complete set of metadata key-value pairs to replace existing metadata | 

### Return type

[**List[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata replaced successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_replace_threat_model_asset_metadata**
> List[Metadata] bulk_replace_threat_model_asset_metadata(threat_model_id, asset_id, metadata)

Bulk replace asset metadata

Replaces all metadata for the entity. All existing metadata is deleted and replaced with the provided set. To clear all metadata, send an empty array.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    asset_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Asset identifier
    metadata = [tmi_client.Metadata()] # List[Metadata] | Complete set of metadata key-value pairs to replace existing metadata

    try:
        # Bulk replace asset metadata
        api_response = api_instance.bulk_replace_threat_model_asset_metadata(threat_model_id, asset_id, metadata)
        print("The response of ThreatModelSubResourcesApi->bulk_replace_threat_model_asset_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->bulk_replace_threat_model_asset_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **asset_id** | **UUID**| Asset identifier | 
 **metadata** | [**List[Metadata]**](Metadata.md)| Complete set of metadata key-value pairs to replace existing metadata | 

### Return type

[**List[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata replaced successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_replace_threat_model_metadata**
> List[Metadata] bulk_replace_threat_model_metadata(threat_model_id, metadata)

Bulk replace threat model metadata

Replaces all metadata for the entity. All existing metadata is deleted and replaced with the provided set. To clear all metadata, send an empty array.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    metadata = [tmi_client.Metadata()] # List[Metadata] | Complete set of metadata key-value pairs to replace existing metadata

    try:
        # Bulk replace threat model metadata
        api_response = api_instance.bulk_replace_threat_model_metadata(threat_model_id, metadata)
        print("The response of ThreatModelSubResourcesApi->bulk_replace_threat_model_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->bulk_replace_threat_model_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **metadata** | [**List[Metadata]**](Metadata.md)| Complete set of metadata key-value pairs to replace existing metadata | 

### Return type

[**List[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata replaced successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update_threat_model_threats**
> List[Threat] bulk_update_threat_model_threats(threat_model_id, threat_bulk_update_item)

Bulk update threats

Updates multiple threats in a single operation for the specified threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.threat import Threat
from tmi_client.models.threat_bulk_update_item import ThreatBulkUpdateItem
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    threat_bulk_update_item = [{"id":"750e8400-e29b-41d4-a716-446655440001","name":"Updated SQL Injection Attack","description":"Updated description for SQL injection vulnerability","impact":"High","likelihood":"Low","risk_rating":"Medium","metadata":[{"key":"category","value":"injection"},{"key":"mitigation","value":"parameterized-queries"}],"threat_type":["tampering"]}] # List[ThreatBulkUpdateItem] | Array of threats to upsert in bulk

    try:
        # Bulk update threats
        api_response = api_instance.bulk_update_threat_model_threats(threat_model_id, threat_bulk_update_item)
        print("The response of ThreatModelSubResourcesApi->bulk_update_threat_model_threats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->bulk_update_threat_model_threats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **threat_bulk_update_item** | [**List[ThreatBulkUpdateItem]**](ThreatBulkUpdateItem.md)| Array of threats to upsert in bulk | 

### Return type

[**List[Threat]**](Threat.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Threats updated successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_upsert_diagram_metadata**
> List[Metadata] bulk_upsert_diagram_metadata(threat_model_id, diagram_id, metadata)

Bulk upsert diagram metadata

Creates or updates only the provided metadata keys. Keys not included in the request are left unchanged. This is a merge/upsert operation.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    diagram_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Diagram identifier
    metadata = [tmi_client.Metadata()] # List[Metadata] | Metadata key-value pairs to create or update (merge)

    try:
        # Bulk upsert diagram metadata
        api_response = api_instance.bulk_upsert_diagram_metadata(threat_model_id, diagram_id, metadata)
        print("The response of ThreatModelSubResourcesApi->bulk_upsert_diagram_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->bulk_upsert_diagram_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **diagram_id** | **UUID**| Diagram identifier | 
 **metadata** | [**List[Metadata]**](Metadata.md)| Metadata key-value pairs to create or update (merge) | 

### Return type

[**List[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata upserted successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_upsert_document_metadata**
> List[Metadata] bulk_upsert_document_metadata(threat_model_id, document_id, metadata)

Bulk upsert document metadata

Creates or updates only the provided metadata keys. Keys not included in the request are left unchanged. This is a merge/upsert operation.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    document_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Document identifier
    metadata = [tmi_client.Metadata()] # List[Metadata] | Metadata key-value pairs to create or update (merge)

    try:
        # Bulk upsert document metadata
        api_response = api_instance.bulk_upsert_document_metadata(threat_model_id, document_id, metadata)
        print("The response of ThreatModelSubResourcesApi->bulk_upsert_document_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->bulk_upsert_document_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **document_id** | **UUID**| Document identifier | 
 **metadata** | [**List[Metadata]**](Metadata.md)| Metadata key-value pairs to create or update (merge) | 

### Return type

[**List[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata upserted successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_upsert_note_metadata**
> List[Metadata] bulk_upsert_note_metadata(threat_model_id, note_id, metadata)

Bulk upsert note metadata

Creates or updates only the provided metadata keys. Keys not included in the request are left unchanged. This is a merge/upsert operation.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    note_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Note identifier
    metadata = [tmi_client.Metadata()] # List[Metadata] | Metadata key-value pairs to create or update (merge)

    try:
        # Bulk upsert note metadata
        api_response = api_instance.bulk_upsert_note_metadata(threat_model_id, note_id, metadata)
        print("The response of ThreatModelSubResourcesApi->bulk_upsert_note_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->bulk_upsert_note_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **note_id** | **UUID**| Note identifier | 
 **metadata** | [**List[Metadata]**](Metadata.md)| Metadata key-value pairs to create or update (merge) | 

### Return type

[**List[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata upserted successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_upsert_repository_metadata**
> List[Metadata] bulk_upsert_repository_metadata(threat_model_id, repository_id, metadata)

Bulk upsert repository metadata

Creates or updates only the provided metadata keys. Keys not included in the request are left unchanged. This is a merge/upsert operation.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    repository_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Repository identifier
    metadata = [tmi_client.Metadata()] # List[Metadata] | Metadata key-value pairs to create or update (merge)

    try:
        # Bulk upsert repository metadata
        api_response = api_instance.bulk_upsert_repository_metadata(threat_model_id, repository_id, metadata)
        print("The response of ThreatModelSubResourcesApi->bulk_upsert_repository_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->bulk_upsert_repository_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **repository_id** | **UUID**| Repository identifier | 
 **metadata** | [**List[Metadata]**](Metadata.md)| Metadata key-value pairs to create or update (merge) | 

### Return type

[**List[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata upserted successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_upsert_threat_metadata**
> List[Metadata] bulk_upsert_threat_metadata(threat_model_id, threat_id, metadata)

Bulk upsert threat metadata

Creates or updates only the provided metadata keys. Keys not included in the request are left unchanged. This is a merge/upsert operation.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    threat_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat identifier
    metadata = [tmi_client.Metadata()] # List[Metadata] | Metadata key-value pairs to create or update (merge)

    try:
        # Bulk upsert threat metadata
        api_response = api_instance.bulk_upsert_threat_metadata(threat_model_id, threat_id, metadata)
        print("The response of ThreatModelSubResourcesApi->bulk_upsert_threat_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->bulk_upsert_threat_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **threat_id** | **UUID**| Threat identifier | 
 **metadata** | [**List[Metadata]**](Metadata.md)| Metadata key-value pairs to create or update (merge) | 

### Return type

[**List[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata upserted successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_upsert_threat_model_asset_metadata**
> List[Metadata] bulk_upsert_threat_model_asset_metadata(threat_model_id, asset_id, metadata)

Bulk upsert asset metadata

Creates or updates only the provided metadata keys. Keys not included in the request are left unchanged. This is a merge/upsert operation.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    asset_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Asset identifier
    metadata = [tmi_client.Metadata()] # List[Metadata] | Metadata key-value pairs to create or update (merge)

    try:
        # Bulk upsert asset metadata
        api_response = api_instance.bulk_upsert_threat_model_asset_metadata(threat_model_id, asset_id, metadata)
        print("The response of ThreatModelSubResourcesApi->bulk_upsert_threat_model_asset_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->bulk_upsert_threat_model_asset_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **asset_id** | **UUID**| Asset identifier | 
 **metadata** | [**List[Metadata]**](Metadata.md)| Metadata key-value pairs to create or update (merge) | 

### Return type

[**List[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata upserted successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_upsert_threat_model_assets**
> List[Asset] bulk_upsert_threat_model_assets(threat_model_id, asset)

Bulk upsert assets

Create or update multiple assets in a single request

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.asset import Asset
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    asset = [{"id":"550e8400-e29b-41d4-a716-446655440001","name":"API Gateway Updated","type":"software","description":"Updated gateway service"}] # List[Asset] | Array of assets to upsert in bulk

    try:
        # Bulk upsert assets
        api_response = api_instance.bulk_upsert_threat_model_assets(threat_model_id, asset)
        print("The response of ThreatModelSubResourcesApi->bulk_upsert_threat_model_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->bulk_upsert_threat_model_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **asset** | [**List[Asset]**](Asset.md)| Array of assets to upsert in bulk | 

### Return type

[**List[Asset]**](Asset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Assets created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_upsert_threat_model_documents**
> List[Document] bulk_upsert_threat_model_documents(threat_model_id, document)

Bulk upsert documents

Create or update multiple documents in a single request

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.document import Document
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    document = [{"id":"770e8400-e29b-41d4-a716-446655440010","name":"Threat Model Report Updated","uri":"https://docs.example.com/threat-report-v2.pdf","description":"Updated threat assessment document","threat_model_id":"550e8400-e29b-41d4-a716-446655440000","created_at":"2025-01-10T09:00:00Z","modified_at":"2025-01-10T09:00:00Z"},{"name":"Security Requirements","description":"Security requirements and compliance standards","metadata":[{"key":"classification","value":"internal"},{"key":"department","value":"security"}],"uri":"https://docs.company.com/security.pdf","id":"550e8400-e29b-41d4-a716-446655440001"}] # List[Document] | Array of documents to upsert in bulk

    try:
        # Bulk upsert documents
        api_response = api_instance.bulk_upsert_threat_model_documents(threat_model_id, document)
        print("The response of ThreatModelSubResourcesApi->bulk_upsert_threat_model_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->bulk_upsert_threat_model_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **document** | [**List[Document]**](Document.md)| Array of documents to upsert in bulk | 

### Return type

[**List[Document]**](Document.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Documents created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_upsert_threat_model_metadata**
> List[Metadata] bulk_upsert_threat_model_metadata(threat_model_id, metadata)

Bulk upsert threat model metadata

Creates or updates only the provided metadata keys. Keys not included in the request are left unchanged. This is a merge/upsert operation.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    metadata = [tmi_client.Metadata()] # List[Metadata] | Metadata key-value pairs to create or update (merge)

    try:
        # Bulk upsert threat model metadata
        api_response = api_instance.bulk_upsert_threat_model_metadata(threat_model_id, metadata)
        print("The response of ThreatModelSubResourcesApi->bulk_upsert_threat_model_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->bulk_upsert_threat_model_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **metadata** | [**List[Metadata]**](Metadata.md)| Metadata key-value pairs to create or update (merge) | 

### Return type

[**List[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata upserted successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_upsert_threat_model_repositories**
> List[Repository] bulk_upsert_threat_model_repositories(threat_model_id, repository)

Bulk upsert repositories

Create or update multiple repositories in a single request

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.repository import Repository
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    repository = [{"id":"990e8400-e29b-41d4-a716-446655440013","name":"API Repository Updated","uri":"https://github.com/example/api-v2","description":"Updated backend API source code","threat_model_id":"550e8400-e29b-41d4-a716-446655440000","created_at":"2025-01-12T08:00:00Z","modified_at":"2025-01-12T08:00:00Z"},{"name":"Database Connection Pool","description":"Database connection management","metadata":[{"key":"type","value":"infrastructure"},{"key":"criticality","value":"high"}],"uri":"https://github.com/company/repo/blob/main/db/pool.go","id":"550e8400-e29b-41d4-a716-446655440001"}] # List[Repository] | Array of repositorys to upsert in bulk

    try:
        # Bulk upsert repositories
        api_response = api_instance.bulk_upsert_threat_model_repositories(threat_model_id, repository)
        print("The response of ThreatModelSubResourcesApi->bulk_upsert_threat_model_repositories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->bulk_upsert_threat_model_repositories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **repository** | [**List[Repository]**](Repository.md)| Array of repositorys to upsert in bulk | 

### Return type

[**List[Repository]**](Repository.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Sources created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_diagram_metadata**
> Metadata create_diagram_metadata(threat_model_id, diagram_id, metadata)

Create diagram metadata

Creates a new metadata entry for the specified diagram. Returns 409 Conflict if the key already exists.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    diagram_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Diagram identifier
    metadata = tmi_client.Metadata() # Metadata | Metadata key-value pair to create

    try:
        # Create diagram metadata
        api_response = api_instance.create_diagram_metadata(threat_model_id, diagram_id, metadata)
        print("The response of ThreatModelSubResourcesApi->create_diagram_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->create_diagram_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **diagram_id** | **UUID**| Diagram identifier | 
 **metadata** | [**Metadata**](Metadata.md)| Metadata key-value pair to create | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Metadata entry created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**409** | Conflict - Metadata key already exists for this entity |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_document_metadata**
> Metadata create_document_metadata(threat_model_id, document_id, metadata)

Create document metadata

Creates new metadata entry for the specified document. Returns 409 Conflict if the key already exists.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    document_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Document identifier
    metadata = tmi_client.Metadata() # Metadata | Metadata key-value pair to create

    try:
        # Create document metadata
        api_response = api_instance.create_document_metadata(threat_model_id, document_id, metadata)
        print("The response of ThreatModelSubResourcesApi->create_document_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->create_document_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **document_id** | **UUID**| Document identifier | 
 **metadata** | [**Metadata**](Metadata.md)| Metadata key-value pair to create | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Metadata entry created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**409** | Conflict - Metadata key already exists for this entity |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_note_metadata**
> Metadata create_note_metadata(threat_model_id, note_id, metadata)

Create note metadata

Creates new metadata entry for the specified note. Returns 409 Conflict if the key already exists.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    note_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Note identifier
    metadata = tmi_client.Metadata() # Metadata | Metadata key-value pair to create

    try:
        # Create note metadata
        api_response = api_instance.create_note_metadata(threat_model_id, note_id, metadata)
        print("The response of ThreatModelSubResourcesApi->create_note_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->create_note_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **note_id** | **UUID**| Note identifier | 
 **metadata** | [**Metadata**](Metadata.md)| Metadata key-value pair to create | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Metadata entry created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**409** | Conflict - Metadata key already exists for this entity |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository_metadata**
> Metadata create_repository_metadata(threat_model_id, repository_id, metadata)

Create source metadata

Creates new metadata entry for the specified source reference. Returns 409 Conflict if the key already exists.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    repository_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Repository identifier
    metadata = tmi_client.Metadata() # Metadata | Metadata key-value pair to create

    try:
        # Create source metadata
        api_response = api_instance.create_repository_metadata(threat_model_id, repository_id, metadata)
        print("The response of ThreatModelSubResourcesApi->create_repository_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->create_repository_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **repository_id** | **UUID**| Repository identifier | 
 **metadata** | [**Metadata**](Metadata.md)| Metadata key-value pair to create | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Metadata entry created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**409** | Conflict - Metadata key already exists for this entity |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_threat_metadata**
> Metadata create_threat_metadata(threat_model_id, threat_id, metadata)

Create threat metadata

Creates new metadata entry for the specified threat. Returns 409 Conflict if the key already exists.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    threat_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat identifier
    metadata = tmi_client.Metadata() # Metadata | Metadata key-value pair to create

    try:
        # Create threat metadata
        api_response = api_instance.create_threat_metadata(threat_model_id, threat_id, metadata)
        print("The response of ThreatModelSubResourcesApi->create_threat_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->create_threat_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **threat_id** | **UUID**| Threat identifier | 
 **metadata** | [**Metadata**](Metadata.md)| Metadata key-value pair to create | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Metadata entry created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**409** | Conflict - Metadata key already exists for this entity |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_threat_model_asset**
> Asset create_threat_model_asset(threat_model_id, asset_input)

Create a new asset

Creates a new asset within the specified threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.asset import Asset
from tmi_client.models.asset_input import AssetInput
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    asset_input = tmi_client.AssetInput() # AssetInput | Asset creation data

    try:
        # Create a new asset
        api_response = api_instance.create_threat_model_asset(threat_model_id, asset_input)
        print("The response of ThreatModelSubResourcesApi->create_threat_model_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->create_threat_model_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **asset_input** | [**AssetInput**](AssetInput.md)| Asset creation data | 

### Return type

[**Asset**](Asset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Asset created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_threat_model_asset_metadata**
> Metadata create_threat_model_asset_metadata(threat_model_id, asset_id, metadata)

Add metadata to an asset

Adds a new metadata key-value pair to the specified asset. Returns 409 Conflict if the key already exists.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    asset_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Asset identifier
    metadata = tmi_client.Metadata() # Metadata | Metadata key-value pair to create

    try:
        # Add metadata to an asset
        api_response = api_instance.create_threat_model_asset_metadata(threat_model_id, asset_id, metadata)
        print("The response of ThreatModelSubResourcesApi->create_threat_model_asset_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->create_threat_model_asset_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **asset_id** | **UUID**| Asset identifier | 
 **metadata** | [**Metadata**](Metadata.md)| Metadata key-value pair to create | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Metadata created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**409** | Conflict - Metadata key already exists for this entity |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_threat_model_diagram**
> DfdDiagram create_threat_model_diagram(threat_model_id, create_diagram_request)

Create a new diagram

Creates a new diagram within the specified threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.create_diagram_request import CreateDiagramRequest
from tmi_client.models.dfd_diagram import DfdDiagram
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    create_diagram_request = tmi_client.CreateDiagramRequest() # CreateDiagramRequest | Diagram creation data

    try:
        # Create a new diagram
        api_response = api_instance.create_threat_model_diagram(threat_model_id, create_diagram_request)
        print("The response of ThreatModelSubResourcesApi->create_threat_model_diagram:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->create_threat_model_diagram: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **create_diagram_request** | [**CreateDiagramRequest**](CreateDiagramRequest.md)| Diagram creation data | 

### Return type

[**DfdDiagram**](DfdDiagram.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Diagram created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_threat_model_document**
> Document create_threat_model_document(threat_model_id, document_input)

Create a new document

Creates a new document within the specified threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.document import Document
from tmi_client.models.document_input import DocumentInput
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    document_input = {"name":"Security Requirements","description":"Application security requirements specification","uri":"https://docs.example.com/security-requirements.pdf"} # DocumentInput | Document creation data

    try:
        # Create a new document
        api_response = api_instance.create_threat_model_document(threat_model_id, document_input)
        print("The response of ThreatModelSubResourcesApi->create_threat_model_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->create_threat_model_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **document_input** | [**DocumentInput**](DocumentInput.md)| Document creation data | 

### Return type

[**Document**](Document.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Document created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_threat_model_metadata**
> Metadata create_threat_model_metadata(threat_model_id, metadata)

Create threat model metadata

Creates new metadata entry for the specified threat model. Returns 409 Conflict if the key already exists.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    metadata = tmi_client.Metadata() # Metadata | Metadata key-value pair to create

    try:
        # Create threat model metadata
        api_response = api_instance.create_threat_model_metadata(threat_model_id, metadata)
        print("The response of ThreatModelSubResourcesApi->create_threat_model_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->create_threat_model_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **metadata** | [**Metadata**](Metadata.md)| Metadata key-value pair to create | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Metadata entry created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**409** | Conflict - Metadata key already exists for this entity |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_threat_model_note**
> Note create_threat_model_note(threat_model_id, note_input)

Create a new note

Creates a new note within the specified threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.note import Note
from tmi_client.models.note_input import NoteInput
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    note_input = tmi_client.NoteInput() # NoteInput | Note creation data

    try:
        # Create a new note
        api_response = api_instance.create_threat_model_note(threat_model_id, note_input)
        print("The response of ThreatModelSubResourcesApi->create_threat_model_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->create_threat_model_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **note_input** | [**NoteInput**](NoteInput.md)| Note creation data | 

### Return type

[**Note**](Note.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Note created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_threat_model_repository**
> Repository create_threat_model_repository(threat_model_id, repository_input)

Create a new source reference

Creates a new source code reference within the specified threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.repository import Repository
from tmi_client.models.repository_input import RepositoryInput
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    repository_input = tmi_client.RepositoryInput() # RepositoryInput | Repository creation data

    try:
        # Create a new source reference
        api_response = api_instance.create_threat_model_repository(threat_model_id, repository_input)
        print("The response of ThreatModelSubResourcesApi->create_threat_model_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->create_threat_model_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **repository_input** | [**RepositoryInput**](RepositoryInput.md)| Repository creation data | 

### Return type

[**Repository**](Repository.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Source reference created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_threat_model_threat**
> Threat create_threat_model_threat(threat_model_id, threat_input)

Create a new threat

Creates a new threat within the specified threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.threat import Threat
from tmi_client.models.threat_input import ThreatInput
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    threat_input = tmi_client.ThreatInput() # ThreatInput | Threat creation data

    try:
        # Create a new threat
        api_response = api_instance.create_threat_model_threat(threat_model_id, threat_input)
        print("The response of ThreatModelSubResourcesApi->create_threat_model_threat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->create_threat_model_threat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **threat_input** | [**ThreatInput**](ThreatInput.md)| Threat creation data | 

### Return type

[**Threat**](Threat.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Threat created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_diagram_metadata_by_key**
> delete_diagram_metadata_by_key(threat_model_id, diagram_id, key)

Delete diagram metadata by key

Removes a specific metadata entry for the diagram by key

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    diagram_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Diagram identifier
    key = 'key_example' # str | Metadata key

    try:
        # Delete diagram metadata by key
        api_instance.delete_diagram_metadata_by_key(threat_model_id, diagram_id, key)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->delete_diagram_metadata_by_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **diagram_id** | **UUID**| Diagram identifier | 
 **key** | **str**| Metadata key | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Metadata entry deleted successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document_metadata_by_key**
> delete_document_metadata_by_key(threat_model_id, document_id, key)

Delete document metadata by key

Deletes a specific metadata entry by key for the specified document

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    document_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Document identifier
    key = 'key_example' # str | Metadata key

    try:
        # Delete document metadata by key
        api_instance.delete_document_metadata_by_key(threat_model_id, document_id, key)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->delete_document_metadata_by_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **document_id** | **UUID**| Document identifier | 
 **key** | **str**| Metadata key | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Metadata entry deleted successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_note_metadata_by_key**
> delete_note_metadata_by_key(threat_model_id, note_id, key)

Delete note metadata by key

Deletes a specific metadata entry by key for the specified note

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    note_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Note identifier
    key = 'key_example' # str | Metadata key

    try:
        # Delete note metadata by key
        api_instance.delete_note_metadata_by_key(threat_model_id, note_id, key)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->delete_note_metadata_by_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **note_id** | **UUID**| Note identifier | 
 **key** | **str**| Metadata key | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Metadata entry deleted successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_repository_metadata_by_key**
> delete_repository_metadata_by_key(threat_model_id, repository_id, key)

Delete source metadata by key

Deletes a specific metadata entry by key for the specified source reference

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    repository_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Repository identifier
    key = 'key_example' # str | Metadata key

    try:
        # Delete source metadata by key
        api_instance.delete_repository_metadata_by_key(threat_model_id, repository_id, key)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->delete_repository_metadata_by_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **repository_id** | **UUID**| Repository identifier | 
 **key** | **str**| Metadata key | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Metadata entry deleted successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_threat_metadata_by_key**
> delete_threat_metadata_by_key(threat_model_id, threat_id, key)

Delete threat metadata by key

Deletes a specific metadata entry by key for the specified threat

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    threat_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat identifier
    key = 'key_example' # str | Metadata key

    try:
        # Delete threat metadata by key
        api_instance.delete_threat_metadata_by_key(threat_model_id, threat_id, key)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->delete_threat_metadata_by_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **threat_id** | **UUID**| Threat identifier | 
 **key** | **str**| Metadata key | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Metadata entry deleted successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_threat_model_asset**
> delete_threat_model_asset(threat_model_id, asset_id)

Delete an asset

Deletes an asset from the specified threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    asset_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Asset identifier

    try:
        # Delete an asset
        api_instance.delete_threat_model_asset(threat_model_id, asset_id)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->delete_threat_model_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **asset_id** | **UUID**| Asset identifier | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Asset deleted successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_threat_model_asset_metadata**
> delete_threat_model_asset_metadata(threat_model_id, asset_id, key)

Delete asset metadata

Deletes a metadata key-value pair from the specified asset

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    asset_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Asset identifier
    key = 'key_example' # str | Metadata key

    try:
        # Delete asset metadata
        api_instance.delete_threat_model_asset_metadata(threat_model_id, asset_id, key)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->delete_threat_model_asset_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **asset_id** | **UUID**| Asset identifier | 
 **key** | **str**| Metadata key | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Metadata deleted successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_threat_model_diagram**
> delete_threat_model_diagram(threat_model_id, diagram_id)

Delete a diagram

Permanently removes a diagram from the threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    diagram_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Diagram identifier

    try:
        # Delete a diagram
        api_instance.delete_threat_model_diagram(threat_model_id, diagram_id)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->delete_threat_model_diagram: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **diagram_id** | **UUID**| Diagram identifier | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Diagram deleted successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**409** | Conflict - Cannot delete diagram while collaboration session is active |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_threat_model_document**
> delete_threat_model_document(threat_model_id, document_id)

Delete a document

Deletes a specific document from the threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    document_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Document identifier

    try:
        # Delete a document
        api_instance.delete_threat_model_document(threat_model_id, document_id)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->delete_threat_model_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **document_id** | **UUID**| Document identifier | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Document deleted successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_threat_model_metadata_by_key**
> delete_threat_model_metadata_by_key(threat_model_id, key)

Delete threat model metadata by key

Deletes a specific metadata entry by key for the specified threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    key = 'key_example' # str | Metadata key

    try:
        # Delete threat model metadata by key
        api_instance.delete_threat_model_metadata_by_key(threat_model_id, key)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->delete_threat_model_metadata_by_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **key** | **str**| Metadata key | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Metadata entry deleted successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_threat_model_note**
> delete_threat_model_note(threat_model_id, note_id)

Delete a note

Deletes a specific note from the threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    note_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Note identifier

    try:
        # Delete a note
        api_instance.delete_threat_model_note(threat_model_id, note_id)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->delete_threat_model_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **note_id** | **UUID**| Note identifier | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Note deleted successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_threat_model_repository**
> delete_threat_model_repository(threat_model_id, repository_id)

Delete a source reference

Deletes a specific source code reference from the threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    repository_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Repository identifier

    try:
        # Delete a source reference
        api_instance.delete_threat_model_repository(threat_model_id, repository_id)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->delete_threat_model_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **repository_id** | **UUID**| Repository identifier | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Source reference deleted successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_threat_model_threat**
> delete_threat_model_threat(threat_model_id, threat_id)

Delete a threat

Deletes a specific threat from the threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    threat_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat identifier

    try:
        # Delete a threat
        api_instance.delete_threat_model_threat(threat_model_id, threat_id)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->delete_threat_model_threat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **threat_id** | **UUID**| Threat identifier | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Threat deleted successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_diagram_metadata**
> List[Metadata] get_diagram_metadata(threat_model_id, diagram_id)

Get diagram metadata

Retrieves all metadata entries for the specified diagram

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    diagram_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Diagram identifier

    try:
        # Get diagram metadata
        api_response = api_instance.get_diagram_metadata(threat_model_id, diagram_id)
        print("The response of ThreatModelSubResourcesApi->get_diagram_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->get_diagram_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **diagram_id** | **UUID**| Diagram identifier | 

### Return type

[**List[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of metadata entries |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_diagram_metadata_by_key**
> Metadata get_diagram_metadata_by_key(threat_model_id, diagram_id, key)

Get diagram metadata by key

Retrieves a specific metadata entry for the diagram by key

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    diagram_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Diagram identifier
    key = 'key_example' # str | Metadata key

    try:
        # Get diagram metadata by key
        api_response = api_instance.get_diagram_metadata_by_key(threat_model_id, diagram_id, key)
        print("The response of ThreatModelSubResourcesApi->get_diagram_metadata_by_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->get_diagram_metadata_by_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **diagram_id** | **UUID**| Diagram identifier | 
 **key** | **str**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata entry |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_diagram_model**
> MinimalDiagramModel get_diagram_model(threat_model_id, diagram_id, format=format)

Get minimal diagram model for automated analysis

Returns a minimal representation of the diagram optimized for automated threat modeling. Strips all visual styling, layout, and rendering properties. Includes threat model context, computed parent-child relationships, and flattened metadata.

Content negotiation: Use the Accept header (application/json, application/x-yaml, application/xml) or the ?format query parameter. Query parameter takes precedence if both are specified. Default: application/json.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.minimal_diagram_model import MinimalDiagramModel
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model UUID
    diagram_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Diagram UUID
    format = json # str | Output format for the diagram model (case-insensitive). Defaults to json if not specified. (optional) (default to json)

    try:
        # Get minimal diagram model for automated analysis
        api_response = api_instance.get_diagram_model(threat_model_id, diagram_id, format=format)
        print("The response of ThreatModelSubResourcesApi->get_diagram_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->get_diagram_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model UUID | 
 **diagram_id** | **UUID**| Diagram UUID | 
 **format** | **str**| Output format for the diagram model (case-insensitive). Defaults to json if not specified. | [optional] [default to json]

### Return type

[**MinimalDiagramModel**](MinimalDiagramModel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Minimal diagram model successfully retrieved in requested format |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid UUID format or invalid format parameter |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Unauthorized - authentication required |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Forbidden - insufficient permissions (requires at least reader role) |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Threat model or diagram not found, or diagram not associated with threat model |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Rate limit exceeded |  * X-RateLimit-Limit - Request limit per window <br>  * X-RateLimit-Remaining - Remaining requests in current window <br>  * X-RateLimit-Reset - Unix timestamp when limit resets <br>  * Retry-After - Seconds until retry allowed <br>  |
**500** | Internal server error (e.g., serialization failure) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_metadata**
> List[Metadata] get_document_metadata(threat_model_id, document_id)

Get document metadata

Returns all metadata key-value pairs for the specified document

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    document_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Document identifier

    try:
        # Get document metadata
        api_response = api_instance.get_document_metadata(threat_model_id, document_id)
        print("The response of ThreatModelSubResourcesApi->get_document_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->get_document_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **document_id** | **UUID**| Document identifier | 

### Return type

[**List[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document metadata list |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_metadata_by_key**
> Metadata get_document_metadata_by_key(threat_model_id, document_id, key)

Get document metadata by key

Returns a specific metadata entry by key for the specified document

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    document_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Document identifier
    key = 'key_example' # str | Metadata key

    try:
        # Get document metadata by key
        api_response = api_instance.get_document_metadata_by_key(threat_model_id, document_id, key)
        print("The response of ThreatModelSubResourcesApi->get_document_metadata_by_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->get_document_metadata_by_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **document_id** | **UUID**| Document identifier | 
 **key** | **str**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata entry |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_note_metadata**
> List[Metadata] get_note_metadata(threat_model_id, note_id)

Get note metadata

Returns all metadata key-value pairs for the specified note

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    note_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Note identifier

    try:
        # Get note metadata
        api_response = api_instance.get_note_metadata(threat_model_id, note_id)
        print("The response of ThreatModelSubResourcesApi->get_note_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->get_note_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **note_id** | **UUID**| Note identifier | 

### Return type

[**List[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Note metadata list |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_note_metadata_by_key**
> Metadata get_note_metadata_by_key(threat_model_id, note_id, key)

Get note metadata by key

Returns a specific metadata entry by key for the specified note

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    note_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Note identifier
    key = 'key_example' # str | Metadata key

    try:
        # Get note metadata by key
        api_response = api_instance.get_note_metadata_by_key(threat_model_id, note_id, key)
        print("The response of ThreatModelSubResourcesApi->get_note_metadata_by_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->get_note_metadata_by_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **note_id** | **UUID**| Note identifier | 
 **key** | **str**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata entry |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository_metadata**
> List[Metadata] get_repository_metadata(threat_model_id, repository_id)

Get source metadata

Returns all metadata key-value pairs for the specified source reference

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    repository_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Repository identifier

    try:
        # Get source metadata
        api_response = api_instance.get_repository_metadata(threat_model_id, repository_id)
        print("The response of ThreatModelSubResourcesApi->get_repository_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->get_repository_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **repository_id** | **UUID**| Repository identifier | 

### Return type

[**List[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Source metadata list |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository_metadata_by_key**
> Metadata get_repository_metadata_by_key(threat_model_id, repository_id, key)

Get source metadata by key

Returns a specific metadata entry by key for the specified source reference

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    repository_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Repository identifier
    key = 'key_example' # str | Metadata key

    try:
        # Get source metadata by key
        api_response = api_instance.get_repository_metadata_by_key(threat_model_id, repository_id, key)
        print("The response of ThreatModelSubResourcesApi->get_repository_metadata_by_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->get_repository_metadata_by_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **repository_id** | **UUID**| Repository identifier | 
 **key** | **str**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata entry |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_threat_metadata**
> List[Metadata] get_threat_metadata(threat_model_id, threat_id)

Get threat metadata

Returns all metadata key-value pairs for the specified threat

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    threat_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat identifier

    try:
        # Get threat metadata
        api_response = api_instance.get_threat_metadata(threat_model_id, threat_id)
        print("The response of ThreatModelSubResourcesApi->get_threat_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->get_threat_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **threat_id** | **UUID**| Threat identifier | 

### Return type

[**List[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Threat metadata list |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_threat_metadata_by_key**
> Metadata get_threat_metadata_by_key(threat_model_id, threat_id, key)

Get threat metadata by key

Returns a specific metadata entry by key for the specified threat

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    threat_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat identifier
    key = 'key_example' # str | Metadata key

    try:
        # Get threat metadata by key
        api_response = api_instance.get_threat_metadata_by_key(threat_model_id, threat_id, key)
        print("The response of ThreatModelSubResourcesApi->get_threat_metadata_by_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->get_threat_metadata_by_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **threat_id** | **UUID**| Threat identifier | 
 **key** | **str**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata entry |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_threat_model_asset**
> Asset get_threat_model_asset(threat_model_id, asset_id)

Get a specific asset

Returns a single asset by its ID

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.asset import Asset
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    asset_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Asset identifier

    try:
        # Get a specific asset
        api_response = api_instance.get_threat_model_asset(threat_model_id, asset_id)
        print("The response of ThreatModelSubResourcesApi->get_threat_model_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->get_threat_model_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **asset_id** | **UUID**| Asset identifier | 

### Return type

[**Asset**](Asset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Asset details |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_threat_model_asset_metadata**
> List[Metadata] get_threat_model_asset_metadata(threat_model_id, asset_id)

Get all metadata for an asset

Returns all metadata key-value pairs for the specified asset

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    asset_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Asset identifier

    try:
        # Get all metadata for an asset
        api_response = api_instance.get_threat_model_asset_metadata(threat_model_id, asset_id)
        print("The response of ThreatModelSubResourcesApi->get_threat_model_asset_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->get_threat_model_asset_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **asset_id** | **UUID**| Asset identifier | 

### Return type

[**List[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Asset metadata |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_threat_model_asset_metadata_by_key**
> Metadata get_threat_model_asset_metadata_by_key(threat_model_id, asset_id, key)

Get specific metadata for an asset

Returns a single metadata value by its key

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    asset_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Asset identifier
    key = 'key_example' # str | Metadata key

    try:
        # Get specific metadata for an asset
        api_response = api_instance.get_threat_model_asset_metadata_by_key(threat_model_id, asset_id, key)
        print("The response of ThreatModelSubResourcesApi->get_threat_model_asset_metadata_by_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->get_threat_model_asset_metadata_by_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **asset_id** | **UUID**| Asset identifier | 
 **key** | **str**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata value |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_threat_model_assets**
> ListAssetsResponse get_threat_model_assets(threat_model_id, limit=limit, offset=offset, include_deleted=include_deleted)

List assets in a threat model

Returns a paginated list of assets within the specified threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.list_assets_response import ListAssetsResponse
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    limit = 20 # int | Maximum number of results to return (optional) (default to 20)
    offset = 0 # int | Number of results to skip (optional) (default to 0)
    include_deleted = False # bool | Include soft-deleted (tombstoned) entities in the response. Requires owner or admin role. (optional) (default to False)

    try:
        # List assets in a threat model
        api_response = api_instance.get_threat_model_assets(threat_model_id, limit=limit, offset=offset, include_deleted=include_deleted)
        print("The response of ThreatModelSubResourcesApi->get_threat_model_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->get_threat_model_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **limit** | **int**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]
 **include_deleted** | **bool**| Include soft-deleted (tombstoned) entities in the response. Requires owner or admin role. | [optional] [default to False]

### Return type

[**ListAssetsResponse**](ListAssetsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of assets |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_threat_model_diagram**
> DfdDiagram get_threat_model_diagram(threat_model_id, diagram_id)

Get a specific diagram

Retrieves a specific diagram from the threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.dfd_diagram import DfdDiagram
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    diagram_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Diagram identifier

    try:
        # Get a specific diagram
        api_response = api_instance.get_threat_model_diagram(threat_model_id, diagram_id)
        print("The response of ThreatModelSubResourcesApi->get_threat_model_diagram:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->get_threat_model_diagram: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **diagram_id** | **UUID**| Diagram identifier | 

### Return type

[**DfdDiagram**](DfdDiagram.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Diagram details |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_threat_model_diagrams**
> ListDiagramsResponse get_threat_model_diagrams(threat_model_id, limit=limit, offset=offset, include_deleted=include_deleted)

List threat model diagrams

Returns all diagrams associated with a specific threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.list_diagrams_response import ListDiagramsResponse
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    limit = 20 # int | Maximum number of results to return (optional) (default to 20)
    offset = 0 # int | Number of results to skip (optional) (default to 0)
    include_deleted = False # bool | Include soft-deleted (tombstoned) entities in the response. Requires owner or admin role. (optional) (default to False)

    try:
        # List threat model diagrams
        api_response = api_instance.get_threat_model_diagrams(threat_model_id, limit=limit, offset=offset, include_deleted=include_deleted)
        print("The response of ThreatModelSubResourcesApi->get_threat_model_diagrams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->get_threat_model_diagrams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **limit** | **int**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]
 **include_deleted** | **bool**| Include soft-deleted (tombstoned) entities in the response. Requires owner or admin role. | [optional] [default to False]

### Return type

[**ListDiagramsResponse**](ListDiagramsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of diagrams |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_threat_model_document**
> Document get_threat_model_document(threat_model_id, document_id)

Get a specific document

Returns details of a specific document within the threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.document import Document
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    document_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Document identifier

    try:
        # Get a specific document
        api_response = api_instance.get_threat_model_document(threat_model_id, document_id)
        print("The response of ThreatModelSubResourcesApi->get_threat_model_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->get_threat_model_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **document_id** | **UUID**| Document identifier | 

### Return type

[**Document**](Document.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document details |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_threat_model_documents**
> ListDocumentsResponse get_threat_model_documents(threat_model_id, limit=limit, offset=offset, include_deleted=include_deleted)

List documents in a threat model

Returns a paginated list of documents within the specified threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.list_documents_response import ListDocumentsResponse
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    limit = 20 # int | Maximum number of results to return (optional) (default to 20)
    offset = 0 # int | Number of results to skip (optional) (default to 0)
    include_deleted = False # bool | Include soft-deleted (tombstoned) entities in the response. Requires owner or admin role. (optional) (default to False)

    try:
        # List documents in a threat model
        api_response = api_instance.get_threat_model_documents(threat_model_id, limit=limit, offset=offset, include_deleted=include_deleted)
        print("The response of ThreatModelSubResourcesApi->get_threat_model_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->get_threat_model_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **limit** | **int**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]
 **include_deleted** | **bool**| Include soft-deleted (tombstoned) entities in the response. Requires owner or admin role. | [optional] [default to False]

### Return type

[**ListDocumentsResponse**](ListDocumentsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of documents |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_threat_model_metadata**
> List[Metadata] get_threat_model_metadata(threat_model_id)

Get threat model metadata

Returns all metadata key-value pairs for the specified threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier

    try:
        # Get threat model metadata
        api_response = api_instance.get_threat_model_metadata(threat_model_id)
        print("The response of ThreatModelSubResourcesApi->get_threat_model_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->get_threat_model_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 

### Return type

[**List[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Threat model metadata list |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_threat_model_metadata_by_key**
> Metadata get_threat_model_metadata_by_key(threat_model_id, key)

Get threat model metadata by key

Returns a specific metadata entry by key for the specified threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    key = 'key_example' # str | Metadata key

    try:
        # Get threat model metadata by key
        api_response = api_instance.get_threat_model_metadata_by_key(threat_model_id, key)
        print("The response of ThreatModelSubResourcesApi->get_threat_model_metadata_by_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->get_threat_model_metadata_by_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **key** | **str**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata entry |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_threat_model_note**
> Note get_threat_model_note(threat_model_id, note_id)

Get a specific note

Returns details of a specific note within the threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.note import Note
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    note_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Note identifier

    try:
        # Get a specific note
        api_response = api_instance.get_threat_model_note(threat_model_id, note_id)
        print("The response of ThreatModelSubResourcesApi->get_threat_model_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->get_threat_model_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **note_id** | **UUID**| Note identifier | 

### Return type

[**Note**](Note.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Note details |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_threat_model_notes**
> ListNotesResponse get_threat_model_notes(threat_model_id, limit=limit, offset=offset, include_deleted=include_deleted)

List notes in a threat model

Returns a paginated list of notes within the specified threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.list_notes_response import ListNotesResponse
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    limit = 20 # int | Maximum number of results to return (optional) (default to 20)
    offset = 0 # int | Number of results to skip (optional) (default to 0)
    include_deleted = False # bool | Include soft-deleted (tombstoned) entities in the response. Requires owner or admin role. (optional) (default to False)

    try:
        # List notes in a threat model
        api_response = api_instance.get_threat_model_notes(threat_model_id, limit=limit, offset=offset, include_deleted=include_deleted)
        print("The response of ThreatModelSubResourcesApi->get_threat_model_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->get_threat_model_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **limit** | **int**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]
 **include_deleted** | **bool**| Include soft-deleted (tombstoned) entities in the response. Requires owner or admin role. | [optional] [default to False]

### Return type

[**ListNotesResponse**](ListNotesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of notes |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_threat_model_repositories**
> ListRepositoriesResponse get_threat_model_repositories(threat_model_id, limit=limit, offset=offset, include_deleted=include_deleted)

List sources in a threat model

Returns a paginated list of source code references within the specified threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.list_repositories_response import ListRepositoriesResponse
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    limit = 20 # int | Maximum number of results to return (optional) (default to 20)
    offset = 0 # int | Number of results to skip (optional) (default to 0)
    include_deleted = False # bool | Include soft-deleted (tombstoned) entities in the response. Requires owner or admin role. (optional) (default to False)

    try:
        # List sources in a threat model
        api_response = api_instance.get_threat_model_repositories(threat_model_id, limit=limit, offset=offset, include_deleted=include_deleted)
        print("The response of ThreatModelSubResourcesApi->get_threat_model_repositories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->get_threat_model_repositories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **limit** | **int**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]
 **include_deleted** | **bool**| Include soft-deleted (tombstoned) entities in the response. Requires owner or admin role. | [optional] [default to False]

### Return type

[**ListRepositoriesResponse**](ListRepositoriesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of source code references |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_threat_model_repository**
> Repository get_threat_model_repository(threat_model_id, repository_id)

Get a specific source reference

Returns details of a specific source code reference within the threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.repository import Repository
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    repository_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Repository identifier

    try:
        # Get a specific source reference
        api_response = api_instance.get_threat_model_repository(threat_model_id, repository_id)
        print("The response of ThreatModelSubResourcesApi->get_threat_model_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->get_threat_model_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **repository_id** | **UUID**| Repository identifier | 

### Return type

[**Repository**](Repository.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Source reference details |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_threat_model_threat**
> Threat get_threat_model_threat(threat_model_id, threat_id)

Get a specific threat

Returns details of a specific threat within the threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.threat import Threat
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    threat_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat identifier

    try:
        # Get a specific threat
        api_response = api_instance.get_threat_model_threat(threat_model_id, threat_id)
        print("The response of ThreatModelSubResourcesApi->get_threat_model_threat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->get_threat_model_threat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **threat_id** | **UUID**| Threat identifier | 

### Return type

[**Threat**](Threat.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Threat details |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_threat_model_threats**
> ListThreatsResponse get_threat_model_threats(threat_model_id, limit=limit, offset=offset, sort=sort, name=name, description=description, threat_type=threat_type, severity=severity, priority=priority, status=status, mitigated=mitigated, diagram_id=diagram_id, cell_id=cell_id, score_gt=score_gt, score_lt=score_lt, score_eq=score_eq, score_ge=score_ge, score_le=score_le, created_after=created_after, created_before=created_before, modified_after=modified_after, modified_before=modified_before, include_deleted=include_deleted)

List threats in a threat model

Returns a paginated list of threats within the specified threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.list_threats_response import ListThreatsResponse
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    limit = 20 # int | Maximum number of results to return (optional) (default to 20)
    offset = 0 # int | Number of results to skip (optional) (default to 0)
    sort = 'created_at:desc' # str | Sort order (e.g., created_at:desc, name:asc, severity:desc, score:desc) (optional) (default to 'created_at:desc')
    name = 'name_example' # str | Filter by name (case-insensitive substring match) (optional)
    description = 'description_example' # str | Filter by threat model description (partial match) (optional)
    threat_type = ['[\"spoofing\",\"tampering\"]'] # List[str] | Filter by threat types (OR logic). Returns threats matching ANY of the specified types. Example: ?threat_type=Tampering&threat_type=Spoofing (optional)
    severity = ['severity_example'] # List[str] | Filter by severity level (OR logic). Returns threats matching ANY of the specified severities. Example: ?severity=high&severity=critical (optional)
    priority = ['[\"high\",\"critical\"]'] # List[str] | Filter by priority (OR logic). Returns threats matching ANY of the specified priorities. Example: ?priority=high&priority=critical (optional)
    status = ['[\"identified\",\"mitigated\"]'] # List[str] | Filter by status (OR logic). Returns threats matching ANY of the specified statuses. Example: ?status=identified&status=mitigated (optional)
    mitigated = True # bool | Filter by mitigated status (exact match) (optional)
    diagram_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Filter by diagram ID (exact match) (optional)
    cell_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Filter by cell ID (exact match) (optional)
    score_gt = 3.4 # float | Filter threats with score greater than this value (optional)
    score_lt = 3.4 # float | Filter threats with score less than this value (optional)
    score_eq = 3.4 # float | Filter threats with score equal to this value (optional)
    score_ge = 3.4 # float | Filter threats with score greater than or equal to this value (optional)
    score_le = 3.4 # float | Filter threats with score less than or equal to this value (optional)
    created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results created after this timestamp (ISO 8601) (optional)
    created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results created before this timestamp (ISO 8601) (optional)
    modified_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results modified after this timestamp (ISO 8601) (optional)
    modified_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results modified before this timestamp (ISO 8601) (optional)
    include_deleted = False # bool | Include soft-deleted (tombstoned) entities in the response. Requires owner or admin role. (optional) (default to False)

    try:
        # List threats in a threat model
        api_response = api_instance.get_threat_model_threats(threat_model_id, limit=limit, offset=offset, sort=sort, name=name, description=description, threat_type=threat_type, severity=severity, priority=priority, status=status, mitigated=mitigated, diagram_id=diagram_id, cell_id=cell_id, score_gt=score_gt, score_lt=score_lt, score_eq=score_eq, score_ge=score_ge, score_le=score_le, created_after=created_after, created_before=created_before, modified_after=modified_after, modified_before=modified_before, include_deleted=include_deleted)
        print("The response of ThreatModelSubResourcesApi->get_threat_model_threats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->get_threat_model_threats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **limit** | **int**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]
 **sort** | **str**| Sort order (e.g., created_at:desc, name:asc, severity:desc, score:desc) | [optional] [default to &#39;created_at:desc&#39;]
 **name** | **str**| Filter by name (case-insensitive substring match) | [optional] 
 **description** | **str**| Filter by threat model description (partial match) | [optional] 
 **threat_type** | [**List[str]**](str.md)| Filter by threat types (OR logic). Returns threats matching ANY of the specified types. Example: ?threat_type&#x3D;Tampering&amp;threat_type&#x3D;Spoofing | [optional] 
 **severity** | [**List[str]**](str.md)| Filter by severity level (OR logic). Returns threats matching ANY of the specified severities. Example: ?severity&#x3D;high&amp;severity&#x3D;critical | [optional] 
 **priority** | [**List[str]**](str.md)| Filter by priority (OR logic). Returns threats matching ANY of the specified priorities. Example: ?priority&#x3D;high&amp;priority&#x3D;critical | [optional] 
 **status** | [**List[str]**](str.md)| Filter by status (OR logic). Returns threats matching ANY of the specified statuses. Example: ?status&#x3D;identified&amp;status&#x3D;mitigated | [optional] 
 **mitigated** | **bool**| Filter by mitigated status (exact match) | [optional] 
 **diagram_id** | **UUID**| Filter by diagram ID (exact match) | [optional] 
 **cell_id** | **UUID**| Filter by cell ID (exact match) | [optional] 
 **score_gt** | **float**| Filter threats with score greater than this value | [optional] 
 **score_lt** | **float**| Filter threats with score less than this value | [optional] 
 **score_eq** | **float**| Filter threats with score equal to this value | [optional] 
 **score_ge** | **float**| Filter threats with score greater than or equal to this value | [optional] 
 **score_le** | **float**| Filter threats with score less than or equal to this value | [optional] 
 **created_after** | **datetime**| Filter results created after this timestamp (ISO 8601) | [optional] 
 **created_before** | **datetime**| Filter results created before this timestamp (ISO 8601) | [optional] 
 **modified_after** | **datetime**| Filter results modified after this timestamp (ISO 8601) | [optional] 
 **modified_before** | **datetime**| Filter results modified before this timestamp (ISO 8601) | [optional] 
 **include_deleted** | **bool**| Include soft-deleted (tombstoned) entities in the response. Requires owner or admin role. | [optional] [default to False]

### Return type

[**ListThreatsResponse**](ListThreatsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of threats |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_threat_model_diagram**
> DfdDiagram patch_threat_model_diagram(threat_model_id, diagram_id, json_patch_document_inner)

Partially update a diagram

Apply JSON Patch operations to update specific parts of a diagram

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.dfd_diagram import DfdDiagram
from tmi_client.models.json_patch_document_inner import JsonPatchDocumentInner
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    diagram_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Diagram identifier
    json_patch_document_inner = [{"op":"replace","path":"/name","value":"Updated Diagram Name"}] # List[JsonPatchDocumentInner] | JSON Patch operations to apply to the diagram

    try:
        # Partially update a diagram
        api_response = api_instance.patch_threat_model_diagram(threat_model_id, diagram_id, json_patch_document_inner)
        print("The response of ThreatModelSubResourcesApi->patch_threat_model_diagram:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->patch_threat_model_diagram: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **diagram_id** | **UUID**| Diagram identifier | 
 **json_patch_document_inner** | [**List[JsonPatchDocumentInner]**](JsonPatchDocumentInner.md)| JSON Patch operations to apply to the diagram | 

### Return type

[**DfdDiagram**](DfdDiagram.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Diagram updated successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**422** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**409** | Conflict - Cannot modify diagram while collaboration session is active |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_threat_model_threat**
> Threat patch_threat_model_threat(threat_model_id, threat_id, json_patch_document_inner)

Partially update a threat

Applies JSON patch operations to a specific threat within the threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.json_patch_document_inner import JsonPatchDocumentInner
from tmi_client.models.threat import Threat
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    threat_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat identifier
    json_patch_document_inner = [{"op":"replace","path":"/name","value":"Updated SQL Injection Threat"},{"op":"replace","path":"/severity","value":"Critical"},{"op":"replace","path":"/description","value":"Updated description with more details"}] # List[JsonPatchDocumentInner] | JSON Patch operations to apply to the threat

    try:
        # Partially update a threat
        api_response = api_instance.patch_threat_model_threat(threat_model_id, threat_id, json_patch_document_inner)
        print("The response of ThreatModelSubResourcesApi->patch_threat_model_threat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->patch_threat_model_threat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **threat_id** | **UUID**| Threat identifier | 
 **json_patch_document_inner** | [**List[JsonPatchDocumentInner]**](JsonPatchDocumentInner.md)| JSON Patch operations to apply to the threat | 

### Return type

[**Threat**](Threat.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Threat patched successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_asset**
> Asset restore_asset(threat_model_id, asset_id)

Restore a soft-deleted asset

Restores a soft-deleted asset within a threat model. The parent threat model must not be deleted; returns 409 if it is. Restricted to owner role or administrators.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.asset import Asset
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    asset_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Asset identifier

    try:
        # Restore a soft-deleted asset
        api_response = api_instance.restore_asset(threat_model_id, asset_id)
        print("The response of ThreatModelSubResourcesApi->restore_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->restore_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **asset_id** | **UUID**| Asset identifier | 

### Return type

[**Asset**](Asset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Entity restored successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**409** | Conflict - Entity is not in a deleted state, or parent threat model is deleted |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_diagram**
> DfdDiagram restore_diagram(threat_model_id, diagram_id)

Restore a soft-deleted diagram

Restores a soft-deleted diagram within a threat model. The parent threat model must not be deleted; returns 409 if it is. Restricted to owner role or administrators.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.dfd_diagram import DfdDiagram
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    diagram_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Diagram identifier

    try:
        # Restore a soft-deleted diagram
        api_response = api_instance.restore_diagram(threat_model_id, diagram_id)
        print("The response of ThreatModelSubResourcesApi->restore_diagram:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->restore_diagram: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **diagram_id** | **UUID**| Diagram identifier | 

### Return type

[**DfdDiagram**](DfdDiagram.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Entity restored successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**409** | Conflict - Entity is not in a deleted state, or parent threat model is deleted |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_document**
> Document restore_document(threat_model_id, document_id)

Restore a soft-deleted document

Restores a soft-deleted document within a threat model. The parent threat model must not be deleted; returns 409 if it is. Restricted to owner role or administrators.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.document import Document
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    document_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Document identifier

    try:
        # Restore a soft-deleted document
        api_response = api_instance.restore_document(threat_model_id, document_id)
        print("The response of ThreatModelSubResourcesApi->restore_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->restore_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **document_id** | **UUID**| Document identifier | 

### Return type

[**Document**](Document.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Entity restored successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**409** | Conflict - Entity is not in a deleted state, or parent threat model is deleted |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_note**
> Note restore_note(threat_model_id, note_id)

Restore a soft-deleted note

Restores a soft-deleted note within a threat model. The parent threat model must not be deleted; returns 409 if it is. Restricted to owner role or administrators.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.note import Note
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    note_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Note identifier

    try:
        # Restore a soft-deleted note
        api_response = api_instance.restore_note(threat_model_id, note_id)
        print("The response of ThreatModelSubResourcesApi->restore_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->restore_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **note_id** | **UUID**| Note identifier | 

### Return type

[**Note**](Note.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Entity restored successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**409** | Conflict - Entity is not in a deleted state, or parent threat model is deleted |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_repository**
> Repository restore_repository(threat_model_id, repository_id)

Restore a soft-deleted repository

Restores a soft-deleted repository within a threat model. The parent threat model must not be deleted; returns 409 if it is. Restricted to owner role or administrators.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.repository import Repository
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    repository_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Repository identifier

    try:
        # Restore a soft-deleted repository
        api_response = api_instance.restore_repository(threat_model_id, repository_id)
        print("The response of ThreatModelSubResourcesApi->restore_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->restore_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **repository_id** | **UUID**| Repository identifier | 

### Return type

[**Repository**](Repository.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Entity restored successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**409** | Conflict - Entity is not in a deleted state, or parent threat model is deleted |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_threat**
> Threat restore_threat(threat_model_id, threat_id)

Restore a soft-deleted threat

Restores a soft-deleted threat within a threat model. The parent threat model must not be deleted; returns 409 if it is. Restricted to owner role or administrators.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.threat import Threat
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    threat_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat identifier

    try:
        # Restore a soft-deleted threat
        api_response = api_instance.restore_threat(threat_model_id, threat_id)
        print("The response of ThreatModelSubResourcesApi->restore_threat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->restore_threat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **threat_id** | **UUID**| Threat identifier | 

### Return type

[**Threat**](Threat.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Entity restored successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**409** | Conflict - Entity is not in a deleted state, or parent threat model is deleted |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_diagram_metadata_by_key**
> Metadata update_diagram_metadata_by_key(threat_model_id, diagram_id, key, update_diagram_metadata_by_key_request)

Update diagram metadata by key

Updates or creates a metadata entry for the diagram with the specified key

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.models.update_diagram_metadata_by_key_request import UpdateDiagramMetadataByKeyRequest
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    diagram_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Diagram identifier
    key = 'key_example' # str | Metadata key
    update_diagram_metadata_by_key_request = {"value":"example-metadata-value"} # UpdateDiagramMetadataByKeyRequest | Metadata value to set

    try:
        # Update diagram metadata by key
        api_response = api_instance.update_diagram_metadata_by_key(threat_model_id, diagram_id, key, update_diagram_metadata_by_key_request)
        print("The response of ThreatModelSubResourcesApi->update_diagram_metadata_by_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->update_diagram_metadata_by_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **diagram_id** | **UUID**| Diagram identifier | 
 **key** | **str**| Metadata key | 
 **update_diagram_metadata_by_key_request** | [**UpdateDiagramMetadataByKeyRequest**](UpdateDiagramMetadataByKeyRequest.md)| Metadata value to set | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata entry updated successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_document_metadata_by_key**
> Metadata update_document_metadata_by_key(threat_model_id, document_id, key, update_threat_metadata_by_key_request)

Update document metadata by key

Updates a specific metadata entry by key for the specified document

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.models.update_threat_metadata_by_key_request import UpdateThreatMetadataByKeyRequest
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    document_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Document identifier
    key = 'key_example' # str | Metadata key
    update_threat_metadata_by_key_request = {"value":"example-metadata-value"} # UpdateThreatMetadataByKeyRequest | Metadata value to set

    try:
        # Update document metadata by key
        api_response = api_instance.update_document_metadata_by_key(threat_model_id, document_id, key, update_threat_metadata_by_key_request)
        print("The response of ThreatModelSubResourcesApi->update_document_metadata_by_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->update_document_metadata_by_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **document_id** | **UUID**| Document identifier | 
 **key** | **str**| Metadata key | 
 **update_threat_metadata_by_key_request** | [**UpdateThreatMetadataByKeyRequest**](UpdateThreatMetadataByKeyRequest.md)| Metadata value to set | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata entry updated successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_note_metadata_by_key**
> Metadata update_note_metadata_by_key(threat_model_id, note_id, key, update_threat_metadata_by_key_request)

Update note metadata by key

Updates a specific metadata entry by key for the specified note

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.models.update_threat_metadata_by_key_request import UpdateThreatMetadataByKeyRequest
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    note_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Note identifier
    key = 'key_example' # str | Metadata key
    update_threat_metadata_by_key_request = {"value":"example-metadata-value"} # UpdateThreatMetadataByKeyRequest | Metadata value to set

    try:
        # Update note metadata by key
        api_response = api_instance.update_note_metadata_by_key(threat_model_id, note_id, key, update_threat_metadata_by_key_request)
        print("The response of ThreatModelSubResourcesApi->update_note_metadata_by_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->update_note_metadata_by_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **note_id** | **UUID**| Note identifier | 
 **key** | **str**| Metadata key | 
 **update_threat_metadata_by_key_request** | [**UpdateThreatMetadataByKeyRequest**](UpdateThreatMetadataByKeyRequest.md)| Metadata value to set | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata entry updated successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository_metadata_by_key**
> Metadata update_repository_metadata_by_key(threat_model_id, repository_id, key, update_threat_metadata_by_key_request)

Update source metadata by key

Updates a specific metadata entry by key for the specified source reference

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.models.update_threat_metadata_by_key_request import UpdateThreatMetadataByKeyRequest
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    repository_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Repository identifier
    key = 'key_example' # str | Metadata key
    update_threat_metadata_by_key_request = {"value":"example-metadata-value"} # UpdateThreatMetadataByKeyRequest | Metadata value to set

    try:
        # Update source metadata by key
        api_response = api_instance.update_repository_metadata_by_key(threat_model_id, repository_id, key, update_threat_metadata_by_key_request)
        print("The response of ThreatModelSubResourcesApi->update_repository_metadata_by_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->update_repository_metadata_by_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **repository_id** | **UUID**| Repository identifier | 
 **key** | **str**| Metadata key | 
 **update_threat_metadata_by_key_request** | [**UpdateThreatMetadataByKeyRequest**](UpdateThreatMetadataByKeyRequest.md)| Metadata value to set | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata entry updated successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_threat_metadata_by_key**
> Metadata update_threat_metadata_by_key(threat_model_id, threat_id, key, update_threat_metadata_by_key_request)

Update threat metadata by key

Updates a specific metadata entry by key for the specified threat

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.models.update_threat_metadata_by_key_request import UpdateThreatMetadataByKeyRequest
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    threat_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat identifier
    key = 'key_example' # str | Metadata key
    update_threat_metadata_by_key_request = {"value":"example-metadata-value"} # UpdateThreatMetadataByKeyRequest | Metadata value to set

    try:
        # Update threat metadata by key
        api_response = api_instance.update_threat_metadata_by_key(threat_model_id, threat_id, key, update_threat_metadata_by_key_request)
        print("The response of ThreatModelSubResourcesApi->update_threat_metadata_by_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->update_threat_metadata_by_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **threat_id** | **UUID**| Threat identifier | 
 **key** | **str**| Metadata key | 
 **update_threat_metadata_by_key_request** | [**UpdateThreatMetadataByKeyRequest**](UpdateThreatMetadataByKeyRequest.md)| Metadata value to set | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata entry updated successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_threat_model_asset**
> Asset update_threat_model_asset(threat_model_id, asset_id, asset_input)

Update an asset

Updates an existing asset within the specified threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.asset import Asset
from tmi_client.models.asset_input import AssetInput
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    asset_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Asset identifier
    asset_input = tmi_client.AssetInput() # AssetInput | Complete asset data for replacement

    try:
        # Update an asset
        api_response = api_instance.update_threat_model_asset(threat_model_id, asset_id, asset_input)
        print("The response of ThreatModelSubResourcesApi->update_threat_model_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->update_threat_model_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **asset_id** | **UUID**| Asset identifier | 
 **asset_input** | [**AssetInput**](AssetInput.md)| Complete asset data for replacement | 

### Return type

[**Asset**](Asset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Asset updated successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_threat_model_asset_metadata**
> Metadata update_threat_model_asset_metadata(threat_model_id, asset_id, key, metadata)

Update asset metadata

Updates an existing metadata value by its key

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    asset_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Asset identifier
    key = 'key_example' # str | Metadata key
    metadata = tmi_client.Metadata() # Metadata | Metadata value to set

    try:
        # Update asset metadata
        api_response = api_instance.update_threat_model_asset_metadata(threat_model_id, asset_id, key, metadata)
        print("The response of ThreatModelSubResourcesApi->update_threat_model_asset_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->update_threat_model_asset_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **asset_id** | **UUID**| Asset identifier | 
 **key** | **str**| Metadata key | 
 **metadata** | [**Metadata**](Metadata.md)| Metadata value to set | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata updated successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_threat_model_diagram**
> DfdDiagram update_threat_model_diagram(threat_model_id, diagram_id, dfd_diagram_input)

Update a diagram

Completely replaces a diagram with new data. Use DfdDiagramInput schema which excludes readOnly fields (id, created_at, modified_at, update_vector).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.dfd_diagram import DfdDiagram
from tmi_client.models.dfd_diagram_input import DfdDiagramInput
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    diagram_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Diagram identifier
    dfd_diagram_input = tmi_client.DfdDiagramInput() # DfdDiagramInput | Complete diagram data for replacement

    try:
        # Update a diagram
        api_response = api_instance.update_threat_model_diagram(threat_model_id, diagram_id, dfd_diagram_input)
        print("The response of ThreatModelSubResourcesApi->update_threat_model_diagram:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->update_threat_model_diagram: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **diagram_id** | **UUID**| Diagram identifier | 
 **dfd_diagram_input** | [**DfdDiagramInput**](DfdDiagramInput.md)| Complete diagram data for replacement | 

### Return type

[**DfdDiagram**](DfdDiagram.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Diagram updated successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**409** | Conflict - Cannot modify diagram while collaboration session is active |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_threat_model_document**
> Document update_threat_model_document(threat_model_id, document_id, document_input)

Update a document

Updates a specific document within the threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.document import Document
from tmi_client.models.document_input import DocumentInput
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    document_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Document identifier
    document_input = tmi_client.DocumentInput() # DocumentInput | Complete document data for replacement

    try:
        # Update a document
        api_response = api_instance.update_threat_model_document(threat_model_id, document_id, document_input)
        print("The response of ThreatModelSubResourcesApi->update_threat_model_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->update_threat_model_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **document_id** | **UUID**| Document identifier | 
 **document_input** | [**DocumentInput**](DocumentInput.md)| Complete document data for replacement | 

### Return type

[**Document**](Document.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document updated successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_threat_model_metadata_by_key**
> Metadata update_threat_model_metadata_by_key(threat_model_id, key, update_threat_metadata_by_key_request)

Update threat model metadata by key

Updates a specific metadata entry by key for the specified threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.metadata import Metadata
from tmi_client.models.update_threat_metadata_by_key_request import UpdateThreatMetadataByKeyRequest
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    key = 'key_example' # str | Metadata key
    update_threat_metadata_by_key_request = {"value":"example-metadata-value"} # UpdateThreatMetadataByKeyRequest | Metadata value to set

    try:
        # Update threat model metadata by key
        api_response = api_instance.update_threat_model_metadata_by_key(threat_model_id, key, update_threat_metadata_by_key_request)
        print("The response of ThreatModelSubResourcesApi->update_threat_model_metadata_by_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->update_threat_model_metadata_by_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **key** | **str**| Metadata key | 
 **update_threat_metadata_by_key_request** | [**UpdateThreatMetadataByKeyRequest**](UpdateThreatMetadataByKeyRequest.md)| Metadata value to set | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata entry updated successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_threat_model_note**
> Note update_threat_model_note(threat_model_id, note_id, note_input)

Update a note

Updates a specific note within the threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.note import Note
from tmi_client.models.note_input import NoteInput
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    note_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Note identifier
    note_input = tmi_client.NoteInput() # NoteInput | Complete note data for replacement

    try:
        # Update a note
        api_response = api_instance.update_threat_model_note(threat_model_id, note_id, note_input)
        print("The response of ThreatModelSubResourcesApi->update_threat_model_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->update_threat_model_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **note_id** | **UUID**| Note identifier | 
 **note_input** | [**NoteInput**](NoteInput.md)| Complete note data for replacement | 

### Return type

[**Note**](Note.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Note updated successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_threat_model_repository**
> Repository update_threat_model_repository(threat_model_id, repository_id, repository_input)

Update a source reference

Updates a specific source code reference within the threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.repository import Repository
from tmi_client.models.repository_input import RepositoryInput
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    repository_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Repository identifier
    repository_input = tmi_client.RepositoryInput() # RepositoryInput | Complete repository data for replacement

    try:
        # Update a source reference
        api_response = api_instance.update_threat_model_repository(threat_model_id, repository_id, repository_input)
        print("The response of ThreatModelSubResourcesApi->update_threat_model_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->update_threat_model_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **repository_id** | **UUID**| Repository identifier | 
 **repository_input** | [**RepositoryInput**](RepositoryInput.md)| Complete repository data for replacement | 

### Return type

[**Repository**](Repository.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Source reference updated successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_threat_model_threat**
> Threat update_threat_model_threat(threat_model_id, threat_id, threat_input)

Update a threat

Updates a specific threat within the threat model

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.threat import Threat
from tmi_client.models.threat_input import ThreatInput
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.ThreatModelSubResourcesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    threat_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat identifier
    threat_input = tmi_client.ThreatInput() # ThreatInput | Complete threat data for replacement

    try:
        # Update a threat
        api_response = api_instance.update_threat_model_threat(threat_model_id, threat_id, threat_input)
        print("The response of ThreatModelSubResourcesApi->update_threat_model_threat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatModelSubResourcesApi->update_threat_model_threat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **threat_id** | **UUID**| Threat identifier | 
 **threat_input** | [**ThreatInput**](ThreatInput.md)| Complete threat data for replacement | 

### Return type

[**Threat**](Threat.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Threat updated successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

