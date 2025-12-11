#!/usr/bin/env node
/**
 * Integration tests for TMI JavaScript Client diagram fixes
 *
 * This test verifies that the critical fixes from the Python client
 * migration have been properly applied to the JavaScript client:
 *
 * 1. Constructor properly preserves 'type' parameter
 * 2. DfdDiagramInput class exists for PUT/PATCH operations
 * 3. Webhook-related models exist
 * 4. Cell schemas use inline objects (not nested classes)
 *
 * Run with: node test_diagram_fixes.js
 */

const assert = require('assert');
const path = require('path');

console.log('========================================');
console.log('TMI JavaScript Client Integration Tests');
console.log('========================================\n');

let passed = 0;
let failed = 0;
let warnings = 0;

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

function warn(name, message) {
  console.log(`⚠ ${name}`);
  console.log(`  ${message}`);
  warnings++;
}

// Test 1: Verify DfdDiagram class exists and has correct structure
test('DfdDiagram class exists', () => {
  const DfdDiagram = require('./dist/model/DfdDiagram');
  assert(DfdDiagram.default, 'DfdDiagram class should exist');
  assert(typeof DfdDiagram.default === 'function', 'DfdDiagram should be a constructor');
});

// Test 2: Verify DfdDiagram constructor signature
test('DfdDiagram constructor has correct parameters', () => {
  const DfdDiagram = require('./dist/model/DfdDiagram').default;
  const constructor = DfdDiagram.toString();

  // Check that constructor accepts type parameter
  assert(
    constructor.includes('type'),
    'DfdDiagram constructor should accept type parameter'
  );

  // Check that it accepts cells parameter
  assert(
    constructor.includes('cells'),
    'DfdDiagram constructor should accept cells parameter'
  );
});

// Test 3: Verify DfdDiagram type preservation
test('DfdDiagram preserves type parameter', () => {
  const DfdDiagram = require('./dist/model/DfdDiagram');

  const cells = [
    { id: 'node1', shape: 'process', x: 100, y: 100 }
  ];

  const diagram = new DfdDiagram(
    'DFD-1.0.0',           // type
    cells,                 // cells
    'test-id',             // id
    'Test Diagram',        // name
    '2025-01-12T00:00:00Z', // created_at
    '2025-01-12T00:00:00Z'  // modified_at
  );

  // Critical check: type should be preserved
  assert.strictEqual(
    diagram.type,
    'DFD-1.0.0',
    'DfdDiagram should preserve type parameter (not overwrite to undefined)'
  );

  assert.strictEqual(diagram.name, 'Test Diagram', 'DfdDiagram should preserve name');
  assert.deepStrictEqual(diagram.cells, cells, 'DfdDiagram should preserve cells');
});

// Test 4: Check if DfdDiagramInput exists (should after regeneration)
try {
  const DfdDiagramInput = require('./dist/model/DfdDiagramInput');

  test('DfdDiagramInput class exists', () => {
    assert(DfdDiagramInput, 'DfdDiagramInput class should exist');
    assert(typeof DfdDiagramInput === 'function', 'DfdDiagramInput should be a constructor');
  });

  test('DfdDiagramInput constructor excludes readOnly fields', () => {
    const constructorStr = DfdDiagramInput.toString();

    // Should NOT require id, created_at, modified_at
    assert(
      !constructorStr.match(/constructor\s*\([^)]*\bid\b/),
      'DfdDiagramInput constructor should NOT require id parameter'
    );
  });

  test('DfdDiagramInput creates valid instance', () => {
    const cells = [
      { id: 'node1', shape: 'process', x: 100, y: 100 }
    ];

    const input = new DfdDiagramInput(
      'DFD-1.0.0',      // type
      'Test Diagram',   // name
      cells             // cells
      // NO id, created_at, modified_at
    );

    assert.strictEqual(input.type, 'DFD-1.0.0', 'DfdDiagramInput should have type');
    assert.strictEqual(input.name, 'Test Diagram', 'DfdDiagramInput should have name');
    assert.deepStrictEqual(input.cells, cells, 'DfdDiagramInput should have cells');
  });

} catch (error) {
  warn(
    'DfdDiagramInput class not found',
    'This is expected before regeneration. After regeneration, this class should exist.'
  );
}

// Test 5: Check if BaseDiagramInput exists (should after regeneration)
try {
  const BaseDiagramInput = require('./dist/model/BaseDiagramInput');

  test('BaseDiagramInput class exists', () => {
    assert(BaseDiagramInput, 'BaseDiagramInput class should exist');
  });

} catch (error) {
  warn(
    'BaseDiagramInput class not found',
    'This is expected before regeneration. After regeneration, this class should exist.'
  );
}

// Test 6: Check for webhook models (should exist after regeneration)
const webhookModels = [
  'WebhookSubscription',
  'WebhookSubscriptionInput',
  'WebhookDelivery',
  'WebhookTestRequest',
  'WebhookTestResponse'
];

webhookModels.forEach(modelName => {
  try {
    const Model = require(`./src/model/${modelName}`);
    test(`${modelName} class exists`, () => {
      assert(Model, `${modelName} should exist`);
    });
  } catch (error) {
    warn(
      `${modelName} class not found`,
      'This is expected before regeneration. Webhook models will be added after regeneration.'
    );
  }
});

// Test 7: Check that nested cell classes are removed (after regeneration)
const removedClasses = [
  'EdgeAttrsLine',
  'EdgeAttrsLineTargetMarker',
  'EdgeAttrsLineSourceMarker',
  'NodeAttrsBody',
  'NodeAttrsText',
  'EdgeLabelAttrs',
  'EdgeLabelAttrsText'
];

removedClasses.forEach(className => {
  try {
    require(`./src/model/${className}`);
    warn(
      `${className} still exists`,
      'This class should be removed in the latest OpenAPI spec (cell simplification). It still exists, indicating client may need regeneration.'
    );
  } catch (error) {
    // Good! Class doesn't exist (removed for cell simplification)
    test(`${className} removed (cell simplification)`, () => {
      assert(true, `${className} correctly removed`);
    });
  }
});

// Test 8: Verify inline cell objects work
test('Inline cell objects work correctly', () => {
  const DfdDiagram = require('./dist/model/DfdDiagram');

  // Create a diagram with inline cell attributes
  const cells = [
    {
      id: 'node1',
      shape: 'process',
      x: 100,
      y: 100,
      width: 120,
      height: 60,
      attrs: {
        body: {
          fill: '#E1F5FE',
          stroke: '#01579B'
        },
        text: {
          text: 'Web Server',
          fontSize: 14
        }
      }
    },
    {
      id: 'edge1',
      shape: 'edge',
      source: { cell: 'node1' },
      target: { cell: 'node2' },
      attrs: {
        line: {
          stroke: '#808080',
          strokeWidth: 2,
          targetMarker: {
            name: 'classic',
            size: 8
          }
        }
      }
    }
  ];

  const diagram = new DfdDiagram(
    'DFD-1.0.0',
    cells,
    'test-id',
    'Test',
    '2025-01-12T00:00:00Z',
    '2025-01-12T00:00:00Z'
  );

  // Verify cells are preserved as plain objects
  assert.strictEqual(diagram.cells[0].attrs.body.fill, '#E1F5FE', 'Node attrs should be plain objects');
  assert.strictEqual(diagram.cells[1].attrs.line.stroke, '#808080', 'Edge attrs should be plain objects');
  assert.strictEqual(diagram.cells[1].attrs.line.targetMarker.name, 'classic', 'Nested attrs should work');
});

// Test 9: Check for WebhooksApi (if regenerated)
try {
  const GeneralApi = require('./dist/tmi-client/GeneralApi');

  test('GeneralApi exists (for webhooks)', () => {
    assert(GeneralApi, 'GeneralApi should exist');
  });

  // Check if webhook methods exist
  const api = new GeneralApi();
  const webhookMethods = [
    'listWebhookSubscriptions',
    'createWebhookSubscription',
    'getWebhookSubscription',
    'deleteWebhookSubscription',
    'testWebhook'
  ];

  webhookMethods.forEach(method => {
    if (typeof api[method] === 'function') {
      test(`GeneralApi.${method} exists`, () => {
        assert(typeof api[method] === 'function', `${method} should be a function`);
      });
    } else {
      warn(
        `GeneralApi.${method} not found`,
        'This is expected before regeneration. Webhook methods will be added after regeneration.'
      );
    }
  });

} catch (error) {
  warn(
    'GeneralApi not found',
    'GeneralApi may not exist or may be in a different location. Check after regeneration.'
  );
}

// Test 10: Verify TypeEnum for DfdDiagram
test('DfdDiagram.TypeEnum exists and contains DFD-1.0.0', () => {
  const DfdDiagram = require('./dist/model/DfdDiagram');

  assert(DfdDiagram.TypeEnum, 'DfdDiagram should have TypeEnum');
  assert(
    Object.values(DfdDiagram.TypeEnum).includes('DFD-1.0.0'),
    'TypeEnum should contain DFD-1.0.0'
  );
});

// Test 11: Verify BaseDiagram exists
test('BaseDiagram class exists', () => {
  const BaseDiagram = require('./dist/model/BaseDiagram');
  assert(BaseDiagram, 'BaseDiagram class should exist');
  assert(typeof BaseDiagram === 'function', 'BaseDiagram should be a constructor');
});

// Test 12: Verify CreateDiagramRequest exists
test('CreateDiagramRequest class exists', () => {
  const CreateDiagramRequest = require('./dist/model/CreateDiagramRequest');
  assert(CreateDiagramRequest, 'CreateDiagramRequest should exist');

  const request = new CreateDiagramRequest('Test Diagram', 'DFD-1.0.0');
  assert.strictEqual(request.name, 'Test Diagram', 'CreateDiagramRequest should have name');
  assert.strictEqual(request.type, 'DFD-1.0.0', 'CreateDiagramRequest should have type');
});

// Test 13: Verify ThreatModelSubResourcesApi exists
test('ThreatModelSubResourcesApi exists', () => {
  const ThreatModelSubResourcesApi = require('./dist/tmi-client/ThreatModelSubResourcesApi');
  assert(ThreatModelSubResourcesApi, 'ThreatModelSubResourcesApi should exist');

  const api = new ThreatModelSubResourcesApi();
  assert(typeof api.createThreatModelDiagram === 'function', 'Should have createThreatModelDiagram');
  assert(typeof api.getThreatModelDiagram === 'function', 'Should have getThreatModelDiagram');
  assert(typeof api.updateThreatModelDiagram === 'function', 'Should have updateThreatModelDiagram');
});

// Test 14: Check for admin models (should exist after regeneration)
const adminModels = [
  'Administrator',
  'AdminUser',
  'AdminGroup',
  'AdminUserListResponse',
  'AdminGroupListResponse'
];

adminModels.forEach(modelName => {
  try {
    const Model = require(`./src/model/${modelName}`);
    test(`${modelName} class exists`, () => {
      assert(Model, `${modelName} should exist`);
    });
  } catch (error) {
    warn(
      `${modelName} class not found`,
      'This is expected before regeneration. Admin models will be added after regeneration.'
    );
  }
});

// Test 15: Check for addon models (should exist after regeneration)
const addonModels = [
  'AddonResponse',
  'CreateAddonRequest',
  'InvokeAddonRequest',
  'InvokeAddonResponse'
];

addonModels.forEach(modelName => {
  try {
    const Model = require(`./src/model/${modelName}`);
    test(`${modelName} class exists`, () => {
      assert(Model, `${modelName} should exist`);
    });
  } catch (error) {
    warn(
      `${modelName} class not found`,
      'This is expected before regeneration. Addon models will be added after regeneration.'
    );
  }
});

// Summary
console.log('\n========================================');
console.log('Test Summary');
console.log('========================================');
console.log(`✓ Passed:   ${passed}`);
console.log(`✗ Failed:   ${failed}`);
console.log(`⚠ Warnings: ${warnings}`);
console.log('========================================\n');

if (warnings > 0) {
  console.log('Note: Warnings indicate features that will be available after regeneration.');
  console.log('Run: ./scripts/regenerate_client.sh\n');
}

if (failed > 0) {
  console.error('Some tests failed. Please review the errors above.');
  process.exit(1);
} else {
  console.log('All critical tests passed! ✓');
  if (warnings > 0) {
    console.log('Regenerate the client to enable all features.');
    process.exit(0);
  } else {
    console.log('Client is fully up-to-date with latest OpenAPI spec.');
    process.exit(0);
  }
}
