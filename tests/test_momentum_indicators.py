import pytest
import numpy as np
from src.ta_lib_mcp_server.tools.momentum_indicators import (
    calculate_macd,
    calculate_rsi,
    calculate_stochrsi,
    calculate_adx,
    calculate_adxr,
    calculate_apo,
    calculate_aroon,
    calculate_aroonosc,
    calculate_bop,
    calculate_cci,
    calculate_cmo,
    calculate_dx,
    calculate_macdext,
    calculate_macdfix,
    calculate_mfi,
    calculate_minus_di,
    calculate_minus_dm,
    calculate_mom,
    calculate_plus_di,
    calculate_plus_dm,
    calculate_ppo,
    calculate_roc,
    calculate_rocp,
    calculate_rocr,
    calculate_rocr100,
    calculate_stoch,
    calculate_stochf,
    calculate_trix,
    calculate_ultosc,
    calculate_willr,
)


class TestMomentumIndicators:
    """Minimal tests for momentum indicators - verify input/output structure only."""

    def test_macd_structure(self):
        """Test MACD input/output structure."""
        prices = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
        result = calculate_macd(prices)
        assert isinstance(result, dict)
        assert "macd" in result
        assert "macdsignal" in result
        assert "macdhist" in result
        assert len(result["macd"]) == len(prices)

    def test_rsi_structure(self):
        """Test RSI input/output structure."""
        prices = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
        result = calculate_rsi(prices)
        assert isinstance(result, dict)
        assert "rsi" in result
        assert len(result["rsi"]) == len(prices)

    def test_stochrsi_structure(self):
        """Test STOCHRSI input/output structure."""
        prices = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
        result = calculate_stochrsi(prices)
        assert isinstance(result, dict)
        assert "fastk" in result
        assert "fastd" in result
        assert len(result["fastk"]) == len(prices)

    def test_adx_structure(self):
        """Test ADX input/output structure."""
        high = [50.0, 51.0, 52.0, 53.0, 54.0, 55.0]
        low = [48.0, 49.0, 50.0, 51.0, 52.0, 53.0]
        close = [49.0, 50.0, 51.0, 52.0, 53.0, 54.0]
        result = calculate_adx(high, low, close)
        assert isinstance(result, dict)
        assert "adx" in result
        assert len(result["adx"]) == len(close)

    def test_adxr_structure(self):
        """Test ADXR input/output structure."""
        high = [50.0, 51.0, 52.0, 53.0, 54.0, 55.0]
        low = [48.0, 49.0, 50.0, 51.0, 52.0, 53.0]
        close = [49.0, 50.0, 51.0, 52.0, 53.0, 54.0]
        result = calculate_adxr(high, low, close)
        assert isinstance(result, dict)
        assert "adxr" in result
        assert len(result["adxr"]) == len(close)

    def test_apo_structure(self):
        """Test APO input/output structure."""
        prices = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
        result = calculate_apo(prices)
        assert isinstance(result, dict)
        assert "apo" in result
        assert len(result["apo"]) == len(prices)

    def test_aroon_structure(self):
        """Test AROON input/output structure."""
        high = [50.0, 51.0, 52.0, 53.0, 54.0, 55.0]
        low = [48.0, 49.0, 50.0, 51.0, 52.0, 53.0]
        result = calculate_aroon(high, low)
        assert isinstance(result, dict)
        assert "aroondown" in result
        assert "aroonup" in result
        assert len(result["aroondown"]) == len(high)

    def test_aroonosc_structure(self):
        """Test AROONOSC input/output structure."""
        high = [50.0, 51.0, 52.0, 53.0, 54.0, 55.0]
        low = [48.0, 49.0, 50.0, 51.0, 52.0, 53.0]
        result = calculate_aroonosc(high, low)
        assert isinstance(result, dict)
        assert "aroonosc" in result
        assert len(result["aroonosc"]) == len(high)

    def test_bop_structure(self):
        """Test BOP input/output structure."""
        open_prices = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0]
        high = [11.0, 12.0, 13.0, 14.0, 15.0, 16.0]
        low = [9.0, 10.0, 11.0, 12.0, 13.0, 14.0]
        close = [10.5, 11.5, 12.5, 13.5, 14.5, 15.5]
        result = calculate_bop(open_prices, high, low, close)
        assert isinstance(result, dict)
        assert "bop" in result
        assert len(result["bop"]) == len(close)

    def test_cci_structure(self):
        """Test CCI input/output structure."""
        high = [50.0, 51.0, 52.0, 53.0, 54.0, 55.0]
        low = [48.0, 49.0, 50.0, 51.0, 52.0, 53.0]
        close = [49.0, 50.0, 51.0, 52.0, 53.0, 54.0]
        result = calculate_cci(high, low, close)
        assert isinstance(result, dict)
        assert "cci" in result
        assert len(result["cci"]) == len(close)

    def test_cmo_structure(self):
        """Test CMO input/output structure."""
        prices = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
        result = calculate_cmo(prices)
        assert isinstance(result, dict)
        assert "cmo" in result
        assert len(result["cmo"]) == len(prices)

    def test_dx_structure(self):
        """Test DX input/output structure."""
        high = [50.0, 51.0, 52.0, 53.0, 54.0, 55.0]
        low = [48.0, 49.0, 50.0, 51.0, 52.0, 53.0]
        close = [49.0, 50.0, 51.0, 52.0, 53.0, 54.0]
        result = calculate_dx(high, low, close)
        assert isinstance(result, dict)
        assert "dx" in result
        assert len(result["dx"]) == len(close)

    def test_macdext_structure(self):
        """Test MACDEXT input/output structure."""
        prices = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
        result = calculate_macdext(prices)
        assert isinstance(result, dict)
        assert "macd" in result
        assert "macdsignal" in result
        assert "macdhist" in result
        assert len(result["macd"]) == len(prices)

    def test_macdfix_structure(self):
        """Test MACDFIX input/output structure."""
        prices = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
        result = calculate_macdfix(prices)
        assert isinstance(result, dict)
        assert "macd" in result
        assert "macdsignal" in result
        assert "macdhist" in result
        assert len(result["macd"]) == len(prices)

    def test_mfi_structure(self):
        """Test MFI input/output structure."""
        high = [50.0, 51.0, 52.0, 53.0, 54.0, 55.0]
        low = [48.0, 49.0, 50.0, 51.0, 52.0, 53.0]
        close = [49.0, 50.0, 51.0, 52.0, 53.0, 54.0]
        volume = [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0]
        result = calculate_mfi(high, low, close, volume)
        assert isinstance(result, dict)
        assert "mfi" in result
        assert len(result["mfi"]) == len(close)

    def test_minus_di_structure(self):
        """Test MINUS_DI input/output structure."""
        high = [50.0, 51.0, 52.0, 53.0, 54.0, 55.0]
        low = [48.0, 49.0, 50.0, 51.0, 52.0, 53.0]
        close = [49.0, 50.0, 51.0, 52.0, 53.0, 54.0]
        result = calculate_minus_di(high, low, close)
        assert isinstance(result, dict)
        assert "minus_di" in result
        assert len(result["minus_di"]) == len(close)

    def test_minus_dm_structure(self):
        """Test MINUS_DM input/output structure."""
        high = [50.0, 51.0, 52.0, 53.0, 54.0, 55.0]
        low = [48.0, 49.0, 50.0, 51.0, 52.0, 53.0]
        result = calculate_minus_dm(high, low)
        assert isinstance(result, dict)
        assert "minus_dm" in result
        assert len(result["minus_dm"]) == len(high)

    def test_mom_structure(self):
        """Test MOM input/output structure."""
        prices = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
        result = calculate_mom(prices)
        assert isinstance(result, dict)
        assert "mom" in result
        assert len(result["mom"]) == len(prices)

    def test_plus_di_structure(self):
        """Test PLUS_DI input/output structure."""
        high = [50.0, 51.0, 52.0, 53.0, 54.0, 55.0]
        low = [48.0, 49.0, 50.0, 51.0, 52.0, 53.0]
        close = [49.0, 50.0, 51.0, 52.0, 53.0, 54.0]
        result = calculate_plus_di(high, low, close)
        assert isinstance(result, dict)
        assert "plus_di" in result
        assert len(result["plus_di"]) == len(close)

    def test_plus_dm_structure(self):
        """Test PLUS_DM input/output structure."""
        high = [50.0, 51.0, 52.0, 53.0, 54.0, 55.0]
        low = [48.0, 49.0, 50.0, 51.0, 52.0, 53.0]
        result = calculate_plus_dm(high, low)
        assert isinstance(result, dict)
        assert "plus_dm" in result
        assert len(result["plus_dm"]) == len(high)

    def test_ppo_structure(self):
        """Test PPO input/output structure."""
        prices = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
        result = calculate_ppo(prices)
        assert isinstance(result, dict)
        assert "ppo" in result
        assert len(result["ppo"]) == len(prices)

    def test_roc_structure(self):
        """Test ROC input/output structure."""
        prices = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
        result = calculate_roc(prices)
        assert isinstance(result, dict)
        assert "roc" in result
        assert len(result["roc"]) == len(prices)

    def test_rocp_structure(self):
        """Test ROCP input/output structure."""
        prices = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
        result = calculate_rocp(prices)
        assert isinstance(result, dict)
        assert "rocp" in result
        assert len(result["rocp"]) == len(prices)

    def test_rocr_structure(self):
        """Test ROCR input/output structure."""
        prices = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
        result = calculate_rocr(prices)
        assert isinstance(result, dict)
        assert "rocr" in result
        assert len(result["rocr"]) == len(prices)

    def test_rocr100_structure(self):
        """Test ROCR100 input/output structure."""
        prices = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
        result = calculate_rocr100(prices)
        assert isinstance(result, dict)
        assert "rocr100" in result
        assert len(result["rocr100"]) == len(prices)

    def test_stoch_structure(self):
        """Test STOCH input/output structure."""
        high = [50.0, 51.0, 52.0, 53.0, 54.0, 55.0]
        low = [48.0, 49.0, 50.0, 51.0, 52.0, 53.0]
        close = [49.0, 50.0, 51.0, 52.0, 53.0, 54.0]
        result = calculate_stoch(high, low, close)
        assert isinstance(result, dict)
        assert "slowk" in result
        assert "slowd" in result
        assert len(result["slowk"]) == len(close)

    def test_stochf_structure(self):
        """Test STOCHF input/output structure."""
        high = [50.0, 51.0, 52.0, 53.0, 54.0, 55.0]
        low = [48.0, 49.0, 50.0, 51.0, 52.0, 53.0]
        close = [49.0, 50.0, 51.0, 52.0, 53.0, 54.0]
        result = calculate_stochf(high, low, close)
        assert isinstance(result, dict)
        assert "fastk" in result
        assert "fastd" in result
        assert len(result["fastk"]) == len(close)

    def test_trix_structure(self):
        """Test TRIX input/output structure."""
        prices = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
        result = calculate_trix(prices)
        assert isinstance(result, dict)
        assert "trix" in result
        assert len(result["trix"]) == len(prices)

    def test_ultosc_structure(self):
        """Test ULTOSC input/output structure."""
        high = [50.0, 51.0, 52.0, 53.0, 54.0, 55.0]
        low = [48.0, 49.0, 50.0, 51.0, 52.0, 53.0]
        close = [49.0, 50.0, 51.0, 52.0, 53.0, 54.0]
        result = calculate_ultosc(high, low, close)
        assert isinstance(result, dict)
        assert "ultosc" in result
        assert len(result["ultosc"]) == len(close)

    def test_willr_structure(self):
        """Test WILLR input/output structure."""
        high = [50.0, 51.0, 52.0, 53.0, 54.0, 55.0]
        low = [48.0, 49.0, 50.0, 51.0, 52.0, 53.0]
        close = [49.0, 50.0, 51.0, 52.0, 53.0, 54.0]
        result = calculate_willr(high, low, close)
        assert isinstance(result, dict)
        assert "willr" in result
        assert len(result["willr"]) == len(close)