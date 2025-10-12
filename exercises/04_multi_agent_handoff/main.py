"""Exercise 4: Multi-Agent Handoff - Starter Code"""

import asyncio
import uuid
from temporalio.client import Client
from temporalio.worker import Worker

# Import workflow and activities
# from .workflows import MultiAgentWorkflow
# from .activities import triage_query, weather_agent, time_agent


async def main():
    """Run the multi-agent handoff workflow."""
    print("\n🚀 Exercise 4: Multi-Agent Handoff\n")

    # TODO: Generate trace ID
    # trace_id = str(uuid.uuid4())

    # TODO: Connect to Temporal
    # client = await Client.connect("localhost:7233")

    # TODO: Start worker with all activities
    # async with Worker(
    #     client,
    #     task_queue="multi-agent-queue",
    #     workflows=[MultiAgentWorkflow],
    #     activities=[triage_query, weather_agent, time_agent],
    # ):
    #     # TODO: Execute workflow with complex query
    #     query = "What's the weather in London?"
    #     workflow_id = f"multi-agent-{trace_id}"
    #
    #     result = await client.execute_workflow(
    #         MultiAgentWorkflow.run,
    #         args=[query, trace_id],
    #         id=workflow_id,
    #         task_queue="multi-agent-queue",
    #     )
    #
    #     print(f"\n✅ Final Response:\n{result}\n")
    #     print(f"View in Temporal UI: http://localhost:8233/namespaces/default/workflows/{workflow_id}\n")

    print("⚠️  This is starter code - implement the TODOs above!")
    print("   Check solutions/04_multi_agent_handoff/ for the complete solution\n")


if __name__ == "__main__":
    asyncio.run(main())
