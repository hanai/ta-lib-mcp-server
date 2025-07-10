from typing import Literal

from talib._ta_lib import MA_Type

# Define the moving average type literal
MAType = Literal["SMA", "EMA", "WMA", "DEMA", "TEMA", "TRIMA", "KAMA", "MAMA", "T3"]

MA_TYPE_MAP = {
    "SMA": MA_Type.SMA,
    "EMA": MA_Type.EMA,
    "WMA": MA_Type.WMA,
    "DEMA": MA_Type.DEMA,
    "TEMA": MA_Type.TEMA,
    "TRIMA": MA_Type.TRIMA,
    "KAMA": MA_Type.KAMA,
    "MAMA": MA_Type.MAMA,
    "T3": MA_Type.T3,
}
