from typing import Annotated

import numpy as np
import talib
from mcp.types import ToolAnnotations
from pydantic import Field

common_tool_annotations = ToolAnnotations(readOnlyHint=True)


def calculate_cdl2crows(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDL2CROWS(open_nparray, high_nparray, low_nparray, close_nparray)
    return {"result": result.tolist()}


def calculate_cdl3blackcrows(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDL3BLACKCROWS(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdl3inside(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDL3INSIDE(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdl3linestrike(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDL3LINESTRIKE(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdl3outside(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDL3OUTSIDE(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdl3starsinsouth(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDL3STARSINSOUTH(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdl3whitesoldiers(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDL3WHITESOLDIERS(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlabandonedbaby(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
    penetration: float = 0,
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLABANDONEDBABY(
        open_nparray, high_nparray, low_nparray, close_nparray, penetration
    )
    return {"result": result.tolist()}


def calculate_cdladvanceblock(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLADVANCEBLOCK(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlbelthold(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLBELTHOLD(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlbreakaway(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLBREAKAWAY(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlclosingmarubozu(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLCLOSINGMARUBOZU(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlconcealbabyswall(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLCONCEALBABYSWALL(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlcounterattack(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLCOUNTERATTACK(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdldarkcloudcover(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
    penetration: float = 0,
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLDARKCLOUDCOVER(
        open_nparray, high_nparray, low_nparray, close_nparray, penetration
    )
    return {"result": result.tolist()}


def calculate_cdldoji(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLDOJI(open_nparray, high_nparray, low_nparray, close_nparray)
    return {"result": result.tolist()}


def calculate_cdldojistar(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLDOJISTAR(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdldragonflydoji(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLDRAGONFLYDOJI(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlengulfing(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLENGULFING(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdleveningdojistar(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
    penetration: float = 0,
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLEVENINGDOJISTAR(
        open_nparray, high_nparray, low_nparray, close_nparray, penetration
    )
    return {"result": result.tolist()}


def calculate_cdleveningstar(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
    penetration: float = 0,
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLEVENINGSTAR(
        open_nparray, high_nparray, low_nparray, close_nparray, penetration
    )
    return {"result": result.tolist()}


def calculate_cdlgapsidesidewhite(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLGAPSIDESIDEWHITE(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlgravestonedoji(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLGRAVESTONEDOJI(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlhammer(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLHAMMER(open_nparray, high_nparray, low_nparray, close_nparray)
    return {"result": result.tolist()}


def calculate_cdlhangingman(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLHANGINGMAN(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlharami(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLHARAMI(open_nparray, high_nparray, low_nparray, close_nparray)
    return {"result": result.tolist()}


def calculate_cdlharamicross(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLHARAMICROSS(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlhighwave(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLHIGHWAVE(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlhikkake(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLHIKKAKE(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlhikkakemod(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLHIKKAKEMOD(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlhomingpigeon(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLHOMINGPIGEON(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlidentical3crows(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLIDENTICAL3CROWS(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlinneck(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLINNECK(open_nparray, high_nparray, low_nparray, close_nparray)
    return {"result": result.tolist()}


def calculate_cdlinvertedhammer(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLINVERTEDHAMMER(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlkicking(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLKICKING(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlkickingbylength(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLKICKINGBYLENGTH(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlladderbottom(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLLADDERBOTTOM(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdllongleggeddoji(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLLONGLEGGEDDOJI(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdllongline(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLLONGLINE(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlmarubozu(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLMARUBOZU(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlmatchinglow(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLMATCHINGLOW(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlmathold(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
    penetration: float = 0,
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLMATHOLD(
        open_nparray, high_nparray, low_nparray, close_nparray, penetration
    )
    return {"result": result.tolist()}


def calculate_cdlmorningdojistar(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
    penetration: float = 0,
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLMORNINGDOJISTAR(
        open_nparray, high_nparray, low_nparray, close_nparray, penetration
    )
    return {"result": result.tolist()}


def calculate_cdlmorningstar(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
    penetration: float = 0,
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLMORNINGSTAR(
        open_nparray, high_nparray, low_nparray, close_nparray, penetration
    )
    return {"result": result.tolist()}


def calculate_cdlonneck(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLONNECK(open_nparray, high_nparray, low_nparray, close_nparray)
    return {"result": result.tolist()}


def calculate_cdlpiercing(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLPIERCING(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlrickshawman(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLRICKSHAWMAN(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlrisefall3methods(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLRISEFALL3METHODS(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlseparatinglines(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLSEPARATINGLINES(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlshootingstar(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLSHOOTINGSTAR(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlshortline(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLSHORTLINE(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlspinningtop(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLSPINNINGTOP(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlstalledpattern(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLSTALLEDPATTERN(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlsticksandwich(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLSTICKSANDWICH(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdltakuri(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLTAKURI(open_nparray, high_nparray, low_nparray, close_nparray)
    return {"result": result.tolist()}


def calculate_cdltasukigap(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLTASUKIGAP(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlthrusting(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLTHRUSTING(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdltristar(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLTRISTAR(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlunique3river(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLUNIQUE3RIVER(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlupsidegap2crows(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLUPSIDEGAP2CROWS(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def calculate_cdlxsidegap3methods(
    open: list[float],
    high: list[float],
    low: list[float],
    close: list[float],
) -> dict:
    open_nparray = np.array(open, dtype=np.float64)
    high_nparray = np.array(high, dtype=np.float64)
    low_nparray = np.array(low, dtype=np.float64)
    close_nparray = np.array(close, dtype=np.float64)
    result = talib.CDLXSIDEGAP3METHODS(
        open_nparray, high_nparray, low_nparray, close_nparray
    )
    return {"result": result.tolist()}


def register_pattern_recognition(mcp):
    """Register all pattern recognition tools with the MCP server."""

    @mcp.tool(
        title="Calculate CDL2CROWS",
        description="Calculate the CDL2CROWS (Two Crows)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdl2crows(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdl2crows(open, high, low, close)

    @mcp.tool(
        title="Calculate CDL3BLACKCROWS",
        description="Calculate the CDL3BLACKCROWS (Three Black Crows)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdl3blackcrows(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdl3blackcrows(open, high, low, close)

    @mcp.tool(
        title="Calculate CDL3INSIDE",
        description="Calculate the CDL3INSIDE (Three Inside Up/Down)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdl3inside(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdl3inside(open, high, low, close)

    @mcp.tool(
        title="Calculate CDL3LINESTRIKE",
        description="Calculate the CDL3LINESTRIKE (Three-Line Strike)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdl3linestrike(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdl3linestrike(open, high, low, close)

    @mcp.tool(
        title="Calculate CDL3OUTSIDE",
        description="Calculate the CDL3OUTSIDE (Three Outside Up/Down)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdl3outside(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdl3outside(open, high, low, close)

    @mcp.tool(
        title="Calculate CDL3STARSINSOUTH",
        description="Calculate the CDL3STARSINSOUTH (Three Stars In The South)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdl3starsinsouth(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdl3starsinsouth(open, high, low, close)

    @mcp.tool(
        title="Calculate CDL3WHITESOLDIERS",
        description="Calculate the CDL3WHITESOLDIERS (Three Advancing White Soldiers)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdl3whitesoldiers(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdl3whitesoldiers(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLABANDONEDBABY",
        description="Calculate the CDLABANDONEDBABY (Abandoned Baby)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlabandonedbaby(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
        penetration: Annotated[float, Field(description="Penetration")] = 0,
    ):
        return calculate_cdlabandonedbaby(open, high, low, close, penetration)

    @mcp.tool(
        title="Calculate CDLADVANCEBLOCK",
        description="Calculate the CDLADVANCEBLOCK (Advance Block)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdladvanceblock(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdladvanceblock(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLBELTHOLD",
        description="Calculate the CDLBELTHOLD (Belt-hold)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlbelthold(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlbelthold(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLBREAKAWAY",
        description="Calculate the CDLBREAKAWAY (Breakaway)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlbreakaway(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlbreakaway(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLCLOSINGMARUBOZU",
        description="Calculate the CDLCLOSINGMARUBOZU (Closing Marubozu)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlclosingmarubozu(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlclosingmarubozu(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLCONCEALBABYSWALL",
        description="Calculate the CDLCONCEALBABYSWALL (Concealing Baby Swallow)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlconcealbabyswall(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlconcealbabyswall(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLCOUNTERATTACK",
        description="Calculate the CDLCOUNTERATTACK (Counterattack)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlcounterattack(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlcounterattack(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLDARKCLOUDCOVER",
        description="Calculate the CDLDARKCLOUDCOVER (Dark Cloud Cover)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdldarkcloudcover(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
        penetration: Annotated[float, Field(description="Penetration")] = 0,
    ):
        return calculate_cdldarkcloudcover(open, high, low, close, penetration)

    @mcp.tool(
        title="Calculate CDLDOJI",
        description="Calculate the CDLDOJI (Doji)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdldoji(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdldoji(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLDOJISTAR",
        description="Calculate the CDLDOJISTAR (Doji Star)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdldojistar(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdldojistar(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLDRAGONFLYDOJI",
        description="Calculate the CDLDRAGONFLYDOJI (Dragonfly Doji)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdldragonflydoji(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdldragonflydoji(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLENGULFING",
        description="Calculate the CDLENGULFING (Engulfing Pattern)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlengulfing(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlengulfing(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLEVENINGDOJISTAR",
        description="Calculate the CDLEVENINGDOJISTAR (Evening Doji Star)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdleveningdojistar(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
        penetration: Annotated[float, Field(description="Penetration")] = 0,
    ):
        return calculate_cdleveningdojistar(open, high, low, close, penetration)

    @mcp.tool(
        title="Calculate CDLEVENINGSTAR",
        description="Calculate the CDLEVENINGSTAR (Evening Star)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdleveningstar(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
        penetration: Annotated[float, Field(description="Penetration")] = 0,
    ):
        return calculate_cdleveningstar(open, high, low, close, penetration)

    @mcp.tool(
        title="Calculate CDLGAPSIDESIDEWHITE",
        description="Calculate the CDLGAPSIDESIDEWHITE (Up-side/Down-side Gap Three Methods)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlgapsidesidewhite(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlgapsidesidewhite(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLGRAVESTONEDOJI",
        description="Calculate the CDLGRAVESTONEDOJI (Gravestone Doji)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlgravestonedoji(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlgravestonedoji(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLHAMMER",
        description="Calculate the CDLHAMMER (Hammer)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlhammer(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlhammer(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLHANGINGMAN",
        description="Calculate the CDLHANGINGMAN (Hanging Man)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlhangingman(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlhangingman(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLHARAMI",
        description="Calculate the CDLHARAMI (Harami Pattern)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlharami(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlharami(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLHARAMICROSS",
        description="Calculate the CDLHARAMICROSS (Harami Cross Pattern)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlharamicross(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlharamicross(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLHIGHWAVE",
        description="Calculate the CDLHIGHWAVE (High-Wave Candle)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlhighwave(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlhighwave(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLHIKKAKE",
        description="Calculate the CDLHIKKAKE (Hikkake Pattern)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlhikkake(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlhikkake(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLHIKKAKEMOD",
        description="Calculate the CDLHIKKAKEMOD (Modified Hikkake Pattern)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlhikkakemod(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlhikkakemod(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLHOMINGPIGEON",
        description="Calculate the CDLHOMINGPIGEON (Homing Pigeon)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlhomingpigeon(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlhomingpigeon(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLIDENTICAL3CROWS",
        description="Calculate the CDLIDENTICAL3CROWS (Identical Three Crows)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlidentical3crows(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlidentical3crows(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLINNECK",
        description="Calculate the CDLINNECK (In-Neck Pattern)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlinneck(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlinneck(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLINVERTEDHAMMER",
        description="Calculate the CDLINVERTEDHAMMER (Inverted Hammer)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlinvertedhammer(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlinvertedhammer(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLKICKING",
        description="Calculate the CDLKICKING (Kicking)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlkicking(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlkicking(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLKICKINGBYLENGTH",
        description="Calculate the CDLKICKINGBYLENGTH (Kicking - bull/bear determined by the longer marubozu)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlkickingbylength(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlkickingbylength(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLLADDERBOTTOM",
        description="Calculate the CDLLADDERBOTTOM (Ladder Bottom)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlladderbottom(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlladderbottom(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLLONGLEGGEDDOJI",
        description="Calculate the CDLLONGLEGGEDDOJI (Long Legged Doji)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdllongleggeddoji(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdllongleggeddoji(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLLONGLINE",
        description="Calculate the CDLLONGLINE (Long Line Candle)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdllongline(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdllongline(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLMARUBOZU",
        description="Calculate the CDLMARUBOZU (Marubozu)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlmarubozu(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlmarubozu(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLMATCHINGLOW",
        description="Calculate the CDLMATCHINGLOW (Matching Low)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlmatchinglow(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlmatchinglow(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLMATHOLD",
        description="Calculate the CDLMATHOLD (Mat Hold)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlmathold(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
        penetration: Annotated[float, Field(description="Penetration")] = 0,
    ):
        return calculate_cdlmathold(open, high, low, close, penetration)

    @mcp.tool(
        title="Calculate CDLMORNINGDOJISTAR",
        description="Calculate the CDLMORNINGDOJISTAR (Morning Doji Star)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlmorningdojistar(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
        penetration: Annotated[float, Field(description="Penetration")] = 0,
    ):
        return calculate_cdlmorningdojistar(open, high, low, close, penetration)

    @mcp.tool(
        title="Calculate CDLMORNINGSTAR",
        description="Calculate the CDLMORNINGSTAR (Morning Star)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlmorningstar(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
        penetration: Annotated[float, Field(description="Penetration")] = 0,
    ):
        return calculate_cdlmorningstar(open, high, low, close, penetration)

    @mcp.tool(
        title="Calculate CDLONNECK",
        description="Calculate the CDLONNECK (On-Neck Pattern)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlonneck(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlonneck(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLPIERCING",
        description="Calculate the CDLPIERCING (Piercing Pattern)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlpiercing(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlpiercing(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLRICKSHAWMAN",
        description="Calculate the CDLRICKSHAWMAN (Rickshaw Man)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlrickshawman(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlrickshawman(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLRISEFALL3METHODS",
        description="Calculate the CDLRISEFALL3METHODS (Rising/Falling Three Methods)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlrisefall3methods(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlrisefall3methods(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLSEPARATINGLINES",
        description="Calculate the CDLSEPARATINGLINES (Separating Lines)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlseparatinglines(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlseparatinglines(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLSHOOTINGSTAR",
        description="Calculate the CDLSHOOTINGSTAR (Shooting Star)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlshootingstar(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlshootingstar(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLSHORTLINE",
        description="Calculate the CDLSHORTLINE (Short Line Candle)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlshortline(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlshortline(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLSPINNINGTOP",
        description="Calculate the CDLSPINNINGTOP (Spinning Top)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlspinningtop(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlspinningtop(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLSTALLEDPATTERN",
        description="Calculate the CDLSTALLEDPATTERN (Stalled Pattern)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlstalledpattern(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlstalledpattern(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLSTICKSANDWICH",
        description="Calculate the CDLSTICKSANDWICH (Stick Sandwich)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlsticksandwich(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlsticksandwich(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLTAKURI",
        description="Calculate the CDLTAKURI (Takuri (Dragonfly Doji with very long lower shadow))",
        annotations=common_tool_annotations,
    )
    def _calculate_cdltakuri(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdltakuri(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLTASUKIGAP",
        description="Calculate the CDLTASUKIGAP (Tasuki Gap)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdltasukigap(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdltasukigap(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLTHRUSTING",
        description="Calculate the CDLTHRUSTING (Thrusting Pattern)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlthrusting(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlthrusting(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLTRISTAR",
        description="Calculate the CDLTRISTAR (Tristar Pattern)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdltristar(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdltristar(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLUNIQUE3RIVER",
        description="Calculate the CDLUNIQUE3RIVER (Unique 3 River)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlunique3river(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlunique3river(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLUPSIDEGAP2CROWS",
        description="Calculate the CDLUPSIDEGAP2CROWS (Upside Gap Two Crows)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlupsidegap2crows(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlupsidegap2crows(open, high, low, close)

    @mcp.tool(
        title="Calculate CDLXSIDEGAP3METHODS",
        description="Calculate the CDLXSIDEGAP3METHODS (Upside/Downside Gap Three Methods)",
        annotations=common_tool_annotations,
    )
    def _calculate_cdlxsidegap3methods(
        open: Annotated[list[float], Field(description="Open prices")],
        high: Annotated[list[float], Field(description="High prices")],
        low: Annotated[list[float], Field(description="Low prices")],
        close: Annotated[list[float], Field(description="Close prices")],
    ):
        return calculate_cdlxsidegap3methods(open, high, low, close)