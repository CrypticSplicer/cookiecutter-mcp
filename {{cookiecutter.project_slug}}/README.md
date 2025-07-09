# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Overview

This is a Model Context Protocol (MCP) server packaged as a Desktop Extension (DXT) for easy installation and integration with AI applications.

## Features

- ...

## Installation

### Prerequisites

- Python {{ cookiecutter.python_version }}+
- uv (Python package manager)

### Development Setup

1. Create and activate a virtual environment and install dependencies:
   ```bash
   make deps
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Set up pre-commit hooks:
   ```bash
   make setup-pre-commit
   ```

### Configuration

The server supports the following environment variables:

- `DEBUG_MODE`: Enable debug logging (default: false)
- `MAX_RESULTS`: Maximum number of results to return (default: 10)

### Building the Extension

To build the DXT extension:

```bash
make package
```

This will create a `{{ cookiecutter.project_slug }}.dxt` file that can be installed in compatible AI applications.

## Development

### Available Commands

- `make help`: Show available commands
- `make test`: Run tests with coverage
- `make lint`: Run linter
- `make format`: Format code
- `make type-check`: Run type checker
- `make security`: Run security checks
- `make check-all`: Run all checks
- `make clean`: Clean build artifacts
- `make package`: Build DXT extension

### Project Structure

```
{{ cookiecutter.project_slug }}/
├── manifest.json           # DXT extension manifest
├── server/
│   └── main.py            # MCP server implementation
├── tests/                 # Test files
├── pyproject.toml         # Python project configuration
├── Makefile              # Build and development commands
├── .pre-commit-config.yaml # Pre-commit hooks
└── README.md             # This file
```

### Testing

Run tests:

```bash
make tests
```

### Code Quality

This project uses several tools to maintain code quality:

- **Ruff**: Fast Python linter and formatter
- **Pre-commit**: Git hooks for code quality

To run lint :

```bash
make lint
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and quality checks: `make check-all`
5. Submit a pull request

## License

This project is licensed under the {{ cookiecutter.license }} License.

## Support

For issues and support, please visit: {{ cookiecutter.support_url }}

## Author

{{ cookiecutter.author_name }} - {{ cookiecutter.author_email }}

Project homepage: {{ cookiecutter.homepage_url }}