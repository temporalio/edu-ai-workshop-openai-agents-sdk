# Exercise 4: Routing Workflow

**Goal:** Build a routing workflow that intelligently distributes requests to specialized language agents using the handoff pattern.

**Timebox:** 15 minutes

## What You'll Learn

- Implement agent routing/triage patterns with OpenAI Agents SDK
- Create specialized agents for different languages (French, Spanish, English)
- Use handoff patterns for agent-to-agent transitions
- Build production-ready multi-agent systems with Temporal
- Understand how to structure real Temporal applications (separate files for workflow, worker, starter)

## Architecture Pattern 🏗️

This exercise demonstrates the **routing pattern** where a triage agent analyzes incoming requests and delegates to specialized agents:

### High-Level Flow

```
User Query (any language) 👤
    ↓
Temporal Workflow (orchestration layer) 🎭
    ↓
Triage Agent (language detection) 🔍
    ├─→ French Agent 🇫🇷 (if French detected)
    ├─→ Spanish Agent 🇪🇸 (if Spanish detected)
    └─→ English Agent 🇬🇧 (if English detected)
    ↓
Response in appropriate language ✅
```

### Detailed Flow with Temporal Activities

```
User Query 👤
    ↓
Temporal Workflow (orchestration layer) 🎭
    ↓
Activity: Call Triage Agent 🤖
    ↓
[Triage agent analyzes language]
    ↓
Activity: Handoff to Specialist Agent 🔀
    ↓
Activity: Specialist Agent processes query 💬
    ↓
Return response to user ✅
```

**Key Benefits:**
- ✅ Each agent handoff is managed by Temporal
- ✅ Automatic retries if agent calls fail
- ✅ Full execution history in Temporal UI
- ✅ Production-ready multi-agent architecture

## Prerequisites

Before starting this exercise, ensure you have:

### 1. Temporal Server Running

```bash
# Start Temporal using temporal_installation.ipynb notebook:
#   1. Open temporal_installation.ipynb in VS Code
#   2. Run each cell to install Temporal CLI and start the dev server
#   3. Verify In Codespaces: Go to the **Ports** tab → Find port **8233** → Click the **Globe icon** 🌐
```

Verify at: http://localhost:8233

### 2. Dependencies Installed

```bash
# Install from this directory
cd exercises/04_agent_routing
pip install -r requirements.txt

```

### 3. Environment Variables Set

Ensure your `.env` file in the project root contains:

```bash
OPENAI_API_KEY=your_api_key_here
```

Verify with:

```bash
# From project root
make env
```

## File Structure

This exercise uses a **realistic Temporal application structure** with separate Python files:

```
exercises/04_agent_routing/
├── workflow.py      # Workflow definition and agent configurations (TODO)
├── worker.py        # Worker that executes workflows (TODO)
├── starter.py       # Script to run the workflow (TODO)
├── requirements.txt # Dependencies
└── README.md        # This file
```

This mirrors production Temporal applications where:
- **Workflows** define business logic
- **Workers** execute workflows and activities
- **Starters** trigger workflow executions

## Steps

### Step 1: Define the Agents

**Open `workflow.py` and complete the TODOs:**

1. **Implement `french_agent()`:**
   - Return an `Agent` with name "French Agent"
   - Instructions: "You only speak French. Respond naturally to user queries in French."
   - Model: "gpt-4"

2. **Implement `spanish_agent()`:**
   - Return an `Agent` with name "Spanish Agent"
   - Instructions: "You only speak Spanish. Respond naturally to user queries in Spanish."
   - Model: "gpt-4"

3. **Implement `english_agent()`:**
   - Return an `Agent` with name "English Agent"
   - Instructions: "You only speak English. Respond naturally to user queries in English."
   - Model: "gpt-4"

4. **Implement `triage_agent()`:**
   - Return an `Agent` with name "Triage Agent"
   - Instructions: "You are a triage agent. Analyze the language of the user's query and handoff to the appropriate language specialist agent."
   - **Important:** Add `handoffs=[french_agent(), spanish_agent(), english_agent()]`
   - Model: "gpt-4"

**Hint:** Use the `Agent` class from `agents`:

```python
from agents import Agent

return Agent(
    name="...",
    instructions="...",
    model="gpt-4"
)
```

For the triage agent, add the `handoffs` parameter:

```python
return Agent(
    name="Triage Agent",
    instructions="...",
    handoffs=[french_agent(), spanish_agent(), english_agent()],
    model="gpt-4"
)
```

### Step 2: Implement the Workflow

**In `workflow.py`, complete the `RoutingWorkflow.run()` method:**

1. Create a RunConfig instance:
   ```python
   config = RunConfig()
   ```

2. Wrap execution in a trace context:
   ```python
   with trace("Routing example"):
   ```

3. Format the user query as input:
   ```python
   inputs: list[TResponseInputItem] = [{"content": msg, "role": "user"}]
   ```

4. Execute the triage agent with proper parameters:
   ```python
   result = await Runner.run(
       triage_agent(),
       input=inputs,
       run_config=config,
   )
   ```

5. Log handoff completion and return formatted result:
   ```python
   workflow.logger.info("Handoff completed")
   return f"Response: {result.final_output}"
   ```

**Important:** Note the parameter names in `Runner.run()`:
- Use `input=inputs` (not just passing inputs directly)
- Use `run_config=config` (not `config=config`)

### Step 3: Implement the Worker

**Open `worker.py` and complete the TODOs:**

1. Connect to Temporal:
   ```python
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
   ```

2. Create the worker:
   ```python
   worker = Worker(
       client,
       task_queue=TASK_QUEUE,
       workflows=[RoutingWorkflow],
   )
   ```

3. Log worker startup:
   ```python
   print(f"🚀 Worker started successfully")
   print(f"📋 Task Queue: {TASK_QUEUE}")
   print(f"🔄 Workflows: {[w.__name__ for w in [RoutingWorkflow]]}")
   print(f"⏳ Polling for tasks... (Press Ctrl+C to stop)\n")
   ```

4. Run the worker:
   ```python
   await worker.run()
   ```

### Step 4: Implement the Starter

**Open `starter.py` and complete the TODOs:**

1. Connect to Temporal:
   ```python
   client = await Client.connect(
       "localhost:7233",
       plugins=[OpenAIAgentsPlugin()]
   )
   ```

2. Generate workflow ID:
   ```python
   est = pytz.timezone("US/Eastern")
   now = datetime.now(est)
   workflow_id = f"routing-{now.strftime('%a-%b-%d-%I%M%S').lower()}est"
   ```

3. Choose a query to test:
   ```python
   query = "Hi! Tell me a tongue twister."
   ```

4. Print starting information:
   ```python
   print("🚀 Starting Routing Workflow")
   print(f"📋 Workflow ID: {workflow_id}")
   ```

5. Execute the workflow and get result:
   ```python
   result = await client.execute_workflow(
       RoutingWorkflow.run,
       query,
       id=workflow_id,
       task_queue=TASK_QUEUE,
   )
   ```

6. Print Temporal UI link and result:
   ```python
   print(f"🔗 View in Temporal UI: http://localhost:8233/namespaces/default/workflows/{workflow_id}\n")
   print("⏳ Waiting for agent response...\n")
   print(f"💬 Agent Response: {result}")
   ```

### Step 5: Run the Workflow

**Terminal 1 - Start the worker:**

```bash
cd exercises/04_agent_routing
python worker.py
```

Wait for: `🚀 Worker started successfully`

**Terminal 2 - Execute the workflow:**

```bash
cd exercises/04_agent_routing
python starter.py
```

### Step 6: Observe in Temporal UI

1. Open: http://localhost:8233
2. Find your workflow by ID
3. Observe the agent handoff and execution history

### Step 7: Test Different Languages

Modify `starter.py` to test Spanish or English:

```python
query = queries[1]  # Spanish
# or
query = queries[2]  # English
```

Run `python starter.py` again and observe routing to different agents!

## Expected Output

### French Query

**Input:** `"Bonjour! Comment allez-vous aujourd'hui?"`

**Output:**
```
🚀 Starting Routing Workflow
📋 Workflow ID: routing-wed-oct-16-103045est
💬 Query: Bonjour! Comment allez-vous aujourd'hui?

✅ Workflow started: routing-wed-oct-16-103045est
🔗 View in Temporal UI: http://localhost:8233/...
⏳ Waiting for agent response...

======================================================================
🤖 Agent Response
======================================================================
Bonjour! Je vais très bien, merci de demander!
Comment puis-je vous aider aujourd'hui?
======================================================================
```

## Key Concepts

### Routing Pattern

The **routing pattern** (triage pattern) uses:
- **Triage Agent:** Analyzes requests and decides routing
- **Specialist Agents:** Handle specific types of requests
- **Handoff Mechanism:** Transfers control between agents

### Handoff Pattern

Enable agent handoffs with the `handoffs` parameter:

```python
Agent(
    name="Triage Agent",
    handoffs=[agent1(), agent2(), agent3()],
    ...
)
```

### Production File Structure

Real Temporal applications use separate files:
- `workflow.py` - Business logic
- `worker.py` - Execution infrastructure
- `starter.py` - Workflow invocation

## Troubleshooting

**Error: `Failed to connect to Temporal server`**
- Ensure Temporal is running using `temporal_installation.ipynb`:
  1. Open `temporal_installation.ipynb` in VS Code
  2. Run each cell to install and start Temporal
- Check: http://localhost:8233

**Worker exits immediately after starting**
- This happens when TODOs in `worker.py` are not completed
- Complete all TODOs in `worker.py` to create and run the worker
- You should see "⏳ Polling for tasks..." and the worker should continue running
- If you see "⚠️ Worker setup incomplete", complete the TODOs first

**Error: `No module named 'agents'`**
- Run: `pip install openai-agents`

**Error: `OPENAI_API_KEY is not set`**
- Add key to `.env` in project root
- Reload terminal

**Worker not picking up tasks**
- Verify worker is running and showing "⏳ Polling for tasks..."
- Check task queue matches in worker and starter (both should use `TASK_QUEUE`)

## Stretch Goals

1. **Add a fourth language** (German, Italian, etc.)
2. **Add conversation history** to maintain context
3. **Add fallback agent** for unclear languages
4. **Add logging** to track routing decisions
5. **Implement multi-step routing** (language → topic specialists)

## Compare with Solution

After completing the exercise, compare your implementation with:

```bash
cd ../../solutions/04_agent_routing
cat workflow.py
cat worker.py
cat starter.py
```

## Next Steps

Congratulations! You've completed the workshop and learned:

- ✅ Multi-agent architectures with routing patterns
- ✅ Agent handoffs with OpenAI Agents SDK
- ✅ Production-ready Temporal application structure
- ✅ How to observe and debug multi-agent workflows

You now know how to build durable, production-ready AI agents! 🎉
