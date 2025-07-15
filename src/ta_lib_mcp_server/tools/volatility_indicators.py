from typing import Annotated

import numpy as np
import talib
from mcp.types import ToolAnnotations
from pydantic import Field

common_tool_annotations = ToolAnnotations(readOnlyHint=True)


def calculate_atr(
    high: Annotated[list[float], Field(description="List of high prices")],
    low: Annotated[list[float], Field(description="List of low prices")],
    close: Annotated[list[float], Field(description="List of close prices")],
    timeperiod: Annotated[int, Field(description="Number of periods")] = 14,
):
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.ATR(high_nparray, low_nparray, close_nparray, timeperiod)
    return {
        "atr": result.tolist(),
    }


def calculate_natr(
    high: Annotated[list[float], Field(description="List of high prices")],
    low: Annotated[list[float], Field(description="List of low prices")],
    close: Annotated[list[float], Field(description="List of close prices")],
    timeperiod: Annotated[int, Field(description="Number of periods")] = 14,
):
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.NATR(high_nparray, low_nparray, close_nparray, timeperiod)
    return {
        "natr": result.tolist(),
    }


def calculate_trange(
    high: Annotated[list[float], Field(description="List of high prices")],
    low: Annotated[list[float], Field(description="List of low prices")],
    close: Annotated[list[float], Field(description="List of close prices")],
):
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.TRANGE(high_nparray, low_nparray, close_nparray)
    return {
        "trange": result.tolist(),
    }


def register_volatility_indicators(mcp):
    """Register all volatility indicator tools with the MCP server."""

    @mcp.tool(
        title="Calculate ATR",
        description="Calculate the ATR (Average True Range) of high, low, and close prices.",
        annotations=common_tool_annotations,
    )
    def _calculate_atr(
        high: Annotated[list[float], Field(description="List of high prices")],
        low: Annotated[list[float], Field(description="List of low prices")],
        close: Annotated[list[float], Field(description="List of close prices")],
        timeperiod: Annotated[int, Field(description="Number of periods")] = 14,
    ):
        return calculate_atr(high, low, close, timeperiod)

    @mcp.tool(
        title="Calculate NATR",
        description="Calculate the NATR (Normalized Average True Range) of high, low, and close prices.",
        annotations=common_tool_annotations,
    )
    def _calculate_natr(
        high: Annotated[list[float], Field(description="List of high prices")],
        low: Annotated[list[float], Field(description="List of low prices")],
        close: Annotated[list[float], Field(description="List of close prices")],
        timeperiod: Annotated[int, Field(description="Number of periods")] = 14,
    ):
        return calculate_natr(high, low, close, timeperiod)

    @mcp.tool(
        title="Calculate TRANGE",
        description="Calculate the TRANGE (True Range) of high, low, and close prices.",
        annotations=common_tool_annotations,
    )
    def _calculate_trange(
        high: Annotated[list[float], Field(description="List of high prices")],
        low: Annotated[list[float], Field(description="List of low prices")],
        close: Annotated[list[float], Field(description="List of close prices")],
    ):
        return calculate_trange(high, low, close)