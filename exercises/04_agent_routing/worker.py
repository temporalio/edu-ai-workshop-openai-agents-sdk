"""
Temporal worker for the routing workflow pattern.

TODO: Complete the worker implementation below.

A worker polls the Temporal server for workflow tasks and executes them.
"""

import asyncio
from datetime import timedelta
from temporalio.client import Client
from temporalio.worker import Worker
from temporalio.contrib.openai_agents import OpenAIAgentsPlugin, ModelActivityParameters

# Import the workflow class that this worker will execute
from workflow import RoutingWorkflow, TASK_QUEUE


async def main() -> None:
    """
    Start the Temporal worker that executes routing workflows.

    TODO: Complete this function to:
    1. Connect to Temporal server at "localhost:7233"
    2. Include OpenAIAgentsPlugin with 30-second timeout
    3. Create a Worker with:
       - The connected client
       - The TASK_QUEUE
       - RoutingWorkflow in the workflows list
    4. Run the worker
    """
    # TODO: Connect to Temporal client with OpenAIAgentsPlugin
    # client = await Client.connect(...)

    # TODO: Create the worker instance
    # worker = Worker(...)

    # TODO: Log worker startup
    print(f"🚀 Worker started successfully")
    print(f"📋 Task Queue: {TASK_QUEUE}")
    print(f"⏳ Polling for tasks... (Press Ctrl+C to stop)\n")

    # TODO: Start the worker
    # await worker.run()


if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())
