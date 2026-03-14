"""
Unit tests for the data_processor module.
"""

import unittest
from data_processor import calculate_rolling_volatility, calculate_simple_moving_average

class TestDataProcessor(unittest.TestCase):
    """Test suite for financial data processing utilities."""

    def setUp(self) -> None:
        self.sample_prices = [10.0, 12.0, 11.0, 14.0, 13.0, 15.0]

    def test_calculate_simple_moving_average(self) -> None:
        """Tests the SMA calculation with a valid window."""
        expected_sma_3 = [0.0, 0.0, 11.0, 12.333333333333334, 12.666666666666666, 14.0]
        result = calculate_simple_moving_average(self.sample_prices, window_size=3)
        
        for e, r in zip(expected_sma_3, result):
            self.assertAlmostEqual(e, r, places=5)

    def test_sma_invalid_window(self) -> None:
        """Tests SMA calculation with an invalid window size."""
        with self.assertRaises(ValueError):
            calculate_simple_moving_average(self.sample_prices, window_size=0)

    def test_calculate_rolling_volatility(self) -> None:
        """Tests the rolling volatility calculation."""
        result = calculate_rolling_volatility(self.sample_prices, window_size=3)
        self.assertEqual(len(result), len(self.sample_prices))
        self.assertAlmostEqual(result[2], 1.0, places=5)
        self.assertAlmostEqual(result[3], 1.5275252316519465, places=5)

    def test_volatility_invalid_window(self) -> None:
        """Tests volatility calculation with an invalid window size."""
        with self.assertRaises(ValueError):
            calculate_rolling_volatility(self.sample_prices, window_size=1)

if __name__ == '__main__':
    unittest.main()
