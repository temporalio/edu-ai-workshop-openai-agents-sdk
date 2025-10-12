"""Exercise 2: Temporal Hello World - Complete Solution"""

import asyncio
from rich.console import Console
from temporalio.client import Client
from temporalio.worker import Worker

from .activities import process_data
from .workflows import HelloWorkflow

console = Console()


async def main():
    """Run the Temporal Hello World workflow."""
    console.print("\n[bold cyan]🚀 Exercise 2: Temporal Hello World[/bold cyan]\n")

    # Connect to Temporal server
    client = await Client.connect("localhost:7233")
    console.print("[green]✓[/green] Connected to Temporal server\n")

    # Task queue name - workflows and activities are registered on specific queues
    task_queue = "hello-world-queue"

    # Start a worker that executes workflows and activities
    async with Worker(
        client,
        task_queue=task_queue,
        workflows=[HelloWorkflow],
        activities=[process_data],
    ):
        console.print("[green]✓[/green] Worker started and listening for tasks\n")

        # Execute the workflow
        workflow_id = "hello-workflow-1"
        result = await client.execute_workflow(
            HelloWorkflow.run,
            "Temporal",
            id=workflow_id,
            task_queue=task_queue,
        )

        console.print(f"\n[bold green]✅ Workflow Result:[/bold green] {result}\n")
        console.print(
            f"[yellow]View execution history:[/yellow] "
            f"http://localhost:8233/namespaces/default/workflows/{workflow_id}\n"
        )


if __name__ == "__main__":
    asyncio.run(main())
