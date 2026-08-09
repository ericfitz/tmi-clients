/**
 * Smoke tests for the generated TMI TypeScript client.
 *
 * These are hand-written: `typescript-fetch` emits no tests, and this file is
 * preserved across regenerations by the backup/restore step in
 * `regenerate_ts.py`. Keep it version-agnostic — the same file is carried in
 * the `test` directory of every generated TypeScript client version, so it must
 * only rely on surface that is stable across API versions (`ThreatModelsApi`,
 * the `Configuration` runtime, and the shared error types).
 *
 * Everything here runs offline: `fetchApi` is stubbed, so the tests assert how
 * the client *builds requests and maps responses*, never that a server is up.
 */
import { describe, expect, it } from "vitest";

import {
  BASE_PATH,
  Configuration,
  RequiredError,
  ResponseError,
  ThreatModelsApi,
} from "../src";

interface RecordedCall {
  url: string;
  method: string | undefined;
  headers: Headers;
  body: string | undefined;
}

/**
 * Build a stub `fetch` that records what it was called with and replays a
 * canned response, so request construction can be asserted without a network.
 */
function stubFetch(
  body: unknown,
  status = 200,
): { fetchApi: typeof fetch; calls: RecordedCall[] } {
  const calls: RecordedCall[] = [];

  const fetchApi = (async (
    input: RequestInfo | URL,
    init?: RequestInit,
  ): Promise<Response> => {
    calls.push({
      url: String(input),
      method: init?.method,
      headers: new Headers(init?.headers),
      body: typeof init?.body === "string" ? init.body : undefined,
    });
    return new Response(JSON.stringify(body), {
      status,
      headers: { "Content-Type": "application/json" },
    });
  }) as typeof fetch;

  return { fetchApi, calls };
}

/** A minimal, version-stable `listThreatModels` payload. */
const EMPTY_LIST = { threat_models: [], total: 0, limit: 20, offset: 0 };

describe("Configuration", () => {
  it("falls back to the generated BASE_PATH", () => {
    expect(new Configuration().basePath).toBe(BASE_PATH);
    expect(BASE_PATH).not.toMatch(/\/$/);
  });

  it("honours an explicit basePath override", () => {
    const cfg = new Configuration({ basePath: "https://tmi.test" });
    expect(cfg.basePath).toBe("https://tmi.test");
  });

  it("normalises a string accessToken into a token callback", async () => {
    const cfg = new Configuration({ accessToken: "static-token" });
    await expect(cfg.accessToken?.("bearerAuth", [])).resolves.toBe(
      "static-token",
    );
  });
});

describe("request construction", () => {
  it("issues a GET against the configured basePath", async () => {
    const { fetchApi, calls } = stubFetch(EMPTY_LIST);
    const api = new ThreatModelsApi(
      new Configuration({ basePath: "https://tmi.test", fetchApi }),
    );

    await api.listThreatModels();

    expect(calls).toHaveLength(1);
    expect(calls[0].method).toBe("GET");
    expect(calls[0].url).toMatch(/^https:\/\/tmi\.test\/threat_models/);
    expect(calls[0].body).toBeUndefined();
  });

  it("serialises pagination parameters into the query string", async () => {
    const { fetchApi, calls } = stubFetch(EMPTY_LIST);
    const api = new ThreatModelsApi(
      new Configuration({ basePath: "https://tmi.test", fetchApi }),
    );

    await api.listThreatModels({ limit: 5, offset: 10 });

    const query = new URL(calls[0].url).searchParams;
    expect(query.get("limit")).toBe("5");
    expect(query.get("offset")).toBe("10");
  });

  it("omits query parameters that were not supplied", async () => {
    const { fetchApi, calls } = stubFetch(EMPTY_LIST);
    const api = new ThreatModelsApi(
      new Configuration({ basePath: "https://tmi.test", fetchApi }),
    );

    await api.listThreatModels({ limit: 5 });

    const query = new URL(calls[0].url).searchParams;
    expect(query.has("limit")).toBe(true);
    expect(query.has("offset")).toBe(false);
  });

  it("attaches a bearer token when one is configured", async () => {
    const { fetchApi, calls } = stubFetch(EMPTY_LIST);
    const api = new ThreatModelsApi(
      new Configuration({
        basePath: "https://tmi.test",
        fetchApi,
        accessToken: "secret-token",
      }),
    );

    await api.listThreatModels();

    expect(calls[0].headers.get("Authorization")).toBe("Bearer secret-token");
  });

  it("resolves an async accessToken callback per request", async () => {
    const { fetchApi, calls } = stubFetch(EMPTY_LIST);
    const api = new ThreatModelsApi(
      new Configuration({
        basePath: "https://tmi.test",
        fetchApi,
        accessToken: async () => "rotated-token",
      }),
    );

    await api.listThreatModels();

    expect(calls[0].headers.get("Authorization")).toBe("Bearer rotated-token");
  });

  it("sends no Authorization header when unauthenticated", async () => {
    const { fetchApi, calls } = stubFetch(EMPTY_LIST);
    const api = new ThreatModelsApi(
      new Configuration({ basePath: "https://tmi.test", fetchApi }),
    );

    await api.listThreatModels();

    expect(calls[0].headers.get("Authorization")).toBeNull();
  });

  it("merges configuration-level headers into every request", async () => {
    const { fetchApi, calls } = stubFetch(EMPTY_LIST);
    const api = new ThreatModelsApi(
      new Configuration({
        basePath: "https://tmi.test",
        fetchApi,
        headers: { "X-Request-Id": "abc-123" },
      }),
    );

    await api.listThreatModels();

    expect(calls[0].headers.get("X-Request-Id")).toBe("abc-123");
  });
});

describe("parameter validation", () => {
  it("rejects a missing required path parameter before issuing a request", async () => {
    const { fetchApi, calls } = stubFetch(EMPTY_LIST);
    const api = new ThreatModelsApi(
      new Configuration({ basePath: "https://tmi.test", fetchApi }),
    );

    // The generated guard runs before fetch, so no request should go out.
    await expect(
      api.getThreatModel({
        threatModelId: undefined as unknown as string,
      }),
    ).rejects.toBeInstanceOf(RequiredError);
    expect(calls).toHaveLength(0);
  });
});

describe("response handling", () => {
  it("deserialises a successful JSON body into the response model", async () => {
    const { fetchApi } = stubFetch({
      threat_models: [],
      total: 42,
      limit: 20,
      offset: 0,
    });
    const api = new ThreatModelsApi(
      new Configuration({ basePath: "https://tmi.test", fetchApi }),
    );

    const result = await api.listThreatModels();

    expect(result.total).toBe(42);
    expect(result.limit).toBe(20);
    expect(result.offset).toBe(0);
    expect(result.threat_models).toEqual([]);
  });

  it("raises ResponseError carrying the original response on a 4xx", async () => {
    const { fetchApi } = stubFetch({ error: "forbidden" }, 403);
    const api = new ThreatModelsApi(
      new Configuration({ basePath: "https://tmi.test", fetchApi }),
    );

    const error = await api.listThreatModels().catch((e: unknown) => e);

    expect(error).toBeInstanceOf(ResponseError);
    expect((error as ResponseError).response.status).toBe(403);
  });

  it("raises ResponseError on a 5xx", async () => {
    const { fetchApi } = stubFetch({ error: "boom" }, 500);
    const api = new ThreatModelsApi(
      new Configuration({ basePath: "https://tmi.test", fetchApi }),
    );

    const error = await api.listThreatModels().catch((e: unknown) => e);

    expect(error).toBeInstanceOf(ResponseError);
    expect((error as ResponseError).response.status).toBe(500);
  });
});
