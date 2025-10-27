"""
Workflow starter for the routing workflow pattern.

This script connects to the Temporal server and executes a routing workflow.
It demonstrates how to:
- Connect a client with OpenAI Agents SDK plugin
- Start a workflow with a unique ID
- Pass query parameters to the workflow
- Wait for and display results

To run: python starter.py
"""

import asyncio
from datetime import datetime
import pytz
from temporalio.client import Client
from temporalio.contrib.openai_agents import OpenAIAgentsPlugin

# Import workflow class and task queue from workflow module
from routing_workflow import RoutingWorkflow, TASK_QUEUE


async def main():
    """
    Execute the routing workflow with sample queries in different languages.

    This function:
    1. Connects to Temporal server with OpenAI Agents SDK plugin
    2. Generates a unique workflow ID with timestamp
    3. Starts the routing workflow with a user query
    4. Waits for the workflow to complete
    5. Displays the agent's response

    The workflow will route the query to the appropriate language specialist.
    """
    # Connect to local Temporal server
    # OpenAI Agents SDK plugin is required to coordinate agent execution
    client = await Client.connect(
        "localhost:7233",  # Temporal server address (default local dev server)
        plugins=[
            # Enable OpenAI Agents SDK integration
            # This plugin handles agent execution as Temporal activities
            OpenAIAgentsPlugin()
        ],
    )

    # Generate workflow ID with EST timestamp for human-readable tracking
    # This follows the workshop convention: {prefix}-{day}-{month}-{date}-{time}est
    est = pytz.timezone("US/Eastern")  # Create EST timezone object
    now = datetime.now(est)  # Get current time in EST
    # Format timestamp as readable string with day-month-date-time pattern
    workflow_id = f"routing-{now.strftime('%a-%b-%d-%I%M%S').lower()}est"

    print("🚀 Starting Routing Workflow")
    print(f"📋 Workflow ID: {workflow_id}")

    # Start the workflow (non-blocking) and get handle for tracking
    # Using start_workflow (not execute_workflow) allows us to get the handle first
    result = await client.execute_workflow(
        RoutingWorkflow.run,  # Workflow method to execute
        "Hi! Tell me a tongue twister.",  # User query parameter passed to workflow
        id=workflow_id,  # Unique workflow ID for tracking in Temporal UI
        task_queue=TASK_QUEUE,  # Queue where worker will pick up this workflow
    )

    # Print Temporal UI link for observing workflow execution and agent handoffs
    print(
        f"🔗 View in Temporal UI: http://localhost:8233/namespaces/default/workflows/{workflow_id}\n"
    )
    print("⏳ Waiting for agent response...\n")

    print(f"💬 Agent Response: {result}")


if __name__ == "__main__":
    # Run the async main function
    # This executes the workflow and displays results
    asyncio.run(main())
