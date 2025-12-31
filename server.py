from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

@mcp.tool
def ping_server() -> str:
    """Health check tool. Returns 'pong'."""
    return "pong 🟢 Server is alive"

if __name__ == "__main__":

    mcp.run(transport="http", port=8000)
