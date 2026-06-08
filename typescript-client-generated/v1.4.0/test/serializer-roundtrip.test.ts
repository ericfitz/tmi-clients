/**
 * Serializer round-trip tests.
 *
 * typescript-fetch emits a `XFromJSON` / `XToJSON` pair per model. These are
 * the only hand-exercised runtime code paths in the client, and the project's
 * regen patches have historically fixed serialization bugs here, so they are
 * the highest-value thing to test. We assert on representative models that
 * cover the tricky cases:
 *
 *   - Metadata: a flat {key, value} model — the baseline round-trip.
 *   - DfdDiagram / BaseDiagram: Date<->string conversion and the readOnly
 *     fields (id, created_at, modified_at, ...) that ToJSON must strip.
 *   - DfdDiagramAllOfCells: a discriminated union (Node | Edge) keyed on
 *     `shape`, exercising the discriminator routing in both directions.
 */
import { describe, expect, it } from "vitest";

import {
  MetadataFromJSON,
  MetadataToJSON,
  type Metadata,
} from "../src/models/Metadata";
import {
  DfdDiagramFromJSON,
  DfdDiagramToJSON,
  DfdDiagramTypeEnum,
} from "../src/models/DfdDiagram";
import {
  DfdDiagramAllOfCellsFromJSON,
  DfdDiagramAllOfCellsToJSON,
} from "../src/models/DfdDiagramAllOfCells";

describe("Metadata serializer", () => {
  it("round-trips a flat key/value object", () => {
    const wire = { key: "owner", value: "alice" };
    const model = MetadataFromJSON(wire);
    expect(model).toEqual<Metadata>({ key: "owner", value: "alice" });
    expect(MetadataToJSON(model)).toEqual(wire);
  });

  it("passes null through unchanged", () => {
    expect(MetadataFromJSON(null)).toBeNull();
    expect(MetadataToJSON(null)).toBeNull();
  });
});

describe("DfdDiagram serializer", () => {
  const wire = {
    id: "11111111-1111-1111-1111-111111111111",
    name: "Login flow",
    type: "DFD-1.0.0",
    created_at: "2024-01-02T03:04:05.000Z",
    modified_at: "2024-01-02T03:04:05.000Z",
    description: "auth subsystem",
    metadata: [{ key: "owner", value: "alice" }],
    cells: [],
  };

  it("parses ISO timestamps into Date objects via FromJSON", () => {
    const model = DfdDiagramFromJSON(wire);
    expect(model.type).toBe(DfdDiagramTypeEnum.Dfd100);
    expect(model.name).toBe("Login flow");
    expect(model.created_at).toBeInstanceOf(Date);
    expect(model.created_at.toISOString()).toBe("2024-01-02T03:04:05.000Z");
    expect(model.metadata).toEqual([{ key: "owner", value: "alice" }]);
    expect(model.cells).toEqual([]);
  });

  it("strips readOnly fields on the way out via ToJSON", () => {
    const model = DfdDiagramFromJSON(wire);
    const out = DfdDiagramToJSON(model);

    // ToJSONTyped omits id/created_at/modified_at/update_vector/deleted_at.
    expect(out.id).toBeUndefined();
    expect(out.created_at).toBeUndefined();
    expect(out.modified_at).toBeUndefined();

    // Writable fields survive the round-trip.
    expect(out.type).toBe("DFD-1.0.0");
    expect(out.name).toBe("Login flow");
    expect(out.description).toBe("auth subsystem");
    expect(out.metadata).toEqual([{ key: "owner", value: "alice" }]);
    expect(out.cells).toEqual([]);
  });
});

describe("DfdDiagramAllOfCells discriminated union", () => {
  it("routes a Node cell (shape: process) through the discriminator", () => {
    const wire = {
      id: "node-1",
      shape: "process",
      x: 10,
      y: 20,
      width: 120,
      height: 60,
    };
    const cell = DfdDiagramAllOfCellsFromJSON(wire);
    expect(cell.shape).toBe("process");
    expect((cell as { x: number }).x).toBe(10);

    const out = DfdDiagramAllOfCellsToJSON(cell);
    expect(out.shape).toBe("process");
    expect(out.x).toBe(10);
    expect(out.width).toBe(120);
  });

  it("routes an Edge cell (shape: flow) through the discriminator", () => {
    const wire = {
      id: "edge-1",
      shape: "flow",
      source: { cell: "node-1" },
      target: { cell: "node-2" },
    };
    const cell = DfdDiagramAllOfCellsFromJSON(wire);
    expect(cell.shape).toBe("flow");

    const out = DfdDiagramAllOfCellsToJSON(cell);
    expect(out.shape).toBe("flow");
    expect(out.id).toBe("edge-1");
  });
});
