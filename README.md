# TA-Lib MCP Server

A Model Context Protocol (MCP) server that provides access to TA-Lib technical analysis indicators. This server enables AI assistants and other MCP clients to perform technical analysis calculations on financial data.

## Features

For full API reference and examples, see: [TA-Lib Python Documentation](https://ta-lib.github.io/ta-lib-python/doc_index.html)

## Usage

Add the following JSON block to your IDE MCP settings.

```json
{
  "mcp": {
    "servers": {
      "ta-lib": {
        "command": "docker",
        "args": ["run", "-i", "--rm", "ghcr.io/hanai/ta-lib-mcp-server:main"]
      }
    }
  }
}
```

## Dependencies

- TA-Lib: Technical analysis library
- MCP: Model Context Protocol implementation
- NumPy: Numerical computing
- Pydantic: Data validation

## License

This project is open source.
