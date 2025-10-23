# Exercise 1: Agent Hello World

**Goal:** Create a simple AI agent with one tool function using the OpenAI Agents SDK.

**Timebox:** 15 minutes

## What You'll Learn

- How to create an agent using the OpenAI Agents SDK
- How to define tool functions that call real APIs
- How to run the agent and see tool calls in action with real weather data

## Prerequisites

1. **OpenAI API Key:** Add your key to `.env`:
   ```bash
   OPENAI_API_KEY=sk-your-key-here
   ```

2. **Install Dependencies:**
   ```bash
   make setup
   # or manually:
   pip install openai-agents httpx rich python-dotenv
   ```

3. **Internet Connection:** Required for real National Weather Service API calls

## Steps

### 1. Define a Tool Function

Complete the `get_weather_alerts()` function in [exercise.ipynb](exercise.ipynb):
- Use `httpx.get()` to call the NWS API
- Endpoint: `https://api.weather.gov/alerts/active/area/{state}`
- Parse the JSON response and extract alert information
- Handle cases with no active alerts

### 2. Create an Agent

Use the OpenAI Agents SDK to define an agent:
```python
agent = Agent(
    name="Weather Assistant",
    instructions="You help users get weather alert information for US states",
    tools=[get_weather_alerts]
)
```

### 3. Run the Agent

Execute the agent using `Runner.run()`:
```python
result = await Runner.run(agent, query)
print(result.final_output)
```

## Expected Output

```
Query: Are there any weather alerts for California?

🔧 Calling NWS API for state: CA
✓ Found 3 alert(s)

🤖 Agent Response:
Currently there are 3 active weather alerts for California including:
- Wind Advisory (Moderate): Wind Advisory until midnight
- High Surf Advisory (Moderate): High Surf Advisory until 9 PM
- Freeze Warning (Moderate): Freeze Warning from 2 AM to 9 AM

Note: This used a real API call to the National Weather Service!
```

## Testing

To test your implementation:

1. **Open the exercise notebook:**
   ```bash
   jupyter notebook exercises/01_agent_hello_world/exercise.ipynb
   ```

2. **Complete the TODOs** in each cell

3. **Run all cells** to see the agent in action

4. **Compare with solution:**
   ```bash
   jupyter notebook solutions/01_agent_hello_world/solution.ipynb
   ```

## Troubleshooting

**Error: `OPENAI_API_KEY is not set`**
- Ensure `.env` file exists in project root with your API key

**Error: Connection timeout or network error**
- Check your internet connection
- NWS API may be temporarily unavailable (normal behavior)
- Try a different state code

**No active alerts returned**
- This is normal! Many states have no active weather alerts
- Try different states: CA, TX, FL, NY, etc.
- Check [weather.gov](https://www.weather.gov) to find states with active alerts

## Stretch Goals

- Add error handling for invalid state codes
- Modify the tool to support city names (requires geocoding)
- Add a second tool for current weather conditions (not just alerts)
- Try querying multiple states in one question

## Key Concepts

**OpenAI Agents SDK:**
- Modern framework for building agentic AI applications
- Simplified agent creation with `Agent` class
- Automatic tool schema generation with `@function_tool`
- Built-in conversation management via `Runner`

**Tool Functions:**
- Decorated with `@function_tool` for automatic schema generation
- Can call external APIs, databases, or any Python code
- Return values are passed back to the LLM for final response generation

**Real API Integration:**
- NWS API provides free, real-time weather data
- No API key required (but User-Agent header recommended)
- Production-ready example of integrating external data sources
