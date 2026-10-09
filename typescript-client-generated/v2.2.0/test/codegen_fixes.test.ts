// Regression tests for the codegen patches applied by regenerate_ts.py.
// regenerate_ts.py copies this file into each client's test/ directory.
/// <reference types="vite/client" />
import { describe, expect, it } from "vitest";

import {
  DfdDiagramCellsInnerFromJSON,
  DfdDiagramCellsInnerToJSON,
  EdgeConnectorFromJSON,
  EdgeRouterFromJSON,
  instanceOfAsset,
  instanceOfAuditEntry,
  instanceOfAuthorization,
  instanceOfEdge,
  instanceOfEdgeConnectorOneOf,
  instanceOfEdgeRouterOneOf,
  instanceOfJsonPatchDocumentInner,
  instanceOfMinimalNode,
  instanceOfModelError,
  instanceOfNode,
  instanceOfOAuthError,
  instanceOfRelatedProject,
  instanceOfRepositoryBaseParameters,
  instanceOfWebhookDelivery,
  instanceOfWebhookSubscription,
} from "../src/index";

const node = {
  id: "11111111-1111-4111-8111-111111111111",
  shape: "process",
  x: 100,
  y: 100,
  width: 120,
  height: 60,
};

const edge = {
  id: "22222222-2222-4222-8222-222222222222",
  shape: "flow",
  source: { cell: node.id },
  target: { cell: "33333333-3333-4333-8333-333333333333" },
};

const minimalNodeFields = {
  children: [],
  labels: [],
  metadata: [],
  security_boundary: false,
};

describe("enum guard patch (instanceOfNode / instanceOfMinimalNode)", () => {
  it("instanceOfNode accepts every node shape", () => {
    for (const shape of ["actor", "process", "store", "security-boundary", "text-box"]) {
      expect(instanceOfNode({ ...node, shape })).toBe(true);
    }
  });

  it("instanceOfNode rejects an edge", () => {
    expect(instanceOfNode(edge)).toBe(false);
    expect(instanceOfEdge(edge)).toBe(true);
  });

  it("instanceOfNode rejects an unknown shape", () => {
    expect(instanceOfNode({ ...node, shape: "edge" })).toBe(false);
  });

  it("instanceOfMinimalNode accepts a node and rejects an edge shape", () => {
    expect(instanceOfMinimalNode({ ...node, ...minimalNodeFields })).toBe(true);
    expect(instanceOfMinimalNode({ ...edge, ...minimalNodeFields })).toBe(false);
  });

  it("cells still round-trip through the oneOf union", () => {
    for (const cell of [node, edge]) {
      const parsed = DfdDiagramCellsInnerFromJSON(cell);
      expect(parsed.shape).toBe(cell.shape);
      expect(DfdDiagramCellsInnerToJSON(parsed)).toMatchObject(cell);
    }
  });
});

// [name, instanceOf guard, minimal valid object, enum property]
const enumGuardCases: [string, (v: object) => boolean, Record<string, unknown>, string][] = [
  ["Asset.type", instanceOfAsset, { name: "a", type: "data", id: "i" }, "type"],
  [
    "AuditEntry.object_type",
    instanceOfAuditEntry,
    {
      id: "i",
      threat_model_id: "t",
      object_type: "threat",
      object_id: "o",
      change_type: "created",
      actor: {},
      created_at: "2026-01-01T00:00:00Z",
    },
    "object_type",
  ],
  [
    "AuditEntry.change_type",
    instanceOfAuditEntry,
    {
      id: "i",
      threat_model_id: "t",
      object_type: "threat",
      object_id: "o",
      change_type: "created",
      actor: {},
      created_at: "2026-01-01T00:00:00Z",
    },
    "change_type",
  ],
  [
    "Authorization.role",
    instanceOfAuthorization,
    { principal_type: "user", provider: "p", provider_id: "x", role: "reader" },
    "role",
  ],
  [
    "JsonPatchDocumentInner.op",
    instanceOfJsonPatchDocumentInner,
    { op: "add", path: "/a" },
    "op",
  ],
  [
    "RepositoryBaseParameters.refType",
    instanceOfRepositoryBaseParameters,
    { refType: "branch", refValue: "main" },
    "refType",
  ],
  [
    "RelatedProject.relationship",
    instanceOfRelatedProject,
    { related_project_id: "p", relationship: "parent" },
    "relationship",
  ],
  [
    "WebhookDelivery.event_type",
    instanceOfWebhookDelivery,
    {
      id: "i",
      subscription_id: "s",
      event_type: "threat_model.created",
      status: "pending",
      attempts: 0,
      created_at: "2026-01-01T00:00:00Z",
    },
    "event_type",
  ],
  [
    "WebhookDelivery.status",
    instanceOfWebhookDelivery,
    {
      id: "i",
      subscription_id: "s",
      event_type: "threat_model.created",
      status: "pending",
      attempts: 0,
      created_at: "2026-01-01T00:00:00Z",
    },
    "status",
  ],
];

const webhookSubscription = {
  id: "i",
  owner_id: "o",
  name: "w",
  url: "https://example.com/hook",
  events: ["threat_model.created", "threat_model.deleted"],
  status: "active",
  created_at: "2026-01-01T00:00:00Z",
  modified_at: "2026-01-01T00:00:00Z",
};

describe("enum guard patch (required Array<Enum>)", () => {
  it("WebhookSubscription.events accepts known event types", () => {
    expect(instanceOfWebhookSubscription(webhookSubscription)).toBe(true);
    expect(instanceOfWebhookSubscription({ ...webhookSubscription, events: [] })).toBe(true);
  });

  it("WebhookSubscription.events rejects an unknown event type or a non-array", () => {
    const events = ["threat_model.created", "not-a-real-event"];
    expect(instanceOfWebhookSubscription({ ...webhookSubscription, events })).toBe(false);
    expect(instanceOfWebhookSubscription({ ...webhookSubscription, events: "threat_model.created" })).toBe(false);
  });
});

describe("enum guard patch (all required multi-value enums)", () => {
  it.each(enumGuardCases)("%s: accepts a known value, rejects an unknown one", (_n, guard, valid, prop) => {
    expect(guard(valid)).toBe(true);
    expect(guard({ ...valid, [prop]: "not-a-real-value" })).toBe(false);
  });

  // ADR 0005: the server may add error codes, so these guards stay presence-only.
  it("error guards accept an error code this client does not know", () => {
    for (const guard of [instanceOfModelError, instanceOfOAuthError]) {
      expect(guard({ error: "some_future_code", error_description: "d" })).toBe(true);
    }
    expect(instanceOfModelError({ error: "not_found", error_description: "d" })).toBe(true);
    expect(instanceOfOAuthError({ error: "invalid_request", error_description: "d" })).toBe(true);
  });

  it("EdgeRouter keeps an unknown name instead of collapsing to {}", () => {
    const router = EdgeRouterFromJSON({ name: "future-router", args: {} });
    expect(router).toMatchObject({ name: "future-router" });
    expect(EdgeRouterFromJSON({ name: "manhattan" })).toMatchObject({ name: "manhattan" });
    expect(EdgeRouterFromJSON("orth")).toBe("orth");
    expect(instanceOfEdgeRouterOneOf({ name: "future-router" })).toBe(true);
  });

  it("EdgeConnector keeps an unknown name instead of collapsing to {}", () => {
    const connector = EdgeConnectorFromJSON({ name: "future-connector" });
    expect(connector).toMatchObject({ name: "future-connector" });
    expect(EdgeConnectorFromJSON({ name: "rounded" })).toMatchObject({ name: "rounded" });
    expect(EdgeConnectorFromJSON("smooth")).toBe("smooth");
    expect(instanceOfEdgeConnectorOneOf({ name: "future-connector" })).toBe(true);
  });

  // Fails when a regeneration leaves a required enum guard presence-only (the
  // generator emits no value check for multi-value enums, Array<Enum> or
  // Enum | null).
  it("no required enum guard is left presence-only", () => {
    const models = import.meta.glob<string>("../src/models/*.ts", {
      query: "?raw",
      import: "default",
      eager: true,
    });
    expect(Object.keys(models).length).toBeGreaterThan(100);
    // Enum consts by name across all models: shared enum schemas live in their own file.
    const enums = new Map<string, string>();
    for (const src of Object.values(models)) {
      for (const [, name, body] of src.matchAll(/export const (\w+) = \{\n([\s\S]*?)\n\} as const;/g)) {
        enums.set(name, body);
      }
    }
    const exempt = new Set([
      "EdgeRouterOneOf.name",
      "EdgeConnectorOneOf.name",
      "ModelError.error",
      "OAuthError.error",
    ]);
    const unchecked: string[] = [];
    for (const src of Object.values(models)) {
      const fn = /export function instanceOf(\w+)\(value: object\)[^\n]*\{\n([\s\S]*?)\n {4}return true;/.exec(src);
      if (!fn) continue;
      for (const [, prop] of fn[2].matchAll(/if \(!\('([^']+)' in value\)/g)) {
        const type = new RegExp(`^\\s+(?:readonly )?${prop}: (.+);`, "m").exec(src);
        if (!type) continue;
        const shape = /^(?:(\w+)|Array<(\w+)>|(\w+) \| null)$/.exec(type[1]);
        const name = shape && (shape[1] ?? shape[2] ?? shape[3]);
        const body = name && enums.get(name);
        if (!body) continue;
        const count = (body.match(/: /g) ?? []).length;
        let checked: boolean;
        if (shape[2]) {
          checked = fn[2].includes(`!Array.isArray(value['${prop}'])`);
        } else if (shape[3]) {
          checked = fn[2].includes(`value['${prop}'] !== null && value['${prop}'] !== '`);
        } else {
          if (count < 2) continue;
          checked = fn[2].includes(`value['${prop}'] !== '`);
        }
        if (!checked && !exempt.has(`${fn[1]}.${prop}`)) {
          unchecked.push(`${fn[1]}.${prop}`);
        }
      }
    }
    expect(unchecked).toEqual([]);
  });
});
