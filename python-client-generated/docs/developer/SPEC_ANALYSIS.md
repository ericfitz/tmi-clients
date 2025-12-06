================================================================================
OpenAPI Specification Analysis Report
================================================================================

Spec Version: 1.0.0
Title: TMI (Threat Modeling Improved) API
Spec Location: /Users/efitz/Projects/tmi/docs/reference/apis/tmi-openapi.json

================================================================================
1. PATHS ANALYSIS
================================================================================

Total API Paths: 89

Operations by HTTP Method:
  DELETE: 27
  GET: 67
  PATCH: 10
  POST: 41
  PUT: 28

Paths by Tag (API Group):

  Addons (8 operations):
    POST /addons
      Summary: Create add-on
    GET /addons
      Summary: List add-ons
    GET /addons/{id}
      Summary: Get add-on
    DELETE /addons/{id}
      Summary: Delete add-on
    POST /addons/{id}/invoke
      Summary: Invoke add-on
    ... and 3 more

  Administration (27 operations):
    GET /admin/administrators
      Summary: List administrators
    POST /admin/administrators
      Summary: Create administrator grant
    DELETE /admin/administrators/{id}
      Summary: Delete administrator grant
    GET /admin/quotas/users/{user_id}
      Summary: Get user API quota
    PUT /admin/quotas/users/{user_id}
      Summary: Update user API quota
    ... and 22 more

  Assets (1 operations):
    PATCH /threat_models/{threat_model_id}/assets/{asset_id}
      Summary: Partially update asset

  Authentication (19 operations):
    POST /oauth2/introspect
      Summary: Token Introspection
    GET /oauth2/providers
      Summary: List available OAuth providers
    GET /oauth2/providers/{idp}/groups
      Summary: Get groups for identity provider
    GET /oauth2/authorize
      Summary: Initiate OAuth authorization flow
    POST /oauth2/token
      Summary: Exchange OAuth credentials for JWT tokens
    ... and 14 more

  Collaboration (4 operations):
    GET /collaboration/sessions
      Summary: List active collaboration sessions
    GET /threat_models/{threat_model_id}/diagrams/{diagram_id}/collaborate
      Summary: Get diagram collaboration session
    POST /threat_models/{threat_model_id}/diagrams/{diagram_id}/collaborate
      Summary: Create diagram collaboration session
    DELETE /threat_models/{threat_model_id}/diagrams/{diagram_id}/collaborate
      Summary: End diagram collaboration session

  Documents (1 operations):
    PATCH /threat_models/{threat_model_id}/documents/{document_id}
      Summary: Partially update document

  General (1 operations):
    GET /
      Summary: Get API information

  Notes (1 operations):
    PATCH /threat_models/{threat_model_id}/notes/{note_id}
      Summary: Partially update note

  OAuth Discovery (1 operations):
    GET /.well-known/oauth-protected-resource
      Summary: OAuth 2.0 Protected Resource Metadata

  OIDC Discovery (3 operations):
    GET /.well-known/openid-configuration
      Summary: OpenID Connect Discovery Configuration
    GET /.well-known/oauth-authorization-server
      Summary: OAuth 2.0 Authorization Server Metadata
    GET /.well-known/jwks.json
      Summary: JSON Web Key Set

  Repositories (1 operations):
    PATCH /threat_models/{threat_model_id}/repositories/{repository_id}
      Summary: Partially update repository

  SAML (1 operations):
    GET /saml/providers/{idp}/users
      Summary: List SAML users for UI autocomplete

  Threat Model Sub-Resources (89 operations):
    GET /threat_models/{threat_model_id}/threats
      Summary: List threats in a threat model
    POST /threat_models/{threat_model_id}/threats
      Summary: Create a new threat
    GET /threat_models/{threat_model_id}/threats/{threat_id}
      Summary: Get a specific threat
    PUT /threat_models/{threat_model_id}/threats/{threat_id}
      Summary: Update a threat
    PATCH /threat_models/{threat_model_id}/threats/{threat_id}
      Summary: Partially update a threat
    ... and 84 more

  Threat Models (6 operations):
    GET /threat_models
      Summary: List threat models
    POST /threat_models
      Summary: Create a threat model
    GET /threat_models/{threat_model_id}
      Summary: Retrieve a threat model
    PUT /threat_models/{threat_model_id}
      Summary: Update a threat model
    PATCH /threat_models/{threat_model_id}
      Summary: Partially update a threat model
    ... and 1 more

  Threats (2 operations):
    PATCH /threat_models/{threat_model_id}/threats/bulk
      Summary: Bulk PATCH threats
    DELETE /threat_models/{threat_model_id}/threats/bulk
      Summary: Bulk DELETE threats

  Users (1 operations):
    DELETE /users/me
      Summary: Delete authenticated user account and all data

  webhooks (7 operations):
    GET /webhooks/subscriptions
      Summary: List webhook subscriptions
    POST /webhooks/subscriptions
      Summary: Create webhook subscription
    GET /webhooks/subscriptions/{webhook_id}
      Summary: Get webhook subscription
    DELETE /webhooks/subscriptions/{webhook_id}
      Summary: Delete webhook subscription
    POST /webhooks/subscriptions/{webhook_id}/test
      Summary: Test webhook subscription
    ... and 2 more

================================================================================
2. SCHEMAS ANALYSIS
================================================================================

Total Schemas: 90

Schemas with Discriminator: 4
  - BaseDiagram: {'propertyName': 'type', 'mapping': {'DFD-1.0.0': '#/components/schemas/DfdDiagram'}}
  - BaseDiagramInput: {'propertyName': 'type', 'mapping': {'DFD-1.0.0': '#/components/schemas/DfdDiagramInput'}}
  - Diagram: {'propertyName': 'type', 'mapping': {'DFD-1.0.0': '#/components/schemas/DfdDiagram'}}
  - Cell: {'propertyName': 'shape'}

Schemas with ReadOnly Fields: 7
  - BaseDiagram: id, created_at, modified_at, update_vector
  - CollaborationSession: session_id, host, presenter
  - DiagramListItem: id
  - TMListItem: id, status_updated
  - NoteListItem: id, created_at, modified_at
  - AdminUser: is_admin, groups, active_threat_models
  - AdminGroup: used_in_authorizations, used_in_admin_grants, member_count

================================================================================
3. COMPARISON WITH CURRENT CLIENT
================================================================================

Current API modules: 14
Expected API tags: 2
API count change: -12

Current model classes: 106
Expected schemas: 90
Model count change: -16

New Models Expected (36):
  + add_group_member_request
  + addon_invocation_quota
  + addon_response
  + admin_group
  + admin_group_list_response
  + admin_user
  + admin_user_list_response
  + administrator
  + client_credential_info
  + client_credential_response
  + create_addon_request
  + create_admin_group_request
  + create_administrator_request
  + deletion_stats
  + group
  + group_member
  + group_member_list_response
  + invocation_list_response
  + invocation_response
  + invoke_addon_request
  ... and 16 more

Models to be Removed (52):
  - api_info_api
  - api_info_operator
  - api_info_service
  - api_info_status
  - base_diagram_image
  - cell_data
  - edge_attrs_line
  - edge_attrs_line_source_marker
  - edge_attrs_line_target_marker
  - edge_connector_args
  - edge_label_attrs
  - edge_label_attrs_text
  - edge_router_args
  - error_details
  - inline_response200
  - inline_response2001
  - inline_response2002
  - inline_response2002_keys
  - inline_response2003
  - inline_response2004
  ... and 32 more

================================================================================
4. SUMMARY
================================================================================

Key Findings:
  - 89 API endpoints
  - 90 data models
  - 17 API groups/tags
  - 173 total operations

⚠ IMPORTANT: 36 new models will be generated
⚠ IMPORTANT: 52 models will be removed (BREAKING CHANGE)

Next Steps:
  1. Review the changes above
  2. Run: ./scripts/regenerate_client.sh
  3. Review generated migration guide
  4. Test the regenerated client

================================================================================