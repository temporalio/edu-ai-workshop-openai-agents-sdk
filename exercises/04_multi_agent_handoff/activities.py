"""Exercise 4: Multi-Agent Handoff Activities - Starter Code"""

import os
from temporalio import activity
from openai import OpenAI


@activity.defn
async def triage_query(query: str) -> str:
    """
    Activity: Triage agent that routes queries to specialist agents.

    Returns:
        Agent name to handle the query (e.g., "weather_agent", "time_agent")
    """
    activity.logger.info(f"🔍 Triaging query: {query}")

    # TODO: Use LLM to classify the query and determine routing
    # Options: "weather_agent", "time_agent", "general_agent"
    # Hint: Use system prompt to instruct the model to return just the agent name

    return "TODO: Implement triage logic"


@activity.defn
async def weather_agent(query: str, context: dict) -> str:
    """
    Activity: Specialized weather agent.

    Args:
        query: The user's query
        context: Conversation context from previous agents
    """
    activity.logger.info(f"🌤️  Weather agent handling query")

    # TODO: Implement weather agent with get_weather tool
    # This should be similar to Exercise 3 but specialized for weather

    return "TODO: Implement weather agent"


@activity.defn
async def time_agent(query: str, context: dict) -> str:
    """
    Activity: Specialized time agent.

    Args:
        query: The user's query
        context: Conversation context from previous agents
    """
    activity.logger.info(f"🕐 Time agent handling query")

    # TODO: Implement time agent with get_time tool
    # Create a tool function for getting time in different locations

    return "TODO: Implement time agent"
