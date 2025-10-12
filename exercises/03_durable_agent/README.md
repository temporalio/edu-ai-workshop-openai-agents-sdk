# Exercise 3: Durable Agent

**Goal:** Combine OpenAI agents with Temporal workflows to create a durable AI agent with automatic retries and state persistence.

**Timebox:** 15 minutes

## What You'll Learn

- How to wrap LLM calls in Temporal activities for durability
- How to persist agent state across failures using workflows
- How to correlate Temporal execution with OpenAI traces using trace IDs
- How automatic retries work for AI operations

## Prerequisites

Make sure Temporal server is running:

```bash
make temporal-up
```

## Steps

1. **Wrap LLM calls in activities** - Move OpenAI API calls into Temporal activities
2. **Create an agent workflow** - Define workflow that orchestrates the agent
3. **Add state persistence** - Store conversation history in workflow state
4. **Add observability** - Generate trace_id for correlation between Temporal UI and OpenAI
5. **Run and observe** - Execute workflow and view in both Temporal UI and logs

## Expected Output

```
🚀 Starting Durable Agent workflow...
   Trace ID: 550e8400-e29b-41d4-a716-446655440000

🤖 Agent Query: What's the weather in San Francisco?

🔧 Activity: Calling tool get_weather(location="San Francisco")
✓ Tool result: The weather in San Francisco is sunny, 72°F

🤖 Agent Response:
The current weather in San Francisco is sunny with a temperature of 72°F.

✅ Workflow completed successfully

View in Temporal UI: http://localhost:8233/namespaces/default/workflows/durable-agent-1
Trace ID for correlation: 550e8400-e29b-41d4-a716-446655440000
```

## Running the Exercise

```bash
make temporal-up    # Start Temporal server
make exercise-3     # Run the exercise
```

Or directly:

```bash
python exercises/03_durable_agent/main.py
```

## Stretch Goal

- Simulate a failure in the activity and watch it retry automatically
- Add conversation history to maintain context across multiple turns
- Implement exponential backoff retry policy for LLM calls

## Need Help?

Check the solution in `solutions/03_durable_agent/`
