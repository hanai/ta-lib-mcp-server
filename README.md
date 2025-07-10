# TA-Lib MCP Server

A Model Context Protocol (MCP) server that provides access to TA-Lib technical analysis indicators. This server enables AI assistants and other MCP clients to perform technical analysis calculations on financial data.

## Features

- **MACD (Moving Average Convergence/Divergence)**: Trend-following momentum indicator
- **RSI (Relative Strength Index)**: Momentum oscillator measuring price change speed and magnitude
- **STOCHRSI (Stochastic Relative Strength Index)**: Stochastic oscillator applied to RSI values

## Installation

```bash
uv sync
```

## Usage

The server exposes three main tools for technical analysis:

### 1. Calculate MACD

Calculates MACD with customizable fast period, slow period, and signal period.

### 2. Calculate RSI

Calculates RSI with configurable time period (default: 14).

### 3. Calculate STOCHRSI

Calculates Stochastic RSI with configurable RSI period, %K smoothing, %D smoothing, and moving average type.

## Running the Server

```bash
python server.py
```

## Dependencies

- TA-Lib: Technical analysis library
- MCP: Model Context Protocol implementation
- NumPy: Numerical computing
- Pydantic: Data validation

## License

This project is open source.
