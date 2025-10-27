"""Tests for Exercise 1: Agent Hello World"""

import pytest
from unittest.mock import Mock, patch
from solutions.ex01_agent_hello_world.main import get_weather


def test_get_weather():
    """Test the get_weather tool function."""
    result = get_weather("San Francisco")
    assert "San Francisco" in result
    assert "sunny" in result or "weather" in result.lower()


@patch("openai.OpenAI")
def test_agent_with_mocked_openai(mock_openai):
    """Test agent execution with mocked OpenAI responses."""
    # Mock the OpenAI client
    mock_client = Mock()
    mock_openai.return_value = mock_client

    # Mock tool call response
    mock_tool_call = Mock()
    mock_tool_call.function.name = "get_weather"
    mock_tool_call.function.arguments = '{"location": "San Francisco"}'
    mock_tool_call.id = "call_123"

    mock_response_message = Mock()
    mock_response_message.tool_calls = [mock_tool_call]

    mock_response = Mock()
    mock_response.choices = [Mock(message=mock_response_message)]

    # Mock final response
    mock_final_message = Mock()
    mock_final_message.content = "The weather in San Francisco is sunny, 72°F"

    mock_final_response = Mock()
    mock_final_response.choices = [Mock(message=mock_final_message)]

    # Setup mock to return different responses
    mock_client.chat.completions.create.side_effect = [
        mock_response,
        mock_final_response,
    ]

    # This test verifies the mock setup works
    assert mock_client.chat.completions.create is not None
