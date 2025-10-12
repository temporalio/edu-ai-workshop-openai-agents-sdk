"""Exercise 4: Multi-Agent Handoff Workflows - Starter Code"""

from datetime import timedelta
from temporalio import workflow
from temporalio.common import RetryPolicy

# Import activities
# from .activities import triage_query, weather_agent, time_agent


@workflow.defn
class MultiAgentWorkflow:
    """
    Workflow: Orchestrate multi-agent handoffs.

    The workflow:
    1. Uses triage agent to determine routing
    2. Calls appropriate specialist agent
    3. Maintains context across handoffs
    4. Returns combined results
    """

    @workflow.run
    async def run(self, query: str, trace_id: str) -> str:
        """
        Run multi-agent workflow with handoffs.

        Args:
            query: User query
            trace_id: Trace ID for observability

        Returns:
            Final response from agent(s)
        """
        workflow.logger.info(f"🚀 Multi-agent workflow started")
        workflow.logger.info(f"   Query: {query}")

        # Context to maintain across agent handoffs
        context = {"history": [], "trace_id": trace_id}

        # TODO: Call triage agent to determine routing
        # agent_to_use = await workflow.execute_activity(...)

        # TODO: Call the appropriate specialist agent based on triage
        # if agent_to_use == "weather_agent":
        #     result = await workflow.execute_activity(weather_agent, ...)
        # elif agent_to_use == "time_agent":
        #     result = await workflow.execute_activity(time_agent, ...)

        # TODO: Return the result
        return "TODO: Implement multi-agent orchestration"
