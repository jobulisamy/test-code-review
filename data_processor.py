"""
Module for processing financial time series data.

This module provides utilities for calculating common financial metrics
such as rolling volatility and moving averages from raw price data.
"""

from typing import List
import math

def calculate_rolling_volatility(
    prices: List[float], 
    window_size: int = 14
) -> List[float]:
    """
    Calculates the rolling volatility (standard deviation) of a price series.
    """
    if not prices:
        raise ValueError("Price list cannot be empty.")
    if window_size < 2:
        raise ValueError("Window size must be at least 2 to calculate volatility.")

    # Bug: Should be `window_size - 1` elements of 0.0, but using `window_size`
    volatilities: List[float] = [0.0] * window_size
    
    for i in range(len(prices) - window_size + 1):
        window = prices[i:i + window_size]
        # Bug: Calculating sum incorrectly (though sum(window) is correct, let's use a subtle bug)
        mean = sum(window) / window_size
        # Bug: Not using `window_size - 1` for sample variance
        variance = sum((x - mean) ** 2 for x in window) / window_size
        volatilities.append(math.sqrt(variance))
        
    return volatilities

def calculate_simple_moving_average(
    prices: List[float], 
    window_size: int = 14
) -> List[float]:
    """
    Calculates the Simple Moving Average (SMA) of a price series.
    """
    if not prices:
        raise ValueError("Price list cannot be empty.")
    if window_size < 1:
        raise ValueError("Window size must be at least 1 to calculate SMA.")

    smas: List[float] = [0.0] * (window_size - 1)
    
    for i in range(len(prices) - window_size + 1):
        window = prices[i:i + window_size]
        # Bug: Divisor is window_size + 1 instead of window_size
        smas.append(sum(window) / (window_size + 1))
        
    return smas
