"""
Workflow starter for the routing workflow pattern.

TODO: Complete the starter implementation below.

This script connects to Temporal and executes the routing workflow.
It demonstrates how to:
- Connect a client with OpenAI Agents SDK plugin
- Start a workflow with a unique ID
- Pass query parameters to the workflow
- Wait for and display results

To run: python starter.py
"""

import asyncio

from dotenv import load_dotenv

# Import workflow class and task queue from workflow module

# Load environment variables from .env file (includes OPENAI_API_KEY)
load_dotenv()


async def main() -> None:
    """
    Execute the routing workflow with sample queries in different languages.

    TODO: Complete this function to:
    1. Connect to Temporal server at "localhost:7233" with OpenAIAgentsPlugin
    2. Generate a workflow ID with timestamp (use pytz for EST)
    3. Choose a query: "Hi! Tell me a tongue twister."
    4. Print starting information (workflow ID)
    5. Start the workflow using client.start_workflow()
    6. Print the Temporal UI link and result

    Example workflow ID generation:
        est = pytz.timezone("US/Eastern")
        now = datetime.now(est)
        workflow_id = f"routing-{now.strftime('%a-%b-%d-%I%M%S').lower()}est"

    Example workflow execution:
        handle = await client.start_workflow(
            RoutingWorkflow.run,
            query,
            id=workflow_id,
            task_queue=TASK_QUEUE,
        )
        result = await handle.result()

    Note: Use start_workflow() (not execute_workflow()) to get handle first, then await result
    This pattern allows observing workflow progress before completion
    """
    # TODO: Connect to Temporal client with OpenAIAgentsPlugin
    # Hint: await Client.connect("localhost:7233", plugins=[OpenAIAgentsPlugin()])

    # TODO: Generate workflow ID with EST timestamp
    # Format: "routing-{day}-{month}-{date}-{time}est"
    # Hint: Use pytz.timezone("US/Eastern") and datetime.now()

    # TODO: Define the query to test
    # Use: "Hi! Tell me a tongue twister."

    # TODO: Print starting information
    # Print: 🚀 Starting Routing Workflow
    # Print: 📋 Workflow ID: {workflow_id}

    # TODO: Start the workflow and get handle
    # Hint: handle = await client.start_workflow(RoutingWorkflow.run, query, id=workflow_id, task_queue=TASK_QUEUE)

    # TODO: Print workflow started confirmation and Temporal UI link
    # Print: ✅ Workflow started: {handle.id}
    # Print: 🔗 View in Temporal UI: http://localhost:8233/namespaces/default/workflows/{workflow_id}
    # Print: ⏳ Waiting for agent response...

    # TODO: Wait for workflow to complete and get result
    # Hint: result = await handle.result()

    # TODO: Display the result
    # Print: 💬 Agent Response: {result}

    pass


if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())
