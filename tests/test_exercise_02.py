"""Tests for Exercise 2: Temporal Hello World"""

import pytest
from solutions.02_temporal_hello_world.activities import process_data


@pytest.mark.asyncio
async def test_process_data():
    """Test the process_data activity."""
    # Note: This is a simplified test without full Temporal test environment
    # In production, you would use Temporal's testing framework
    result = await process_data("test data")
    assert "test data" in result.upper()
    assert "PROCESSED" in result or "processed" in result.lower()
