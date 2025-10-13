# EQT Code Style Guidelines

## General Principles
- **Clear Comments**: All code must include clear and concise comments explaining its intent and functionality.
- **Meaningful Naming**: Use descriptive variable and function names, avoiding abbreviations or ambiguous terms.
- **Single Responsibility Principle**: Each function or module should handle a single responsibility to ensure modularity and maintainability.

## Naming Conventions
- **Variables and Functions**: Use snake_case naming, with names clearly reflecting functionality, e.g., `energy_density` instead of `ed`.
- **Constants**: Use uppercase letters with underscores between words, e.g., `MAX_FREQUENCY`.
- **Module Names**: Use short, lowercase names, avoiding underscores when possible, e.g., `eqt` instead of `eqt_module`.
- **File Naming**: Match module names, using lowercase letters and underscores, e.g., `energy_density.py`.

## Commenting Guidelines
### File Header Comment
Each source file must include a header comment describing its purpose, author, creation date, and license.

```python
"""
EQT Quantum Density Field Calculation Module
Description: Provides operations and visualization for quantum density fields
Author: [Your Name]
Created: YYYY-MM-DD
License: MIT
"""
```

### Function Comments
Each function must include a detailed docstring describing its functionality, parameters, return values, and examples.

```python
def calculate_energy_density(gradient, frequency):
    """
    Calculate the quantum density field

    Args:
        gradient (ndarray): Quantum density gradient field, in numpy array format
        frequency (float): Quantum energy frequency, in Hz

    Returns:
        ndarray: Calculated quantum density field, in numpy array format

    Raises:
        ValueError: If gradient is not a numpy array or frequency is negative

    Example:
        >>> grad = np.array([[1.0, 2.0], [3.0, 4.0]])
        >>> density = calculate_energy_density(grad, 1e14)
    """
    # Implementation code
    pass
```

### Key Algorithm Comments
Add inline comments for complex algorithms or critical logic, referencing theoretical foundations.

```python
# Use gradient descent to solve for energy minimization
# Reference: EQT theoretical formula F ∝ -∇ρ
force = -learning_rate * density_gradient
```

## Code Formatting
- **Indentation**: Use 4 spaces for indentation; avoid tabs.
- **Line Length**: Limit lines to 88 characters (per PEP 8).
- **Blank Lines**: Use 1-2 blank lines between functions, classes, or logical blocks for clarity.
- **Tools**:
  - Code Formatting: Use `black` or `Prettier` for automatic formatting.
  - Static Analysis: Use `flake8` or `pylint` to check compliance.
  - Run `python -m black .` and `python -m flake8` to ensure code meets standards.

## Error Handling
- **Exception Handling**: Use try-except to handle operations prone to failure (e.g., file I/O, external API calls).
- **Error Messages**: Provide clear error descriptions, e.g., `raise ValueError("Gradient array dimensions mismatch")`.
- **Logging**: Use the `logging` module for debugging instead of `print`.

## Testing Requirements
- Write unit tests for each feature, achieving at least 80% test coverage.
- Use `pytest` to run tests with the command `pytest tests/`.
- Tests should cover normal cases, edge cases, and error conditions.

## Example Code
Below is a complete module example demonstrating naming, commenting, and formatting standards:

```python
"""
EQT Quantum Density Field Calculation Module
Description: Provides calculation and optimization for quantum density fields
Author: [Your Name]
Created: 2025-10-14
License: MIT
"""
import numpy as np
import logging

logger = logging.getLogger(__name__)

def calculate_energy_density(gradient, frequency):
    """
    Calculate the quantum density field

    Args:
        gradient (ndarray): Quantum density gradient field, in numpy array format
        frequency (float): Quantum energy frequency, in Hz

    Returns:
        ndarray: Calculated quantum density field, in numpy array format

    Raises:
        ValueError: If gradient is not a numpy array or frequency is negative

    Example:
        >>> grad = np.array([[1.0, 2.0], [3.0, 4.0]])
        >>> density = calculate_energy_density(grad, 1e14)
    """
    if not isinstance(gradient, np.ndarray):
        raise ValueError("gradient must be a numpy array")
    if frequency < 0:
        raise ValueError("frequency must be non-negative")

    # Use gradient descent to solve for energy minimization
    # Reference: EQT theoretical formula F ∝ -∇ρ
    learning_rate = 0.01
    force = -learning_rate * gradient
    logger.debug("Calculated force field: %s", force)
    return force * frequency
```

## Notes
- **Pre-Submission Checks**: Run `black`, `flake8`, and `pytest` to ensure code formatting, compliance, and tests pass.
- **Dependency Management**: List dependencies in `requirements.txt` or `pyproject.toml` and install with `pip install -r requirements.txt`.
- **License Compliance**: Ensure code adheres to the MIT license and avoid incompatible third-party libraries.

Thank you for your contribution! Please follow these guidelines to ensure high-quality, maintainable code! 🚀
