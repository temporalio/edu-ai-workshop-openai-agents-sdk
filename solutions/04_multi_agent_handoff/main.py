"""Exercise 4: Multi-Agent Handoff - Complete Solution"""

import asyncio
import uuid
from rich.console import Console
from temporalio.client import Client
from temporalio.worker import Worker

from .activities import triage_query, weather_agent, time_agent
from .workflows import MultiAgentWorkflow

console = Console()


async def main():
    """Run the multi-agent handoff workflow."""
    console.print("\n[bold cyan]🚀 Exercise 4: Multi-Agent Handoff[/bold cyan]\n")

    # Generate trace ID
    trace_id = str(uuid.uuid4())
    console.print(f"[yellow]Trace ID:[/yellow] {trace_id}\n")

    # Connect to Temporal
    client = await Client.connect("localhost:7233")
    console.print("[green]✓[/green] Connected to Temporal server\n")

    task_queue = "multi-agent-queue"

    # Start worker with all activities
    async with Worker(
        client,
        task_queue=task_queue,
        workflows=[MultiAgentWorkflow],
        activities=[triage_query, weather_agent, time_agent],
    ):
        console.print("[green]✓[/green] Worker started\n")

        # Execute workflow
        query = "What's the weather like in London?"
        workflow_id = f"multi-agent-{trace_id}"

        console.print(f"[yellow]Query:[/yellow] {query}\n")

        result = await client.execute_workflow(
            MultiAgentWorkflow.run,
            args=[query, trace_id],
            id=workflow_id,
            task_queue=task_queue,
        )

        console.print(f"\n[bold green]✅ Final Response:[/bold green]\n{result}\n")
        console.print(
            f"[yellow]View in Temporal UI:[/yellow] "
            f"http://localhost:8233/namespaces/default/workflows/{workflow_id}"
        )
        console.print(f"[yellow]Trace ID:[/yellow] {trace_id}\n")


if __name__ == "__main__":
    asyncio.run(main())
