"""
Temporal worker for the routing workflow pattern.

A worker is a process that polls the Temporal server for workflow and activity
tasks, then executes them. This worker is configured to:
- Handle RoutingWorkflow executions
- Use OpenAI Agents SDK plugin for agent integration
- Poll the routing-workflow-queue for tasks

To run: python worker.py
"""

import asyncio
from datetime import timedelta
# Import the workflow class that this worker will execute
from routing_workflow import RoutingWorkflow, TASK_QUEUE
from temporalio.client import Client
from temporalio.contrib.openai_agents import ModelActivityParameters, OpenAIAgentsPlugin
from temporalio.worker import Worker

async def main():
    """
    Start the Temporal worker that executes routing workflows.

    The worker:
    1. Connects to the Temporal server with OpenAI Agents SDK plugin
    2. Registers the RoutingWorkflow for execution
    3. Polls the task queue continuously for new work
    4. Executes workflows when tasks are available

    The worker runs indefinitely until stopped (Ctrl+C).
    """
    # Connect to local Temporal server
    # The OpenAI Agents SDK plugin is required for agent-based workflows
    client = await Client.connect(
        "localhost:7233",  # Temporal server address (default local dev server)
        plugins=[
            # Enable OpenAI Agents SDK integration with Temporal
            # This plugin handles the coordination between agents and Temporal activities
            OpenAIAgentsPlugin(
                # Configure timeout settings for AI model inference activities
                # LLM calls can take time, so we set a generous timeout
                model_params=ModelActivityParameters(
                    start_to_close_timeout=timedelta(seconds=30)  # Max time for each LLM call
                )
            )
        ],
    )

    # Create the worker instance
    # The worker polls the task queue and executes workflows assigned to it
    worker = Worker(
        client,  # Use the connected Temporal client
        task_queue=TASK_QUEUE,  # Which queue to poll for tasks
        workflows=[RoutingWorkflow],  # List of workflows this worker can execute
        # Note: No activities are registered here because the OpenAI Agents SDK
        # plugin automatically creates activities for agent execution
    )

    # Log worker startup for observability
    print(f"🚀 Worker started successfully")
    print(f"📋 Task Queue: {TASK_QUEUE}")
    print(f"🔄 Workflows: {[w.__name__ for w in [RoutingWorkflow]]}")
    print(f"⏳ Polling for tasks... (Press Ctrl+C to stop)\n")

    # Start the worker - this blocks indefinitely, processing tasks as they arrive
    # The worker will continue running until explicitly stopped
    await worker.run()


if __name__ == "__main__":
    # Run the async main function
    # This starts the worker and keeps it running until interrupted
    asyncio.run(main())
