// Regression tests for the codegen patches applied by regenerate_ts.py.
// regenerate_ts.py copies this file into each client's test/ directory.
import { describe, expect, it } from "vitest";

import {
  DfdDiagramCellsInnerFromJSON,
  DfdDiagramCellsInnerToJSON,
  instanceOfEdge,
  instanceOfMinimalNode,
  instanceOfNode,
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
