from typing import Annotated

import numpy as np
import talib
from mcp.types import ToolAnnotations
from pydantic import Field

from .types import MA_TYPE_MAP, MAType

common_tool_annotations = ToolAnnotations(readOnlyHint=True)


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
) -> dict[str, list[float]]:
    """Calculate the BBANDS (Bollinger Bands)."""
    real_nparray = np.array(real, dtype=np.float64)
    upperband, middleband, lowerband = talib.BBANDS(
        real_nparray, timeperiod, nbdevup, nbdevdn, MA_TYPE_MAP[matype]
    )
    return {
        "upperband": upperband.tolist(),
        "middleband": middleband.tolist(),
        "lowerband": lowerband.tolist(),
    }


def calculate_dema(
    real: Annotated[
        list[float], Field(description="Array of real values for EMA calculation")
    ],
    timeperiod: Annotated[
        int, Field(description="Number of periods for calculation")
    ] = 30,
) -> dict[str, list[float]]:
    """Calculate the DEMA (Double Exponential Moving Average)."""
    real_nparray = np.array(real, dtype=np.float64)
    result = talib.DEMA(real_nparray, timeperiod)
    return {
        "dema": result.tolist(),
    }


def calculate_ema(
    real: Annotated[
        list[float], Field(description="Array of real values for calculation")
    ],
    timeperiod: Annotated[
        int, Field(description="Number of periods for EMA calculation")
    ] = 30,
) -> dict[str, list[float]]:
    """Calculate the EMA (Exponential Moving Average)."""
    real_nparray = np.array(real, dtype=np.float64)
    result = talib.EMA(real_nparray, timeperiod)
    return {
        "ema": result.tolist(),
    }


def calculate_ht_trendline(
    real: Annotated[
        list[float], Field(description="Array of real values for calculation")
    ],
) -> dict[str, list[float]]:
    """Calculate the HT_TRENDLINE (Hilbert Transform - Instantaneous Trendline)."""
    real_nparray = np.array(real, dtype=np.float64)
    result = talib.HT_TRENDLINE(real_nparray)
    return {
        "ht_trendline": result.tolist(),
    }


def calculate_kama(
    real: Annotated[
        list[float], Field(description="Array of real values for calculation")
    ],
    timeperiod: Annotated[
        int, Field(description="Number of periods for calculation")
    ] = 30,
) -> dict[str, list[float]]:
    """Calculate the KAMA (Kaufman Adaptive Moving Average)."""
    real_nparray = np.array(real, dtype=np.float64)
    result = talib.KAMA(real_nparray, timeperiod)
    return {
        "kama": result.tolist(),
    }


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
) -> dict[str, list[float]]:
    """Calculate the MA (Moving Average)."""
    real_nparray = np.array(real, dtype=np.float64)
    result = talib.MA(real_nparray, timeperiod, MA_TYPE_MAP[matype])
    return {
        "ma": result.tolist(),
    }


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
        float, Field(description="Slow limit for the adaptive moving average calculation")
    ] = 0,
) -> dict[str, list[float]]:
    """Calculate the MAMA (MESA Adaptive Moving Average)."""
    real_nparray = np.array(real, dtype=np.float64)
    mama, fama = talib.MAMA(real_nparray, fastlimit, slowlimit)
    return {
        "mama": mama.tolist(),
        "fama": fama.tolist(),
    }


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
) -> dict[str, list[float]]:
    """Calculate the MAVP (Moving Average with Variable Period)."""
    real_nparray = np.array(real, dtype=np.float64)
    periods_nparray = np.array(periods, dtype=np.float64)
    # Type ignore needed due to incorrect type signature in TA-Lib
    result = talib.MAVP(
        real_nparray, periods_nparray, minperiod, maxperiod, MA_TYPE_MAP[matype]
    )  # type: ignore
    return {
        "mavp": result.tolist(),
    }


def calculate_midpoint(
    real: Annotated[
        list[float], Field(description="Array of real values for calculation")
    ],
    timeperiod: Annotated[
        int, Field(description="Number of periods for calculation")
    ] = 14,
) -> dict[str, list[float]]:
    """Calculate the MIDPOINT (MidPoint over period)."""
    real_nparray = np.array(real, dtype=np.float64)
    result = talib.MIDPOINT(real_nparray, timeperiod)
    return {
        "midpoint": result.tolist(),
    }


def calculate_midprice(
    high: Annotated[list[float], Field(description="Array of high prices")],
    low: Annotated[list[float], Field(description="Array of low prices")],
    timeperiod: Annotated[
        int, Field(description="Number of periods for calculation")
    ] = 14,
) -> dict[str, list[float]]:
    """Calculate the MIDPRICE (Midpoint Price over period)."""
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    result = talib.MIDPRICE(high_nparray, low_nparray, timeperiod)
    return {
        "midprice": result.tolist(),
    }


def calculate_sar(
    high: Annotated[list[float], Field(description="Array of high prices")],
    low: Annotated[list[float], Field(description="Array of low prices")],
    acceleration: Annotated[
        float,
        Field(description="Acceleration factor for SAR calculation (step size)"),
    ] = 0,
    maximum: Annotated[
        float, Field(description="Maximum value for the acceleration factor")
    ] = 0,
) -> dict[str, list[float]]:
    """Calculate the SAR (Parabolic SAR)."""
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    result = talib.SAR(high_nparray, low_nparray, acceleration, maximum)
    return {
        "sar": result.tolist(),
    }


def calculate_sarext(
    high: Annotated[list[float], Field(description="Array of high prices")],
    low: Annotated[list[float], Field(description="Array of low prices")],
    startvalue: Annotated[float, Field(description="Start value for SAR")] = 0,
    offsetonreverse: Annotated[
        float, Field(description="Offset to apply on reversal")
    ] = 0,
    accelerationinitlong: Annotated[
        float, Field(description="Initial acceleration factor for long positions")
    ] = 0,
    accelerationlong: Annotated[
        float, Field(description="Acceleration factor for long positions")
    ] = 0,
    accelerationmaxlong: Annotated[
        float, Field(description="Maximum acceleration factor for long positions")
    ] = 0,
    accelerationinitshort: Annotated[
        float, Field(description="Initial acceleration factor for short positions")
    ] = 0,
    accelerationshort: Annotated[
        float, Field(description="Acceleration factor for short positions")
    ] = 0,
    accelerationmaxshort: Annotated[
        float, Field(description="Maximum acceleration factor for short positions")
    ] = 0,
) -> dict[str, list[float]]:
    """Calculate the SAREXT (Parabolic SAR - Extended)."""
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


def calculate_sma(
    real: Annotated[
        list[float], Field(description="Array of real values for calculation")
    ],
    timeperiod: Annotated[
        int, Field(description="Number of periods for calculation")
    ] = 30,
) -> dict[str, list[float]]:
    """Calculate the SMA (Simple Moving Average)."""
    real_nparray = np.array(real, dtype=np.float64)
    result = talib.SMA(real_nparray, timeperiod)
    return {
        "sma": result.tolist(),
    }


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
) -> dict[str, list[float]]:
    """Calculate the T3 (Triple Exponential Moving Average (T3))."""
    real_nparray = np.array(real, dtype=np.float64)
    result = talib.T3(real_nparray, timeperiod, vfactor)
    return {
        "t3": result.tolist(),
    }


def calculate_tema(
    real: Annotated[
        list[float], Field(description="Array of real values for calculation")
    ],
    timeperiod: Annotated[
        int, Field(description="Number of periods for calculation")
    ] = 30,
) -> dict[str, list[float]]:
    """Calculate the TEMA (Triple Exponential Moving Average)."""
    real_nparray = np.array(real, dtype=np.float64)
    result = talib.TEMA(real_nparray, timeperiod)
    return {
        "tema": result.tolist(),
    }


def calculate_trima(
    real: Annotated[
        list[float], Field(description="Array of real values for calculation")
    ],
    timeperiod: Annotated[
        int, Field(description="Number of periods for calculation")
    ] = 30,
) -> dict[str, list[float]]:
    """Calculate the TRIMA (Triangular Moving Average)."""
    real_nparray = np.array(real, dtype=np.float64)
    result = talib.TRIMA(real_nparray, timeperiod)
    return {
        "trima": result.tolist(),
    }


def calculate_wma(
    real: Annotated[
        list[float], Field(description="Array of real values for calculation")
    ],
    timeperiod: Annotated[
        int, Field(description="Number of periods for calculation")
    ] = 30,
) -> dict[str, list[float]]:
    """Calculate the WMA (Weighted Moving Average)."""
    real_nparray = np.array(real, dtype=np.float64)
    result = talib.WMA(real_nparray, timeperiod)
    return {
        "wma": result.tolist(),
    }


def register_overlap_studies(mcp):
    """Register all overlap studies tools with the MCP server."""

    @mcp.tool(
        title="Calculate BBANDS",
        description="Calculate the BBANDS (Bollinger Bands)",
        annotations=common_tool_annotations,
    )
    def _bbands(
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
        return calculate_bbands(real, timeperiod, nbdevup, nbdevdn, matype)

    @mcp.tool(
        title="Calculate DEMA",
        description="Calculate the DEMA (Double Exponential Moving Average)",
        annotations=common_tool_annotations,
    )
    def _dema(
        real: Annotated[
            list[float], Field(description="Array of real values for EMA calculation")
        ],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 30,
    ):
        return calculate_dema(real, timeperiod)

    @mcp.tool(
        title="Calculate EMA",
        description="Calculate the EMA (Exponential Moving Average)",
        annotations=common_tool_annotations,
    )
    def _ema(
        real: Annotated[
            list[float], Field(description="Array of real values for calculation")
        ],
        timeperiod: Annotated[
            int, Field(description="Number of periods for EMA calculation")
        ] = 30,
    ):
        return calculate_ema(real, timeperiod)

    @mcp.tool(
        title="Calculate HT_TRENDLINE",
        description="Calculate the HT_TRENDLINE (Hilbert Transform - Instantaneous Trendline)",
        annotations=common_tool_annotations,
    )
    def _ht_trendline(
        real: Annotated[
            list[float], Field(description="Array of real values for calculation")
        ],
    ):
        return calculate_ht_trendline(real)

    @mcp.tool(
        title="Calculate KAMA",
        description="Calculate the KAMA (Kaufman Adaptive Moving Average)",
        annotations=common_tool_annotations,
    )
    def _kama(
        real: Annotated[
            list[float], Field(description="Array of real values for calculation")
        ],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 30,
    ):
        return calculate_kama(real, timeperiod)

    @mcp.tool(
        title="Calculate MA",
        description="Calculate the MA (Moving Average)",
        annotations=common_tool_annotations,
    )
    def _ma(
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
        return calculate_ma(real, timeperiod, matype)

    @mcp.tool(
        title="Calculate MAMA",
        description="Calculate the MAMA (MESA Adaptive Moving Average)",
        annotations=common_tool_annotations,
    )
    def _mama(
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
            float, Field(description="Slow limit for the adaptive moving average calculation")
        ] = 0,
    ):
        return calculate_mama(real, fastlimit, slowlimit)

    @mcp.tool(
        title="Calculate MAVP",
        description="Calculate the MAVP (Moving Average with Variable Period)",
        annotations=common_tool_annotations,
    )
    def _mavp(
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
        return calculate_mavp(real, periods, minperiod, maxperiod, matype)

    @mcp.tool(
        title="Calculate MIDPOINT",
        description="Calculate the MIDPOINT (MidPoint over period)",
        annotations=common_tool_annotations,
    )
    def _midpoint(
        real: Annotated[
            list[float], Field(description="Array of real values for calculation")
        ],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 14,
    ):
        return calculate_midpoint(real, timeperiod)

    @mcp.tool(
        title="Calculate MIDPRICE",
        description="Calculate the MIDPRICE (Midpoint Price over period)",
        annotations=common_tool_annotations,
    )
    def _midprice(
        high: Annotated[list[float], Field(description="Array of high prices")],
        low: Annotated[list[float], Field(description="Array of low prices")],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 14,
    ):
        return calculate_midprice(high, low, timeperiod)

    @mcp.tool(
        title="Calculate SAR",
        description="Calculate the SAR (Parabolic SAR)",
        annotations=common_tool_annotations,
    )
    def _sar(
        high: Annotated[list[float], Field(description="Array of high prices")],
        low: Annotated[list[float], Field(description="Array of low prices")],
        acceleration: Annotated[
            float,
            Field(description="Acceleration factor for SAR calculation (step size)"),
        ] = 0,
        maximum: Annotated[
            float, Field(description="Maximum value for the acceleration factor")
        ] = 0,
    ):
        return calculate_sar(high, low, acceleration, maximum)

    @mcp.tool(
        title="Calculate SAREXT",
        description="Calculate the SAREXT (Parabolic SAR - Extended)",
        annotations=common_tool_annotations,
    )
    def _sarext(
        high: Annotated[list[float], Field(description="Array of high prices")],
        low: Annotated[list[float], Field(description="Array of low prices")],
        startvalue: Annotated[float, Field(description="Start value for SAR")] = 0,
        offsetonreverse: Annotated[
            float, Field(description="Offset to apply on reversal")
        ] = 0,
        accelerationinitlong: Annotated[
            float, Field(description="Initial acceleration factor for long positions")
        ] = 0,
        accelerationlong: Annotated[
            float, Field(description="Acceleration factor for long positions")
        ] = 0,
        accelerationmaxlong: Annotated[
            float, Field(description="Maximum acceleration factor for long positions")
        ] = 0,
        accelerationinitshort: Annotated[
            float, Field(description="Initial acceleration factor for short positions")
        ] = 0,
        accelerationshort: Annotated[
            float, Field(description="Acceleration factor for short positions")
        ] = 0,
        accelerationmaxshort: Annotated[
            float, Field(description="Maximum acceleration factor for short positions")
        ] = 0,
    ):
        return calculate_sarext(
            high,
            low,
            startvalue,
            offsetonreverse,
            accelerationinitlong,
            accelerationlong,
            accelerationmaxlong,
            accelerationinitshort,
            accelerationshort,
            accelerationmaxshort,
        )

    @mcp.tool(
        title="Calculate SMA",
        description="Calculate the SMA (Simple Moving Average)",
        annotations=common_tool_annotations,
    )
    def _sma(
        real: Annotated[
            list[float], Field(description="Array of real values for calculation")
        ],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 30,
    ):
        return calculate_sma(real, timeperiod)

    @mcp.tool(
        title="Calculate T3",
        description="Calculate the T3 (Triple Exponential Moving Average (T3))",
        annotations=common_tool_annotations,
    )
    def _t3(
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
        return calculate_t3(real, timeperiod, vfactor)

    @mcp.tool(
        title="Calculate TEMA",
        description="Calculate the TEMA (Triple Exponential Moving Average)",
        annotations=common_tool_annotations,
    )
    def _tema(
        real: Annotated[
            list[float], Field(description="Array of real values for calculation")
        ],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 30,
    ):
        return calculate_tema(real, timeperiod)

    @mcp.tool(
        title="Calculate TRIMA",
        description="Calculate the TRIMA (Triangular Moving Average)",
        annotations=common_tool_annotations,
    )
    def _trima(
        real: Annotated[
            list[float], Field(description="Array of real values for calculation")
        ],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 30,
    ):
        return calculate_trima(real, timeperiod)

    @mcp.tool(
        title="Calculate WMA",
        description="Calculate the WMA (Weighted Moving Average)",
        annotations=common_tool_annotations,
    )
    def _wma(
        real: Annotated[
            list[float], Field(description="Array of real values for calculation")
        ],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 30,
    ):
        return calculate_wma(real, timeperiod)