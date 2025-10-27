"""Tests for Exercise 3: Durable Agent"""

import pytest
from solutions.03_durable_agent.activities import get_weather


def test_get_weather_durable():
    """Test the get_weather tool in durable agent."""
    result = get_weather("London")
    assert "London" in result
    assert "rainy" in result or "weather" in result.lower()


def test_get_weather_unknown_location():
    """Test get_weather with unknown location."""
    result = get_weather("UnknownCity")
    assert "UnknownCity" in result
    assert "cloudy" in result or "weather" in result.lower()
