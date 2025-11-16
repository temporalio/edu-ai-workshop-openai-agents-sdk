"""
Workflow starter for the routing workflow pattern.

This script connects to the Temporal server and executes a routing workflow.
It demonstrates how to:
- Connect a client with OpenAI Agents SDK plugin
- Start a workflow with a unique ID
- Pass query parameters to the workflow
- Wait for and display results

To run: python starter.py "Your query here"
Example: python starter.py "¡Hola! Cuéntame un trabalenguas."
"""

import asyncio
import sys
from datetime import datetime

import pytz
from dotenv import load_dotenv
from temporalio.client import Client
from temporalio.contrib.openai_agents import OpenAIAgentsPlugin

# Import workflow class and task queue from workflow module
from workflow import TASK_QUEUE, RoutingWorkflow

# Load environment variables from .env file (includes OPENAI_API_KEY)
load_dotenv()


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
    # Get query from command line argument or use default
    if len(sys.argv) > 1:
        query = sys.argv[1]
    else:
        query = "Hi! Tell me a tongue twister."

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
    print(f"💬 Query: {query}")

    # Start the workflow and get handle for tracking
    # Using start_workflow (not execute_workflow) returns handle immediately
    # This allows observing workflow progress before it completes
    handle = await client.start_workflow(
        RoutingWorkflow.run,  # Workflow method to execute
        query,  # User query parameter passed to workflow
        id=workflow_id,  # Unique workflow ID for tracking in Temporal UI
        task_queue=TASK_QUEUE,  # Queue where worker will pick up this workflow
    )

    # Print Temporal UI link for observing workflow execution and agent handoffs
    print(f"✅ Workflow started: {handle.id}")
    print(
        f"🔗 View in Temporal UI: http://localhost:8233/namespaces/default/workflows/{workflow_id}\n"
    )
    print("⏳ Waiting for agent response...\n")

    # Wait for the workflow to complete and get the result
    result = await handle.result()

    print(f"💬 Agent Response: {result}")


if __name__ == "__main__":
    # Run the async main function
    # This executes the workflow and displays results
    asyncio.run(main())
