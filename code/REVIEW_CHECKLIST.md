# Code Review Checklist

## Overview

This document provides a standardized code review checklist to guide developers and reviewers in evaluating code quality, functionality, and documentation completeness during the code review process. The goal is to ensure that all Pull Requests (PRs) meet project standards, are functionally correct, and maintainable before merging.

## Objectives

- **Ensure Code Quality**: Adhere to coding standards for consistency and readability.
- **Verify Functionality**: Confirm that implementations meet requirements and are validated by tests.
- **Enhance Maintainability**: Use clear naming, comments, and documentation to reduce future maintenance costs.
- **Reduce Risks**: Ensure robustness by checking edge cases and error handling.

## Review Checklist

### 1. Code Quality

- [ ] **Adheres to Code Style Guidelines**
  - Code complies with project-defined style guidelines (e.g., PEP 8 or rules in `code/.pre-commit-config.yaml` using Black, Flake8).
  - Run `flake8` to ensure no unresolved style warnings.
  - Imports are sorted using `isort` per project conventions.
  - Example: Lines do not exceed 88 characters, no trailing whitespace, and files end with a single newline.

- [ ] **Includes Appropriate Comments**
  - Complex logic, algorithms, or critical code sections have clear comments explaining *what* and *why*.
  - Avoid excessive or redundant comments; keep comments concise and meaningful.
  - Example: For a complex algorithm, include comments describing its purpose and steps.

- [ ] **Clear Function and Variable Naming**
  - Functions, variables, and classes have descriptive names reflecting their purpose.
  - Use meaningful names (e.g., `calculate_quantum_flux` instead of `calc`) and avoid abbreviations or ambiguous names.
  - Follow project naming conventions (e.g., `snake_case` for functions).

- [ ] **No Duplicated Code**
  - Check for duplicated code (DRY principle: Don’t Repeat Yourself).
  - Refactor repeated logic into functions, classes, or modules to improve reusability.
  - Example: Extract repeated density calculations into a shared function in `utils.py`.

- [ ] **Clear Code Structure**
  - Functions and classes follow the Single Responsibility Principle (SRP) with focused responsibilities.
  - Files are modular, with logic organized by module (e.g., `density_field.py` contains only density field logic).
  - Code is easy to understand, avoiding overly complex nesting or long functions.

### 2. Functionality

- [ ] **Implements Specified Requirements**
  - Code fulfills the requirements outlined in the Pull Request or associated Issue.
  - Behavior aligns with the requirements document or user story without omissions or deviations.
  - Example: If the requirement specifies support for multidimensional density arrays, verify correct handling of such inputs.

- [ ] **Includes Unit Tests**
  - All new or modified public APIs have corresponding unit tests (see `code/tests/README.md`).
  - Test files use the `test_` prefix, are placed in the `tests/` directory, and match source file names.
  - Example: Tests for `density_field.py` are in `test_density_field.py`.

- [ ] **Tests Cover Critical Paths**
  - Tests cover all primary functionality paths (happy path) and key logic branches.
  - Use `pytest-cov` to verify test coverage, targeting at least 80% coverage.
  - Example: For `EnergyQuantaField`, tests should cover initialization, core computation methods, and error handling.

- [ ] **Handles Edge Cases Appropriately**
  - Tests and code address edge cases (e.g., empty inputs, negative values, oversized inputs).
  - Error scenarios raise appropriate exceptions with clear error messages.
  - Example: Verify that `EnergyQuantaField` correctly handles invalid inputs like negative density values.

- [ ] **Performance Considerations**
  - Code is optimized within reason, avoiding obvious performance bottlenecks.
  - For high-frequency calls or large datasets, verify the use of efficient algorithms or data structures.
  - Example: Ensure density calculations use NumPy optimizations instead of inefficient Python loops.

### 3. Documentation

- [ ] **Updated Relevant Documentation**
  - All affected documentation (e.g., `README.md`, user guides) is updated.
  - New features or changes are documented with usage instructions.
  - Example: If a new API method is added, update the user guide in the `docs/` directory.

- [ ] **Complete API Documentation**
  - All public classes, functions, and methods have complete documentation per `code/api-documentation.md` standards.
  - Documentation includes function description, parameters, return values, exceptions, and examples.
  - Example: Each method in `EnergyQuantaField` has a Google-style docstring.

- [ ] **Executable Example Code**
  - Code examples in documentation are executable and verified (e.g., using `doctest`).
  - Examples are concise, clear, and cover typical use cases and key scenarios.
  - Example: Ensure `calculate_quantum_flux` examples run correctly and produce expected results.

### 4. Additional Checks

- [ ] **Automated Tools Pass**
  - All pre-commit hooks pass (see `code/development-tools.md`).
  - Run `pre-commit run --all-files` with no errors.
  - Example: Black formatting, Flake8 checks, and isort sorting complete without issues.

- [ ] **Tests Pass**
  - Run `pytest tests/` to ensure all tests pass with no failures or skips.
  - Test coverage report (`pytest-cov`) confirms critical code is covered.
  - Example: Verify that CI pipeline test results are all green.

- [ ] **Compatibility**
  - Code is compatible with the project’s target Python version (recommended: 3.10 or higher) and dependencies.
  - Ensure no breaking changes to existing functionality.
  - Example: Confirm new code is compatible with the target NumPy version.

- [ ] **Security**
  - Check for potential security issues (e.g., unvalidated inputs, sensitive data exposure).
  - For external inputs, verify proper sanitization and validation.
  - Example: Ensure `initial_density` inputs are validated to prevent malicious inputs.

## Review Process

1. **Submit Pull Request**:
   - Submitters must ensure code passes all automated checks (pre-commit, pytest, mypy).
   - Include a description of changes, implemented features, and test coverage in the Pull Request.
   - Link to relevant Issues or requirement documents.

2. **Reviewer Responsibilities**:
   - Review each checklist item to ensure all requirements are met.
   - Verify code logic, test coverage, and documentation completeness.
   - Provide specific, constructive feedback, identifying issues and suggesting improvements.

3. **Iterative Refinement**:
   - Submitters revise code based on review feedback, rerun checks, and update the Pull Request.
   - Conduct multiple reviews if needed until all issues are resolved.

4. **Merge Code**:
   - Only Pull Requests passing all checklist items can be merged into the main branch.
   - Require approval from at least one reviewer before merging.

## Best Practices

- **Clear Communication**: Maintain clear, respectful communication in Pull Requests to streamline the review process.
- **Small, Focused Changes**: Submit small, focused Pull Requests to reduce review effort.
- **Automation First**: Rely on automated tools (e.g., pre-commit, CI pipelines) to catch common issues, allowing reviewers to focus on logic and design.
- **Document Decisions**: Record discussions and decisions for complex changes or contentious points.
- **Continuous Improvement**: Periodically review this checklist’s relevance and propose improvements via Issues.

## Notes

- **Avoid Subjective Style Debates**: Prioritize automated tool rules (e.g., Black) to minimize subjective disputes.
- **Focus on Maintainability**: Consider future maintenance effort during reviews.
- **Test-Driven**: Code without tests is generally not approved unless justified.
- **Internationalization**: For projects targeting global contributors, consider providing an English version of this checklist.

## Project Directory Structure

```
project/
├── code/
│   ├── .pre-commit-config.yaml
│   ├── density_field.py
│   ├── quantum_utils.py
│   ├── api-documentation.md
│   ├── tests/
│   │   ├── test_density_field.py
│   │   └── test_quantum_utils.py
│   └── REVIEW_CHECKLIST.md
├── docs/
├── pyproject.toml
├── pytest.ini
```
