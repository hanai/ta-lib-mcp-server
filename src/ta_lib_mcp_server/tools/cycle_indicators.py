from typing import Annotated

import numpy as np
import talib
from mcp.types import ToolAnnotations
from pydantic import Field

common_tool_annotations = ToolAnnotations(readOnlyHint=True)


def calculate_ht_dcperiod(
    real: Annotated[list[float], Field(description="Real values")],
):
    real_nparray = np.array(real, dtype=np.float64)
    result = talib.HT_DCPERIOD(real_nparray)
    return {"ht_dcperiod": result.tolist()}


def calculate_ht_dcphase(
    real: Annotated[list[float], Field(description="Real values")],
):
    real_nparray = np.array(real, dtype=np.float64)
    result = talib.HT_DCPHASE(real_nparray)
    return {"ht_dcphase": result.tolist()}


def calculate_ht_phasor(
    real: Annotated[list[float], Field(description="Real values")],
):
    real_nparray = np.array(real, dtype=np.float64)
    inphase, quadrature = talib.HT_PHASOR(real_nparray)
    return {"inphase": inphase.tolist(), "quadrature": quadrature.tolist()}


def calculate_ht_sine(
    real: Annotated[list[float], Field(description="Real values")],
):
    real_nparray = np.array(real, dtype=np.float64)
    sine, leadsine = talib.HT_SINE(real_nparray)
    return {"sine": sine.tolist(), "leadsine": leadsine.tolist()}


def calculate_ht_trendmode(
    real: Annotated[list[float], Field(description="Real values")],
):
    real_nparray = np.array(real, dtype=np.float64)
    result = talib.HT_TRENDMODE(real_nparray)
    # Type ignore needed due to incorrect type signature in TA-Lib
    return {"ht_trendmode": result.tolist()}  # type: ignore


def register_cycle_indicators(mcp):
    """Register all cycle indicator tools with the MCP server."""

    @mcp.tool(
        title="Calculate HT_DCPERIOD",
        description="Calculate the HT_DCPERIOD (Hilbert Transform - Dominant Cycle Period)",
        annotations=common_tool_annotations,
    )
    def _calculate_ht_dcperiod(
        real: Annotated[list[float], Field(description="Real values")],
    ):
        return calculate_ht_dcperiod(real)

    @mcp.tool(
        title="Calculate HT_DCPHASE",
        description="Calculate the HT_DCPHASE (Hilbert Transform - Dominant Cycle Phase)",
        annotations=common_tool_annotations,
    )
    def _calculate_ht_dcphase(
        real: Annotated[list[float], Field(description="Real values")],
    ):
        return calculate_ht_dcphase(real)

    @mcp.tool(
        title="Calculate HT_PHASOR",
        description="Calculate the HT_PHASOR (Hilbert Transform - Phasor Components)",
        annotations=common_tool_annotations,
    )
    def _calculate_ht_phasor(
        real: Annotated[list[float], Field(description="Real values")],
    ):
        return calculate_ht_phasor(real)

    @mcp.tool(
        title="Calculate HT_SINE",
        description="Calculate the HT_SINE (Hilbert Transform - SineWave)",
        annotations=common_tool_annotations,
    )
    def _calculate_ht_sine(
        real: Annotated[list[float], Field(description="Real values")],
    ):
        return calculate_ht_sine(real)

    @mcp.tool(
        title="Calculate HT_TRENDMODE",
        description="Calculate the HT_TRENDMODE (Hilbert Transform - Trend vs Cycle Mode)",
        annotations=common_tool_annotations,
    )
    def _calculate_ht_trendmode(
        real: Annotated[list[float], Field(description="Real values")],
    ):
        return calculate_ht_trendmode(real)
