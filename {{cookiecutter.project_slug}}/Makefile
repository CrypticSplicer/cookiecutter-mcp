.PHONY: deps tests lint help

help:
	@echo "Available targets:"
	@echo "  deps  - Install dependencies using uv"
	@echo "  tests - Run tests using uv"
	@echo "  lint  - Run linting and type checking using uv"

deps:
	uv sync  --dev

tests:
	uv run pytest -v tests/

lint:
	uv run ruff check --fix
	uv run ruff format

build:
	uv build

package: build ## Package the DXT extension
	@echo "Building DXT extension..."
	@if command -v dxt >/dev/null 2>&1; then \
		dxt pack . --output $(EXTENSION_NAME).dxt; \
		echo "Extension packaged as $(EXTENSION_NAME).dxt"; \
	else \
		echo "DXT CLI not found. Please install it and try again."; \
	fi