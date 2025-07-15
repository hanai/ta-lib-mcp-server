import pytest
import numpy as np
from src.ta_lib_mcp_server.tools.statistic_functions import (
    calculate_beta,
    calculate_correl,
    calculate_linearreg,
    calculate_linearreg_angle,
    calculate_linearreg_intercept,
    calculate_linearreg_slope,
    calculate_stddev,
    calculate_tsf,
    calculate_var,
)


class TestStatisticFunctions:
    """Minimal tests for statistic functions - verify input/output structure only."""

    def test_beta_structure(self):
        """Test BETA input/output structure."""
        real0 = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0]
        real1 = [20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0]
        result = calculate_beta(real0, real1)
        assert isinstance(result, dict)
        assert "beta" in result
        assert len(result["beta"]) == len(real0)

    def test_correl_structure(self):
        """Test CORREL input/output structure."""
        real0 = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0]
        real1 = [20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0]
        result = calculate_correl(real0, real1)
        assert isinstance(result, dict)
        assert "correl" in result
        assert len(result["correl"]) == len(real0)

    def test_linearreg_structure(self):
        """Test LINEARREG input/output structure."""
        real = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0]
        result = calculate_linearreg(real)
        assert isinstance(result, dict)
        assert "linearreg" in result
        assert len(result["linearreg"]) == len(real)

    def test_linearreg_angle_structure(self):
        """Test LINEARREG_ANGLE input/output structure."""
        real = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0]
        result = calculate_linearreg_angle(real)
        assert isinstance(result, dict)
        assert "linearreg_angle" in result
        assert len(result["linearreg_angle"]) == len(real)

    def test_linearreg_intercept_structure(self):
        """Test LINEARREG_INTERCEPT input/output structure."""
        real = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0]
        result = calculate_linearreg_intercept(real)
        assert isinstance(result, dict)
        assert "linearreg_intercept" in result
        assert len(result["linearreg_intercept"]) == len(real)

    def test_linearreg_slope_structure(self):
        """Test LINEARREG_SLOPE input/output structure."""
        real = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0]
        result = calculate_linearreg_slope(real)
        assert isinstance(result, dict)
        assert "linearreg_slope" in result
        assert len(result["linearreg_slope"]) == len(real)

    def test_stddev_structure(self):
        """Test STDDEV input/output structure."""
        real = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0]
        result = calculate_stddev(real)
        assert isinstance(result, dict)
        assert "stddev" in result
        assert len(result["stddev"]) == len(real)

    def test_tsf_structure(self):
        """Test TSF input/output structure."""
        real = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0]
        result = calculate_tsf(real)
        assert isinstance(result, dict)
        assert "tsf" in result
        assert len(result["tsf"]) == len(real)

    def test_var_structure(self):
        """Test VAR input/output structure."""
        real = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0]
        result = calculate_var(real)
        assert isinstance(result, dict)
        assert "var" in result
        assert len(result["var"]) == len(real)