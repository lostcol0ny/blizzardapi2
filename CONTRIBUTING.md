# Contributing to blizzardapi2

Thank you for your interest in contributing to blizzardapi2! This document provides guidelines and setup instructions for contributors.

## Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/lostcol0ny/blizzardapi2.git
cd blizzardapi2
```

### 2. Install Dependencies

```bash
# Using uv (recommended)
uv venv
uv pip install -e ".[dev]"

# Or using pip
pip install -e ".[dev]"
```

### 3. Setup Pre-commit Hooks (Recommended)

```bash
# Install pre-commit
pip install pre-commit

# Install the git hooks
pre-commit install
```

This will automatically format your code before each commit.

## Code Quality

### Automatic Formatting

The project uses several tools to maintain code quality:

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting

### Manual Formatting

If you need to format code manually:

```bash
# Format with Black
black .

# Sort imports
isort .

# Check linting
flake8 .
```

## GitHub Workflows

The project has several automated workflows:

1. **Format with Black**: Automatically formats code on push/PR
2. **Check Black Formatting**: Validates formatting on PRs
3. **Python Package**: Runs tests and publishes releases

### Workflow Behavior

- **On Push**: Code is automatically formatted and committed
- **On Pull Request**: Formatting is checked (but not changed)
- **On Main**: Full CI/CD pipeline runs

## Making Changes

### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Make Your Changes

Write your code and tests.

### 3. Test Your Changes

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=blizzardapi2
```

### 4. Commit Your Changes

```bash
git add .
git commit -m "feat: add your feature description"
```

The pre-commit hooks will automatically format your code.

### 5. Push and Create a Pull Request

```bash
git push origin feature/your-feature-name
```

## Commit Message Format

Use conventional commit messages:

- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation changes
- `style:` Code formatting changes
- `refactor:` Code refactoring
- `test:` Test changes
- `chore:` Maintenance tasks

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest test_project/test_wow.py

# Run with verbose output
pytest -v
```

### Writing Tests

- Place tests in the `test_project/` directory
- Use descriptive test names
- Include both positive and negative test cases
- Mock external API calls

## API Development

### Adding New Endpoints

1. Add the endpoint method to the appropriate API class
2. Add tests for the new endpoint
3. Update documentation if needed
4. Ensure proper error handling

### Import Fixes

If you encounter import issues:

- Check that classes inherit from `Api` (not `BaseApi`)
- Ensure `Locale` and `Region` are imported from `types.py`
- Verify class names are consistent (e.g., `BattlenetOAuthApi`)

## Release Process

Releases are automated through GitHub Actions:

1. Push to main branch
2. Tests run automatically
3. Version is bumped
4. Package is published to PyPI
5. GitHub release is created

## Getting Help

- Check existing issues and pull requests
- Create a new issue for bugs or feature requests
- Ask questions in discussions

## Code of Conduct

Please be respectful and inclusive in all interactions. We welcome contributors from all backgrounds and experience levels.
