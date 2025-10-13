# Development Tools Configuration Standards

## Overview

This document defines the standards for configuring development tools in the project to enhance code quality, consistency, and development efficiency through automation. The configured tools include code formatters, static analyzers, and linters, applicable to all developers and contributors. These tools are integrated into the development workflow via pre-commit hooks and other automated processes to ensure compliance with project standards.

## Objectives

- **Code Consistency**: Ensure uniform code style using formatters like Black.
- **Code Quality**: Detect potential errors and style issues using static analysis tools like Flake8.
- **Automated Checks**: Run automated checks before code commits using pre-commit hooks to reduce manual effort.
- **Efficient Collaboration**: Standardize tool configurations to minimize learning and debugging costs for team members.

## Core Tool Configurations

### 1. Pre-commit Hooks

The `pre-commit` framework is used to manage automated checks before code commits. The configuration file is `code/.pre-commit-config.yaml`, as shown below:

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: trailing-whitespace
        name: Check Trailing Whitespace
        description: Removes trailing whitespace from code.
      - id: end-of-file-fixer
        name: Fix End of File
        description: Ensures files end with a single newline.
      - id: check-yaml
        name: Check YAML File Format
        description: Validates the syntax of YAML files.
      - id: check-added-large-files
        name: Check Large Files
        description: Prevents committing oversized files (default limit: 500KB).

  - repo: https://github.com/psf/black
    rev: 24.8.0
    hooks:
      - id: black
        name: Format Python Code
        description: Automatically formats Python code with Black for consistent style.
        language_version: python3.10

  - repo: https://github.com/pycqa/flake8
    rev: 7.1.0
    hooks:
      - id: flake8
        name: Python Static Code Analysis
        description: Checks Python code for style and potential errors using Flake8.
        args: [--max-line-length=88, --extend-ignore=E203]

  - repo: https://github.com/PyCQA/isort
    rev: 5.13.2
    hooks:
      - id: isort
        name: Sort Python Imports
        description: Automatically sorts Python import statements with isort.
        args: [--profile=black]
```

#### Configuration Notes
- **Version Updates**: Updated tool versions (e.g., `pre-commit-hooks`, `black`, `flake8`) to recent stable releases for compatibility and feature completeness.
- **Added isort**: Included `isort` to automatically sort Python imports, ensuring compatibility with Black.
- **Flake8 Parameters**: Set maximum line length to 88 (aligned with Black) and ignored `E203` (resolving Black-Flake8 conflicts in slice notation).
- **Descriptive Metadata**: Added names and descriptions for each hook to improve clarity for team members.

### 2. Other Recommended Tools

The following additional development tools are recommended, with suggested configurations:

#### 2.1 Static Type Checking
- **Tool**: `mypy`
- **Purpose**: Validates type annotations in Python code to ensure type safety.
- **Configuration File**: `pyproject.toml`
  ```toml
  [tool.mypy]
  python_version = "3.10"
  warn_return_any = true
  warn_unused_configs = true
  disallow_untyped_defs = true
  ignore_missing_imports = true
  ```
- **Run Command**: `mypy code/ tests/`

#### 2.2 Testing Framework
- **Tool**: `pytest`
- **Purpose**: Executes unit and integration tests to verify code functionality.
- **Configuration File**: `pytest.ini`
  ```ini
  [pytest]
  python_files = test_*.py
  python_functions = test_*
  addopts = --cov=code --cov-report=html
  ```
- **Run Command**: `pytest tests/`

#### 2.3 Documentation Checking
- **Tool**: `pydocstyle`
- **Purpose**: Ensures Python docstrings comply with standards (see `code/api-documentation.md`).
- **Configuration File**: `pyproject.toml`
  ```toml
  [tool.pydocstyle]
  convention = google
  add-ignore = D105,D107
  ```
- **Run Command**: `pydocstyle code/`

## Installation and Setup

### 1. Install pre-commit
```bash
pip install pre-commit
pre-commit install
```
- After installation, pre-commit hooks will run automatically on each `git commit`.
- To manually run hooks:
  ```bash
  pre-commit run --all-files
  ```

### 2. Install Other Tools
```bash
pip install black flake8 isort mypy pytest pytest-cov pydocstyle
```
- Ensure the Python version matches project requirements (Python 3.10 or higher recommended).
- Verify tool configurations by running their respective commands after installation.

### 3. Project Configuration
- Place `.pre-commit-config.yaml` in the `code/` directory.
- Place `pyproject.toml` and `pytest.ini` in the project root directory.
- Ensure tool configurations align with the project structure.

## Best Practices

1. **Automate Checks**: Always enable pre-commit hooks to ensure automated code checks before commits.
2. **Consistent Configurations**: All developers should use the same tool versions and configurations, preferably in a virtual environment (e.g., `venv` or `poetry`).
3. **Incremental Fixes**: If pre-commit detects issues, fix them and recommit; use `pre-commit run` for manual checks.
4. **CI/CD Integration**: Run pre-commit, pytest, and mypy checks in continuous integration (CI) pipelines (e.g., GitHub Actions).
   Example GitHub Actions configuration:
   ```yaml
   name: CI
   on: [push, pull_request]
   jobs:
     lint-and-test:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4
         - uses: actions/setup-python@v5
           with:
             python-version: '3.10'
         - run: pip install pre-commit pytest pytest-cov mypy
         - run: pre-commit run --all-files
         - run: pytest tests/
         - run: mypy code/ tests/
   ```
5. **Version Management**: Regularly update tool versions (e.g., Black, Flake8) and synchronize across the team.
6. **Error Handling**: Provide examples for resolving common tool errors (e.g., Flake8 style issues) to reduce debugging time.

## Contribution Guidelines

- **Tool Configuration Updates**: When adding or modifying tool configurations, update `.pre-commit-config.yaml` or related files and document changes in Pull Requests.
- **Test Tool Configurations**: Verify all tool configurations locally to ensure they do not disrupt existing workflows.
- **Code Review**: During Pull Requests, reviewers must validate the results of pre-commit and other tool checks.
- **Propose Changes**: To modify tool or configuration standards, submit an Issue for team discussion and consensus.

## Notes

- **Performance Optimization**: Avoid excessive hooks to prevent long commit times; prioritize efficient checks.
- **Compatibility**: Ensure tool versions are compatible with project dependencies to avoid conflicts.
- **Synchronized Documentation**: Update this file and related documentation (e.g., `README.md`) when tool configurations change.
- **Internationalization**: For projects targeting global contributors, consider providing an English version of this configuration document.

## Project Directory Structure

```
project/
├── code/
│   ├── .pre-commit-config.yaml
│   ├── density_field.py
│   └── quantum_utils.py
├── tests/
│   ├── test_density_field.py
│   └── test_quantum_utils.py
├── pyproject.toml
├── pytest.ini
```
