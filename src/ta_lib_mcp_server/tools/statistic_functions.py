from typing import Annotated

import numpy as np
import talib
from mcp.types import ToolAnnotations
from pydantic import Field

common_tool_annotations = ToolAnnotations(readOnlyHint=True)


def calculate_beta(
    real0: Annotated[list[float], Field(description="First real data series")],
    real1: Annotated[list[float], Field(description="Second real data series")],
    timeperiod: Annotated[int, Field(description="Time period")] = 5,
):
    real0_nparray = np.array(real0, dtype=np.float64)
    real1_nparray = np.array(real1, dtype=np.float64)
    result = talib.BETA(real0_nparray, real1_nparray, timeperiod)
    return {"beta": result.tolist()}


def calculate_correl(
    real0: Annotated[list[float], Field(description="First real data series")],
    real1: Annotated[list[float], Field(description="Second real data series")],
    timeperiod: Annotated[int, Field(description="Time period")] = 30,
):
    real0_nparray = np.array(real0, dtype=np.float64)
    real1_nparray = np.array(real1, dtype=np.float64)
    result = talib.CORREL(real0_nparray, real1_nparray, timeperiod)
    return {"correl": result.tolist()}


def calculate_linearreg(
    real: Annotated[list[float], Field(description="Real data series")],
    timeperiod: Annotated[int, Field(description="Time period")] = 14,
):
    real_nparray = np.array(real, dtype=np.float64)
    result = talib.LINEARREG(real_nparray, timeperiod)
    return {"linearreg": result.tolist()}


def calculate_linearreg_angle(
    real: Annotated[list[float], Field(description="Real data series")],
    timeperiod: Annotated[int, Field(description="Time period")] = 14,
):
    real_nparray = np.array(real, dtype=np.float64)
    result = talib.LINEARREG_ANGLE(real_nparray, timeperiod)
    return {"linearreg_angle": result.tolist()}


def calculate_linearreg_intercept(
    real: Annotated[list[float], Field(description="Real data series")],
    timeperiod: Annotated[int, Field(description="Time period")] = 14,
):
    real_nparray = np.array(real, dtype=np.float64)
    result = talib.LINEARREG_INTERCEPT(real_nparray, timeperiod)
    return {"linearreg_intercept": result.tolist()}


def calculate_linearreg_slope(
    real: Annotated[list[float], Field(description="Real data series")],
    timeperiod: Annotated[int, Field(description="Time period")] = 14,
):
    real_nparray = np.array(real, dtype=np.float64)
    result = talib.LINEARREG_SLOPE(real_nparray, timeperiod)
    return {"linearreg_slope": result.tolist()}


def calculate_stddev(
    real: Annotated[list[float], Field(description="Real data series")],
    timeperiod: Annotated[int, Field(description="Time period")] = 5,
    nbdev: Annotated[int, Field(description="Number of deviations")] = 1,
):
    real_nparray = np.array(real, dtype=np.float64)
    result = talib.STDDEV(real_nparray, timeperiod, nbdev)
    return {"stddev": result.tolist()}


def calculate_tsf(
    real: Annotated[list[float], Field(description="Real data series")],
    timeperiod: Annotated[int, Field(description="Time period")] = 14,
):
    real_nparray = np.array(real, dtype=np.float64)
    result = talib.TSF(real_nparray, timeperiod)
    return {"tsf": result.tolist()}


def calculate_var(
    real: Annotated[list[float], Field(description="Real data series")],
    timeperiod: Annotated[int, Field(description="Time period")] = 5,
    nbdev: Annotated[int, Field(description="Number of deviations")] = 1,
):
    real_nparray = np.array(real, dtype=np.float64)
    result = talib.VAR(real_nparray, timeperiod, nbdev)
    return {"var": result.tolist()}


def register_statistic_functions(mcp):
    """Register all statistic function tools with the MCP server."""

    @mcp.tool(
        title="Calculate BETA",
        description="Calculate the BETA (Beta)",
        annotations=common_tool_annotations,
    )
    def _calculate_beta(
        real0: Annotated[list[float], Field(description="First real data series")],
        real1: Annotated[list[float], Field(description="Second real data series")],
        timeperiod: Annotated[int, Field(description="Time period")] = 5,
    ):
        return calculate_beta(real0, real1, timeperiod)

    @mcp.tool(
        title="Calculate CORREL",
        description="Calculate the CORREL (Pearson's Correlation Coefficient (r))",
        annotations=common_tool_annotations,
    )
    def _calculate_correl(
        real0: Annotated[list[float], Field(description="First real data series")],
        real1: Annotated[list[float], Field(description="Second real data series")],
        timeperiod: Annotated[int, Field(description="Time period")] = 30,
    ):
        return calculate_correl(real0, real1, timeperiod)

    @mcp.tool(
        title="Calculate LINEARREG",
        description="Calculate the LINEARREG (Linear Regression)",
        annotations=common_tool_annotations,
    )
    def _calculate_linearreg(
        real: Annotated[list[float], Field(description="Real data series")],
        timeperiod: Annotated[int, Field(description="Time period")] = 14,
    ):
        return calculate_linearreg(real, timeperiod)

    @mcp.tool(
        title="Calculate LINEARREG_ANGLE",
        description="Calculate the LINEARREG_ANGLE (Linear Regression Angle)",
        annotations=common_tool_annotations,
    )
    def _calculate_linearreg_angle(
        real: Annotated[list[float], Field(description="Real data series")],
        timeperiod: Annotated[int, Field(description="Time period")] = 14,
    ):
        return calculate_linearreg_angle(real, timeperiod)

    @mcp.tool(
        title="Calculate LINEARREG_INTERCEPT",
        description="Calculate the LINEARREG_INTERCEPT (Linear Regression Intercept)",
        annotations=common_tool_annotations,
    )
    def _calculate_linearreg_intercept(
        real: Annotated[list[float], Field(description="Real data series")],
        timeperiod: Annotated[int, Field(description="Time period")] = 14,
    ):
        return calculate_linearreg_intercept(real, timeperiod)

    @mcp.tool(
        title="Calculate LINEARREG_SLOPE",
        description="Calculate the LINEARREG_SLOPE (Linear Regression Slope)",
        annotations=common_tool_annotations,
    )
    def _calculate_linearreg_slope(
        real: Annotated[list[float], Field(description="Real data series")],
        timeperiod: Annotated[int, Field(description="Time period")] = 14,
    ):
        return calculate_linearreg_slope(real, timeperiod)

    @mcp.tool(
        title="Calculate STDDEV",
        description="Calculate the STDDEV (Standard Deviation)",
        annotations=common_tool_annotations,
    )
    def _calculate_stddev(
        real: Annotated[list[float], Field(description="Real data series")],
        timeperiod: Annotated[int, Field(description="Time period")] = 5,
        nbdev: Annotated[int, Field(description="Number of deviations")] = 1,
    ):
        return calculate_stddev(real, timeperiod, nbdev)

    @mcp.tool(
        title="Calculate TSF",
        description="Calculate the TSF (Time Series Forecast)",
        annotations=common_tool_annotations,
    )
    def _calculate_tsf(
        real: Annotated[list[float], Field(description="Real data series")],
        timeperiod: Annotated[int, Field(description="Time period")] = 14,
    ):
        return calculate_tsf(real, timeperiod)

    @mcp.tool(
        title="Calculate VAR",
        description="Calculate the VAR (Variance)",
        annotations=common_tool_annotations,
    )
    def _calculate_var(
        real: Annotated[list[float], Field(description="Real data series")],
        timeperiod: Annotated[int, Field(description="Time period")] = 5,
        nbdev: Annotated[int, Field(description="Number of deviations")] = 1,
    ):
        return calculate_var(real, timeperiod, nbdev)