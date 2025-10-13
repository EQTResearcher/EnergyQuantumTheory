# Contributing Guidelines

Welcome to contribute to this project! To ensure code quality and collaboration efficiency, please follow the guidelines below.

## Development Workflow
1. **Fork the Repository and Create a Feature Branch**  
   - Fork this repository to your GitHub account.
   - Create a new feature branch with a naming convention like `<type>/<short-description>`, e.g., `feat/energy-density` or `fix/bug-123`.
2. **Follow Code Style Guidelines**  
   - Refer to the [Code Style Guidelines](#code-style-guidelines) (e.g., `CODE_STYLE.md`) in the project root to ensure consistent code style.
   - Use linter or formatting tools (e.g., ESLint, Prettier) to check code formatting.
3. **Add Unit Tests**  
   - Write unit tests for new features or bug fixes, ensuring test coverage meets [project requirements, e.g., 80%].
   - Run `npm test` or other test commands to verify all tests pass.
4. **Update Related Documentation**  
   - Update documentation related to your changes, such as `README.md`, API documentation, or other technical documents.
   - Ensure documentation is clear, accurate, and includes example code when necessary.
5. **Submit a Pull Request (PR)**  
   - Submit your PR to the main repository's `main` branch.
   - The PR title should be concise and follow the commit message format (e.g., `feat: add quantum density field calculation module`).
   - The PR description should include:
     - The purpose and context of the changes.
     - Related Issue number (e.g., `#123`).
     - Testing and validation methods (e.g., manual testing, unit test results).
   - Ensure all CI/CD checks (e.g., lint, tests, build) pass.

## Commit Message Guidelines
Commit messages should clearly describe the changes, following the format: `<type>(<scope>): <short-description>`  
- **Type**:
  - `feat`: New feature or functionality.
  - `fix`: Bug fix.
  - `docs`: Documentation updates.
  - `style`: Code formatting changes (no functional impact, e.g., whitespace, line breaks).
  - `refactor`: Code refactoring (no new features or bug fixes).
  - `test`: Adding or modifying test cases.
  - `chore`: Changes to the build process, dependencies, or auxiliary tools.
- **Scope** (optional): A short identifier for the module, component, or feature, e.g., `energy-density`, `api`.
- **Short Description**: A concise description of the change, starting with a lowercase letter and without a trailing period.

**Examples**:
- `feat(energy): add quantum density field calculation module`
- `fix(api): resolve error in energy calculation interface`
- `docs(readme): update installation instructions`

## Code Style Guidelines
- Refer to `CODE_STYLE.md` in the project root (if available).
- Recommended tools:
  - Code formatting: Prettier, ESLint (or other language-specific tools).
  - Static analysis: SonarQube, CodeClimate.
- Run `npm run lint` or similar commands before submitting to ensure compliance with code style guidelines.

## Notes
- Ensure your code passes all CI/CD checks (e.g., lint, tests, build).
- Before submitting a PR, rebase or merge the latest `main` branch to avoid conflicts.
- If you have questions, feel free to communicate with maintainers via Issues or PRs.

Thank you for your contribution! 🚀
