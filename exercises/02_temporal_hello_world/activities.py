"""Exercise 2: Temporal Activities - Starter Code"""

from temporalio import activity


@activity.defn
async def process_data(data: str) -> str:
    """
    Activity: Process some data.

    Activities are the unit of work in Temporal that:
    - Can be retried automatically on failure
    - Have their execution recorded
    - Can be called from workflows
    """
    # TODO: Add logging to show activity execution
    # activity.logger.info(f"Processing data: {data}")

    # TODO: Simulate some work (e.g., data processing)
    # In a real app, this might call external APIs, databases, etc.

    # TODO: Return processed result
    pass
