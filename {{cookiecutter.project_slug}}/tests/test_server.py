"""Tests for the MCP server implementation."""

import pytest
from fastmcp import Client

from server.main import mcp

@pytest.fixture()
def mcp_server():
    return mcp


async def test_tool_functionality(mcp_server):
    # Pass the server directly to the Client constructor
    async with Client(mcp_server) as client:
        result = await client.call_tool("add", {"a": 1, "b": 2})
        assert result.data == 3