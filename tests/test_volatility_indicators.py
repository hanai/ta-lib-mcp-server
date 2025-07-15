import pytest
import numpy as np
from src.ta_lib_mcp_server.tools.volatility_indicators import (
    calculate_atr,
    calculate_natr,
    calculate_trange,
)


class TestVolatilityIndicators:
    """Minimal tests for volatility indicator functions - verify input/output structure only."""

    def test_atr_structure(self):
        """Test ATR input/output structure."""
        high = [11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
        low = [9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0]
        close = [10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5]
        result = calculate_atr(high, low, close)
        assert isinstance(result, dict)
        assert "atr" in result
        assert len(result["atr"]) == len(close)

    def test_natr_structure(self):
        """Test NATR input/output structure."""
        high = [11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
        low = [9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0]
        close = [10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5]
        result = calculate_natr(high, low, close)
        assert isinstance(result, dict)
        assert "natr" in result
        assert len(result["natr"]) == len(close)

    def test_trange_structure(self):
        """Test TRANGE input/output structure."""
        high = [11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
        low = [9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0]
        close = [10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5]
        result = calculate_trange(high, low, close)
        assert isinstance(result, dict)
        assert "trange" in result
        assert len(result["trange"]) == len(close)