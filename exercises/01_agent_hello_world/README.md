# Exercise 1: Agent Hello World

**Goal:** Create a simple AI agent with one tool function using the OpenAI Agents SDK.

**Timebox:** 15 minutes

## What You'll Learn

- How to create an agent with system instructions
- How to define and register tool functions
- How to run the agent and see tool calls in action

## Steps

1. **Define a tool function** - Create a simple `get_weather()` function that returns weather data
2. **Create the agent** - Initialize an OpenAI agent with system instructions
3. **Register the tool** - Connect your function to the agent
4. **Run the agent** - Execute with a query that triggers the tool
5. **Observe the output** - See the agent call your function and generate a response

## Expected Output

```
🤖 Agent Response:
The current weather in San Francisco is sunny with a temperature of 72°F.

🔧 Tools Called:
  - get_weather(location="San Francisco")
```

## Running the Exercise

```bash
make exercise-1
```

Or directly:

```bash
python exercises/01_agent_hello_world/main.py
```

## Stretch Goal

- Add a second tool function (e.g., `get_time()`)
- Modify the query to use both tools
- Observe how the agent orchestrates multiple tool calls

## Need Help?

Check the solution in `solutions/01_agent_hello_world/main.py`
