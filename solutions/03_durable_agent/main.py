"""Exercise 3: Durable Agent - Complete Solution"""

import asyncio
import uuid
from rich.console import Console
from temporalio.client import Client
from temporalio.worker import Worker

from .activities import call_agent_with_tools
from .workflows import DurableAgentWorkflow

console = Console()


async def main():
    """Run the durable agent workflow."""
    console.print("\n[bold cyan]🚀 Exercise 3: Durable Agent[/bold cyan]\n")

    # Generate unique trace ID for observability correlation
    trace_id = str(uuid.uuid4())
    console.print(f"[yellow]Trace ID:[/yellow] {trace_id}\n")

    # Connect to Temporal
    client = await Client.connect("localhost:7233")
    console.print("[green]✓[/green] Connected to Temporal server\n")

    task_queue = "durable-agent-queue"

    # Start worker
    async with Worker(
        client,
        task_queue=task_queue,
        workflows=[DurableAgentWorkflow],
        activities=[call_agent_with_tools],
    ):
        console.print("[green]✓[/green] Worker started\n")

        # Execute workflow
        query = "What's the weather like in San Francisco?"
        workflow_id = f"durable-agent-{trace_id}"

        console.print(f"[yellow]Query:[/yellow] {query}\n")

        result = await client.execute_workflow(
            DurableAgentWorkflow.run,
            args=[query, trace_id],
            id=workflow_id,
            task_queue=task_queue,
        )

        console.print(f"\n[bold green]🤖 Agent Response:[/bold green]\n{result}\n")
        console.print(
            f"[yellow]View in Temporal UI:[/yellow] "
            f"http://localhost:8233/namespaces/default/workflows/{workflow_id}"
        )
        console.print(f"[yellow]Trace ID for correlation:[/yellow] {trace_id}\n")


if __name__ == "__main__":
    asyncio.run(main())
