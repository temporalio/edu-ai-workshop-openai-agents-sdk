"""Exercise 2: Temporal Activities - Complete Solution"""

import asyncio
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
    activity.logger.info(f"🔧 Activity started: Processing '{data}'")

    # Simulate some work (in real apps: API calls, DB queries, etc.)
    await asyncio.sleep(1)

    result = f"Processed: {data.upper()}"
    activity.logger.info(f"✅ Activity completed: {result}")

    return result
