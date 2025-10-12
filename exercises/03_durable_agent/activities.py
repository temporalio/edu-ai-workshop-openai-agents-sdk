"""Exercise 3: Durable Agent Activities - Starter Code"""

import os
from temporalio import activity
from openai import OpenAI


def get_weather(location: str) -> str:
    """Tool function: Get weather for a location."""
    weather_data = {
        "San Francisco": "sunny, 72°F",
        "New York": "cloudy, 65°F",
        "London": "rainy, 58°F",
    }
    return f"The weather in {location} is {weather_data.get(location, 'partly cloudy, 68°F')}"


@activity.defn
async def call_agent_with_tools(query: str, trace_id: str) -> str:
    """
    Activity: Call OpenAI agent with tools.

    Wrapping LLM calls in activities provides:
    - Automatic retries on API failures
    - Execution history and observability
    - State persistence across crashes
    """
    activity.logger.info(f"🤖 Calling agent with query: {query}")
    activity.logger.info(f"   Trace ID: {trace_id}")

    # TODO: Initialize OpenAI client
    # client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # TODO: Define tool schema for the agent
    # tools = [...]

    # TODO: Make initial API call with the query
    # messages = [{"role": "user", "content": query}]
    # response = client.chat.completions.create(...)

    # TODO: Handle tool calls if present
    # if tool_calls:
    #     # Execute tools and get final response
    #     pass

    # TODO: Return the agent's response
    return "TODO: Implement agent call"
