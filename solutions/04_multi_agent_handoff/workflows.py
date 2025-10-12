"""Exercise 4: Multi-Agent Handoff Workflows - Complete Solution"""

from datetime import timedelta
from temporalio import workflow
from temporalio.common import RetryPolicy

with workflow.unsafe.imports_passed_through():
    from .activities import triage_query, weather_agent, time_agent


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
        """Run multi-agent workflow with handoffs."""
        workflow.logger.info(f"🚀 Multi-agent workflow started")
        workflow.logger.info(f"   Query: {query}")
        workflow.logger.info(f"   Trace ID: {trace_id}")

        # Context to maintain across agent handoffs
        context = {"history": [], "trace_id": trace_id}

        # Triage to determine which agent to use
        agent_to_use = await workflow.execute_activity(
            triage_query,
            args=[query],
            start_to_close_timeout=timedelta(seconds=10),
            retry_policy=RetryPolicy(
                maximum_attempts=3,
                initial_interval=timedelta(seconds=1),
            ),
        )

        workflow.logger.info(f"   Routing to: {agent_to_use}")

        # Call the appropriate specialist agent
        if agent_to_use == "weather_agent":
            result = await workflow.execute_activity(
                weather_agent,
                args=[query, context],
                start_to_close_timeout=timedelta(seconds=30),
                retry_policy=RetryPolicy(maximum_attempts=3),
            )
        elif agent_to_use == "time_agent":
            result = await workflow.execute_activity(
                time_agent,
                args=[query, context],
                start_to_close_timeout=timedelta(seconds=30),
                retry_policy=RetryPolicy(maximum_attempts=3),
            )
        else:
            result = "Query routed to general agent (not implemented in this exercise)"

        workflow.logger.info(f"✅ Multi-agent workflow completed")
        return result
