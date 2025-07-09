#!/usr/bin/env python3
"""
{{ cookiecutter.project_name }} - MCP Server
{{ cookiecutter.project_description }}

This server demonstrates basic MCP functionality with tools and resources.
"""

from typing import Annotated

from fastmcp import FastMCP
from pydantic import Field

mcp = FastMCP(
    name="{{ cookiecutter.project_slug }}",
    version="{{ cookiecutter.version }}"
)

# Example tool
@mcp.tool
def add(a: Annotated[int, Field(description="A number.")],
        b: Annotated[int, Field(description="A number.")]) -> int:
    """Adds two integer numbers together."""
    return a + b

# Example static resource
@mcp.resource("resource://config")
def get_config() -> dict:
    """Provides the application's configuration."""
    return {"version": "1.0", "author": "MyTeam"}

# Example dynamic resource template
@mcp.resource("greetings://{name}")
def personalized_greeting(name: Annotated[str, Field(description="The name to greet.")]) -> str:
    """Generates a personalized greeting for the given name."""
    return f"Hello, {name}! Welcome to the MCP server."


if __name__ == "__main__":
    mcp.run()