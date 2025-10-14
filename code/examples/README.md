# Example Code Standards

## Overview

This document defines the standards for writing and organizing example code in the project, aimed at providing clear, executable code samples to demonstrate core functionality and typical use cases. Example code resides in the `code/examples/` directory and must be easy to understand, executable, and consistent with the project’s API documentation (`code/api-documentation.md`). All example code must be validated to ensure correctness and compliance with project standards.

## Objectives

- **Demonstrate Functionality**: Showcase core API usage through concise examples to help users get started quickly.
- **Reduce Learning Curve**: Provide executable code to minimize user understanding and debugging time.
- **Ensure Consistency**: Align example code with project code style, documentation, and testing standards.
- **Support Education and Outreach**: Enhance project accessibility and community engagement with high-quality examples.

## Example Code Requirements

All example code must meet the following requirements:

1. **Clear Documentation**:
   - Each example file and function must include a docstring describing its purpose and functionality.
   - Documentation should specify the code’s context, input requirements, and expected output.
   - Example: File-level docstrings describe overall purpose; function-level docstrings detail specific functionality.

2. **Executability**:
   - Example code must be standalone and executable, including all necessary import statements.
   - Avoid dependencies on external files or complex configurations.
   - Example: Use `if __name__ == "__main__":` to ensure code runs directly.

3. **Conciseness**:
   - Focus on demonstrating a single feature or use case, avoiding unnecessary complexity.
   - Keep code length between 50–100 lines, with clear logic.

4. **Consistency**:
   - Adhere to project code style (e.g., Black formatting, see `code/development-tools.md`).
   - Use naming and terminology consistent with API documentation (`code/api-documentation.md`).

5. **Validation**:
   - Example code must be validated (e.g., via `doctest` or manual execution).
   - Include expected outputs or result verification to help users confirm correctness.

6. **Coverage of Typical Use Cases**:
   - Cover core API use cases, including basic and advanced scenarios.
   - Example: Basic initialization, key computation methods, and error handling.

## Example Code Structure

Example code should be placed in the `code/examples/` directory, with file names following these rules:
- Names should reflect the example’s purpose, using lowercase with underscores (e.g., `basic_usage.py`).
- Each file should focus on a single theme or module (e.g., `EnergyQuantaField` initialization and computation).
- Optional: Use subdirectories for complex modules (e.g., `code/examples/energy_field/`).

### Example File Template

Below is an improved version of `code/examples/basic_usage.py`, demonstrating the recommended structure and style:

```python
"""
EQT Basic Usage Example

Demonstrates the basic computation workflow for the energy quantum density field,
showing how to initialize EnergyQuantaField and perform core operations.
Suitable for new users to quickly understand project functionality.

Dependencies:
    - numpy
    - eqt (project core module)
"""

import numpy as np
from eqt.core import EnergyQuantaField

def basic_calculation_example():
    """
    Basic Computation Example

    Demonstrates how to create an energy quantum field and compute its density gradient.

    Returns:
        None

    Examples:
        >&gt;&gt; import numpy as np
        &gt;&gt;&gt; from eqt.core import EnergyQuantaField
        &gt;&gt;&gt; initial_density = np.ones((10, 10))
        &gt;&gt;&gt; eq_field = EnergyQuantaField(initial_density)
        &gt;&gt;&gt; gradient = eq_field.calculate_gradient()
        &gt;&gt;&gt; print(gradient.shape)
        (10, 10)
    """
    # Initialize a uniform density field
    initial_density = np.ones((100, 100))

    # Create an EnergyQuantaField instance
    eq_field = EnergyQuantaField(initial_density)

    # Compute the density gradient
    gradient = eq_field.calculate_gradient()

    # Output results
    print(f"Density gradient shape: {gradient.shape}")
    print("Basic computation completed")

def error_handling_example():
    """
    Error Handling Example

    Demonstrates how EnergyQuantaField handles invalid inputs.

    Raises:
        ValueError: If the input density contains negative values.
        TypeError: If the input is not a NumPy array.

    Examples:
        &gt;&gt;&gt; import numpy as np
        &gt;&gt;&gt; from eqt.core import EnergyQuantaField
        &gt;&gt;&gt; invalid_density = np.array([[-1.0, 2.0], [3.0, 4.0]])
        &gt;&gt;&gt; EnergyQuantaField(invalid_density)
        Traceback (most recent call last):
            ...
        ValueError: Negative values not allowed
    """
    try:
        # Attempt to initialize with invalid density
        invalid_density = np.array([[-1.0, 2.0], [3.0, 4.0]])
        eq_field = EnergyQuantaField(invalid_density)
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print("Expected error not caught")

if __name__ == "__main__":
    basic_calculation_example()
    error_handling_example()
```

#### Improvements
- **Enhanced Documentation**: File and function docstrings are more detailed, including dependencies, return types, and error handling examples.
- **Added Error Handling**: Included `error_handling_example` to demonstrate handling of invalid inputs, improving understanding of API robustness.
- **Executability**: Includes all import statements for standalone execution.
- **Validation**: Added doctest-compatible examples for automated verification.
- **Focus**: Each function demonstrates a single feature (initialization/computation, error handling) for clarity.

### Other Recommended Examples

To comprehensively showcase project functionality, consider adding the following example files in `code/examples/`:
- `advanced_usage.py`: Demonstrates advanced features, such as multidimensional density field processing or complex workflows.
- `performance_optimization.py`: Shows performance optimization techniques (e.g., using NumPy vectorization).
- `integration_example.py`: Illustrates integration with external libraries or modules (e.g., plotting density fields with matplotlib).

Example directory structure:
```
code/examples/
├── basic_usage.py
├── advanced_usage.py
├── performance_optimization.py
└── integration_example.py
```

## Best Practices

1. **Keep It Concise**: Focus each example on a single feature, avoiding complex logic.
2. **Validate Correctness**: Use `doctest` or manual execution to verify example code.
   ```bash
   python -m doctest code/examples/basic_usage.py -v
   ```
3. **Ensure Style Consistency**: Run `pre-commit run --all-files` to ensure examples pass Black, Flake8, and other checks (see `code/development-tools.md`).
4. **User-Oriented**: Tailor examples to target users (e.g., scientists, developers) with clear inputs and outputs.
5. **Showcase Errors**: Include error-handling examples to clarify API behavior under invalid inputs.
6. **Version Information**: Note the applicable project version in docstrings (e.g., `@since 1.0.0`).
7. **Extensibility**: Use separate files or subdirectories for complex features to avoid overly long files.

## Validation and Maintenance

- **Validation Process**:
  - Before submitting, run `python code/examples/<file&gt;.py` to ensure executability.
  - Validate docstring examples using `doctest`:
    ```bash
    python -m doctest code/examples/*.py -v
    ```
  - Ensure examples pass CI pipeline checks (e.g., `pytest` or `pre-commit` in GitHub Actions).

- **Maintenance Process**:
  - Update example code when APIs change.
  - Verify example correctness and documentation consistency in Pull Requests (see `code/REVIEW_CHECKLIST.md`).
  - Periodically review examples to ensure compatibility with the latest project version.

## Contribution Guidelines

- **Adding Examples**:
  - Place new example code in `code/examples/`, following this standard.
  - In Pull Requests, describe the example’s purpose and covered use cases.
- **Review Requirements**:
  - Reviewers must verify example executability, documentation completeness, and style consistency.
  - Ensure examples pass `doctest` and pre-commit checks.
- **Updates and Removal**:
  - Update or remove examples when features change or are deprecated.
  - Submit Issues to discuss improvements or new example requirements.

## Notes

- **Minimize Dependencies**: Limit external dependencies to standard libraries or core project modules.
- **Clear Outputs**: Include print statements or other methods to display results for user verification.
- **Internationalization**: For global audiences, consider providing English versions of example code.
- **Synchronized Updates**: Keep examples consistent with API documentation and test cases (`code/tests/README.md`).

## Project Directory Structure

```
project/
├── code/
│   ├── examples/
│   │   ├── basic_usage.py
│   │   ├── advanced_usage.py
│   │   ├── performance_optimization.py
│   │   └── integration_example.py
│   ├── api-documentation.md
│   ├── development-tools.md
│   ├── tests/
│   │   ├── test_density_field.py
│   │   └── test_quantum_utils.py
│   └── REVIEW_CHECKLIST.md
├── docs/
├── pyproject.toml
├── pytest.ini
```
