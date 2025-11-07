"""
Routing workflow implementation using OpenAI Agents SDK.

TODO: Complete the agent definitions and workflow implementation below.

This workflow demonstrates intelligent request distribution to specialized
language agents using the handoff pattern.
"""

from temporalio import workflow
from agents import Agent, RunConfig, Runner, TResponseInputItem, trace

# Task queue name for this workflow pattern
TASK_QUEUE = "routing-workflow-queue"


def french_agent() -> Agent:
    """
    Create a French language specialist agent.

    TODO: Complete this function to return an Agent that:
    - Has name "French Agent"
    - Only speaks French
    - Uses "gpt-4" model

    Example structure:
        return Agent(
            name="French Agent",
            instructions="You only speak French. Respond naturally to user queries in French.",
            model="gpt-4",
        )
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

    Example structure:
        return Agent(
            name="Spanish Agent",
            instructions="You only speak Spanish. Respond naturally to user queries in Spanish.",
            model="gpt-4",
        )
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

    Example structure:
        return Agent(
            name="English Agent",
            instructions="You only speak English. Respond naturally to user queries in English.",
            model="gpt-4",
        )
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

    Example structure:
        return Agent(
            name="Triage Agent",
            instructions=(
                "You are a triage agent. Analyze the language of the user's query "
                "and handoff to the appropriate language specialist agent. "
                "Detect if the query is in French, Spanish, or English, then route accordingly."
            ),
            handoffs=[french_agent(), spanish_agent(), english_agent()],
            model="gpt-4",
        )
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
    async def run(self, msg: str) -> str:
        """
        Execute the routing workflow with language detection and handoff.

        Args:
            msg: The user's input in any language (French/Spanish/English)

        Returns:
            The specialist agent's response in the appropriate language (formatted string)

        TODO: Implement the workflow run method:
        1. Create a RunConfig instance: config = RunConfig()
        2. Wrap execution in trace context: with trace("Routing example"):
        3. Format the user query as input list:
           inputs: list[TResponseInputItem] = [{"content": msg, "role": "user"}]
        4. Execute the triage agent with:
           result = await Runner.run(
               triage_agent(),
               input=inputs,
               run_config=config,
           )
        5. Log handoff completion: workflow.logger.info("Handoff completed")
        6. Return formatted result: return f"Response: {result.final_output}"

        Note: The parameter names are important:
        - Use input=inputs (not just passing inputs as positional argument)
        - Use run_config=config (not config=config)
        """
        # TODO: Implement workflow execution logic
        pass
