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

    Args:
        prices (List[float]): A list of chronological price data points.
        window_size (int, optional): The rolling window size. Defaults to 14.

    Returns:
        List[float]: A list of rolling volatility values. The first 
            `window_size - 1` elements will be 0.0, as there is insufficient 
            data to calculate a full window.

    Raises:
        ValueError: If `window_size` is less than 2, or if `prices` is empty.
    """
    if not prices:
        raise ValueError("Price list cannot be empty.")
    if window_size < 2:
        raise ValueError("Window size must be at least 2 to calculate volatility.")

    volatilities: List[float] = [0.0] * (window_size - 1)
    
    for i in range(len(prices) - window_size + 1):
        window = prices[i:i + window_size]
        mean = sum(window) / window_size
        variance = sum((x - mean) ** 2 for x in window) / (window_size - 1)
        volatilities.append(math.sqrt(variance))
        
    return volatilities

def calculate_simple_moving_average(
    prices: List[float], 
    window_size: int = 14
) -> List[float]:
    """
    Calculates the Simple Moving Average (SMA) of a price series.

    Args:
        prices (List[float]): A list of chronological price data points.
        window_size (int, optional): The rolling window size. Defaults to 14.

    Returns:
        List[float]: A list of SMA values. The first `window_size - 1` elements 
            will be 0.0, as there is insufficient data to calculate a full window.

    Raises:
        ValueError: If `window_size` is less than 1, or if `prices` is empty.
    """
    if not prices:
        raise ValueError("Price list cannot be empty.")
    if window_size < 1:
        raise ValueError("Window size must be at least 1 to calculate SMA.")

    smas: List[float] = [0.0] * (window_size - 1)
    
    for i in range(len(prices) - window_size + 1):
        window = prices[i:i + window_size]
        smas.append(sum(window) / window_size)
        
    return smas
