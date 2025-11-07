"""
Temporal worker for the routing workflow pattern.

TODO: Complete the worker implementation below.

A worker polls the Temporal server for workflow tasks and executes them.
This worker is configured to handle RoutingWorkflow executions using the
OpenAI Agents SDK plugin for agent integration.
"""

import asyncio
from datetime import timedelta

from dotenv import load_dotenv
from temporalio.client import Client
from temporalio.contrib.openai_agents import ModelActivityParameters, OpenAIAgentsPlugin
from temporalio.worker import Worker

# Import the workflow class that this worker will execute
from workflow import RoutingWorkflow, TASK_QUEUE

# Load environment variables from .env file (includes OPENAI_API_KEY)
load_dotenv()


async def main() -> None:
    """
    Start the Temporal worker that executes routing workflows.

    TODO: Complete this function to:
    1. Connect to Temporal server at "localhost:7233" with OpenAIAgentsPlugin
       - Include OpenAIAgentsPlugin with ModelActivityParameters
       - Set start_to_close_timeout to 30 seconds for LLM calls
    2. Create a Worker with:
       - The connected client
       - The TASK_QUEUE
       - RoutingWorkflow in the workflows list
    3. Log worker startup information
    4. Run the worker (this will block until stopped)

    Example connection pattern:
        client = await Client.connect(
            "localhost:7233",
            plugins=[
                OpenAIAgentsPlugin(
                    model_params=ModelActivityParameters(
                        start_to_close_timeout=timedelta(seconds=30)
                    )
                )
            ],
        )

    Example worker creation:
        worker = Worker(
            client,
            task_queue=TASK_QUEUE,
            workflows=[RoutingWorkflow],
        )

    Example logging:
        print(f"🚀 Worker started successfully")
        print(f"📋 Task Queue: {TASK_QUEUE}")
        print(f"🔄 Workflows: {[w.__name__ for w in [RoutingWorkflow]]}")
        print(f"⏳ Polling for tasks... (Press Ctrl+C to stop)\\n")
    """
    # TODO: Connect to Temporal client with OpenAIAgentsPlugin
    # Hint: Use Client.connect() with localhost:7233 and OpenAIAgentsPlugin

    # TODO: Create the worker instance
    # Hint: Use Worker() with client, task_queue, and workflows parameters

    # TODO: Log worker startup information
    # Hint: Print emoji messages showing task queue and workflow names

    # TODO: Start the worker (this blocks until stopped)
    # Hint: await worker.run()

    # Placeholder message - remove after completing TODOs
    print("⚠️  Worker setup incomplete. Complete the TODOs above to run the worker.")


if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())
