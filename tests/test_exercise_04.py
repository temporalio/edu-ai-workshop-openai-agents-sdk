"""Tests for Exercise 4: Multi-Agent Handoff"""

import pytest
from solutions.04_multi_agent_handoff.activities import get_weather, get_time


def test_get_weather_multi_agent():
    """Test weather tool in multi-agent system."""
    result = get_weather("Tokyo")
    assert "Tokyo" in result
    assert "clear" in result or "weather" in result.lower()


def test_get_time():
    """Test time tool function."""
    result = get_time("New York")
    assert "New York" in result
    assert "EST" in result or "time" in result.lower()


def test_get_time_unknown_location():
    """Test get_time with unknown location."""
    result = get_time("UnknownCity")
    assert "UnknownCity" in result
    assert "PM" in result or "AM" in result or "time" in result.lower()
