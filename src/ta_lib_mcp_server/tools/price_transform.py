from typing import Annotated

import numpy as np
import talib
from mcp.types import ToolAnnotations
from pydantic import Field

common_tool_annotations = ToolAnnotations(readOnlyHint=True)


def calculate_avgprice(
    open: Annotated[list[float], Field(description="Open prices")],
    high: Annotated[list[float], Field(description="High prices")],
    low: Annotated[list[float], Field(description="Low prices")],
    close: Annotated[list[float], Field(description="Close prices")],
):
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.AVGPRICE(open_nparray, high_nparray, low_nparray, close_nparray)
    return {"avgprice": result.tolist()}


def calculate_medprice(
    high: Annotated[list[float], Field(description="High prices")],
    low: Annotated[list[float], Field(description="Low prices")],
):
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    result = talib.MEDPRICE(high_nparray, low_nparray)
    return {"medprice": result.tolist()}


def calculate_typprice(
    high: Annotated[list[float], Field(description="High prices")],
    low: Annotated[list[float], Field(description="Low prices")],
    close: Annotated[list[float], Field(description="Close prices")],
):
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.TYPPRICE(high_nparray, low_nparray, close_nparray)
    return {"typprice": result.tolist()}


def calculate_wclprice(
    high: Annotated[list[float], Field(description="High prices")],
    low: Annotated[list[float], Field(description="Low prices")],
    close: Annotated[list[float], Field(description="Close prices")],
):
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.WCLPRICE(high_nparray, low_nparray, close_nparray)
    return {"wclprice": result.tolist()}


def register_price_transform(mcp):
    """Register all price transform tools with the MCP server."""

    @mcp.tool(
        title="Calculate AVGPRICE",
        description="Calculate the AVGPRICE (Average Price)",
        annotations=common_tool_annotations,
    )
    def _calculate_avgprice(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_avgprice(open, high, low, close)

    @mcp.tool(
        title="Calculate MEDPRICE",
        description="Calculate the MEDPRICE (Median Price)",
        annotations=common_tool_annotations,
    )
    def _calculate_medprice(
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
    ):
        return calculate_medprice(high, low)

    @mcp.tool(
        title="Calculate TYPPRICE",
        description="Calculate the TYPPRICE (Typical Price)",
        annotations=common_tool_annotations,
    )
    def _calculate_typprice(
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_typprice(high, low, close)

    @mcp.tool(
        title="Calculate WCLPRICE",
        description="Calculate the WCLPRICE (Weighted Close Price)",
        annotations=common_tool_annotations,
    )
    def _calculate_wclprice(
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_wclprice(high, low, close)
