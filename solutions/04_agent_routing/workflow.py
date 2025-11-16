"""
Routing workflow implementation using OpenAI Agents SDK.

Demonstrates intelligent request distribution to specialized language agents.
The triage agent analyzes incoming queries and routes them to the appropriate
language specialist (French, Spanish, or English) using the handoff pattern.
"""

from agents import Agent, RunConfig, Runner, TResponseInputItem, trace
from temporalio import workflow

# Task queue name for this workflow pattern
TASK_QUEUE = "routing-workflow-queue"


def french_agent() -> Agent:
    """
    Create a French language specialist agent.

    This agent only communicates in French and handles French language queries.
    Uses OpenAI's GPT-4 model for natural language understanding and generation.
    """
    return Agent(
        name="French Agent",
        # Instruct the agent to respond exclusively in French
        instructions="You only speak French. Respond naturally to user queries in French.",
        model="gpt-4",  # OpenAI model as per workshop requirements
    )


def spanish_agent() -> Agent:
    """
    Create a Spanish language specialist agent.

    This agent only communicates in Spanish and handles Spanish language queries.
    Uses OpenAI's GPT-4 model for natural language understanding and generation.
    """
    return Agent(
        name="Spanish Agent",
        # Instruct the agent to respond exclusively in Spanish
        instructions="You only speak Spanish. Respond naturally to user queries in Spanish.",
        model="gpt-4",  # OpenAI model as per workshop requirements
    )


def english_agent() -> Agent:
    """
    Create an English language specialist agent.

    This agent only communicates in English and handles English language queries.
    Uses OpenAI's GPT-4 model for natural language understanding and generation.
    """
    return Agent(
        name="English Agent",
        # Instruct the agent to respond exclusively in English
        instructions="You only speak English. Respond naturally to user queries in English.",
        model="gpt-4",  # OpenAI model as per workshop requirements
    )


def triage_agent() -> Agent:
    """
    Create a triage agent that routes requests to language specialists.

    This agent analyzes the language of incoming queries and hands off to
    the appropriate specialist agent. This demonstrates the handoff pattern
    where one agent can transfer control to another specialized agent.

    The handoff pattern enables multi-agent architectures where different
    agents have different specializations and can collaborate on tasks.
    """
    return Agent(
        name="Triage Agent",
        # Instruct the triage agent to detect language and route appropriately
        instructions=(
            "You are a triage agent. Analyze the language of the user's query "
            "and handoff to the appropriate language specialist agent. "
            "Detect if the query is in French, Spanish, or English, then route accordingly."
        ),
        # Provide list of specialist agents available for handoff
        # The triage agent will choose which specialist to invoke based on language
        handoffs=[french_agent(), spanish_agent(), english_agent()],
        model="gpt-4",  # OpenAI model for language detection and routing
    )


@workflow.defn
class RoutingWorkflow:
    @workflow.run
    async def run(self, msg: str) -> str:
        config = RunConfig()

        with trace("Routing example"):
            inputs: list[TResponseInputItem] = [{"content": msg, "role": "user"}]

            # Run the triage agent to determine which language agent to handoff to
            result = await Runner.run(
                triage_agent(),
                input=inputs,
                run_config=config,
            )

            # Log that the handoff to the specialist agent has completed
            workflow.logger.info("Handoff completed")

            # Return the formatted response from the specialist agent
            return f"Response: {result.final_output}"
