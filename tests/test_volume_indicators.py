import numpy as np
from src.ta_lib_mcp_server.tools.volume_indicators import (
    calculate_ad,
    calculate_adosc,
    calculate_obv,
)


class TestVolumeIndicators:
    """Minimal tests for volume indicator functions - verify input/output structure only."""

    def test_ad_structure(self):
        """Test AD input/output structure."""
        high = [11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
        low = [9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0]
        close = [10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5]
        volume = [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0]
        result = calculate_ad(high, low, close, volume)
        assert isinstance(result, dict)
        assert "ad" in result
        assert len(result["ad"]) == len(close)

    def test_adosc_structure(self):
        """Test ADOSC input/output structure."""
        high = [11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
        low = [9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0]
        close = [10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5]
        volume = [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0]
        result = calculate_adosc(high, low, close, volume)
        assert isinstance(result, dict)
        assert "adosc" in result
        assert len(result["adosc"]) == len(close)

    def test_obv_structure(self):
        """Test OBV input/output structure."""
        close = [10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5]
        volume = [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0]
        result = calculate_obv(close, volume)
        assert isinstance(result, dict)
        assert "obv" in result
        assert len(result["obv"]) == len(close)