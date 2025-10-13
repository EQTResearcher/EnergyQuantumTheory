# API Documentation Standards

## Overview

This document defines the standards for writing documentation for all public APIs (classes, functions, and methods) in the project. The goal is to ensure **consistency**, **readability**, and **completeness** in API documentation. Adhering to these standards facilitates collaboration, improves code maintainability, and supports integration with automated documentation tools (e.g., Sphinx, MkDocs). All developers and contributors must follow these guidelines.

## Documentation Requirements

All public classes, functions, and methods must include the following in their documentation:

1. **Function Description**: A concise and clear explanation of the API's purpose and functionality.
2. **Parameter Details**: A list of all parameters, including their names, types, default values (if applicable), and descriptions.
3. **Return Value**: A description of the return value's type, content, and meaning.
4. **Exceptions**: A list of possible exceptions and their triggering conditions.
5. **Usage Examples**: At least one executable code example demonstrating typical use cases.
6. **Version Information** (optional): The API's introduction version or deprecation status.
7. **Notes** (optional): Special considerations or limitations when using the API.

### Additional Requirements
- Documentation should be written in **Markdown** format for easy rendering and readability.
- Code examples must be concise, self-contained, executable, and include necessary import statements.
- Parameter and return value types should use type annotations (e.g., Python’s `typing` module) or be explicitly described.
- For complex APIs, include **background information** or **use cases** to provide context.

## Documentation Format

Documentation should follow the structure below, preferably using Python docstring formats (e.g., Google or NumPy style) embedded in the code, compatible with extraction to external documentation (e.g., Sphinx).

### Example Template

Below is an example of a Python class with recommended documentation format:

```python
from typing import List
import numpy as np

class EnergyQuantaField:
    """
    Energy Quantum Field Computation Class

    Manages and computes physical properties of energy quantum density fields.
    Suitable for quantum physics simulations and energy field analysis.

    Attributes:
        density (np.ndarray): The current density distribution array.
    """

    def __init__(self, initial_density: np.ndarray):
        """
        Initialize the energy quantum field.

        Args:
            initial_density (np.ndarray): Initial density distribution, a 2D array of shape (n, m).

        Raises:
            ValueError: If initial_density contains negative values or has an invalid shape.
            TypeError: If initial_density is not a NumPy array.

        Examples:
            >>> import numpy as np
            >>> density = np.array([[1.0, 2.0], [3.0, 4.0]])
            >>> field = EnergyQuantaField(density)
        """
        pass

    def compute_energy(self, factor: float = 1.0) -> float:
        """
        Compute the total energy of the quantum field.

        Args:
            factor (float, optional): Energy scaling factor, defaults to 1.0.

        Returns:
            float: The total energy value.

        Raises:
            ValueError: If factor is less than 0.

        Examples:
            >>> import numpy as np
            >>> field = EnergyQuantaField(np.array([[1.0, 2.0], [3.0, 4.0]]))
            >>> energy = field.compute_energy(factor=0.5)
            >>> print(energy)
            5.0
        """
        pass
```

### Function Example

```python
def calculate_quantum_flux(density: List[float], scale: float = 1.0) -> float:
    """
    Calculate the quantum flux.

    Args:
        density (List[float]): List of quantum density values.
        scale (float, optional): Flux scaling factor, defaults to 1.0.

    Returns:
        float: The computed quantum flux.

    Raises:
        ValueError: If density contains negative values or scale is less than 0.
        TypeError: If density is not a list or contains non-numeric elements.

    Examples:
        >>> flux = calculate_quantum_flux([1.0, 2.0, 3.0], scale=2.0)
        >>> print(flux)
        12.0
    """
    pass
```

## Best Practices

1. **Be Concise**: Keep function descriptions to 1–3 sentences, avoiding unnecessary verbosity.
2. **Specify Types**: Use type annotations (e.g., `List[float]`, `np.ndarray`) or clearly describe types in the documentation.
3. **Executable Examples**: Ensure code examples are runnable in a standalone environment, including necessary imports.
4. **Detailed Exceptions**: List all possible exceptions with their triggering conditions.
5. **Multi-Language Support**: For APIs supporting multiple languages (e.g., REST APIs), provide examples in each language.
6. **Version Tracking**: Include version information (e.g., `@since 1.0.0` or `@deprecated in 2.0.0`) to track API changes.
7. **Tool Compatibility**: Ensure documentation is compatible with tools like Sphinx (supporting reStructuredText or Markdown) and regularly generate API reference manuals.
8. **Periodic Review**: Verify documentation compliance during code reviews.

## Tool Support

- **Documentation Generation**: Use Sphinx (supports reStructuredText and Markdown) or MkDocs to generate static documentation.
- **Type Checking**: Use `mypy` or `pyright` to validate type annotations.
- **Format Checking**: Use `pydocstyle` or similar tools to ensure docstrings meet standards.
- **Example Testing**: Include documentation examples in test suites (e.g., via `doctest`) to ensure accuracy.

## Notes

- **Avoid Redundancy**: Focus on describing *what* the API does, not *how* it is implemented.
- **Consistency**: Use consistent terminology (e.g., “parameters” instead of “inputs”) across all documentation.
- **Internationalization**: For projects targeting global users, consider providing an English version of the documentation.
- **Synchronized Updates**: Update documentation whenever code changes to prevent discrepancies.

## Contribution Guidelines

- When adding or modifying APIs, update documentation simultaneously and ensure compliance with this standard.
- During Pull Requests, verify documentation completeness and adherence to these guidelines in code reviews.
- To propose changes to this documentation standard, submit an Issue for team discussion and consensus.
