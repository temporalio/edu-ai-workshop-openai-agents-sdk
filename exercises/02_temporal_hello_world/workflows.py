"""Exercise 2: Temporal Workflows - Starter Code"""

from datetime import timedelta
from temporalio import workflow

# Import activities
# from .activities import process_data


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
        # TODO: Call the process_data activity
        # result = await workflow.execute_activity(
        #     process_data,
        #     args=[f"Hello {name}"],
        #     start_to_close_timeout=timedelta(seconds=10),
        # )

        # TODO: Return the workflow result
        # return f"Workflow completed: {result}"

        return "TODO: Implement workflow execution"
