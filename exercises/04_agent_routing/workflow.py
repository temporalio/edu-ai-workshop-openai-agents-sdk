"""
Routing workflow implementation using OpenAI Agents SDK.

TODO: Complete the agent definitions and workflow implementation below.

This workflow demonstrates intelligent request distribution to specialized
language agents using the handoff pattern.
"""

from temporalio import workflow
from agents import Agent, Runner
from openai.types.chat import ChatCompletionMessageParam

# Task queue name for this workflow pattern
TASK_QUEUE = "routing-workflow-queue"


def french_agent() -> Agent:
    """
    Create a French language specialist agent.

    TODO: Complete this function to return an Agent that:
    - Has name "French Agent"
    - Only speaks French
    - Uses "gpt-4" model
    """
    # TODO: Implement French agent
    pass


def spanish_agent() -> Agent:
    """
    Create a Spanish language specialist agent.

    TODO: Complete this function to return an Agent that:
    - Has name "Spanish Agent"
    - Only speaks Spanish
    - Uses "gpt-4" model
    """
    # TODO: Implement Spanish agent
    pass


def english_agent() -> Agent:
    """
    Create an English language specialist agent.

    TODO: Complete this function to return an Agent that:
    - Has name "English Agent"
    - Only speaks English
    - Uses "gpt-4" model
    """
    # TODO: Implement English agent
    pass


def triage_agent() -> Agent:
    """
    Create a triage agent that routes requests to language specialists.

    TODO: Complete this function to return an Agent that:
    - Has name "Triage Agent"
    - Detects language and routes to appropriate specialist
    - Has handoffs to all three language agents
    - Uses "gpt-4" model
    """
    # TODO: Implement triage agent with handoffs
    pass


@workflow.defn
class RoutingWorkflow:
    """
    Workflow that routes user queries to specialized language agents.

    TODO: Complete the run method to execute the routing workflow.
    """

    @workflow.run
    async def run(self, user_query: str) -> str:
        """
        Execute the routing workflow with language detection and handoff.

        Args:
            user_query: The user's input in any language (French/Spanish/English)

        Returns:
            The specialist agent's response in the appropriate language

        TODO: Implement the workflow run method:
        1. Format the user query as a ChatCompletionMessageParam with role="user"
        2. Execute the triage agent with: await Runner.run(triage_agent(), new_message)
        3. Extract and return result.final_output

        Hint: Runner.run() takes (agent, message) - no config parameter needed!
        """
        # TODO: Implement workflow execution logic
        pass
