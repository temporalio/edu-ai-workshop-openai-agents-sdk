"""Exercise 1: Agent Hello World - Complete Solution"""

import os
from dotenv import load_dotenv
from openai import OpenAI
from rich.console import Console

# Load environment variables
load_dotenv()
console = Console()


def get_weather(location: str) -> str:
    """
    Tool function: Get current weather for a location.

    In a real application, this would call a weather API.
    For this exercise, we return mock data.
    """
    weather_data = {
        "San Francisco": "sunny, 72°F",
        "New York": "cloudy, 65°F",
        "London": "rainy, 58°F",
        "Tokyo": "clear, 70°F",
    }
    # Default weather if location not in our mock data
    weather = weather_data.get(location, "partly cloudy, 68°F")
    return f"The weather in {location} is {weather}"


def main():
    """Run the agent with a simple weather query."""
    console.print("\n[bold cyan]🤖 Exercise 1: Agent Hello World[/bold cyan]\n")

    # Initialize OpenAI client
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Define the tool schema for OpenAI
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
                            "description": "The city name, e.g., San Francisco",
                        }
                    },
                    "required": ["location"],
                },
            },
        }
    ]

    # User query that will trigger the tool
    query = "What's the weather like in San Francisco?"
    console.print(f"[yellow]Query:[/yellow] {query}\n")

    # Initial API call
    messages = [{"role": "user", "content": query}]
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools,
    )

    # Check if the model wants to call a tool
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    if tool_calls:
        # Execute tool calls
        console.print("[green]🔧 Tool Called:[/green]")
        messages.append(response_message)

        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_args = eval(tool_call.function.arguments)

            console.print(f"   {function_name}({function_args})")

            # Call our tool function
            if function_name == "get_weather":
                function_response = get_weather(**function_args)

                # Add tool response to messages
                messages.append({
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                })

        # Get final response from the model
        final_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
        )
        final_message = final_response.choices[0].message.content
    else:
        final_message = response_message.content

    console.print(f"\n[bold green]🤖 Agent Response:[/bold green]\n{final_message}\n")


if __name__ == "__main__":
    main()
