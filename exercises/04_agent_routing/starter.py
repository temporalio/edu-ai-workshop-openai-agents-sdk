"""
Workflow starter for the routing workflow pattern.

TODO: Complete the starter implementation below.

This script connects to Temporal and executes the routing workflow.
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
    3. Choose a query in French, Spanish, or English
    4. Start the workflow using client.start_workflow()
    5. Wait for and display the result
    """
    # TODO: Connect to Temporal client with OpenAIAgentsPlugin
    # client = await Client.connect(...)

    # TODO: Generate workflow ID with EST timestamp
    # Format: "routing-{day}-{month}-{date}-{time}est"
    # est = pytz.timezone("US/Eastern")
    # now = datetime.now(est)
    # workflow_id = f"routing-{now.strftime('%a-%b-%d-%I%M%S').lower()}est"

    # Sample queries in different languages
    queries = [
        "Bonjour! Comment allez-vous aujourd'hui?",  # French
        "¡Hola! ¿Cómo estás hoy?",  # Spanish
        "Hello! How are you doing today?",  # English
    ]

    # TODO: Choose a query to test
    # query = queries[0]  # Change index to test different languages

    # TODO: Print starting information
    # print("🚀 Starting Routing Workflow")
    # print(f"📋 Workflow ID: {workflow_id}")
    # print(f"💬 Query: {query}\n")

    # TODO: Start the workflow
    # handle = await client.start_workflow(...)

    # TODO: Print workflow started message and Temporal UI link
    # print(f"✅ Workflow started: {handle.id}")
    # print(f"🔗 View in Temporal UI: http://localhost:8233/namespaces/default/workflows/{workflow_id}\n")
    # print("⏳ Waiting for agent response...\n")

    # TODO: Wait for workflow result
    # result = await handle.result()

    # TODO: Display the result
    # print("=" * 70)
    # print("🤖 Agent Response")
    # print("=" * 70)
    # print(result)
    # print("=" * 70)


if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())
