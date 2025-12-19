/*
 * TMI (Threat Modeling Improved) API
 *
 * Type aliases for types that swagger-codegen failed to generate properly.
 * These are defined as `object` or untyped schemas in the OpenAPI spec.
 */
package tmiclient

// Object represents an arbitrary JSON object (map[string]interface{})
type Object map[string]interface{}

// CellData represents arbitrary cell data (used by Cell.data field)
type CellData map[string]interface{}

// ModelMap represents an arbitrary JSON object map
type ModelMap map[string]interface{}
