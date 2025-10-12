# Temporal + OpenAI Agents SDK Workshop

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/your-username/temporal-ai-agents-workshop)

Learn to build **durable AI agents** using **OpenAI Agents SDK + Temporal** in this hands-on 90-minute workshop. Everything runs in GitHub Codespaces with zero local setup required.

## 🎯 What You'll Build

By the end of this workshop, you'll understand how to:

- Create AI agents with tool calling using OpenAI's API
- Build durable workflows with Temporal for reliability and retries
- Combine both to create production-ready AI agents that survive failures
- Implement multi-agent systems with handoff patterns
- Observe and debug agent execution using Temporal UI

## 📋 Prerequisites

- Basic Python knowledge
- OpenAI API key ([get one here](https://platform.openai.com/api-keys))
- GitHub account (for Codespaces)

## 🚀 Quick Start

### Option 1: GitHub Codespaces (Recommended)

1. Click the "Open in GitHub Codespaces" badge above
2. Wait ~90 seconds for the environment to set up
3. Add your OpenAI API key to `.env`:
   ```bash
   cp .env.sample .env
   # Edit .env and add your OPENAI_API_KEY
   ```
4. Start Temporal server:
   ```bash
   make temporal-up
   ```
5. You're ready to start the exercises!

### Option 2: Local Setup

```bash
# Clone the repository
git clone https://github.com/your-username/temporal-ai-agents-workshop.git
cd temporal-ai-agents-workshop

# Create and activate virtual environment
python3.11 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
make setup

# Set up environment
cp .env.sample .env
# Edit .env and add your OPENAI_API_KEY

# Install Temporal CLI (if not already installed)
curl -sSf https://temporal.download/cli.sh | sh

# Start Temporal server
make temporal-up
```

## 📚 Workshop Structure

This is a 90-minute workshop: **30 minutes instruction + 4×15 minute exercises**

### Exercise 1: Agent Hello World
**Goal:** Create a simple AI agent with tool calling

- Build your first OpenAI agent with a weather tool
- Understand the agent → tool → response flow
- See how LLMs decide when to use tools

**Run it:**
```bash
make exercise-1
# Or open: exercises/01_agent_hello_world/exercise.ipynb
```

### Exercise 2: Temporal Hello World
**Goal:** Understand Temporal workflows and activities

- Create your first Temporal workflow
- Learn about activities as units of work
- Observe execution in the Temporal UI

**Run it:**
```bash
make temporal-up    # Start Temporal server
make exercise-2
# Or open: exercises/02_temporal_hello_world/exercise.ipynb
```

### Exercise 3: Durable Agent
**Goal:** Combine agents + Temporal for production durability

- Wrap LLM calls in Temporal activities
- Get automatic retries on failures
- Persist agent state across crashes
- Add observability with trace IDs

**Run it:**
```bash
make exercise-3
# Or open: exercises/03_durable_agent/exercise.ipynb
```

### Exercise 4: Multi-Agent Handoff
**Goal:** Build multi-agent systems with workflow orchestration

- Implement agent routing/triage patterns
- Create specialized agents for different tasks
- Orchestrate agent handoffs with Temporal
- Maintain context across agent transitions

**Run it:**
```bash
make exercise-4
# Or open: exercises/04_multi_agent_handoff/exercise.ipynb
```

## 🛠️ Common Commands

```bash
# Setup and validation
make setup          # Install all dependencies
make env            # Check environment variables

# Development
make lint           # Run code linters
make test           # Run test suite

# Temporal
make temporal-up    # Start Temporal dev server
make temporal-down  # Stop Temporal server

# Exercises (both .py scripts and .ipynb notebooks available)
make exercise-1     # Run Exercise 1
make exercise-2     # Run Exercise 2
make exercise-3     # Run Exercise 3
make exercise-4     # Run Exercise 4
```

## 🔍 Key Concepts

### Why Temporal for AI Agents?

AI agents in production face several challenges:

1. **API Failures:** LLM APIs can be rate-limited or temporarily unavailable
2. **Crashes:** Your agent process might crash mid-execution
3. **Long-Running Operations:** Multi-step agent flows need to resume from checkpoints
4. **Observability:** You need to debug what your agent actually did

Temporal solves these by providing:

- **Automatic retries** with configurable policies
- **State persistence** across failures and restarts
- **Execution history** for debugging and auditing
- **Durable execution** that survives crashes

### Architecture Pattern

```
User Query
    ↓
Temporal Workflow (orchestration layer)
    ↓
Activity: Call LLM with tools
    ↓
[If tool needed] Activity: Execute tool
    ↓
Activity: Get final LLM response
    ↓
Return to user
```

Each activity can retry independently, and the entire flow is durable.

## 🐛 Troubleshooting

### Environment Issues

**Problem:** `OPENAI_API_KEY` not found

```bash
# Check your .env file exists
ls -la .env

# Verify the key is set
python scripts/check_env.py
```

**Problem:** Temporal server not running

```bash
# Check if it's running
pgrep -f temporal

# Start it
make temporal-up

# Or manually
temporal server start-dev
```

### Exercise Issues

**Problem:** Import errors when running exercises

```bash
# Reinstall dependencies
pip install -e ".[dev]"
```

**Problem:** Notebook kernel not found

```bash
# Install ipykernel
pip install ipykernel
python -m ipykernel install --user --name temporal-workshop
```

## 📖 Additional Resources

- [Temporal Documentation](https://docs.temporal.io/)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [OpenAI Agents SDK](https://platform.openai.com/docs/guides/function-calling)
- [Temporal Python SDK](https://docs.temporal.io/dev-guide/python)

## 🎓 Instructor Notes

### Timing Breakdown

- **00:00-10:00** - Introduction & Setup verification
- **10:00-25:00** - Demo Exercise 1 + Q&A
- **25:00-40:00** - Students work on Exercise 1
- **40:00-55:00** - Demo Exercise 2 + Q&A
- **55:00-70:00** - Students work on Exercise 2
- **70:00-80:00** - Demo Exercise 3 (key integration)
- **80:00-90:00** - Students explore Exercise 3 & 4

### Common Pitfalls

1. **Students skip checking `.env`** - Do environment check before starting
2. **Temporal not running** - Remind students to run `make temporal-up` for Ex 2+
3. **Tool call parsing** - Show the `eval()` pattern for function arguments (or use `json.loads()` in production)
4. **Activity timeouts** - Explain start_to_close_timeout defaults

### Key Teaching Points

- **Exercise 1:** Emphasize tool calling as the foundation of agentic behavior
- **Exercise 2:** Show the Temporal UI extensively - it's powerful for debugging
- **Exercise 3:** THIS IS THE KEY - show how activities make LLM calls durable
- **Exercise 4:** Advanced - focus on the routing pattern and context passing

## 📝 License

MIT License - feel free to use this workshop material for educational purposes.

## 🤝 Contributing

Found a bug or have a suggestion? Please open an issue or submit a pull request!
