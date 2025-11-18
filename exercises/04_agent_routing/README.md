# 🔀 Activity 4: Routing Workflow

<div align="center">

**🌍 Build a Polyglot Agent Team - Homework Exercise! 🌍**

*French • Spanish • English — Your agents speak them all!*

⚡ 🎯 🤖 🚀

</div>

---

**Goal:** Build a routing workflow that intelligently distributes requests to specialized language agents using the handoff pattern.

**Timebox:** ⏱️ 15 minutes

**📚 Homework Note:** This is the practice version! Use this after the workshop to build the routing workflow from scratch. During the workshop, you explored the [complete solution](../../solutions/04_agent_routing/).

## 🎓 What You'll Learn

<div align="center">

**🚀 Master Multi-Agent Systems! 🚀**

</div>

By completing this exercise, you'll master:

- 🎯 **Agent routing/triage patterns** with OpenAI Agents SDK
- 🌍 **Specialized language agents** (French 🇫🇷, Spanish 🇪🇸, English 🇬🇧)
- 🔀 **Handoff patterns** for seamless agent-to-agent transitions
- 📁 **Production-ready multi-agent** systems with Temporal
- 🏗️ **Real Temporal application structure** (separate files for workflow, worker, starter)

> 💡 **This is how pros build it!** Real production patterns, not toy examples!

## 🏗️ Architecture Pattern

<div align="center">

**🎭 The Magic of Intelligent Routing 🎭**

</div>

This exercise demonstrates the **routing pattern** where a triage agent analyzes incoming requests and delegates to specialized agents:

### High-Level Flow

```
   User Query (any language) 👤
           ↓
   ┌───────────────────────────┐
   │ Temporal Workflow         │  🎭 Orchestration
   │ (orchestration layer)     │
   └───────────────────────────┘
           ↓
   ┌───────────────────────────┐
   │ Triage Agent              │  🔍 Language Detection
   │ (language detection)      │
   └───────────────────────────┘
           ↓
      ┌────┴────┬────────┐
      ↓         ↓        ↓
   French    Spanish   English
   Agent 🇫🇷  Agent 🇪🇸  Agent 🇬🇧
      ↓         ↓        ↓
      └────┬────┴────────┘
           ↓
   Response in appropriate language ✅
```

### Detailed Flow with Temporal Activities

```
       User Query 👤
           ↓
   ┌───────────────────────────┐
   │ Temporal Workflow         │  🎭 Orchestration Layer
   │ (orchestration layer)     │
   └───────────────────────────┘
           ↓
   ┌───────────────────────────┐
   │ Activity: Call Triage     │  🤖 Analyze Request
   │    Agent                  │
   └───────────────────────────┘
           ↓
   [Triage agent analyzes language]
           ↓
   ┌───────────────────────────┐
   │ Activity: Handoff to      │  🔀 Smart Routing
   │    Specialist Agent       │
   └───────────────────────────┘
           ↓
   ┌───────────────────────────┐
   │ Activity: Specialist      │  💬 Expert Response
   │    Agent processes query  │
   └───────────────────────────┘
           ↓
       Return response to user ✅
```

**🌟 Key Benefits:**
- ✅ Each agent handoff is managed by Temporal
- ✅ Automatic retries if agent calls fail
- ✅ Full execution history in Temporal UI
- ✅ Production-ready multi-agent architecture

> 🎯 **Pro Tip**: This pattern scales to dozens of specialist agents!

## ✅ Prerequisites

<div align="center">

**🔧 Get Ready to Build! 🔧**

</div>

Before starting this exercise, make sure you have:

### 1️⃣ Temporal Server Running ⚡

```bash
# Start Temporal using temporal_installation.ipynb notebook:
   1. Open temporal_installation.ipynb in VS Code
   2. Run each cell to install Temporal CLI and start the dev server
```

**Verify In Codespaces:** Go to the **Ports** tab → Find port **8233** → Click the **Globe icon** 🌐

### 2️⃣ Dependencies Installed 📦

```bash
# Install from this directory
cd exercises/04_agent_routing
pip install -r requirements.txt
```

### 3️⃣ Environment Variables Set 🔑

Ensure your `.env` file in the project root contains. (You should have already done this in step 03 of the Quickstart of the main README):

```bash
OPENAI_API_KEY=your_api_key_here
```

> ⚠️ **Important**: All three must be ready before you start!

## 📁 File Structure

<div align="center">

**🏗️ Production-Ready Architecture 🏗️**

*This is how real apps are built!*

</div>

This exercise uses a **realistic Temporal application structure** with separate Python files:

```
exercises/04_agent_routing/
├── workflow.py      # 🎭 Workflow definition and agent configurations (TODO)
├── worker.py        # ⚙️ Worker that executes workflows (TODO)
├── starter.py       # 🚀 Script to run the workflow (TODO)
├── requirements.txt # 📦 Dependencies
└── README.md        # 📖 This file (you are here!)
```

<table>
<tr>
<td width="150px"><strong>workflow.py</strong></td>
<td>🎭 Defines business logic - your agent team's playbook</td>
</tr>
<tr>
<td><strong>worker.py</strong></td>
<td>⚙️ Executes workflows and activities - the engine that runs it all</td>
</tr>
<tr>
<td><strong>starter.py</strong></td>
<td>🚀 Triggers workflow executions - starts your agent team</td>
</tr>
</table>

> 💡 **Why separate files?** This mirrors production Temporal applications and enables:
> - ✅ Independent deployment of workers
> - ✅ Multiple workers for horizontal scaling  
> - ✅ Different starters for different use cases

## 📝 Steps

<div align="center">

**👷 Time to Build! 👷**

*Follow these steps to create your multi-agent system*

</div>

### Step 1: Define the Agents 🤖

**Open `workflow.py` and complete the TODOs:**

<details>
<summary><strong>1️⃣ Implement <code>french_agent()</code></strong> 🇫🇷</summary>

- Return an `Agent` with name "French Agent"
- Instructions: "You only speak French. Respond naturally to user queries in French."
- Model: "gpt-4"

</details>

<details>
<summary><strong>2️⃣ Implement <code>spanish_agent()</code></strong> 🇪🇸</summary>

- Return an `Agent` with name "Spanish Agent"
- Instructions: "You only speak Spanish. Respond naturally to user queries in Spanish."
- Model: "gpt-4"

</details>

<details>
<summary><strong>3️⃣ Implement <code>english_agent()</code></strong> 🇬🇧</summary>

- Return an `Agent` with name "English Agent"
- Instructions: "You only speak English. Respond naturally to user queries in English."
- Model: "gpt-4"

</details>

<details>
<summary><strong>4️⃣ Implement <code>triage_agent()</code></strong> 🔍</summary>

- Return an `Agent` with name "Triage Agent"
- Instructions: "You are a triage agent. Analyze the language of the user's query and handoff to the appropriate language specialist agent."
- **Important:** Add `handoffs=[french_agent(), spanish_agent(), english_agent()]`
- Model: "gpt-4"

</details>

**💡 Hint:** Use the `Agent` class from `agents`:

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

---

### Step 2: Implement the Workflow 🎭

**In `workflow.py`, complete the `RoutingWorkflow.run()` method:**

<details>
<summary><strong>Click to see the implementation steps</strong></summary>

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

</details>

**⚠️ Important:** Note the parameter names in `Runner.run()`:
- Use `input=inputs` (not just passing inputs directly)
- Use `run_config=config` (not `config=config`)

---

### Step 3: Implement the Worker ⚙️

**Open `worker.py` and complete the TODOs:**

<details>
<summary><strong>Click to see the implementation steps</strong></summary>

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
   print(f"🔄 Workflows: {RoutingWorkflow.__name__}")
   print(f"⏳ Polling for tasks... (Press Ctrl+C to stop)\n")
   ```

4. Run the worker:
   ```python
   await worker.run()
   ```

</details>

---

### Step 4: Implement the Starter 🚀

**Open `starter.py` and complete the TODOs:**

<details>
<summary><strong>Click to see the implementation steps</strong></summary>

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

5. Start the workflow and get handle:
   ```python
   handle = await client.start_workflow(
       RoutingWorkflow.run,
       query,
       id=workflow_id,
       task_queue=TASK_QUEUE,
   )
   ```

6. Print confirmation and Temporal UI link:
   ```python
   print(f"✅ Workflow started: {handle.id}")
   print(f"🔗 View in Temporal UI: http://localhost:8233/namespaces/default/workflows/{workflow_id}\n")
   print("⏳ Waiting for agent response...\n")
   ```

7. Wait for result and display:
   ```python
   result = await handle.result()
   print(f"💬 Agent Response: {result}")
   ```

</details>

---

### Step 5: Run the Workflow ▶️

<div align="center">

**🎬 Showtime! 🎬**

</div>

**Terminal 1 - Start the worker:**

```bash
cd exercises/04_agent_routing
python worker.py
```

**Wait for:** `🚀 Worker started successfully` ✅

**Terminal 2 - Execute the workflow:**

```bash
cd exercises/04_agent_routing
python starter.py
```

> 🎉 **Watch the magic happen!** Your triage agent will detect the language and route to the right specialist!

---

### Step 6: Observe in Temporal UI 🔍

<div align="center">

**👀 See It In Action! 👀**

</div>

1. Open: http://localhost:8233
2. Find your workflow by ID (e.g., `routing-wed-oct-16-103045est`)
3. Observe the agent handoff and execution history
4. See how the triage agent detected English and routed to the English Agent

> 💡 **Pro Tip**: Click through the execution events to see each step!

---

### Step 7: Test Different Languages 🌍

<div align="center">

**🎨 Get Creative! 🎨**

</div>

Modify the query in `starter.py` to test routing to different language agents:

```python
# Change the query variable to:
query = "Bonjour! Raconte-moi une histoire."  # 🇫🇷 Routes to French Agent
# or
query = "¡Hola! Cuéntame un chiste."  # 🇪🇸 Routes to Spanish Agent
```

Run `python starter.py` again and observe routing to different agents in the Temporal UI!

> 🌟 **Challenge**: Can you make the agent handle mixed-language queries?

## ✨ Expected Output

<div align="center">

**🎬 What Success Looks Like! 🎬**

</div>

### English Query (Tongue Twister) 🇬🇧

**Input:** `"Hi! Tell me a tongue twister."`

**Output:**
```
🚀 Starting Routing Workflow
📋 Workflow ID: routing-wed-oct-16-103045est

✅ Workflow started: routing-wed-oct-16-103045est
🔗 View in Temporal UI: http://localhost:8233/namespaces/default/workflows/routing-wed-oct-16-103045est

⏳ Waiting for agent response...

💬 Agent Response: Response: She sells seashells by the seashore. The shells she sells are surely seashells.
```

---

### Testing Other Languages 🌍

<div align="center">

**Try these different language queries!**

</div>

<table>
<tr>
<td width="100px"><strong>🇫🇷 French</strong></td>
<td>
<code>query = "Bonjour! Comment allez-vous aujourd'hui?"</code><br>
<strong>Expected:</strong> Response in French from French Agent
</td>
</tr>
<tr>
<td><strong>🇪🇸 Spanish</strong></td>
<td>
<code>query = "¡Hola! ¿Cómo estás hoy?"</code><br>
<strong>Expected:</strong> Response in Spanish from Spanish Agent
</td>
</tr>
<tr>
<td><strong>🇬🇧 English</strong></td>
<td>
<code>query = "Hello! How are you doing today?"</code><br>
<strong>Expected:</strong> Response in English from English Agent
</td>
</tr>
</table>

> 💡 **Notice**: The triage agent automatically detects the language and routes to the right specialist!

## 🧠 Key Concepts

<div align="center">

**💡 Understanding the Magic 💡**

</div>

### 🎯 Routing Pattern

The **routing pattern** (triage pattern) uses:

<table>
<tr>
<td width="180px">🔍 <strong>Triage Agent</strong></td>
<td>Analyzes requests and decides routing (the "brain")</td>
</tr>
<tr>
<td>🎓 <strong>Specialist Agents</strong></td>
<td>Handle specific types of requests (the "experts")</td>
</tr>
<tr>
<td>🔀 <strong>Handoff Mechanism</strong></td>
<td>Transfers control between agents (the "dispatcher")</td>
</tr>
</table>

> 💪 **Power Move**: This pattern scales to hundreds of specialists!

---

### 🔀 Handoff Pattern

Enable agent handoffs with the `handoffs` parameter:

```python
Agent(
    name="Triage Agent",
    handoffs=[agent1(), agent2(), agent3()],
    ...
)
```

> 🎯 **Key Insight**: The triage agent can invoke ANY agent in its handoffs list based on its analysis!

---

### 🏗️ Production File Structure

Real Temporal applications use separate files:

<table>
<tr>
<td width="150px"><code>workflow.py</code></td>
<td>🎭 Business logic (what to do)</td>
</tr>
<tr>
<td><code>worker.py</code></td>
<td>⚙️ Execution infrastructure (how to run it)</td>
</tr>
<tr>
<td><code>starter.py</code></td>
<td>🚀 Workflow invocation (when to start it)</td>
</tr>
</table>

**🌟 Why this matters:**
- ✅ Workers can scale independently
- ✅ Deploy updates without downtime
- ✅ Different starters for different scenarios
- ✅ Production-ready from day one!

## 🐛 Troubleshooting

<div align="center">

**🔧 Quick Fixes for Common Issues 🔧**

</div>

<details>
<summary><strong>❌ Error: <code>Failed to connect to Temporal server</code></strong></summary>

**Solution:**
- Ensure Temporal is running using `temporal_installation.ipynb`:
  1. Open `temporal_installation.ipynb` in VS Code
  2. Run each cell to install and start Temporal
- Check server at: http://localhost:8233
- Verify port 7233 is not blocked

</details>

<details>
<summary><strong>⚠️ Worker exits immediately after starting</strong></summary>

**Why this happens:**
- This occurs when TODOs in `worker.py` are not completed

**Solution:**
- Complete all TODOs in `worker.py` to create and run the worker
- You should see "⏳ Polling for tasks..." and the worker should continue running
- If you see "⚠️ Worker setup incomplete", complete the TODOs first

> 💡 **Pro Tip**: A healthy worker keeps running and doesn't exit!

</details>

<details>
<summary><strong>❌ Error: <code>No module named 'agents'</code></strong></summary>

**Solution:**
```bash
pip install openai-agents
```

</details>

<details>
<summary><strong>❌ Error: <code>OPENAI_API_KEY is not set</code></strong></summary>

**Solution:**
- Add key to `.env` in project root
- Reload terminal
- Run `make env` to verify

</details>

<details>
<summary><strong>⚠️ Worker not picking up tasks</strong></summary>

**Solution:**
- Verify worker is running and showing "⏳ Polling for tasks..."
- Check task queue matches in worker and starter (both should use `TASK_QUEUE`)
- Restart the worker if needed

</details>

---

> 🆘 **Still stuck?** Check the [main README troubleshooting section](../../README.md#-troubleshooting) or open an issue!

## 🚀 Stretch Goals

<div align="center">

**🌟 Level Up Your Skills! 🌟**

*For those who finish early and want more challenges!*

</div>

### 1️⃣ Add a Fourth Language 🇩🇪

Add a German agent to the routing workflow:

```python
def german_agent() -> Agent:
    return Agent(
        name="German Agent",
        instructions="You only speak German. Respond naturally in German.",
        model="gpt-4",
    )

def triage_agent() -> Agent:
    return Agent(
        # ...
        handoffs=[french_agent(), spanish_agent(), english_agent(), german_agent()],
    )
```

**Test with:** `"Hallo! Wie geht es Ihnen heute?"`

---

### 2️⃣ Add Context Passing 💬

Modify the workflow to maintain conversation history:

```python
@workflow.run
async def run(self, user_query: str, conversation_history: list = None) -> str:
    # Pass history to agents for multi-turn conversations
    # ...
```

---

### 3️⃣ Add Fallback Agent 🛟

Create a "general" agent that handles queries when language is unclear:

```python
def general_agent() -> Agent:
    return Agent(
        name="General Agent",
        instructions="You handle queries when language is unclear or mixed.",
        model="gpt-4",
    )
```

---

### 4️⃣ Add Logging and Metrics 📊

Enhance observability with structured logging:

```python
@workflow.run
async def run(self, user_query: str) -> str:
    workflow.logger.info(f"Routing query: {user_query[:50]}...")
    # Log which agent was selected
    # Log response time
    # ...
```

---

### 5️⃣ Multi-Step Routing 🎯

Implement a workflow where the triage agent can route to multiple specialists in sequence:

```python
# First, route to language specialist
# Then, route to topic specialist (tech, health, finance)
# Combine responses
```

> 🏆 **Champion Challenge**: Implement all 5 stretch goals and share your implementation!

## 📚 Compare with Solution

<div align="center">

**✅ Ready to Check Your Work? ✅**

</div>

After completing the exercise, compare your implementation with the solution:

```bash
cd ../../solutions/04_agent_routing
cat workflow.py
cat worker.py
cat starter.py
```

> 💡 **Learning Tip**: Try to complete it yourself first! The struggle is where the learning happens! 💪

---

