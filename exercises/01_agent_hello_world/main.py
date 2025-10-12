"""Exercise 1: Agent Hello World - Starter Code"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()


def get_weather(location: str) -> str:
    """
    Tool function: Get current weather for a location.

    In a real application, this would call a weather API.
    For this exercise, we return mock data.
    """
    # TODO: Return mock weather data
    # Example: return f"The weather in {location} is sunny, 72°F"
    pass


def main():
    """Run the agent with a simple weather query."""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # TODO: Create an agent with system instructions
    # agent = client.beta.agents.create(...)

    # TODO: Register the tool function
    # agent.add_tool(get_weather)

    # TODO: Run the agent with a query
    # query = "What's the weather like in San Francisco?"
    # response = agent.run(query)

    # TODO: Print the response and tool calls
    # print(f"🤖 Agent Response: {response}")

    print("⚠️  This is starter code - implement the TODOs above!")
    print("   Check solutions/01_agent_hello_world/main.py for the complete solution")


if __name__ == "__main__":
    main()
