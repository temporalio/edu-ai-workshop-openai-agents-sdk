"""Exercise 2: Temporal Workflows - Complete Solution"""

from datetime import timedelta
from temporalio import workflow

# Import activities
with workflow.unsafe.imports_passed_through():
    from .activities import process_data


@workflow.defn
class HelloWorkflow:
    """
    Workflow: Orchestrate activity execution.

    Workflows are durable functions that:
    - Coordinate activity execution
    - Maintain state across failures
    - Can be paused and resumed
    """

    @workflow.run
    async def run(self, name: str) -> str:
        """
        Run the workflow.

        Args:
            name: Input parameter for the workflow

        Returns:
            Result message from the workflow
        """
        workflow.logger.info(f"🚀 Workflow started with input: {name}")

        # Execute activity with timeout
        # Activities handle the actual work and can be retried
        result = await workflow.execute_activity(
            process_data,
            args=[f"Hello {name}"],
            start_to_close_timeout=timedelta(seconds=10),
        )

        workflow.logger.info(f"✅ Workflow completed successfully")

        return f"Workflow result: {result}"
