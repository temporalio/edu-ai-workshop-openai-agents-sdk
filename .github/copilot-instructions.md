# Temporal + OpenAI Agents SDK Workshop - AI Coding Instructions

## Project Architecture

This is a 90-minute educational workshop teaching **durable AI agents** using **OpenAI + Temporal**. The architecture follows a progressive learning path through 4 exercises, each building on the previous one.

### Core Integration Pattern

**Critical concept:** LLM calls are wrapped in **Temporal activities** (not called directly in workflows) to provide:

- Automatic retries on API failures
- State persistence across crashes
- Execution history and observability

```python
# ✅ Correct: LLM calls in activities
@activity.defn
async def call_agent_with_tools(query: str, trace_id: str) -> str:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    # LLM call here

# ❌ Avoid: Direct LLM calls in workflows (not replay-safe)
```

### Exercise Progression

1. **Exercise 1:** Basic OpenAI agent with tool calling (no Temporal)
2. **Exercise 2:** Basic Temporal workflow + activity (no AI)
3. **Exercise 3:** **Core pattern** - AI agent wrapped in Temporal activities
4. **Exercise 4:** Multi-agent handoff with workflow orchestration

## Development Workflow

### Essential Commands

```bash
make setup          # Install deps - ALWAYS run first
make env            # Validate OPENAI_API_KEY - run before exercises 1,3,4
make temporal-up    # Start Temporal server - REQUIRED for exercises 2,3,4
make exercise-{1-4} # Run specific exercise
make test           # Run mocked tests (no API key needed)
```

### File Organization

- `exercises/` - Starter notebooks with TODOs (`exercise.ipynb`)
- `solutions/` - Complete standalone notebooks (`solution.ipynb`)
- `scripts/` - Bootstrap, env checking, Temporal startup helpers
- Notebooks must run end-to-end without importing repo modules; duplicate helper code inside the notebook that needs it

## Project-Specific Conventions

### Teaching-First Code Style

- **Clarity over abstraction:** Linear, readable flow
- **Verbose naming:** `call_agent_with_tools()` not `call_agent()`
- **Instructional logging:** Log activity starts, retries, workflow events
- **File length limit:** Keep files ≤80 lines for workshop readability
- **Comments explain WHY:** Focus on durability, retries, state persistence
- **Notebook self-containment:** Define utilities inside each notebook; avoid `from solutions...` imports

### Tool Function Pattern

All exercises use mock tool functions with consistent structure:

```python
def get_weather(location: str) -> str:
    """Tool function: Get weather for a location."""
    weather_data = {
        "San Francisco": "sunny, 72°F",
        "New York": "cloudy, 65°F",
        "London": "rainy, 58°F",
    }
    return f"The weather in {location} is {weather_data.get(location, 'partly cloudy, 68°F')}"
```

### Observability Pattern

Exercise 3+ includes `trace_id` for correlation between Temporal UI and OpenAI traces:

```python
trace_id = str(uuid.uuid4())
workflow_id = f"durable-agent-{trace_id}"
# Print both Temporal UI URL and trace_id for debugging
```

### OpenAI Tool Integration

Standard pattern for tool calling:

```python
# 1. Define tools schema
tools = [{"type": "function", "function": {...}}]

# 2. Initial call with tools
response = client.chat.completions.create(model="gpt-4o-mini", messages=messages, tools=tools)

# 3. Handle tool calls
if response.choices[0].message.tool_calls:
    # Execute tools, append results to messages
    # Make final call for natural language response
```

## Critical Dependencies

### Environment Requirements

- Python 3.11 (exact version required)
- `OPENAI_API_KEY` env var (exercises 1,3,4)
- Temporal CLI + dev server (exercises 2,3,4)

### Import Patterns

```python
# Workflows must use unsafe imports for activities
with workflow.unsafe.imports_passed_through():
    from .activities import call_agent_with_tools

# Activities use standard imports
from temporalio import activity
from openai import OpenAI
```

## Debugging Guidelines

### Environment Issues

1. Run `make env` to check OPENAI_API_KEY
2. Run `make temporal-up` and verify "✅ Temporal server started"
3. Check ports 7233 (server) and 8233 (UI) are forwarded in Codespaces

### Temporal Patterns

- Workflows coordinate, activities do the work
- Activities can retry, workflows maintain state
- Use `workflow.logger.info()` and `activity.logger.info()` for visibility
- Temporal UI at http://localhost:8233 shows execution history

### Testing Strategy

- Tests mock OpenAI responses (see `tests/test_exercise_*.py`)
- Use `unittest.mock.patch("openai.OpenAI")` pattern
- Tests must pass without real API keys in CI

## Workshop-Specific Gotchas

- `scripts/run_temporal.sh` is idempotent - safe to run multiple times
- Bootstrap flow in Codespaces takes ~90 seconds, includes Temporal CLI installation
- Include a comment for every line of code added in exercises. Don't include comments for imports or logging statements.
- When running Temporal workers inside notebooks, always pass `workflow_runner=UnsandboxedWorkflowRunner()` and `debug_mode=True` so the sandbox does not require a `__file__` attribute.
- Declare notebook activities with `async def` (or configure an `activity_executor`) to prevent the worker from erroring on synchronous activity definitions.
