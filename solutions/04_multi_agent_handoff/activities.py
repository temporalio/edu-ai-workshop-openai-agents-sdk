"""Exercise 4: Multi-Agent Handoff Activities - Complete Solution"""

import os
from datetime import datetime
from temporalio import activity
from openai import OpenAI


def get_weather(location: str) -> str:
    """Tool: Get weather for a location."""
    weather_data = {
        "San Francisco": "sunny, 72°F",
        "New York": "cloudy, 65°F",
        "London": "rainy, 58°F",
        "Tokyo": "clear, 70°F",
    }
    weather = weather_data.get(location, "partly cloudy, 68°F")
    return f"The weather in {location} is {weather}"


def get_time(location: str) -> str:
    """Tool: Get current time for a location (mock implementation)."""
    time_data = {
        "San Francisco": "10:45 AM PST",
        "New York": "1:45 PM EST",
        "London": "6:45 PM GMT",
        "Tokyo": "3:45 AM JST",
    }
    time = time_data.get(location, "12:00 PM")
    return f"The current time in {location} is {time}"


@activity.defn
async def triage_query(query: str) -> str:
    """
    Activity: Triage agent that routes queries to specialist agents.
    """
    activity.logger.info(f"🔍 Triaging query: {query}")

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Use LLM to classify the query
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a query classifier. Classify queries into one of: "
                    "'weather_agent', 'time_agent', or 'general_agent'. "
                    "Respond with ONLY the agent name, nothing else."
                ),
            },
            {"role": "user", "content": query},
        ],
    )

    agent_name = response.choices[0].message.content.strip()
    activity.logger.info(f"   → Routed to: {agent_name}")

    return agent_name


@activity.defn
async def weather_agent(query: str, context: dict) -> str:
    """Activity: Specialized weather agent."""
    activity.logger.info(f"🌤️  Weather agent handling query")

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get current weather for a location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {"type": "string", "description": "City name"}
                    },
                    "required": ["location"],
                },
            },
        }
    ]

    messages = [
        {"role": "system", "content": "You are a weather specialist assistant."},
        {"role": "user", "content": query},
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini", messages=messages, tools=tools
    )

    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    if tool_calls:
        messages.append(response_message)
        for tool_call in tool_calls:
            function_args = eval(tool_call.function.arguments)
            function_response = get_weather(**function_args)
            messages.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": "get_weather",
                "content": function_response,
            })

        final_response = client.chat.completions.create(
            model="gpt-4o-mini", messages=messages
        )
        result = final_response.choices[0].message.content
    else:
        result = response_message.content

    activity.logger.info(f"✅ Weather agent completed")
    return result


@activity.defn
async def time_agent(query: str, context: dict) -> str:
    """Activity: Specialized time agent."""
    activity.logger.info(f"🕐 Time agent handling query")

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_time",
                "description": "Get current time for a location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {"type": "string", "description": "City name"}
                    },
                    "required": ["location"],
                },
            },
        }
    ]

    messages = [
        {"role": "system", "content": "You are a time specialist assistant."},
        {"role": "user", "content": query},
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini", messages=messages, tools=tools
    )

    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    if tool_calls:
        messages.append(response_message)
        for tool_call in tool_calls:
            function_args = eval(tool_call.function.arguments)
            function_response = get_time(**function_args)
            messages.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": "get_time",
                "content": function_response,
            })

        final_response = client.chat.completions.create(
            model="gpt-4o-mini", messages=messages
        )
        result = final_response.choices[0].message.content
    else:
        result = response_message.content

    activity.logger.info(f"✅ Time agent completed")
    return result
