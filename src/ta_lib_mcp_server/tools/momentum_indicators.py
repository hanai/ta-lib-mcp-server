from typing import Annotated

import numpy as np
import talib
from mcp.types import ToolAnnotations
from pydantic import Field

from .types import MA_TYPE_MAP, MAType

common_tool_annotations = ToolAnnotations(readOnlyHint=True)


def register_momentum_indicators(mcp):
    """Register all momentum indicator tools with the MCP server."""

    @mcp.tool(
        title="Calculate MACD",
        description="Calculate the MACD (Moving Average Convergence/Divergence) of a list of real numbers.",
        annotations=common_tool_annotations,
    )
    def calculate_macd(
        real: Annotated[
            list[float],
            Field(description="List of price values (typically closing prices)"),
        ],
        fastperiod: Annotated[int, Field(description="Period for fast EMA")] = 12,
        slowperiod: Annotated[int, Field(description="Period for slow EMA")] = 26,
        signalperiod: Annotated[
            int, Field(description="Period for signal line EMA")
        ] = 9,
    ):
        real_nparray = np.array(real, dtype=np.float64)
        macd, macdsignal, macdhist = talib.MACD(
            real_nparray, fastperiod, slowperiod, signalperiod
        )
        return {
            "macd": macd.tolist(),
            "macdsignal": macdsignal.tolist(),
            "macdhist": macdhist.tolist(),
        }

    @mcp.tool(
        title="Calculate RSI",
        description="Calculate the RSI (Relative Strength Index) of a list of real numbers.",
        annotations=common_tool_annotations,
    )
    def calculate_rsi(
        real: Annotated[
            list[float],
            Field(description="List of price values (typically closing prices)"),
        ],
        timeperiod: Annotated[
            int, Field(description="Number of periods for RSI calculation")
        ] = 14,
    ):
        real_nparray = np.array(real, dtype=np.float64)
        result = talib.RSI(real_nparray, timeperiod)
        return {"rsi": result.tolist()}

    @mcp.tool(
        title="Calculate STOCHRSI",
        description="Calculate the STOCHRSI (Stochastic Relative Strength Index) of a list of real numbers. This applies the Stochastic Oscillator formula to RSI values instead of typical price data.",
        annotations=common_tool_annotations,
    )
    def calculate_stochrsi(
        real: Annotated[
            list[float],
            Field(description="List of price values (typically closing prices)"),
        ],
        timeperiod: Annotated[
            int, Field(description="Period for RSI calculation")
        ] = 14,
        fastk_period: Annotated[
            int,
            Field(description="Period for %K smoothing in the Stochastic calculation"),
        ] = 5,
        fastd_period: Annotated[
            int,
            Field(description="Period for %D smoothing in the Stochastic calculation"),
        ] = 3,
        fastd_matype: Annotated[
            MAType,
            Field(description="Moving average type for %D calculation"),
        ] = "SMA",
    ):
        real_nparray = np.array(real, dtype=np.float64)
        fastk, fastd = talib.STOCHRSI(
            real_nparray,
            timeperiod,
            fastk_period,
            fastd_period,
            MA_TYPE_MAP[fastd_matype],
        )
        return {"fastk": fastk.tolist(), "fastd": fastd.tolist()}

    @mcp.tool(
        title="Calculate ADX",
        description="Calculate the ADX (Average Directional Movement Index)",
        annotations=common_tool_annotations,
    )
    def calculate_adx(
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 14,
    ):
        high_nparray = np.array(high, dtype=np.float64)
        low_nparray = np.array(low, dtype=np.float64)
        close_nparray = np.array(close, dtype=np.float64)
        result = talib.ADX(high_nparray, low_nparray, close_nparray, timeperiod)
        return {"adx": result.tolist()}

    @mcp.tool(
        title="Calculate ADXR",
        description="Calculate the ADXR (Average Directional Movement Index Rating)",
        annotations=common_tool_annotations,
    )
    def calculate_adxr(
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 14,
    ):
        high_nparray = np.array(high, dtype=np.float64)
        low_nparray = np.array(low, dtype=np.float64)
        close_nparray = np.array(close, dtype=np.float64)
        result = talib.ADXR(high_nparray, low_nparray, close_nparray, timeperiod)
        return {"adxr": result.tolist()}

    @mcp.tool(
        title="Calculate APO",
        description="Calculate the APO (Absolute Price Oscillator)",
        annotations=common_tool_annotations,
    )
    def calculate_apo(
        real: Annotated[list[float], Field(description="Real values")],
        fastperiod: Annotated[int, Field(description="Fast period")] = 12,
        slowperiod: Annotated[int, Field(description="Slow period")] = 26,
        matype: Annotated[MAType, Field(description="Moving average type")] = "SMA",
    ):
        real_nparray = np.array(real, dtype=np.float64)
        result = talib.APO(real_nparray, fastperiod, slowperiod, MA_TYPE_MAP[matype])
        return {"apo": result.tolist()}

    @mcp.tool(
        title="Calculate AROON",
        description="Calculate the AROON",
        annotations=common_tool_annotations,
    )
    def calculate_aroon(
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 14,
    ):
        high_nparray = np.array(high, dtype=np.float64)
        low_nparray = np.array(low, dtype=np.float64)
        aroondown, aroonup = talib.AROON(high_nparray, low_nparray, timeperiod)
        return {"aroondown": aroondown.tolist(), "aroonup": aroonup.tolist()}

    @mcp.tool(
        title="Calculate AROONOSC",
        description="Calculate the AROONOSC (Aroon Oscillator)",
        annotations=common_tool_annotations,
    )
    def calculate_aroonosc(
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 14,
    ):
        high_nparray = np.array(high, dtype=np.float64)
        low_nparray = np.array(low, dtype=np.float64)
        result = talib.AROONOSC(high_nparray, low_nparray, timeperiod)
        return {"aroonosc": result.tolist()}

    @mcp.tool(
        title="Calculate BOP",
        description="Calculate the BOP (Balance Of Power)",
        annotations=common_tool_annotations,
    )
    def calculate_bop(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        open_nparray = np.array(open, dtype=np.float64)
        high_nparray = np.array(high, dtype=np.float64)
        low_nparray = np.array(low, dtype=np.float64)
        close_nparray = np.array(close, dtype=np.float64)
        result = talib.BOP(open_nparray, high_nparray, low_nparray, close_nparray)
        return {"bop": result.tolist()}

    @mcp.tool(
        title="Calculate CCI",
        description="Calculate the CCI (Commodity Channel Index)",
        annotations=common_tool_annotations,
    )
    def calculate_cci(
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 14,
    ):
        high_nparray = np.array(high, dtype=np.float64)
        low_nparray = np.array(low, dtype=np.float64)
        close_nparray = np.array(close, dtype=np.float64)
        result = talib.CCI(high_nparray, low_nparray, close_nparray, timeperiod)
        return {"cci": result.tolist()}

    @mcp.tool(
        title="Calculate CMO",
        description="Calculate the CMO (Chande Momentum Oscillator)",
        annotations=common_tool_annotations,
    )
    def calculate_cmo(
        real: Annotated[list[float], Field(description="Real values")],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 14,
    ):
        real_nparray = np.array(real, dtype=np.float64)
        result = talib.CMO(real_nparray, timeperiod)
        return {"cmo": result.tolist()}

    @mcp.tool(
        title="Calculate DX",
        description="Calculate the DX (Directional Movement Index)",
        annotations=common_tool_annotations,
    )
    def calculate_dx(
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 14,
    ):
        high_nparray = np.array(high, dtype=np.float64)
        low_nparray = np.array(low, dtype=np.float64)
        close_nparray = np.array(close, dtype=np.float64)
        result = talib.DX(high_nparray, low_nparray, close_nparray, timeperiod)
        return {"dx": result.tolist()}

    @mcp.tool(
        title="Calculate MACDEXT",
        description="Calculate the MACDEXT (MACD with controllable MA type)",
        annotations=common_tool_annotations,
    )
    def calculate_macdext(
        real: Annotated[list[float], Field(description="Real values")],
        fastperiod: Annotated[int, Field(description="Fast period")] = 12,
        fastmatype: Annotated[MAType, Field(description="Fast MA type")] = "SMA",
        slowperiod: Annotated[int, Field(description="Slow period")] = 26,
        slowmatype: Annotated[MAType, Field(description="Slow MA type")] = "SMA",
        signalperiod: Annotated[int, Field(description="Signal period")] = 9,
        signalmatype: Annotated[MAType, Field(description="Signal MA type")] = "SMA",
    ):
        real_nparray = np.array(real, dtype=np.float64)
        macd, macdsignal, macdhist = talib.MACDEXT(
            real_nparray,
            fastperiod,
            MA_TYPE_MAP[fastmatype],
            slowperiod,
            MA_TYPE_MAP[slowmatype],
            signalperiod,
            MA_TYPE_MAP[signalmatype],
        )
        return {
            "macd": macd.tolist(),
            "macdsignal": macdsignal.tolist(),
            "macdhist": macdhist.tolist(),
        }

    @mcp.tool(
        title="Calculate MACDFIX",
        description="Calculate the MACDFIX (Moving Average Convergence/Divergence Fix 12/26)",
        annotations=common_tool_annotations,
    )
    def calculate_macdfix(
        real: Annotated[list[float], Field(description="Real values")],
        signalperiod: Annotated[int, Field(description="Signal period")] = 9,
    ):
        real_nparray = np.array(real, dtype=np.float64)
        macd, macdsignal, macdhist = talib.MACDFIX(real_nparray, signalperiod)
        return {
            "macd": macd.tolist(),
            "macdsignal": macdsignal.tolist(),
            "macdhist": macdhist.tolist(),
        }

    @mcp.tool(
        title="Calculate MFI",
        description="Calculate the MFI (Money Flow Index)",
        annotations=common_tool_annotations,
    )
    def calculate_mfi(
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
        volume: Annotated[list[float], Field(description="Volume")],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 14,
    ):
        high_nparray = np.array(high, dtype=np.float64)
        low_nparray = np.array(low, dtype=np.float64)
        close_nparray = np.array(close, dtype=np.float64)
        volume_nparray = np.array(volume, dtype=np.float64)
        result = talib.MFI(
            high_nparray, low_nparray, close_nparray, volume_nparray, timeperiod
        )
        return {"mfi": result.tolist()}

    @mcp.tool(
        title="Calculate MINUS_DI",
        description="Calculate the MINUS_DI (Minus Directional Indicator)",
        annotations=common_tool_annotations,
    )
    def calculate_minus_di(
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 14,
    ):
        high_nparray = np.array(high, dtype=np.float64)
        low_nparray = np.array(low, dtype=np.float64)
        close_nparray = np.array(close, dtype=np.float64)
        result = talib.MINUS_DI(high_nparray, low_nparray, close_nparray, timeperiod)
        return {"minus_di": result.tolist()}

    @mcp.tool(
        title="Calculate MINUS_DM",
        description="Calculate the MINUS_DM (Minus Directional Movement)",
        annotations=common_tool_annotations,
    )
    def calculate_minus_dm(
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 14,
    ):
        high_nparray = np.array(high, dtype=np.float64)
        low_nparray = np.array(low, dtype=np.float64)
        result = talib.MINUS_DM(high_nparray, low_nparray, timeperiod)
        return {"minus_dm": result.tolist()}

    @mcp.tool(
        title="Calculate MOM",
        description="Calculate the MOM (Momentum)",
        annotations=common_tool_annotations,
    )
    def calculate_mom(
        real: Annotated[list[float], Field(description="Real values")],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 10,
    ):
        real_nparray = np.array(real, dtype=np.float64)
        result = talib.MOM(real_nparray, timeperiod)
        return {"mom": result.tolist()}

    @mcp.tool(
        title="Calculate PLUS_DI",
        description="Calculate the PLUS_DI (Plus Directional Indicator)",
        annotations=common_tool_annotations,
    )
    def calculate_plus_di(
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 14,
    ):
        high_nparray = np.array(high, dtype=np.float64)
        low_nparray = np.array(low, dtype=np.float64)
        close_nparray = np.array(close, dtype=np.float64)
        result = talib.PLUS_DI(high_nparray, low_nparray, close_nparray, timeperiod)
        return {"plus_di": result.tolist()}

    @mcp.tool(
        title="Calculate PLUS_DM",
        description="Calculate the PLUS_DM (Plus Directional Movement)",
        annotations=common_tool_annotations,
    )
    def calculate_plus_dm(
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 14,
    ):
        high_nparray = np.array(high, dtype=np.float64)
        low_nparray = np.array(low, dtype=np.float64)
        result = talib.PLUS_DM(high_nparray, low_nparray, timeperiod)
        return {"plus_dm": result.tolist()}

    @mcp.tool(
        title="Calculate PPO",
        description="Calculate the PPO (Percentage Price Oscillator)",
        annotations=common_tool_annotations,
    )
    def calculate_ppo(
        real: Annotated[list[float], Field(description="Real values")],
        fastperiod: Annotated[int, Field(description="Fast period")] = 12,
        slowperiod: Annotated[int, Field(description="Slow period")] = 26,
        matype: Annotated[MAType, Field(description="Moving average type")] = "SMA",
    ):
        real_nparray = np.array(real, dtype=np.float64)
        result = talib.PPO(real_nparray, fastperiod, slowperiod, MA_TYPE_MAP[matype])
        return {"ppo": result.tolist()}

    @mcp.tool(
        title="Calculate ROC",
        description="Calculate the ROC (Rate of change : ((price/prevPrice)-1)*100)",
        annotations=common_tool_annotations,
    )
    def calculate_roc(
        real: Annotated[list[float], Field(description="Real values")],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 10,
    ):
        real_nparray = np.array(real, dtype=np.float64)
        result = talib.ROC(real_nparray, timeperiod)
        return {"roc": result.tolist()}

    @mcp.tool(
        title="Calculate ROCP",
        description="Calculate the ROCP (Rate of change Percentage: (price-prevPrice)/prevPrice)",
        annotations=common_tool_annotations,
    )
    def calculate_rocp(
        real: Annotated[list[float], Field(description="Real values")],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 10,
    ):
        real_nparray = np.array(real, dtype=np.float64)
        result = talib.ROCP(real_nparray, timeperiod)
        return {"rocp": result.tolist()}

    @mcp.tool(
        title="Calculate ROCR",
        description="Calculate the ROCR (Rate of change ratio: (price/prevPrice))",
        annotations=common_tool_annotations,
    )
    def calculate_rocr(
        real: Annotated[list[float], Field(description="Real values")],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 10,
    ):
        real_nparray = np.array(real, dtype=np.float64)
        result = talib.ROCR(real_nparray, timeperiod)
        return {"rocr": result.tolist()}

    @mcp.tool(
        title="Calculate ROCR100",
        description="Calculate the ROCR100 (Rate of change ratio 100 scale: (price/prevPrice)*100)",
        annotations=common_tool_annotations,
    )
    def calculate_rocr100(
        real: Annotated[list[float], Field(description="Real values")],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 10,
    ):
        real_nparray = np.array(real, dtype=np.float64)
        result = talib.ROCR100(real_nparray, timeperiod)
        return {"rocr100": result.tolist()}

    @mcp.tool(
        title="Calculate STOCH",
        description="Calculate the STOCH (Stochastic)",
        annotations=common_tool_annotations,
    )
    def calculate_stoch(
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
        fastk_period: Annotated[int, Field(description="Fast K period")] = 5,
        slowk_period: Annotated[int, Field(description="Slow K period")] = 3,
        slowk_matype: Annotated[MAType, Field(description="Slow K MA type")] = "SMA",
        slowd_period: Annotated[int, Field(description="Slow D period")] = 3,
        slowd_matype: Annotated[MAType, Field(description="Slow D MA type")] = "SMA",
    ):
        high_nparray = np.array(high, dtype=np.float64)
        low_nparray = np.array(low, dtype=np.float64)
        close_nparray = np.array(close, dtype=np.float64)
        slowk, slowd = talib.STOCH(
            high_nparray,
            low_nparray,
            close_nparray,
            fastk_period,
            slowk_period,
            MA_TYPE_MAP[slowk_matype],
            slowd_period,
            MA_TYPE_MAP[slowd_matype],
        )
        return {"slowk": slowk.tolist(), "slowd": slowd.tolist()}

    @mcp.tool(
        title="Calculate STOCHF",
        description="Calculate the STOCHF (Stochastic Fast)",
        annotations=common_tool_annotations,
    )
    def calculate_stochf(
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
        fastk_period: Annotated[int, Field(description="Fast K period")] = 5,
        fastd_period: Annotated[int, Field(description="Fast D period")] = 3,
        fastd_matype: Annotated[MAType, Field(description="Fast D MA type")] = "SMA",
    ):
        high_nparray = np.array(high, dtype=np.float64)
        low_nparray = np.array(low, dtype=np.float64)
        close_nparray = np.array(close, dtype=np.float64)
        fastk, fastd = talib.STOCHF(
            high_nparray,
            low_nparray,
            close_nparray,
            fastk_period,
            fastd_period,
            MA_TYPE_MAP[fastd_matype],
        )
        return {"fastk": fastk.tolist(), "fastd": fastd.tolist()}

    @mcp.tool(
        title="Calculate TRIX",
        description="Calculate the TRIX (1-day Rate-Of-Change (ROC) of a Triple Smooth EMA)",
        annotations=common_tool_annotations,
    )
    def calculate_trix(
        real: Annotated[list[float], Field(description="Real values")],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 30,
    ):
        real_nparray = np.array(real, dtype=np.float64)
        result = talib.TRIX(real_nparray, timeperiod)
        return {"trix": result.tolist()}

    @mcp.tool(
        title="Calculate ULTOSC",
        description="Calculate the ULTOSC (Ultimate Oscillator)",
        annotations=common_tool_annotations,
    )
    def calculate_ultosc(
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
        timeperiod1: Annotated[int, Field(description="First time period")] = 7,
        timeperiod2: Annotated[int, Field(description="Second time period")] = 14,
        timeperiod3: Annotated[int, Field(description="Third time period")] = 28,
    ):
        high_nparray = np.array(high, dtype=np.float64)
        low_nparray = np.array(low, dtype=np.float64)
        close_nparray = np.array(close, dtype=np.float64)
        result = talib.ULTOSC(
            high_nparray,
            low_nparray,
            close_nparray,
            timeperiod1,
            timeperiod2,
            timeperiod3,
        )
        return {"ultosc": result.tolist()}

    @mcp.tool(
        title="Calculate WILLR",
        description="Calculate the WILLR (Williams' %R)",
        annotations=common_tool_annotations,
    )
    def calculate_willr(
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
        timeperiod: Annotated[
            int, Field(description="Number of periods for calculation")
        ] = 14,
    ):
        high_nparray = np.array(high, dtype=np.float64)
        low_nparray = np.array(low, dtype=np.float64)
        close_nparray = np.array(close, dtype=np.float64)
        result = talib.WILLR(high_nparray, low_nparray, close_nparray, timeperiod)
        return {"willr": result.tolist()}
