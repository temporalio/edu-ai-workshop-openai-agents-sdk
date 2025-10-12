# Exercise 4: Multi-Agent Handoff

**Goal:** Implement agent handoff pattern where specialized agents handle different tasks, orchestrated by Temporal workflows.

**Timebox:** 15 minutes

## What You'll Learn

- How to implement multi-agent architectures with Temporal
- Agent handoff patterns for specialized tasks
- Maintaining conversation context across agent transitions
- Workflow-based orchestration of multiple agents

## Prerequisites

Make sure Temporal server is running:

```bash
make temporal-up
```

## Scenario

Build a customer service system with two specialized agents:
- **Triage Agent**: Routes queries to the appropriate specialist
- **Weather Agent**: Handles weather-related questions
- **Time Agent**: Handles time-related questions

The workflow orchestrates handoffs between agents based on the triage decision.

## Steps

1. **Define specialist agents** - Create weather and time agent activities
2. **Implement triage logic** - Create activity that routes to correct agent
3. **Build orchestration workflow** - Coordinate agent handoffs
4. **Maintain conversation context** - Pass context through handoffs
5. **Run and observe** - See multi-agent coordination in Temporal UI

## Expected Output

```
🚀 Multi-Agent Handoff System

Query: What's the weather in London and what time is it there?

🔍 Triage Agent: Routing query...
   → Routed to: weather_agent

🌤️  Weather Agent: Handling weather query...
   Result: The weather in London is rainy, 58°F

🔍 Triage Agent: Additional routing needed...
   → Routed to: time_agent

🕐 Time Agent: Handling time query...
   Result: The current time in London is 3:45 PM GMT

✅ Final Response:
The weather in London is rainy with 58°F. The current time there is 3:45 PM GMT.

View in Temporal UI: http://localhost:8233/...
```

## Running the Exercise

```bash
make temporal-up    # Start Temporal server
make exercise-4     # Run the exercise
```

Or directly:

```bash
python exercises/04_multi_agent_handoff/main.py
```

## Stretch Goal

- Add a third specialist agent (e.g., translation agent)
- Implement conversation history that persists across handoffs
- Add decision logic for when to use multiple agents vs single agent

## Need Help?

Check the solution in `solutions/04_multi_agent_handoff/`
