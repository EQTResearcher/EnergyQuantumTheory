# Test Standards

## Overview

This document outlines the standards for writing and organizing tests in the project to ensure code quality, reliability, and maintainability. Tests must be clear, consistent, and comprehensive, covering all public APIs and critical functionality. These guidelines apply to all developers and contributors to ensure a unified testing approach that integrates with automated testing tools (e.g., pytest, unittest).

## Test File Naming

- Test files must start with `test_` to be recognized by testing frameworks.
- Test files should correspond directly to the source file they test. For example:
  - Source file: `density_field.py` → Test file: `test_density_field.py`
- Place test files in the `tests/` directory, mirroring the structure of the `code/` directory where applicable.

## Test Class and Function Naming

- **Test Classes**: Use the prefix `Test` followed by the name of the class or module being tested. For example:
  - For `EnergyQuantaField` class → `TestEnergyQuantaField`
- **Test Methods/Functions**: Use the prefix `test_` followed by a descriptive name of the functionality being tested. For example:
  - `test_initialization` for testing the initialization logic.
  - `test_gradient_calculation` for testing gradient computation.
- Use clear, concise names that reflect the specific behavior or edge case being tested.

## Test Structure and Requirements

All tests must include:

1. **Clear Objective**: A docstring or comment describing what the test verifies.
2. **Setup and Teardown**: Use fixtures or setup methods to prepare the test environment and clean up afterward.
3. **Assertions**: Use precise assertions to validate expected behavior.
4. **Edge Cases**: Test boundary conditions, invalid inputs, and error scenarios.
5. **Independence**: Tests must not depend on each other or external state.
6. **Reproducibility**: Tests should produce consistent results across runs.

### Example Template

Below is an example of a test class for the `EnergyQuantaField` class, demonstrating the recommended structure:

```python
import pytest
import numpy as np
from code.density_field import EnergyQuantaField

class TestEnergyQuantaField:
    """Tests for the EnergyQuantaField class functionality."""

    @pytest.fixture
    def field(self):
        """Fixture to provide a pre-initialized EnergyQuantaField instance."""
        return EnergyQuantaField(np.array([[1.0, 2.0], [3.0, 4.0]]))

    def test_initialization(self, field):
        """Test initialization of the EnergyQuantaField with valid input."""
        assert np.array_equal(field.density, np.array([[1.0, 2.0], [3.0, 4.0]]))
        assert field.density.shape == (2, 2)

    def test_initialization_invalid_input(self):
        """Test initialization with invalid input raises appropriate errors."""
        with pytest.raises(ValueError, match="Negative values not allowed"):
            EnergyQuantaField(np.array([[1.0, -2.0], [3.0, 4.0]]))
        with pytest.raises(TypeError, match="Expected np.ndarray"):
            EnergyQuantaField([[1.0, 2.0], [3.0, 4.0]])

    def test_gradient_calculation(self, field):
        """Test gradient computation for the energy field."""
        expected_gradient = np.array([[1.0, 1.0], [1.0, 1.0]])  # Example expected output
        result = field.compute_gradient()
        assert np.allclose(result, expected_gradient, atol=1e-5)
```

### Function Test Example

```python
from code.quantum_utils import calculate_quantum_flux

def test_calculate_quantum_flux():
    """Test quantum flux calculation with valid input."""
    density = [1.0, 2.0, 3.0]
    scale = 2.0
    result = calculate_quantum_flux(density, scale)
    assert result == 12.0  # Example expected output

def test_calculate_quantum_flux_invalid_input():
    """Test quantum flux calculation with invalid input raises errors."""
    with pytest.raises(ValueError, match="Negative values not allowed"):
        calculate_quantum_flux([-1.0, 2.0, 3.0])
    with pytest.raises(TypeError, match="Expected list of floats"):
        calculate_quantum_flux([1, 2, "3"])
```

## Best Practices

1. **Use Descriptive Names**: Test names should clearly indicate the functionality or scenario being tested (e.g., `test_initialization_invalid_input`).
2. **Leverage Fixtures**: Use pytest fixtures for reusable setup/teardown logic to reduce code duplication.
3. **Test Coverage**: Aim for at least 80% code coverage, prioritizing critical paths and edge cases.
4. **Mock External Dependencies**: Use libraries like `unittest.mock` to mock external services or complex dependencies.
5. **Parameterized Tests**: Use `@pytest.mark.parametrize` to test multiple input scenarios efficiently.
6. **Fast and Isolated**: Tests should run quickly and be isolated from external systems (e.g., databases, networks).
7. **Clear Assertions**: Use specific assertions (e.g., `assert np.allclose` for floating-point comparisons) and include meaningful error messages.
8. **Document Edge Cases**: Explicitly test boundary conditions, invalid inputs, and error cases.

## Tool Support

- **Testing Framework**: Use `pytest` (recommended) or `unittest` for writing and running tests.
- **Coverage Analysis**: Use `pytest-cov` to measure test coverage and identify untested code.
- **Linting and Style**: Use `flake8` or `pylint` to ensure test code adheres to style guidelines.
- **Continuous Integration**: Integrate tests with CI/CD pipelines (e.g., GitHub Actions) to run automatically on commits or pull requests.
- **Documentation Testing**: Use `doctest` to verify examples in API documentation (see `code/api-documentation.md`).

## Directory Structure

```
project/
├── code/
│   ├── density_field.py
│   └── quantum_utils.py
├── tests/
│   ├── test_density_field.py
│   └── test_quantum_utils.py
```

- Mirror the `code/` directory structure in `tests/` for clarity.
- Use `__init__.py` in the `tests/` directory to make it a Python package.

## Contribution Guidelines

- **Test Coverage for New Code**: All new or modified APIs must include corresponding tests that meet these standards.
- **Run Tests Locally**: Run `pytest` locally before submitting changes to ensure all tests pass.
- **Code Review**: During Pull Requests, reviewers must verify that tests are comprehensive and adhere to this standard.
- **Update Tests**: When updating code, ensure corresponding tests are updated to reflect changes.
- **Propose Changes**: To modify this testing standard, submit an Issue for team discussion and consensus.

## Notes

- **Avoid Fragile Tests**: Tests should not break due to minor implementation changes unless functionality changes.
- **Performance**: Ensure tests run efficiently, especially for large test suites.
- **Maintainability**: Refactor tests as needed to keep them clear and maintainable.
- **Internationalization**: If the project targets global contributors, consider providing test documentation in English (as done here).
