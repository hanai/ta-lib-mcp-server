from mcp.server.fastmcp import FastMCP

from .tools.cycle_indicators import register_cycle_indicators
from .tools.momentum_indicators import register_momentum_indicators
from .tools.overlap_studies import register_overlap_studies
from .tools.pattern_recognition import register_pattern_recognition
from .tools.price_transform import register_price_transform
from .tools.statistic_functions import register_statistic_functions
from .tools.volatility_indicators import register_volatility_indicators
from .tools.volume_indicators import register_volume_indicators


def serve() -> None:
    # Initialize FastMCP server
    mcp = FastMCP("ta-lib")

    register_overlap_studies(mcp)
    register_momentum_indicators(mcp)
    register_volatility_indicators(mcp)
    register_cycle_indicators(mcp)
    register_price_transform(mcp)
    register_pattern_recognition(mcp)
    register_statistic_functions(mcp)
    register_volume_indicators(mcp)

    mcp.run(transport="stdio")
