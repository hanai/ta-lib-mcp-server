from typing import Annotated

import numpy as np
import talib
from pydantic import Field

from mcp.types import ToolAnnotations

common_tool_annotations = ToolAnnotations(readOnlyHint=True)


def to_np_array(data):
    """Convert a list of floats to a numpy array of type float64."""
    return np.array(data, dtype=np.float64)


def calculate_ad(
    high: Annotated[list[float], Field(description="High prices")],
    low: Annotated[list[float], Field(description="Low prices")],
    close: Annotated[list[float], Field(description="Close prices")],
    volume: Annotated[list[float], Field(description="Volume")],
):
    high_nparray = to_np_array(high)
    low_nparray = to_np_array(low)
    close_nparray = to_np_array(close)
    volume_nparray = to_np_array(volume)
    result = talib.AD(high_nparray, low_nparray, close_nparray, volume_nparray)
    return {"ad": result.tolist()}


def calculate_adosc(
    high: Annotated[list[float], Field(description="High prices")],
    low: Annotated[list[float], Field(description="Low prices")],
    close: Annotated[list[float], Field(description="Close prices")],
    volume: Annotated[list[float], Field(description="Volume")],
    fastperiod: Annotated[int, Field(description="Fast period")] = 3,
    slowperiod: Annotated[int, Field(description="Slow period")] = 10,
):
    high_nparray = to_np_array(high)
    low_nparray = to_np_array(low)
    close_nparray = to_np_array(close)
    volume_nparray = to_np_array(volume)
    result = talib.ADOSC(
        high_nparray,
        low_nparray,
        close_nparray,
        volume_nparray,
        fastperiod,
        slowperiod,
    )
    return {"adosc": result.tolist()}


def calculate_obv(
    close: Annotated[list[float], Field(description="Close prices")],
    volume: Annotated[list[float], Field(description="Volume")],
):
    close_nparray = to_np_array(close)
    volume_nparray = to_np_array(volume)
    result = talib.OBV(close_nparray, volume_nparray)
    return {"obv": result.tolist()}


def register_volume_indicators(mcp):
    """Register all volume indicator tools with the MCP server."""

    @mcp.tool(
        title="Calculate AD",
        description="Calculate the AD (Chaikin A/D Line)",
        annotations=common_tool_annotations,
    )
    def _calculate_ad(
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
        volume: Annotated[list[float], Field(description="Volume")],
    ):
        return calculate_ad(high, low, close, volume)

    @mcp.tool(
        title="Calculate ADOSC",
        description="Calculate the ADOSC (Chaikin A/D Oscillator)",
        annotations=common_tool_annotations,
    )
    def _calculate_adosc(
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
        volume: Annotated[list[float], Field(description="Volume")],
        fastperiod: Annotated[int, Field(description="Fast period")] = 3,
        slowperiod: Annotated[int, Field(description="Slow period")] = 10,
    ):
        return calculate_adosc(high, low, close, volume, fastperiod, slowperiod)

    @mcp.tool(
        title="Calculate OBV",
        description="Calculate the OBV (On Balance Volume)",
        annotations=common_tool_annotations,
    )
    def _calculate_obv(
        close: Annotated[list[float], Field(description="Close prices")],
        volume: Annotated[list[float], Field(description="Volume")],
    ):
        return calculate_obv(close, volume)