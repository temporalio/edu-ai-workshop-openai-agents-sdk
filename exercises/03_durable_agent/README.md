# Exercise 3: Durable Agent

**Goal:** Take the **"Web Research Agent" from Exercise 1** and wrap it in **Temporal workflows** for automatic retries and durability.

**Timebox:** 15 minutes

## What You'll Learn

- How to wrap the same agent from Exercise 1 in Temporal activities
- How automatic retries work without changing the agent code
- How to test durability by simulating network failures
- How Temporal makes agents production-ready with zero agent modifications

## Setup

Before doing the exercise, you need to:

- Install necessary dependencies
- Create your `.env` file and supply your API key
- Load the environment variables
- Download and start a local Temporal Service

## Architecture

This exercise builds on Exercise 1 by adding Temporal's durability layer:

```
┌─────────────────────────────────────────────────┐
│           Temporal Workflow                      │
│  ┌───────────────────────────────────────────┐  │
│  │      Temporal Activity                    │  │
│  │  ┌─────────────────────────────────────┐  │  │
│  │  │   OpenAI Agents SDK                 │  │  │
│  │  │  ┌───────────────────────────────┐  │  │  │
│  │  │  │  Agent with WebSearchTool     │  │  │  │
│  │  │  │  ┌─────────────────────────┐  │  │  │  │
│  │  │  │  │  Web Search API Call    │  │  │  │  │
│  │  │  │  └─────────────────────────┘  │  │  │  │
│  │  │  └───────────────────────────────┘  │  │  │
│  │  └─────────────────────────────────────┘  │  │
│  │    ↑ Automatic retries on failure         │  │
│  └───────────────────────────────────────────┘  │
│    ↑ State persistence across failures          │
└─────────────────────────────────────────────────┘
```

## Steps

### 1. Create the Same Agent from Exercise 1

Use the **exact same "Web Research Agent"** from Exercise 1:

```python
from agents import Agent, WebSearchTool

# THE SAME agent from Exercise 1 - copy and paste!
agent = Agent(
    name="Web Research Agent",
    instructions="You are a helpful assistant that can search the web for information. Provide accurate, up-to-date answers based on your search results.",
    tools=[WebSearchTool()]
)
```

**Key Insight:**

- We're not changing the agent at all
- Same name, same instructions, same tools
- Temporal adds durability WITHOUT modifying agent code

### 2. Wrap Agent in Temporal Activity

Create an activity that wraps the agent execution:

```python
@activity.defn
async def run_web_agent(query: str, trace_id: str) -> str:
    # Log attempt number for observability
    attempt = activity.info().attempt
    activity.logger.info("Running agent (attempt %d)", attempt)

    # Run the SAME agent - this can fail and trigger Temporal retries
    result = await Runner.run(agent, input=query)
    return result.final_output
```

**What this does:**

- Wraps the agent call in a Temporal activity
- Enables automatic retries if the web search fails
- Provides observability with attempt numbers

### 3. Create Durable Workflow with Retry Policy

Define workflow that executes the activity with automatic retries:

```python
@workflow.defn
class DurableAgentWorkflow:
    @workflow.run
    async def run(self, query: str, trace_id: str) -> str:
        return await workflow.execute_activity(
            run_web_agent,
            args=[query, trace_id],
            start_to_close_timeout=timedelta(minutes=2),
            retry_policy=RetryPolicy(
                maximum_attempts=5,  # Try up to 5 times
                initial_interval=timedelta(seconds=2),
                backoff_coefficient=2.0,  # Exponential backoff
            ),
        )
```

**What this does:**

- Orchestrates the activity execution
- Defines retry policy (5 attempts with exponential backoff)
- Persists workflow state across failures

### 4. Execute and Test

Run the workflow with proper asyncio handling and optionally test durability.

## Expected Output

### Normal Execution:

```
🚀 Exercise 3: Durable Agent with WebSearchTool

Trace ID: abc123...

Query: What are the current weather alerts for California?

🔍 Agent searching the web (attempt 1)...
✓ Web search completed successfully

🤖 Agent Response:
Based on current information, California has several active weather alerts:
- Wind Advisory in effect for multiple counties until 10 PM tonight
- High Surf Advisory along the central coast through midnight
- Freeze Warning for inland valleys from 2 AM to 9 AM tomorrow

View in Temporal UI: http://localhost:8233/...
```

### With Network Failure (Durability Demo):

```
🔍 Agent searching the web (attempt 1)...
✗ Network error: Connection failed

[Temporal automatically retries with exponential backoff...]

🔍 Agent searching the web (attempt 2)...
✓ Web search completed successfully

🤖 Agent Response:
[Successfully completes after network recovery]
```

## Testing Durability

To demonstrate Temporal's automatic retry:

### Step-by-Step:

1. **Start the workflow:**

   ```bash
   jupyter notebook exercises/03_durable_agent/exercise.ipynb
   ```

   Run all cells

2. **While executing, disconnect network:**

   - **macOS:** Turn off WiFi OR `sudo ifconfig en0 down`
   - **Linux:** `sudo ip link set <interface> down`
   - **Windows:** Disable network adapter

3. **Observe the failure:**

   - Console shows: `✗ Failed to fetch weather alerts`
   - Temporal logs show retry scheduling

4. **Reconnect network:**

   - Turn WiFi back on OR `sudo ifconfig en0 up`

5. **Watch automatic recovery:**

   - Temporal retries the activity
   - API call succeeds
   - Workflow completes successfully!

6. **Check Temporal UI:**
   - Visit: http://localhost:8233
   - Find your workflow by ID
   - See retry attempts, errors, and recovery

## Key Concepts

### OpenAI Agents SDK Integration

- **Agent:** Defines behavior and available tools
- **Runner:** Executes the agent and handles tool calls with asyncio
- **WebSearchTool:** Built-in tool for web search (no custom implementation needed)

### Temporal Durability

- **Activities:** Wrap external operations (agent execution, web searches, LLM calls)
- **Retry Policies:** Automatic retry on failures with exponential backoff
- **State Persistence:** Workflow state survives crashes and restarts
- **Execution History:** Full audit trail in Temporal UI

### Asyncio Integration

- **All operations use asyncio:** `await Runner.run()`, `async def` activities/workflows
- **Non-blocking I/O:** Efficient handling of network operations
- **Jupyter support:** `nest_asyncio` enables async in notebooks

## Comparison with Exercise 1

| Aspect               | Exercise 1                | Exercise 3                                  |
| -------------------- | ------------------------- | ------------------------------------------- |
| **Agent Code**       | ✅ Web Research Agent     | ✅ **SAME** Web Research Agent              |
| **Framework**        | Agents SDK only           | Agents SDK + Temporal                       |
| **Retries**          | None                      | Automatic (5 attempts, exponential backoff) |
| **State**            | Ephemeral (lost on crash) | Persisted (survives crashes)                |
| **Network Failure**  | ❌ Immediate failure      | ✅ Auto-retry and recover                   |
| **Observability**    | Console logs only         | Full history in Temporal UI                 |
| **Production Ready** | No                        | Yes                                         |

**The Key Insight:** The agent itself doesn't change. Temporal adds durability by wrapping the agent execution, not by modifying the agent code.

## Troubleshooting

**Error: `Failed to connect to Temporal server`**

- Ensure Temporal is running: `make temporal-up`
- Check server at: http://localhost:8233

**Error: `OPENAI_API_KEY is not set`**

- Add key to `.env` file in project root
- Reload environment: `load_dotenv()`

**Network disconnect doesn't cause retry:**

- Disconnect **during** API call, not before
- Check retry policy has `maximum_attempts > 1`
- Look for retry logs in Temporal UI

**No active alerts returned:**

- Normal! Many states have no alerts
- Try: CA, TX, FL (often have weather activity)
- Check https://www.weather.gov for active alerts

## Stretch Goals

1. **Extended Retry Policy:**

   - Increase `maximum_attempts` to 10
   - Add exponential backoff
   - Test with longer network outages

2. **Multi-Turn Conversation:**

   - Add conversation history to agent
   - Support follow-up questions
   - Persist context in workflow state

3. **Multiple Tools:**

   - Add current weather (not just alerts)
   - Add forecast endpoint
   - Let agent choose appropriate tool

4. **Error Handling:**
   - Distinguish retryable vs non-retryable errors
   - Custom retry policies per error type
   - Fallback responses when max retries exceeded

## Next Steps

After completing this exercise, you've learned the foundation of durable AI agents. Proceed to:

**Exercise 4: Multi-Agent Handoff** - Build systems with multiple specialized agents orchestrated by Temporal
