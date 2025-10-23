# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a 90-minute workshop repository teaching developers how to build **durable AI agents** using **[OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) + Temporal**. The workshop is designed to run in GitHub Codespaces with zero local setup required.

[OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) is critical to this entire workshop. All LLM tool calls must happen using this SDK.

All tool calls have to be real, no mocking. Use the [weather API](https://docs.temporal.io/ai-cookbook/tool-calling-python#create-the-activity-for-the-tool-invocation). All code uses **asyncio** for efficient I/O operations.

**Target Audience:** Beginner-intermediate Python developers
**Workshop Format:** 30 minutes instruction + 4×15 minute exercises

## Tech Stack

- **Python 3.11** - Primary language
- **openai agents sdk** - [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)
- **temporalio** - Workflow orchestration for durability and retries
- **Temporal CLI** - Local development server
- **Development tools:** `rich`, `typer`, `pytest`, `ruff`, `mypy`
- **Interactive environment:** Jupyter notebooks for hands-on exercises
- **Deployment:** GitHub Codespaces (devcontainer-based)

## Common Commands

### Setup & Environment

```bash
make setup          # Install dependencies and set up environment
make env            # Validate environment variables (OPENAI_API_KEY)
```

### Development

```bash
make lint           # Run ruff linter
make test           # Run pytest test suite
```

### Temporal Server

```bash
temporal server start-dev     # Start Temporal local dev server (idempotent)
```

### Exercises

- All exercises and solutions live in `.ipynb` self-contained files that have all of the necessary code to work independently. No extra files should be required.

## Repository Architecture

### Four-Exercise Progression

The workshop follows a progressive learning path:

1. **Exercise 1 - Agent Hello World** (`exercises/01_agent_hello_world/`)

   - Minimal OpenAI Agents SDK usage with custom weather tool calling the [National Weather Service API](https://docs.temporal.io/ai-cookbook/tool-calling-python#create-the-activity-for-the-tool-invocation)
   - Demonstrates `@function_tool` decorator for custom tools
   - Real API calls with async/await patterns

```py
# Example from Exercise 1
import asyncio
import httpx
from agents import Agent, Runner, function_tool

@function_tool
async def get_weather_alerts(state: str) -> str:
    """Get weather alerts for a US state from NWS."""
    url = f"https://api.weather.gov/alerts/active/area/{state.upper()}"
    headers = {"User-Agent": "OpenAI-Agents-Workshop"}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, timeout=10.0)
        data = response.json()
        features = data.get("features", [])

        if not features:
            return f"No active weather alerts for {state.upper()}."

        # Format alerts
        alerts = [f.get("properties", {}).get("event") for f in features[:5]]
        return f"Active alerts: {', '.join(alerts)}"

agent = Agent(
    name="Weather Agent",
    instructions="You help users get weather alerts for US states.",
    tools=[get_weather_alerts]
)

async def main():
    result = await Runner.run(agent, "Are there weather alerts for CA?")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
```

- Demonstrates custom tool creation with `@function_tool`
- Real API integration (no mocking)
- Available as Jupyter notebook (`exercise.ipynb`)
- No Temporal integration yet

2. **Exercise 2 - Temporal Hello World** (`exercises/02_temporal_hello_world/`)

   - 1 workflow + 1 activity in Python
   - Introduces Temporal concepts without AI complexity
   - Shows durability and retry mechanisms

3. **Exercise 3 - Durable Agent** (`exercises/03_durable_agent/`)

   - **Core integration:** Weather agent with Temporal activities as tools using `activity_as_tool()` pattern
   - **4-component structure** mirrors production applications (activities, workflow, worker, starter)
   - Workflow-based state persistence with asyncio throughout
   - Demonstrates retry logic and durability for AI operations
   - Demonstrates network disconnection and Temporal's ability to automatically retry and recover
   - All async: `await Runner().run()`, `async def` activities and workflows

### **The 4-Component Pattern**

Exercise 3 follows the production-ready structure from [temporal-weather-openai-agents](https://github.com/nadvolod/temporal-weather-openai-agents):

#### **Component 1: activities.py**
```py
import httpx
from temporalio import activity

@activity.defn(name="get_weather")
async def get_weather(state: str) -> dict:
    """Fetch active NWS alerts for a 2-letter US state code."""
    headers = {"User-Agent": "Temporal-Agents-Workshop/1.0"}
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.get(
            f"https://api.weather.gov/alerts/active/area/{state}",
            headers=headers
        )
        r.raise_for_status()
        data = r.json()

    alerts = []
    for f in (data.get("features") or [])[:5]:
        p = f.get("properties", {})
        alerts.append({
            "event": p.get("event"),
            "headline": p.get("headline"),
            "severity": p.get("severity"),
            "area": p.get("areaDesc"),
        })

    return {"state": state.upper(), "count": len(alerts), "alerts": alerts}
```

#### **Component 2: workflow.py**
```py
from datetime import timedelta
from temporalio import workflow
from temporalio.contrib import openai_agents
from agents import Agent, Runner

TASK_QUEUE = "weather-agents"

@workflow.defn
class WeatherAgentWorkflow:
    @workflow.run
    async def run(self, user_query: str) -> str:
        agent = Agent(
            name="Weather Assistant",
            instructions="You are a helpful assistant that explains current weather alerts for U.S. states.",
            tools=[
                openai_agents.workflow.activity_as_tool(
                    get_weather,
                    start_to_close_timeout=timedelta(seconds=10),
                )
            ],
        )
        # Note: Runner() is instantiated, not just Runner
        result = await Runner().run(agent, user_query)
        return getattr(result, "final_output", str(result))
```

#### **Component 3: worker.py**
```py
from temporalio.client import Client
from temporalio.worker import Worker
from temporalio.contrib.openai_agents import OpenAIAgentsPlugin, ModelActivityParameters
from temporalio.worker.workflow_sandbox import SandboxedWorkflowRunner, SandboxRestrictions

async def main():
    client = await Client.connect(
        "localhost:7233",
        plugins=[
            OpenAIAgentsPlugin(
                model_params=ModelActivityParameters(
                    start_to_close_timeout=timedelta(seconds=30)
                )
            )
        ],
    )

    worker = Worker(
        client,
        task_queue=TASK_QUEUE,
        workflows=[WeatherAgentWorkflow],
        activities=[get_weather],
        workflow_runner=SandboxedWorkflowRunner(
            restrictions=SandboxRestrictions.default.with_passthrough_modules("httpx")
        )
    )
    await worker.run()
```

#### **Component 4: starter.py**
```py
from temporalio.client import Client
from temporalio.contrib.openai_agents import OpenAIAgentsPlugin

async def main():
    client = await Client.connect("localhost:7233", plugins=[OpenAIAgentsPlugin()])

    # Use start_workflow, not execute_workflow
    handle = await client.start_workflow(
        WeatherAgentWorkflow.run,
        "What weather alerts are active in CA?",
        id="weather-workflow-id",
        task_queue=TASK_QUEUE
    )

    print(f"🚀 Started workflow: {handle.id}")
    result = await handle.result()
    print(f"🤖 Response: {result}")
```

**Key Benefits:**
- ✅ Clean separation of concerns - each component has one responsibility
- ✅ Agent tool calls are durable and automatically retried by Temporal
- ✅ Full execution history visible in Temporal UI
- ✅ Survives network failures, API errors, and crashes
- ✅ Production-ready pattern that scales to real applications
- ✅ Proper sandbox configuration with `with_passthrough_modules()`

**Important Notes:**
- Activity returns `dict` not string - LLM interprets structured data
- Single parameter: `user_query` (no trace_id)
- `Runner()` is instantiated (not just `Runner`)
- Use `start_workflow` (not `execute_workflow`)
- Each Jupyter cell represents one component file

4. **Exercise 4 - Multi-Agent Handoff** (`exercises/04_multi_agent_handoff/`)
   - Advanced: Multiple specialized agents from OpenAI Agents SDK similar to https://openai.github.io/openai-agents-python/quickstart/#put-it-all-together
   - Triage agent routes queries to specialist agents
   - Context maintained across agent handoffs
   - Workflow orchestration of agent-to-agent transitions

### Directory Structure

```
exercises/     # Starter code for workshop participants
solutions/     # Complete reference implementations
slides/        # Workshop presentation materials
scripts/       # Bootstrap, environment checks, Temporal startup
.devcontainer/ # Codespaces configuration
```

Each exercise directory contains:

- Jupyter notebooks for interactive learning (where applicable)
- `README.md` with: Goal, Steps (≤5), Expected Output, Stretch Goal, Timebox

## Key Architectural Patterns

### Durability Through Activities

In Exercise 3, LLM calls are wrapped in **Temporal activities** rather than called directly in workflows. This provides:

- Automatic retries on failure
- State persistence across crashes
- Replay-safe execution
- Example of stopping the internet to show Temporal's durability

### Workflow ID Naming Convention

All workflows in this repository follow a consistent naming pattern for workflow IDs:

**Pattern:** `{prefix}-{day}-{month}-{date}-{time}est`

**Example:** `durable-agent-wed-oct-16-094832est`

**Implementation:**
```python
from datetime import datetime
import pytz

# Generate workflow ID with EST timestamp
est = pytz.timezone('US/Eastern')
now = datetime.now(est)
workflow_id = f"durable-agent-{now.strftime('%a-%b-%d-%I%M%S').lower()}est"
```

**Benefits:**
- Human-readable workflow IDs
- Chronologically sortable in Temporal UI
- Timezone-aware (EST) for workshop coordination
- Consistent pattern across all exercises

**Examples by Exercise:**
- Exercise 2: `hello-workflow-thu-oct-16-095919est`
- Exercise 3: `durable-agent-wed-oct-16-094832est`
- Exercise 4: `multi-agent-fri-oct-17-103045est`

**Required Dependencies:**
- Add `pytz` to pip install commands: `%pip install --quiet temporalio openai-agents httpx rich nest-asyncio pytz`
- Import: `from datetime import datetime` and `import pytz`

### Observability Integration

The durable agent implementation connects two observability systems:

- **Temporal UI:** Shows workflow execution, retries, state (workflows are easily identifiable by their human-readable IDs)
- **OpenAI Traces:** Shows LLM calls and tool usage
- **`trace_id`:** Correlation key printed to link both systems

### Teaching-First Code Style

All code follows these principles:

- **Clarity over abstraction:** Linear, readable flow
- **Verbose naming:** Self-documenting variable and function names
- **Instructional logging:** Log activity starts/ends, retries, workflow resumptions
- **Explanatory comments:** Focus on _why_ (durability, retries, state), not _what_
- **With valuable comments** A valuable comment for each line of code. No comments for imports or no comments for logging statements.

## Environment & Secrets

### Required Environment Variables

- `OPENAI_API_KEY` - Required for exercises 1, 3, 4

### Security Model

- `.env.sample` provides template (never commit `.env`)
- `scripts/check_env.py` validates environment before exercises run

## DevEx & Codespaces

### Bootstrap Flow

1. Codespaces creates container from `.devcontainer/`
2. Post-create: `scripts/bootstrap.sh` runs automatically
   - Installs Python dependencies
   - Installs Temporal CLI
   - Validates environment
3. Ready to run exercises in ≤90 seconds

### Idempotent Temporal Startup

`scripts/run_temporal.sh` checks if Temporal is already running. If yes, exits cleanly without error.

## Working with This Repository

### When Adding New Exercises

- Follow the 15-minute timebox constraint
- Include README with 5 or fewer steps
- Mirror in `/solutions/` with complete, commented implementation

### When Modifying Existing Code

- Maintain teaching clarity - avoid clever abstractions
- Add logs for observable events (retries, state changes, tool calls)
- Update corresponding solution if changing exercise starter code
- Ensure comments explain the "why" behind durability patterns
- Don't use yellow as a logging color

### When Debugging

- Check `make env` output for missing environment variables
- Verify Temporal is running: `make temporal-up`
- Exercise 3 prints Temporal UI URL and `trace_id` for correlation
- Look for activity retry logs in Temporal UI

## CI/CD

GitHub Actions workflow (`.github/workflows/ci.yml`):

- Runs on push/PR
- Tests on Python 3.11
- Executes: `ruff` → `mypy` → `pytest -q`
