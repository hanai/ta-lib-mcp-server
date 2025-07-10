from typing import Annotated

import numpy as np
import talib
from mcp.types import ToolAnnotations
from pydantic import Field

from .types import MA_TYPE_MAP, MAType

common_tool_annotations = ToolAnnotations(readOnlyHint=True)


def register_overlap_studies(mcp):
    """Register all overlap studies tools with the MCP server."""

    @mcp.tool(
        title="Calculate BBANDS",
        description="Calculate the BBANDS (Bollinger Bands)",
        annotations=common_tool_annotations,
    )
    def calculate_bbands(
        real: Annotated[
            list[float], Field(description="Array of real values for calculation")
        ],
        timeperiod: Annotated[
            int, Field(description="Number of periods for Bollinger Bands calculation")
        ] = 5,
        nbdevup: Annotated[
            float, Field(description="Number of standard deviations for upper band")
        ] = 2,
        nbdevdn: Annotated[
            float, Field(description="Number of standard deviations for lower band")
        ] = 2,
        matype: Annotated[
            MAType,
            Field(description="Moving average type for calculation"),
        ] = "SMA",
    ):
        real_nparray = np.array(real, dtype=np.float64)
        upperband, middleband, lowerband = talib.BBANDS(
            real_nparray, timeperiod, nbdevup, nbdevdn, MA_TYPE_MAP[matype]
        )
        return {
            "upperband": upperband.tolist(),
            "middleband": middleband.tolist(),
            "lowerband": lowerband.tolist(),
        }

    @mcp.tool(
        title="Calculate DEMA",
        description="Calculate the DEMA (Double Exponential Moving Average)",
        annotations=common_tool_annotations,
    )
    def calculate_dema(
        real: Annotated[
            list[float], Field(description="Array of real values for EMA calculation")
        ],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 30,
    ):
        real_nparray = np.array(real, dtype=np.float64)
        result = talib.DEMA(real_nparray, timeperiod)
        return {
            "dema": result.tolist(),
        }

    @mcp.tool(
        title="Calculate EMA",
        description="Calculate the EMA (Exponential Moving Average)",
        annotations=common_tool_annotations,
    )
    def calculate_ema(
        real: Annotated[list[float], Field(description="")],
        timeperiod: Annotated[
            int, Field(description="Number of periods for EMA calculation")
        ] = 30,
    ):
        real_nparray = np.array(real, dtype=np.float64)
        result = talib.EMA(real_nparray, timeperiod)
        return {
            "ema": result.tolist(),
        }

    @mcp.tool(
        title="Calculate HT_TRENDLINE",
        description="Calculate the HT_TRENDLINE (Hilbert Transform - Instantaneous Trendline)",
        annotations=common_tool_annotations,
    )
    def calculate_ht_trendline(
        real: Annotated[
            list[float], Field(description="Array of real values for calculation")
        ],
    ):
        real_nparray = np.array(real, dtype=np.float64)
        result = talib.HT_TRENDLINE(real_nparray)
        return {
            "ht_trendline": result.tolist(),
        }

    @mcp.tool(
        title="Calculate KAMA",
        description="Calculate the KAMA (Kaufman Adaptive Moving Average)",
        annotations=common_tool_annotations,
    )
    def calculate_kama(
        real: Annotated[
            list[float], Field(description="Array of real values for calculation")
        ],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 30,
    ):
        real_nparray = np.array(real, dtype=np.float64)
        result = talib.KAMA(real_nparray, timeperiod)
        return {
            "kama": result.tolist(),
        }

    @mcp.tool(
        title="Calculate MA",
        description="Calculate the MA (Moving Average)",
        annotations=common_tool_annotations,
    )
    def calculate_ma(
        real: Annotated[
            list[float], Field(description="Array of real values for calculation")
        ],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 30,
        matype: Annotated[
            MAType,
            Field(description="Moving average type for calculation"),
        ] = "SMA",
    ):
        real_nparray = np.array(real, dtype=np.float64)
        result = talib.MA(real_nparray, timeperiod, MA_TYPE_MAP[matype])
        return {
            "ma": result.tolist(),
        }

    @mcp.tool(
        title="Calculate MAMA",
        description="Calculate the MAMA (MESA Adaptive Moving Average)",
        annotations=common_tool_annotations,
    )
    def calculate_mama(
        real: Annotated[
            list[float], Field(description="Array of real values for calculation")
        ],
        fastlimit: Annotated[
            float,
            Field(
                description="Upper limit for the adaptive factor in MAMA calculation"
            ),
        ] = 0,
        slowlimit: Annotated[
            float,
            Field(description="Slow limit for the adaptive moving average calculation"),
        ] = 0,
    ):
        real_nparray = np.array(real, dtype=np.float64)
        mama, fama = talib.MAMA(real_nparray, fastlimit, slowlimit)
        return {
            "mama": mama.tolist(),
            "fama": fama.tolist(),
        }

    @mcp.tool(
        title="Calculate MAVP",
        description="Calculate the MAVP (Moving Average with Variable Period)",
        annotations=common_tool_annotations,
    )
    def calculate_mavp(
        real: Annotated[
            list[float], Field(description="Array of real values for calculation")
        ],
        periods: Annotated[list[float], Field(description="Array of period values")],
        minperiod: Annotated[
            int, Field(description="Minimum period for the moving average calculation")
        ] = 2,
        maxperiod: Annotated[
            int,
            Field(
                description="Maximum period value for variable period moving average calculation"
            ),
        ] = 30,
        matype: Annotated[
            MAType,
            Field(description="Moving average type for calculation"),
        ] = "SMA",
    ):
        real_nparray = np.array(real, dtype=np.float64)
        periods_nparray = np.array(periods, dtype=np.float64)
        # Type ignore needed due to incorrect type signature in TA-Lib
        result = talib.MAVP(
            real_nparray, periods_nparray, minperiod, maxperiod, MA_TYPE_MAP[matype]
        )  # type: ignore
        return {
            "mavp": result.tolist(),
        }

    @mcp.tool(
        title="Calculate MIDPOINT",
        description="Calculate the MIDPOINT (MidPoint over period)",
        annotations=common_tool_annotations,
    )
    def calculate_midpoint(
        real: Annotated[
            list[float], Field(description="Array of real values for calculation")
        ],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 14,
    ):
        real_nparray = np.array(real, dtype=np.float64)
        result = talib.MIDPOINT(real_nparray, timeperiod)
        return {
            "midpoint": result.tolist(),
        }

    @mcp.tool(
        title="Calculate MIDPRICE",
        description="Calculate the MIDPRICE (Midpoint Price over period)",
        annotations=common_tool_annotations,
    )
    def calculate_midprice(
        high: Annotated[list[float], Field(description="Array of high prices")],
        low: Annotated[list[float], Field(description="Array of low prices")],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 14,
    ):
        high_nparray = np.array(high, dtype=np.float64)
        low_nparray = np.array(low, dtype=np.float64)
        result = talib.MIDPRICE(high_nparray, low_nparray, timeperiod)
        return {
            "midprice": result.tolist(),
        }

    @mcp.tool(
        title="Calculate SAR",
        description="Calculate the SAR (Parabolic SAR)",
        annotations=common_tool_annotations,
    )
    def calculate_sar(
        high: Annotated[list[float], Field(description="Array of high prices")],
        low: Annotated[list[float], Field(description="Array of low prices")],
        acceleration: Annotated[
            float,
            Field(description="Acceleration factor for SAR calculation (step size)"),
        ] = 0,
        maximum: Annotated[float, Field(description="")] = 0,
    ):
        high_nparray = np.array(high, dtype=np.float64)
        low_nparray = np.array(low, dtype=np.float64)
        result = talib.SAR(high_nparray, low_nparray, acceleration, maximum)
        return {
            "sar": result.tolist(),
        }

    @mcp.tool(
        title="Calculate SAREXT",
        description="Calculate the SAREXT (Parabolic SAR - Extended)",
        annotations=common_tool_annotations,
    )
    def calculate_sarext(
        high: Annotated[list[float], Field(description="Array of high prices")],
        low: Annotated[list[float], Field(description="Array of low prices")],
        startvalue: Annotated[float, Field(description="")] = 0,
        offsetonreverse: Annotated[float, Field(description="")] = 0,
        accelerationinitlong: Annotated[float, Field(description="")] = 0,
        accelerationlong: Annotated[float, Field(description="")] = 0,
        accelerationmaxlong: Annotated[float, Field(description="")] = 0,
        accelerationinitshort: Annotated[float, Field(description="")] = 0,
        accelerationshort: Annotated[float, Field(description="")] = 0,
        accelerationmaxshort: Annotated[float, Field(description="")] = 0,
    ):
        high_nparray = np.array(high, dtype=np.float64)
        low_nparray = np.array(low, dtype=np.float64)
        result = talib.SAREXT(
            high_nparray,
            low_nparray,
            startvalue,
            offsetonreverse,
            accelerationinitlong,
            accelerationlong,
            accelerationmaxlong,
            accelerationinitshort,
            accelerationshort,
            accelerationmaxshort,
        )
        return {
            "sarext": result.tolist(),
        }

    @mcp.tool(
        title="Calculate SMA",
        description="Calculate the SMA (Simple Moving Average)",
        annotations=common_tool_annotations,
    )
    def calculate_sma(
        real: Annotated[
            list[float], Field(description="Array of real values for calculation")
        ],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 30,
    ):
        real_nparray = np.array(real, dtype=np.float64)
        result = talib.SMA(real_nparray, timeperiod)
        return {
            "sma": result.tolist(),
        }

    @mcp.tool(
        title="Calculate T3",
        description="Calculate the T3 (Triple Exponential Moving Average (T3))",
        annotations=common_tool_annotations,
    )
    def calculate_t3(
        real: Annotated[
            list[float], Field(description="Array of real values for calculation")
        ],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 5,
        vfactor: Annotated[
            float,
            Field(
                description="Volume factor for T3 calculation (typically between 0 and 1)"
            ),
        ] = 0,
    ):
        real_nparray = np.array(real, dtype=np.float64)
        result = talib.T3(real_nparray, timeperiod, vfactor)
        return {
            "t3": result.tolist(),
        }

    @mcp.tool(
        title="Calculate TEMA",
        description="Calculate the TEMA (Triple Exponential Moving Average)",
        annotations=common_tool_annotations,
    )
    def calculate_tema(
        real: Annotated[
            list[float], Field(description="Array of real values for calculation")
        ],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 30,
    ):
        real_nparray = np.array(real, dtype=np.float64)
        result = talib.TEMA(real_nparray, timeperiod)
        return {
            "tema": result.tolist(),
        }

    @mcp.tool(
        title="Calculate TRIMA",
        description="Calculate the TRIMA (Triangular Moving Average)",
        annotations=common_tool_annotations,
    )
    def calculate_trima(
        real: Annotated[
            list[float], Field(description="Array of real values for calculation")
        ],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 30,
    ):
        real_nparray = np.array(real, dtype=np.float64)
        result = talib.TRIMA(real_nparray, timeperiod)
        return {
            "trima": result.tolist(),
        }

    @mcp.tool(
        title="Calculate WMA",
        description="Calculate the WMA (Weighted Moving Average)",
        annotations=common_tool_annotations,
    )
    def calculate_wma(
        real: Annotated[
            list[float], Field(description="Array of real values for calculation")
        ],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 30,
    ):
        real_nparray = np.array(real, dtype=np.float64)
        result = talib.WMA(real_nparray, timeperiod)
        return {
            "wma": result.tolist(),
        }
