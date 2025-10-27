# Exercise 4: Routing Workflow

**Goal:** Build a routing workflow that intelligently distributes requests to specialized language agents using the handoff pattern.

**Timebox:** 15 minutes

## What You'll Learn

- Implement agent routing/triage patterns with OpenAI Agents SDK
- Create specialized agents for different languages (French, Spanish, English)
- Use handoff patterns for agent-to-agent transitions
- Build production-ready multi-agent systems with Temporal
- Understand how to structure real Temporal applications (separate files for workflow, worker, starter)

## Architecture

This exercise demonstrates the **routing pattern** where a triage agent analyzes incoming requests and delegates to specialized agents:

```
User Query (any language)
    ↓
Temporal Workflow 🎭
    ↓
Triage Agent 🔍
    ├─→ French Agent 🇫🇷 (if French detected)
    ├─→ Spanish Agent 🇪🇸 (if Spanish detected)
    └─→ English Agent 🇬🇧 (if English detected)
    ↓
Response in appropriate language ✅
```

## Prerequisites

Before running this exercise, ensure you have:

### 1. Temporal Server Running

```bash
# Start Temporal dev server (from project root)
make temporal-up

# Or manually:
temporal server start-dev
```

Verify at: http://localhost:8233

### 2. Dependencies Installed

```bash
# Install from this directory
pip install -r requirements.txt

# Or from project root:
pip install temporalio openai-agents httpx rich pytz
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
solutions/04_agent_routing/
├── workflow.py      # Workflow definition and agent configurations
├── worker.py        # Worker that executes workflows
├── starter.py       # Script to run the workflow
├── requirements.txt # Dependencies
└── README.md        # This file
```

This mirrors production Temporal applications where:
- **Workflows** define business logic
- **Workers** execute workflows and activities
- **Starters** trigger workflow executions

## Steps to Run

### Step 1: Review the Code

**Open and examine:**

1. **`workflow.py`** - Contains:
   - Agent definitions (French, Spanish, English, Triage)
   - `RoutingWorkflow` class with handoff pattern
   - Agent routing logic

2. **`worker.py`** - Contains:
   - Temporal client connection with OpenAI Agents SDK plugin
   - Worker registration for RoutingWorkflow
   - Task queue configuration

3. **`starter.py`** - Contains:
   - Workflow execution logic
   - Sample queries in different languages
   - Result display

### Step 2: Start the Worker

Open a terminal in this directory and start the worker:

```bash
python worker.py
```

**Expected output:**

```
🚀 Worker started successfully
📋 Task Queue: routing-workflow-queue
🔄 Workflows: ['RoutingWorkflow']
⏳ Polling for tasks... (Press Ctrl+C to stop)
```

**Keep this terminal running!** The worker must be active to process workflows.

### Step 3: Execute the Workflow

Open a **new terminal** in this directory and run the starter:

```bash
python starter.py
```

**Expected output:**

```
🚀 Starting Routing Workflow
📋 Workflow ID: routing-wed-oct-16-103045est
💬 Query: Bonjour! Comment allez-vous aujourd'hui?

✅ Workflow started: routing-wed-oct-16-103045est
🔗 View in Temporal UI: http://localhost:8233/namespaces/default/workflows/routing-wed-oct-16-103045est

⏳ Waiting for agent response...

======================================================================
🤖 Agent Response
======================================================================
Triage Agent: [routing decision]

Response: Bonjour! Je vais bien, merci! Comment puis-je vous aider aujourd'hui?
======================================================================

💡 The triage agent detected the language and routed to the specialist!
🔗 Check the Temporal UI to see the complete execution history
```

### Step 4: Observe in Temporal UI

1. Open: http://localhost:8233
2. Find your workflow (search by workflow ID)
3. Observe:
   - Workflow execution timeline
   - Agent handoff from triage to specialist
   - Complete execution history
   - Input/output for each step

### Step 5: Test Different Languages

**Modify `starter.py` to test other languages:**

```python
# In starter.py, around line 43-47, change the query:

queries = [
    "Bonjour! Comment allez-vous aujourd'hui?",  # French
    "¡Hola! ¿Cómo estás hoy?",  # Spanish
    "Hello! How are you doing today?",  # English
]

# Change line 51 to test different languages:
query = queries[1]  # Try Spanish
# or
query = queries[2]  # Try English
```

Then run `python starter.py` again and observe routing to different specialists!

## Expected Output Examples

### French Query

**Input:** `"Bonjour! Comment allez-vous aujourd'hui?"`

**Output:** French response from French Agent

```
Response: Bonjour! Je vais très bien, merci de demander!
Comment puis-je vous aider aujourd'hui?
```

### Spanish Query

**Input:** `"¡Hola! ¿Cómo estás hoy?"`

**Output:** Spanish response from Spanish Agent

```
Response: ¡Hola! Estoy muy bien, gracias por preguntar.
¿En qué puedo ayudarte hoy?
```

### English Query

**Input:** `"Hello! How are you doing today?"`

**Output:** English response from English Agent

```
Response: Hello! I'm doing great, thank you for asking!
How can I assist you today?
```

## Key Concepts

### Routing Pattern

The **routing pattern** (also called **triage pattern**) is a multi-agent architecture where:

1. **Triage Agent** analyzes incoming requests
2. **Specialist Agents** handle specific types of requests
3. **Handoff Mechanism** transfers control between agents

**Benefits:**
- Separation of concerns (each agent has one job)
- Scalable to many specialists
- Clear decision boundaries

### Handoff Pattern

The **handoff pattern** in OpenAI Agents SDK allows agents to transfer control:

```python
def triage_agent() -> Agent:
    return Agent(
        name="Triage Agent",
        instructions="Route to the appropriate specialist...",
        handoffs=[french_agent(), spanish_agent(), english_agent()],
    )
```

The triage agent can invoke any agent in its `handoffs` list based on its analysis.

### Temporal Integration

Wrapping agents in Temporal workflows provides:
- **Durability:** Survives crashes and restarts
- **Retries:** Automatic retry on failures
- **Observability:** Full execution history in UI
- **Scalability:** Workers can scale independently

### Production Structure

This exercise uses a **3-file pattern** common in production:

1. **`workflow.py`** - Business logic (workflows and agents)
2. **`worker.py`** - Execution infrastructure (polls and runs)
3. **`starter.py`** - Workflow invocation (triggers execution)

This separation enables:
- Independent deployment of workers
- Multiple workers for horizontal scaling
- Different starters for different use cases

## Troubleshooting

### Error: `Failed to connect to Temporal server`

**Solution:**
- Ensure Temporal is running: `make temporal-up`
- Check server at: http://localhost:8233
- Verify port 7233 is not blocked

### Error: `No module named 'agents'`

**Solution:**
```bash
pip install openai-agents
```

### Error: `OPENAI_API_KEY is not set`

**Solution:**
- Add key to `.env` file in project root
- Load environment: `source .env` or restart terminal

### Worker not picking up tasks

**Solution:**
- Verify worker is running (check terminal output)
- Ensure task queue matches in worker and starter
- Check worker logs for errors

### No response or timeout

**Solution:**
- Check OPENAI_API_KEY is valid
- Verify internet connection for OpenAI API calls
- Increase timeout in `worker.py` if needed

## Stretch Goals

### 1. Add a Fourth Language

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

Test with: `"Hallo! Wie geht es Ihnen heute?"`

### 2. Add Context Passing

Modify the workflow to maintain conversation history:

```python
@workflow.run
async def run(self, user_query: str, conversation_history: list = None) -> str:
    # Pass history to agents for multi-turn conversations
    # ...
```

### 3. Add Fallback Agent

Create a "general" agent that handles queries when language is unclear:

```python
def general_agent() -> Agent:
    return Agent(
        name="General Agent",
        instructions="You handle queries when language is unclear or mixed.",
        model="gpt-4",
    )
```

### 4. Add Logging and Metrics

Enhance observability with structured logging:

```python
@workflow.run
async def run(self, user_query: str) -> str:
    workflow.logger.info(f"Routing query: {user_query[:50]}...")
    # Log which agent was selected
    # Log response time
    # ...
```

### 5. Multi-Step Routing

Implement a workflow where the triage agent can route to multiple specialists in sequence:

```python
# First, route to language specialist
# Then, route to topic specialist (tech, health, finance)
# Combine responses
```

## Next Steps

After completing this exercise, you've learned:

- ✅ Multi-agent architectures with routing patterns
- ✅ Agent handoffs with OpenAI Agents SDK
- ✅ Production-ready Temporal application structure
- ✅ How to observe and debug multi-agent workflows

**Congratulations!** You've completed the workshop. You now know how to build durable, production-ready AI agents with:
- OpenAI Agents SDK for intelligent agent behavior
- Temporal for durability, retries, and observability
- Real-world application patterns for deployment

## Additional Resources

- [OpenAI Agents SDK Documentation](https://openai.github.io/openai-agents-python/)
- [Temporal Python SDK Documentation](https://docs.temporal.io/dev-guide/python)
- [Temporal Samples - Agent Patterns](https://github.com/temporalio/samples-python/tree/main/openai_agents/agent_patterns)
- [Workshop Slides](https://docs.google.com/presentation/d/1ZKj-PUm8-swnwP7jQPyQNMs4NIBAuCuglU3iByWn4CM/)
