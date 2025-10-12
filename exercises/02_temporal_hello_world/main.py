"""Exercise 2: Temporal Hello World - Starter Code"""

import asyncio
from temporalio.client import Client
from temporalio.worker import Worker

# Import workflow and activities
# from .workflows import HelloWorkflow
# from .activities import process_data


async def main():
    """Run the Temporal Hello World workflow."""
    print("\n🚀 Exercise 2: Temporal Hello World\n")

    # TODO: Connect to Temporal server
    # client = await Client.connect("localhost:7233")

    # TODO: Start a worker to execute workflows and activities
    # async with Worker(
    #     client,
    #     task_queue="hello-world-queue",
    #     workflows=[HelloWorkflow],
    #     activities=[process_data],
    # ):
    #     # TODO: Execute the workflow
    #     result = await client.execute_workflow(
    #         HelloWorkflow.run,
    #         "Temporal",
    #         id="hello-workflow-1",
    #         task_queue="hello-world-queue",
    #     )
    #
    #     print(f"\n✅ Workflow Result: {result}\n")
    #     print("View execution in Temporal UI: http://localhost:8233\n")

    print("⚠️  This is starter code - implement the TODOs above!")
    print("   Check solutions/02_temporal_hello_world/ for the complete solution\n")


if __name__ == "__main__":
    asyncio.run(main())
