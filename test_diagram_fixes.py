#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "six",
#     "certifi",
#     "python-dateutil",
#     "urllib3",
# ]
# ///
"""
Integration test to verify all OpenAPI diagram issues are resolved.

Tests:
1. DfdDiagram can be instantiated with proper type handling
2. DfdDiagramInput can be instantiated without readOnly fields
3. Both classes properly inherit from their base classes
4. Type discriminator works correctly
"""

import sys
sys.path.insert(0, 'python-client-generated')

from swagger_client.models.dfd_diagram import DfdDiagram
from swagger_client.models.dfd_diagram_input import DfdDiagramInput
from swagger_client.models.base_diagram import BaseDiagram
from swagger_client.models.base_diagram_input import BaseDiagramInput

def test_dfd_diagram_instantiation():
    """Test 1: DfdDiagram instantiation - CRITICAL BUG FIX"""
    print("Test 1: Testing DfdDiagram instantiation...")
    try:
        dfd = DfdDiagram(
            type="DFD-1.0.0",
            cells=[],
            name="Test Diagram",
            id="123e4567-e89b-12d3-a456-426614174000",
            created_at="2025-01-01T00:00:00Z",
            modified_at="2025-01-01T00:00:00Z"
        )
        assert dfd.type == "DFD-1.0.0", f"Expected type 'DFD-1.0.0', got '{dfd.type}'"
        assert dfd.name == "Test Diagram", f"Expected name 'Test Diagram', got '{dfd.name}'"
        assert dfd.cells == [], f"Expected empty cells, got {dfd.cells}"
        print("  ✓ DfdDiagram instantiation successful")
        print(f"    - type: {dfd.type}")
        print(f"    - name: {dfd.name}")
        print(f"    - cells: {dfd.cells}")
        return True
    except Exception as e:
        print(f"  ✗ FAILED: {str(e)}")
        return False


def test_dfd_diagram_input_instantiation():
    """Test 2: DfdDiagramInput instantiation without readOnly fields"""
    print("\nTest 2: Testing DfdDiagramInput instantiation (no readOnly fields)...")
    try:
        dfd_input = DfdDiagramInput(
            type="DFD-1.0.0",
            cells=[],
            name="Test Diagram Input"
            # Note: No id, created_at, modified_at, update_vector
        )
        assert dfd_input.type == "DFD-1.0.0", f"Expected type 'DFD-1.0.0', got '{dfd_input.type}'"
        assert dfd_input.name == "Test Diagram Input", f"Expected name 'Test Diagram Input', got '{dfd_input.name}'"
        assert dfd_input.cells == [], f"Expected empty cells, got {dfd_input.cells}"
        print("  ✓ DfdDiagramInput instantiation successful")
        print(f"    - type: {dfd_input.type}")
        print(f"    - name: {dfd_input.name}")
        print(f"    - No readOnly fields required")
        return True
    except Exception as e:
        print(f"  ✗ FAILED: {str(e)}")
        return False


def test_inheritance():
    """Test 3: Verify proper inheritance"""
    print("\nTest 3: Testing inheritance hierarchy...")
    try:
        dfd = DfdDiagram(type="DFD-1.0.0", cells=[], name="Test", id="test", created_at="2025-01-01T00:00:00Z", modified_at="2025-01-01T00:00:00Z")
        dfd_input = DfdDiagramInput(type="DFD-1.0.0", cells=[], name="Test Input")

        assert isinstance(dfd, BaseDiagram), "DfdDiagram should inherit from BaseDiagram"
        assert isinstance(dfd_input, BaseDiagramInput), "DfdDiagramInput should inherit from BaseDiagramInput"

        print("  ✓ Inheritance correct")
        print(f"    - DfdDiagram inherits from BaseDiagram: True")
        print(f"    - DfdDiagramInput inherits from BaseDiagramInput: True")
        return True
    except Exception as e:
        print(f"  ✗ FAILED: {str(e)}")
        return False


def test_discriminator():
    """Test 4: Verify discriminator handling"""
    print("\nTest 4: Testing discriminator (type field)...")
    try:
        dfd = DfdDiagram(type="DFD-1.0.0", cells=[], name="Test", id="test", created_at="2025-01-01T00:00:00Z", modified_at="2025-01-01T00:00:00Z")

        # Check that discriminator is set
        assert hasattr(dfd, 'discriminator'), "DfdDiagram should have discriminator attribute"

        # Verify type is correctly set and not overwritten by parent
        assert dfd.type == "DFD-1.0.0", f"Type was overwritten! Expected 'DFD-1.0.0', got '{dfd.type}'"

        print("  ✓ Discriminator handling correct")
        print(f"    - discriminator attribute exists: True")
        print(f"    - type preserved through inheritance: True")
        return True
    except Exception as e:
        print(f"  ✗ FAILED: {str(e)}")
        return False


def test_to_dict():
    """Test 5: Verify serialization works"""
    print("\nTest 5: Testing serialization to dict...")
    try:
        dfd_input = DfdDiagramInput(type="DFD-1.0.0", cells=[], name="Test Serialize")
        data_dict = dfd_input.to_dict()

        assert 'type' in data_dict, "Serialized dict should contain 'type'"
        assert data_dict['type'] == "DFD-1.0.0", f"Expected type 'DFD-1.0.0' in dict, got '{data_dict.get('type')}'"
        assert 'name' in data_dict, "Serialized dict should contain 'name'"
        assert 'cells' in data_dict, "Serialized dict should contain 'cells'"

        # Verify readOnly fields are NOT in the input object
        assert 'id' not in data_dict or data_dict['id'] is None, "DfdDiagramInput should not have 'id'"
        assert 'created_at' not in data_dict or data_dict['created_at'] is None, "DfdDiagramInput should not have 'created_at'"

        print("  ✓ Serialization works correctly")
        print(f"    - to_dict() contains: {list(data_dict.keys())}")
        return True
    except Exception as e:
        print(f"  ✗ FAILED: {str(e)}")
        return False


def main():
    print("=" * 70)
    print("TMI OpenAPI Client - Diagram Fixes Verification")
    print("=" * 70)

    results = []
    results.append(test_dfd_diagram_instantiation())
    results.append(test_dfd_diagram_input_instantiation())
    results.append(test_inheritance())
    results.append(test_discriminator())
    results.append(test_to_dict())

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    passed = sum(results)
    total = len(results)
    print(f"Tests passed: {passed}/{total}")

    if passed == total:
        print("✓ ALL TESTS PASSED - All issues resolved!")
        return 0
    else:
        print(f"✗ {total - passed} test(s) failed - Issues remain")
        return 1


if __name__ == "__main__":
    sys.exit(main())
