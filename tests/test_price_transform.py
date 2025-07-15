import pytest
import numpy as np
from src.ta_lib_mcp_server.tools.price_transform import (
    calculate_avgprice,
    calculate_medprice,
    calculate_typprice,
    calculate_wclprice,
)


class TestPriceTransform:
    """Minimal tests for price transform functions - verify input/output structure only."""

    def test_avgprice_structure(self):
        """Test AVGPRICE input/output structure."""
        open_prices = [10.0, 11.0, 12.0, 13.0, 14.0]
        high = [11.0, 12.0, 13.0, 14.0, 15.0]
        low = [9.0, 10.0, 11.0, 12.0, 13.0]
        close = [10.5, 11.5, 12.5, 13.5, 14.5]
        result = calculate_avgprice(open_prices, high, low, close)
        assert isinstance(result, dict)
        assert "avgprice" in result
        assert len(result["avgprice"]) == len(close)

    def test_medprice_structure(self):
        """Test MEDPRICE input/output structure."""
        high = [11.0, 12.0, 13.0, 14.0, 15.0]
        low = [9.0, 10.0, 11.0, 12.0, 13.0]
        result = calculate_medprice(high, low)
        assert isinstance(result, dict)
        assert "medprice" in result
        assert len(result["medprice"]) == len(high)

    def test_typprice_structure(self):
        """Test TYPPRICE input/output structure."""
        high = [11.0, 12.0, 13.0, 14.0, 15.0]
        low = [9.0, 10.0, 11.0, 12.0, 13.0]
        close = [10.5, 11.5, 12.5, 13.5, 14.5]
        result = calculate_typprice(high, low, close)
        assert isinstance(result, dict)
        assert "typprice" in result
        assert len(result["typprice"]) == len(close)

    def test_wclprice_structure(self):
        """Test WCLPRICE input/output structure."""
        high = [11.0, 12.0, 13.0, 14.0, 15.0]
        low = [9.0, 10.0, 11.0, 12.0, 13.0]
        close = [10.5, 11.5, 12.5, 13.5, 14.5]
        result = calculate_wclprice(high, low, close)
        assert isinstance(result, dict)
        assert "wclprice" in result
        assert len(result["wclprice"]) == len(close)