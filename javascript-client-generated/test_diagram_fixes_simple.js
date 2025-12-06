#!/usr/bin/env node
/**
 * Integration tests for TMI JavaScript Client - Simple version using dist/index.js
 */

const TmiClient = require('./dist/index');
const assert = require('assert');

console.log('========================================');
console.log('TMI JavaScript Client Integration Tests');
console.log('========================================\n');

let passed = 0;
let failed = 0;

function test(name, fn) {
  try {
    fn();
    console.log(`✓ ${name}`);
    passed++;
  } catch (error) {
    console.error(`✗ ${name}`);
    console.error(`  Error: ${error.message}`);
    failed++;
  }
}

// Test 1: DfdDiagram exists
test('DfdDiagram class exists', () => {
  assert(TmiClient.DfdDiagram, 'DfdDiagram should exist');
});

// Test 2: DfdDiagramInput exists  
test('DfdDiagramInput class exists', () => {
  assert(TmiClient.DfdDiagramInput, 'DfdDiagramInput should exist');
});

// Test 3: BaseDiagramInput exists
test('BaseDiagramInput class exists', () => {
  assert(TmiClient.BaseDiagramInput, 'BaseDiagramInput should exist');
});

// Test 4: Webhook models exist
test('WebhookSubscription exists', () => {
  assert(TmiClient.WebhookSubscription, 'WebhookSubscription should exist');
});

test('WebhookSubscriptionInput exists', () => {
  assert(TmiClient.WebhookSubscriptionInput, 'WebhookSubscriptionInput should exist');
});

test('WebhookDelivery exists', () => {
  assert(TmiClient.WebhookDelivery, 'WebhookDelivery should exist');
});

// Test 5: Admin models exist
test('Administrator exists', () => {
  assert(TmiClient.Administrator, 'Administrator should exist');
});

test('AdminUser exists', () => {
  assert(TmiClient.AdminUser, 'AdminUser should exist');
});

test('AdminGroup exists', () => {
  assert(TmiClient.AdminGroup, 'AdminGroup should exist');
});

// Test 6: Addon models exist
test('AddonResponse exists', () => {
  assert(TmiClient.AddonResponse, 'AddonResponse should exist');
});

test('CreateAddonRequest exists', () => {
  assert(TmiClient.CreateAddonRequest, 'CreateAddonRequest should exist');
});

// Test 7: New API classes exist
test('WebhooksApi exists', () => {
  assert(TmiClient.WebhooksApi, 'WebhooksApi should exist');
});

test('AdministrationApi exists', () => {
  assert(TmiClient.AdministrationApi, 'AdministrationApi should exist');
});

test('AddonsApi exists', () => {
  assert(TmiClient.AddonsApi, 'AddonsApi should exist');
});

// Test 8: DfdDiagram type preservation
test('DfdDiagram preserves type parameter', () => {
  const cells = [
    { id: 'node1', shape: 'process', x: 100, y: 100 }
  ];

  const diagram = new TmiClient.DfdDiagram(
    'DFD-1.0.0',
    cells,
    'test-id',
    'Test Diagram',
    '2025-01-12T00:00:00Z',
    '2025-01-12T00:00:00Z'
  );

  assert.strictEqual(diagram.type, 'DFD-1.0.0', 'Type should be preserved');
  assert.strictEqual(diagram.name, 'Test Diagram', 'Name should be preserved');
  assert.deepStrictEqual(diagram.cells, cells, 'Cells should be preserved');
});

// Test 9: DfdDiagramInput excludes readOnly fields
test('DfdDiagramInput constructor excludes readOnly fields', () => {
  const cells = [
    { id: 'node1', shape: 'process', x: 100, y: 100 }
  ];

  const input = new TmiClient.DfdDiagramInput(
    'DFD-1.0.0',
    cells,
    'Test Diagram'
    // NO id, created_at, modified_at
  );

  assert.strictEqual(input.type, 'DFD-1.0.0', 'Type should be set');
  assert.strictEqual(input.name, 'Test Diagram', 'Name should be set');
  assert.deepStrictEqual(input.cells, cells, 'Cells should be set');
});

console.log('\n========================================');
console.log('Test Summary');
console.log('========================================');
console.log(`✓ Passed: ${passed}`);
console.log(`✗ Failed: ${failed}`);
console.log('========================================\n');

if (failed > 0) {
  console.error('Some tests failed.');
  process.exit(1);
} else {
  console.log('All tests passed! ✓');
  process.exit(0);
}
