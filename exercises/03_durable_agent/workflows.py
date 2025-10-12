"""Exercise 3: Durable Agent Workflows - Starter Code"""

from datetime import timedelta
from temporalio import workflow

# Import activities
# from .activities import call_agent_with_tools


@workflow.defn
class DurableAgentWorkflow:
    """
    Workflow: Orchestrate durable AI agent execution.

    Benefits of using workflows for agents:
    - State persists across failures
    - Automatic retry of LLM calls
    - Full execution history
    - Correlation with external systems via trace_id
    """

    @workflow.run
    async def run(self, query: str, trace_id: str) -> str:
        """
        Run the durable agent workflow.

        Args:
            query: User query for the agent
            trace_id: Unique ID for observability correlation

        Returns:
            Agent response
        """
        workflow.logger.info(f"🚀 Durable agent workflow started")
        workflow.logger.info(f"   Query: {query}")
        workflow.logger.info(f"   Trace ID: {trace_id}")

        # TODO: Call the agent activity with retry policy
        # result = await workflow.execute_activity(
        #     call_agent_with_tools,
        #     args=[query, trace_id],
        #     start_to_close_timeout=timedelta(seconds=30),
        #     retry_policy=...,
        # )

        # TODO: Return the agent response
        return "TODO: Implement workflow"
