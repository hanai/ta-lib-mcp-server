import pytest
import numpy as np
from src.ta_lib_mcp_server.tools.cycle_indicators import (
    calculate_ht_dcperiod,
    calculate_ht_dcphase,
    calculate_ht_phasor,
    calculate_ht_sine,
    calculate_ht_trendmode,
)


class TestCycleIndicators:
    """Minimal tests for cycle indicators - verify input/output structure only."""

    def test_ht_dcperiod_structure(self):
        """Test HT_DCPERIOD input/output structure."""
        prices = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
        result = calculate_ht_dcperiod(prices)
        assert isinstance(result, dict)
        assert "ht_dcperiod" in result
        assert len(result["ht_dcperiod"]) == len(prices)

    def test_ht_dcphase_structure(self):
        """Test HT_DCPHASE input/output structure."""
        prices = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
        result = calculate_ht_dcphase(prices)
        assert isinstance(result, dict)
        assert "ht_dcphase" in result
        assert len(result["ht_dcphase"]) == len(prices)

    def test_ht_phasor_structure(self):
        """Test HT_PHASOR input/output structure."""
        prices = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
        result = calculate_ht_phasor(prices)
        assert isinstance(result, dict)
        assert "inphase" in result
        assert "quadrature" in result
        assert len(result["inphase"]) == len(prices)

    def test_ht_sine_structure(self):
        """Test HT_SINE input/output structure."""
        prices = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
        result = calculate_ht_sine(prices)
        assert isinstance(result, dict)
        assert "sine" in result
        assert "leadsine" in result
        assert len(result["sine"]) == len(prices)

    def test_ht_trendmode_structure(self):
        """Test HT_TRENDMODE input/output structure."""
        prices = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
        result = calculate_ht_trendmode(prices)
        assert isinstance(result, dict)
        assert "ht_trendmode" in result
        assert len(result["ht_trendmode"]) == len(prices)