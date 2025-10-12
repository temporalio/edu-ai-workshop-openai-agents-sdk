"""Exercise 3: Durable Agent Activities - Complete Solution"""

import os
from temporalio import activity
from temporalio.common import RetryPolicy
from openai import OpenAI


def get_weather(location: str) -> str:
    """Tool function: Get weather for a location."""
    weather_data = {
        "San Francisco": "sunny, 72°F",
        "New York": "cloudy, 65°F",
        "London": "rainy, 58°F",
        "Tokyo": "clear, 70°F",
    }
    weather = weather_data.get(location, "partly cloudy, 68°F")
    return f"The weather in {location} is {weather}"


@activity.defn
async def call_agent_with_tools(query: str, trace_id: str) -> str:
    """
    Activity: Call OpenAI agent with tools.

    Wrapping LLM calls in activities provides:
    - Automatic retries on API failures
    - Execution history and observability
    - State persistence across crashes
    """
    activity.logger.info(f"🤖 Activity started: Agent query")
    activity.logger.info(f"   Query: {query}")
    activity.logger.info(f"   Trace ID: {trace_id}")

    # Initialize OpenAI client
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Define tool schema
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get the current weather for a location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city name",
                        }
                    },
                    "required": ["location"],
                },
            },
        }
    ]

    # Initial API call
    messages = [{"role": "user", "content": query}]
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools,
    )

    # Handle tool calls
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    if tool_calls:
        activity.logger.info(f"🔧 Tool calls detected: {len(tool_calls)}")
        messages.append(response_message)

        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_args = eval(tool_call.function.arguments)
            activity.logger.info(f"   Calling: {function_name}({function_args})")

            # Execute tool
            if function_name == "get_weather":
                function_response = get_weather(**function_args)

                messages.append({
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                })

        # Get final response
        final_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
        )
        final_message = final_response.choices[0].message.content
    else:
        final_message = response_message.content

    activity.logger.info(f"✅ Activity completed: Agent response generated")
    return final_message
