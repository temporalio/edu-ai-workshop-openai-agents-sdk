"""Exercise 3: Durable Agent - Starter Code"""

import asyncio
import uuid
from temporalio.client import Client
from temporalio.worker import Worker

# Import workflow and activities
# from .workflows import DurableAgentWorkflow
# from .activities import call_agent_with_tools


async def main():
    """Run the durable agent workflow."""
    print("\n🚀 Exercise 3: Durable Agent\n")

    # TODO: Generate a unique trace ID for observability
    # trace_id = str(uuid.uuid4())
    # print(f"Trace ID: {trace_id}\n")

    # TODO: Connect to Temporal
    # client = await Client.connect("localhost:7233")

    # TODO: Start worker
    # async with Worker(
    #     client,
    #     task_queue="durable-agent-queue",
    #     workflows=[DurableAgentWorkflow],
    #     activities=[call_agent_with_tools],
    # ):
    #     # TODO: Execute workflow
    #     query = "What's the weather like in San Francisco?"
    #     workflow_id = f"durable-agent-{trace_id}"
    #
    #     result = await client.execute_workflow(
    #         DurableAgentWorkflow.run,
    #         args=[query, trace_id],
    #         id=workflow_id,
    #         task_queue="durable-agent-queue",
    #     )
    #
    #     print(f"\n✅ Agent Response:\n{result}\n")
    #     print(f"View in Temporal UI: http://localhost:8233/namespaces/default/workflows/{workflow_id}")
    #     print(f"Trace ID: {trace_id}\n")

    print("⚠️  This is starter code - implement the TODOs above!")
    print("   Check solutions/03_durable_agent/ for the complete solution\n")


if __name__ == "__main__":
    asyncio.run(main())
