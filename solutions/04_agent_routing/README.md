# 🔀 Activity 4: Routing Workflow

<div align="center">

**🌍 Multi-Language Agent Team - Workshop Activity 🌍**

_Explore this complete implementation during the workshop!_

⚡ 🎯 🤖 🚀

</div>

---

**Goal:** Build a routing workflow that intelligently distributes requests to specialized language agents using the handoff pattern.

**Timebox:** ⏱️ 15 minutes

**📚 Workshop Note:** During the workshop, you'll explore and run this complete solution. After the workshop, try building it yourself from scratch using the [exercise version](../../exercises/04_agent_routing/)!

## 🎓 What You'll Learn

<div align="center">

**🚀 Master Multi-Agent Systems! 🚀**

</div>

This solution demonstrates:

- 🎯 **Agent routing/triage patterns** with OpenAI Agents SDK
- 🌍 **Specialized language agents** (French 🇫🇷, Spanish 🇪🇸, English 🇬🇧)
- 🔀 **Handoff patterns** for agent-to-agent transitions
- 📁 **Production-ready multi-agent** systems with Temporal
- 🏗️ **Real Temporal application structure** (separate files for workflow, worker, starter)

> 💡 **This is production-ready code!** Use it as a template for your own projects!

## 🏗️ Architecture Pattern

<div align="center">

**🎭 The Magic of Intelligent Routing 🎭**

</div>

This solution demonstrates the **routing pattern** where a triage agent analyzes incoming requests and delegates to specialized agents:

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

> 🎯 **Scalability**: This pattern easily scales to dozens of specialist agents!

## ✅ Prerequisites

<div align="center">

**🔧 Before You Run This Solution 🔧**

</div>

Make sure you have everything ready:

### 1️⃣ Temporal Server Running ⚡

```bash
# Start Temporal using temporal_installation.ipynb notebook:
#   1. Open temporal_installation.ipynb in VS Code
#   2. Run each cell to install Temporal CLI and start the dev server
```

**Verify In Codespaces:** Go to the **Ports** tab → Find port **8233** → Click the **Globe icon** 🌐

### 2️⃣ Dependencies Installed 📦

```bash
# Install from this directory
cd solutions/04_agent_routing
pip install -r requirements.txt
```

### 3️⃣ Environment Variables Set 🔑

Ensure your `.env` file in the project root contains:

```bash
OPENAI_API_KEY=your_api_key_here
```

**Verify with:**

```bash
# From project root
make env
```

> ✨ **Ready to go?** Let's see this solution in action!

## 📁 File Structure

<div align="center">

**🏗️ Production-Ready Architecture 🏗️**

_This is how the pros do it!_

</div>

This solution uses a **realistic Temporal application structure** with separate Python files:

```
solutions/04_agent_routing/
├── workflow.py      # 🎭 Workflow definition and agent configurations
├── worker.py        # ⚙️ Worker that executes workflows
├── starter.py       # 🚀 Script to run the workflow
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
>
> - ✅ Independent deployment of workers
> - ✅ Multiple workers for horizontal scaling
> - ✅ Different starters for different use cases
> - ✅ Clean separation of concerns

## 🚀 Steps to Run

<div align="center">

**▶️ Let's See It In Action! ▶️**

</div>

### Step 1: Review the Code 📖

**Open and examine the complete solution:**

<table>
<tr>
<td width="150px"><strong>workflow.py</strong></td>
<td>Contains:
<ul>
<li>Agent definitions (French, Spanish, English, Triage)</li>
<li><code>RoutingWorkflow</code> class with handoff pattern</li>
<li>Agent routing logic</li>
</ul>
</td>
</tr>
<tr>
<td><strong>worker.py</strong></td>
<td>Contains:
<ul>
<li>Temporal client connection with OpenAI Agents SDK plugin</li>
<li>Worker registration for RoutingWorkflow</li>
<li>Task queue configuration</li>
</ul>
</td>
</tr>
<tr>
<td><strong>starter.py</strong></td>
<td>Contains:
<ul>
<li>Workflow execution logic</li>
<li>Sample queries in different languages</li>
<li>Result display</li>
</ul>
</td>
</tr>
</table>

> 💡 **Pro Tip**: Read through the code to understand the complete implementation!

---

### Step 2: Start the Worker ⚙️

<div align="center">

**🔧 Fire up the engine! 🔧**

</div>

Open a terminal in this directory and start the worker:

```bash
cd solutions/04_agent_routing/
python worker.py
```

**Expected output:**

```
🚀 Worker started successfully
📋 Task Queue: routing-workflow-queue
🔄 Workflows: ['RoutingWorkflow']
⏳ Polling for tasks... (Press Ctrl+C to stop)
```

**⚠️ Keep this terminal running!** The worker must be active to process workflows.

---

### Step 3: Execute the Workflow 🚀

<div align="center">

**🎬 Showtime! 🎬**

</div>

Open a **new terminal** in this directory and run the starter:

```bash
# With default English query
cd solutions/04_agent_routing/

python starter.py

# Or pass a custom query as a command line argument
python starter.py "¡Hola! Cuéntame un trabalenguas."
python starter.py "Bonjour! Comment allez-vous aujourd'hui?"
python starter.py "Hello! How are you doing today?"
```

**Expected output:**

```
🚀 Starting Routing Workflow
📋 Workflow ID: routing-wed-oct-16-103045est
💬 Query: ¡Hola! Cuéntame un trabalenguas.

✅ Workflow started: routing-wed-oct-16-103045est
🔗 View in Temporal UI: http://localhost:8233/namespaces/default/workflows/routing-wed-oct-16-103045est

⏳ Waiting for agent response...

💬 Agent Response: Tres tristes tigres tragaban trigo en un trigal...

💡 The triage agent detected the language and routed to the Spanish specialist!
🔗 Check the Temporal UI to see the complete execution history
```

---

### Step 4: Demonstrate Temporal Durability 🛡️

<div align="center">

**💪 See Temporal's Durability in Action! 💪**

</div>

This workflow includes a 10-second pause after the triage agent completes. This demonstrates Temporal's durability - you can kill the worker and it will resume exactly where it left off!

**To demonstrate:**

1. **Watch the worker terminal** - you'll see the pause message:

   ```
   ⏸️  Pausing for 10 seconds to demonstrate durability...
   ```

2. **Kill the worker** during the 10-second pause:

   - Press `Ctrl+C` in the worker terminal

3. **Restart the worker** immediately:

   ```bash
   python worker.py
   ```

4. **Observe the magic** ✨:

   - The workflow resumes from the pause point
   - It does NOT re-run the triage agent
   - The specialist agent completes the response
   - No data is lost!

5. **Check the Temporal UI**:
   - You'll see the workflow paused during the delay
   - Then resumed after the worker restarted
   - Full execution history is preserved

> 🎯 **Key Insight**: This is Temporal's durability guarantee. Even if your worker crashes, workflows resume exactly where they left off. The triage agent call is never re-executed!

---

### Step 5: Observe in Temporal UI 🔍

<div align="center">

**👀 See the Magic Happen! 👀**

</div>

1. **Open Temporal UI:**
2. **Find** your workflow (search by workflow ID)
3. **Observe:**
   - Workflow execution timeline
   - Agent handoff from triage to specialist
   - The 10-second timer during the pause
   - Complete execution history
   - Input/output for each step

> 🎯 **Pro Tip**: Click through the events to understand the agent routing flow!

---

### Step 6: Test Different Languages 🌍

<div align="center">

**🎨 Experiment with Different Languages! 🎨**

</div>

**Test different languages using command line arguments:**

```bash
# Test French
python starter.py "Bonjour! Raconte-moi un virelangue."

# Test Spanish
python starter.py "¡Hola! Cuéntame un trabalenguas."

# Test English
python starter.py "Hi! Tell me a tongue twister."

# Test mixed or edge cases
python starter.py "Hello! ¿Cómo estás? Je vais bien."
```

Then observe in the Temporal UI how the triage agent routes to different specialists!

> 🌟 **Challenge**: Try mixed-language queries or edge cases!

## ✨ Expected Output Examples

<div align="center">

**🎬 What Success Looks Like! 🎬**

</div>

### French Query 🇫🇷

**Input:** `"Bonjour! Comment allez-vous aujourd'hui?"`

**Output:** French response from French Agent

```
Response: Bonjour! Je vais très bien, merci de demander!
Comment puis-je vous aider aujourd'hui?
```

---

### Spanish Query 🇪🇸

**Input:** `"¡Hola! ¿Cómo estás hoy?"`

**Output:** Spanish response from Spanish Agent

```
Response: ¡Hola! Estoy muy bien, gracias por preguntar.
¿En qué puedo ayudarte hoy?
```

---

### English Query 🇬🇧

**Input:** `"Hello! How are you doing today?"`

**Output:** English response from English Agent

```
Response: Hello! I'm doing great, thank you for asking!
How can I assist you today?
```

> 💡 **Notice**: Each agent responds naturally in its own language!

## 🧠 Key Concepts

<div align="center">

**💡 Understanding the Implementation 💡**

</div>

### 🎯 Routing Pattern

The **routing pattern** (also called **triage pattern**) is a multi-agent architecture where:

<table>
<tr>
<td width="50px">1️⃣</td>
<td><strong>Triage Agent</strong> analyzes incoming requests</td>
</tr>
<tr>
<td>2️⃣</td>
<td><strong>Specialist Agents</strong> handle specific types of requests</td>
</tr>
<tr>
<td>3️⃣</td>
<td><strong>Handoff Mechanism</strong> transfers control between agents</td>
</tr>
</table>

**🌟 Benefits:**

- ✅ Separation of concerns (each agent has one job)
- ✅ Scalable to many specialists
- ✅ Clear decision boundaries
- ✅ Easy to add new specialists

---

### 🔀 Handoff Pattern

The **handoff pattern** in OpenAI Agents SDK allows agents to transfer control:

```python
def triage_agent() -> Agent:
    return Agent(
        name="Triage Agent",
        instructions="Route to the appropriate specialist...",
        handoffs=[french_agent(), spanish_agent(), english_agent()],
    )
```

> 🎯 **Key Point**: The triage agent can invoke ANY agent in its `handoffs` list based on its analysis!

---

### ⚡ Temporal Integration

Wrapping agents in Temporal workflows provides:

<table>
<tr>
<td width="150px">🛡️ <strong>Durability</strong></td>
<td>Survives crashes and restarts</td>
</tr>
<tr>
<td>🔄 <strong>Retries</strong></td>
<td>Automatic retry on failures</td>
</tr>
<tr>
<td>🔍 <strong>Observability</strong></td>
<td>Full execution history in UI</td>
</tr>
<tr>
<td>📈 <strong>Scalability</strong></td>
<td>Workers can scale independently</td>
</tr>
</table>

---

### 🏗️ Production Structure

This solution uses a **3-file pattern** common in production:

<table>
<tr>
<td width="150px"><code>workflow.py</code></td>
<td>Business logic (workflows and agents)</td>
</tr>
<tr>
<td><code>worker.py</code></td>
<td>Execution infrastructure (polls and runs)</td>
</tr>
<tr>
<td><code>starter.py</code></td>
<td>Workflow invocation (triggers execution)</td>
</tr>
</table>

**🌟 This separation enables:**

- ✅ Independent deployment of workers
- ✅ Multiple workers for horizontal scaling
- ✅ Different starters for different use cases
- ✅ Clean code organization and maintenance

> 💪 **Production-Ready**: This is how real companies structure their Temporal applications!

## 🐛 Troubleshooting

<div align="center">

**🔧 Common Issues & Quick Fixes 🔧**

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
<summary><strong>❌ Error: <code>No module named 'agents'</code></strong></summary>

**Solution:**

```bash
pip install openai-agents
```

</details>

<details>
<summary><strong>❌ Error: <code>OPENAI_API_KEY is not set</code></strong></summary>

**Solution:**

- Add key to `.env` file in project root
- Load environment: `source .env` or restart terminal
- Verify with: `make env`

</details>

<details>
<summary><strong>⚠️ Worker not picking up tasks</strong></summary>

**Solution:**

- Verify worker is running (check terminal output)
- Ensure task queue matches in worker and starter
- Check worker logs for errors
- Restart the worker if needed

</details>

<details>
<summary><strong>⏰ No response or timeout</strong></summary>

**Solution:**

- Check OPENAI_API_KEY is valid
- Verify internet connection for OpenAI API calls
- Increase timeout in `worker.py` if needed

</details>

---

> 🆘 **Still stuck?** Check the [main README troubleshooting section](../../README.md#-troubleshooting) or open an issue!

## 🚀 Stretch Goals

<div align="center">

**🌟 Level Up Your Skills! 🌟**

_Extend this solution with advanced features!_

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

> 🏆 **Master Challenge**: Implement all 5 stretch goals and create a production-ready multi-agent system!

## 🎉 Next Steps

<div align="center">

**🏆 Congratulations! 🏆**

_You've completed the workshop!_

</div>

After completing this exercise, you've learned:

- ✅ **Multi-agent architectures** with routing patterns
- ✅ **Agent handoffs** with OpenAI Agents SDK
- ✅ **Production-ready** Temporal application structure
- ✅ **How to observe and debug** multi-agent workflows

<div align="center">

### 🚀 **You now know how to build durable, production-ready AI agents!** 🚀

---

**What's Next?**

<table>
<tr>
<td width="50px">📚</td>
<td><strong>Dive Deeper</strong><br>
Explore the <a href="https://docs.temporal.io/">Temporal Documentation</a> and <a href="https://platform.openai.com/docs/guides/function-calling">OpenAI Agents SDK</a></td>
</tr>
<tr>
<td>💬</td>
<td><strong>Join the Community</strong><br>
Connect with others on <a href="https://temporal.io/slack">Temporal Slack</a></td>
</tr>
<tr>
<td>🔬</td>
<td><strong>Experiment</strong><br>
Try the stretch goals above to deepen your understanding</td>
</tr>
<tr>
<td>🌟</td>
<td><strong>Build & Share</strong><br>
Create something amazing and share it with the world!</td>
</tr>
<tr>
<td>📖</td>
<td><strong>Keep Learning</strong><br>
Check out <a href="https://github.com/temporalio/samples-python/tree/main/openai_agents/agent_patterns">Temporal Samples - Agent Patterns</a></td>
</tr>
</table>

---

## 📖 Additional Resources

- 🤖 [OpenAI Agents SDK Documentation](https://openai.github.io/openai-agents-python/)
- 📚 [Temporal Python SDK Documentation](https://docs.temporal.io/dev-guide/python)
- 🎯 [Temporal Samples - Agent Patterns](https://github.com/temporalio/samples-python/tree/main/openai_agents/agent_patterns)
- 💡 [Workshop Slides](https://docs.google.com/presentation/d/1ZKj-PUm8-swnwP7jQPyQNMs4NIBAuCuglU3iByWn4CM/)

---

Made with ❤️ by the Temporal Community

**Keep building! Keep learning! Keep being awesome!** 🎉

</div>
