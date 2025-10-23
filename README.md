# 🤖 Temporal + OpenAI Agents SDK Workshop

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/nadvolod/temporal-openai-agents-sdk)

Learn to build **durable AI agents** using **OpenAI Agents SDK + Temporal** in this hands-on 90-minute workshop. Everything runs in GitHub Codespaces with zero local setup required! 🎉

## 🎯 What You'll Build

By the end of this workshop, you'll understand how to:

- ✨ Create AI agents with tool calling using OpenAI's Agents SDK
- 🛡️ Build durable workflows with Temporal for reliability and retries
- 🚀 Combine both to create production-ready AI agents that survive failures
- 🤝 Implement multi-agent systems with handoff patterns
- 🔍 Observe and debug agent execution using Temporal UI

## 📋 Prerequisites

- 🐍 Basic Python knowledge
- 🔑 OpenAI API key ([get one here](https://platform.openai.com/api-keys))
- 🐙 GitHub account (for Codespaces)

## 🚀 Quick Start

### Option 1: GitHub Codespaces (Recommended) ⭐

1. Click the "Open in GitHub Codespaces" badge above 👆
2. Wait ~90 seconds for the environment to set up ⏱️
3. Add your OpenAI API key to `.env`:
   ```bash
   cp .env.sample .env
   # Edit .env and add your OPENAI_API_KEY
   ```
4. Start Temporal server:
   ```bash
   make temporal-up
   ```
5. You're ready to start the exercises! 🎓

#### 📓 Alternative: One-Click Temporal Installation

For easiest Temporal setup, you can also use the Jupyter notebook:

1. Open `temporal_installation.ipynb` in VS Code or Jupyter Lab
2. Run each cell to:
   - Install the Temporal CLI
   - Start the Temporal dev server

This method works in Codespaces, local dev containers, and most Linux environments.

### Option 2: Local Setup 💻

#### 📓 One-Click Temporal Installation (Recommended)

You can use the Jupyter notebook for local setup:

1. Open `temporal_installation.ipynb` in VS Code or Jupyter Lab
2. Run each cell to:
   - Install the Temporal CLI
   - Start the Temporal dev server

#### Manual Installation

```bash
# Clone the repository
git clone https://github.com/nadvolod/temporal-openai-agents-sdk.git
cd temporal-openai-agents-sdk

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

This is a **90-minute workshop**: 30 minutes instruction + 4×15 minute exercises

All exercises are **Jupyter notebooks** 📓 - no command-line scripts needed!

### 📂 Repository Navigation

```
📁 temporal-openai-agents-sdk/
├── 📓 exercises/                    # Work here during the workshop
│   ├── 01_agent_hello_world/       # Exercise 1 - OpenAI agent basics
│   ├── 02_temporal_hello_world/    # Exercise 2 - Temporal fundamentals
│   ├── 03_durable_agent/           # Exercise 3 - Combine both! 🎯
│   └── 04_multi_agent_handoff/     # Exercise 4 - Multi-agent systems
│
├── 📗 solutions/                    # Compare your work
│   ├── 01_agent_hello_world/
│   ├── 02_temporal_hello_world/
│   ├── 03_durable_agent/
│   └── 04_multi_agent_handoff/
│
├── 🛠️  scripts/                     # Helper scripts (bootstrap, env checks)
├── 🧪 tests/                       # Automated tests with mocked APIs
├── 📝 Makefile                     # Common commands (setup, lint, test)
├── 📋 WORKSHOP_SPEC.md             # Workshop design specification
└── 📖 README.md                    # You are here! 👋
```

## 🎓 Workshop Exercises

### Exercise 1: Agent Hello World 🌍

**Goal:** Create a simple AI agent with tool calling using real weather data

**What you'll learn:**
- 🤖 Build your first OpenAI agent with a weather tool
- 🔧 Understand the agent → tool → response flow
- 💡 See how LLMs decide when to use tools
- 🌐 Call real APIs (National Weather Service)

**Run it:**
```bash
# Open the Jupyter notebook in VS Code or Jupyter Lab:
exercises/01_agent_hello_world/exercise.ipynb
```

**Time:** 15 minutes ⏱️

---

### Exercise 2: Temporal Hello World 🌊

**Goal:** Understand Temporal workflows and activities

**What you'll learn:**
- 🏗️ Create your first Temporal workflow
- ⚙️ Learn about activities as units of work
- 🔍 Observe execution in the Temporal UI
- 💪 Experience automatic retries

**Prerequisites:**
```bash
make temporal-up    # Start Temporal server first!
```

**Run it:**
```bash
# Open the Jupyter notebook:
exercises/02_temporal_hello_world/exercise.ipynb
```

**Time:** 15 minutes ⏱️

---

### Exercise 3: Durable Agent 🛡️

**Goal:** Combine agents + Temporal for production durability ⭐

**What you'll learn:**
- 🔄 Wrap LLM calls in Temporal activities
- ✨ Get automatic retries on failures (magic! ✨)
- 💾 Persist agent state across crashes
- 📊 Add observability with trace IDs
- 🚀 Build production-ready AI agents

**This is the KEY exercise!** 🎯

**Run it:**
```bash
# Open the Jupyter notebook:
exercises/03_durable_agent/exercise.ipynb
```

**Time:** 15 minutes ⏱️

---

### Exercise 4: Multi-Agent Handoff 🤝

**Goal:** Build multi-agent systems with workflow orchestration

**What you'll learn:**
- 🎯 Implement agent routing/triage patterns
- 👥 Create specialized agents for different tasks
- 🔀 Orchestrate agent handoffs with Temporal
- 💬 Maintain context across agent transitions

**Run it:**
```bash
# Open the Jupyter notebook:
exercises/04_multi_agent_handoff/exercise.ipynb
```

**Time:** 15 minutes ⏱️

## 🛠️ Common Commands

```bash
# 🔧 Setup and validation
make setup          # Install all dependencies
make env            # Check environment variables (OPENAI_API_KEY)

# 🧹 Code quality
make lint           # Run code linters (ruff, mypy)
make test           # Run test suite (mocked - no API key needed!)

# ⚡ Temporal server
make temporal-up    # Start Temporal dev server
make temporal-down  # Stop Temporal server

# 📓 Working with exercises
# All exercises are Jupyter notebooks!
# Open them in VS Code or Jupyter Lab:
#   exercises/01_agent_hello_world/exercise.ipynb
#   exercises/02_temporal_hello_world/exercise.ipynb
#   exercises/03_durable_agent/exercise.ipynb
#   exercises/04_multi_agent_handoff/exercise.ipynb
#
# Compare with solutions at:
#   solutions/01_agent_hello_world/solution.ipynb
#   solutions/02_temporal_hello_world/solution.ipynb
#   solutions/03_durable_agent/solution.ipynb
#   solutions/04_multi_agent_handoff/solution.ipynb
```

## 🔍 Key Concepts

### Why Temporal for AI Agents? 🤔

AI agents in production face several challenges:

1. **API Failures** 💥: LLM APIs can be rate-limited or temporarily unavailable
2. **Crashes** 🔥: Your agent process might crash mid-execution
3. **Long-Running Operations** ⏳: Multi-step agent flows need to resume from checkpoints
4. **Observability** 🔍: You need to debug what your agent actually did

Temporal solves these by providing:

- ✅ **Automatic retries** with configurable policies
- ✅ **State persistence** across failures and restarts
- ✅ **Execution history** for debugging and auditing
- ✅ **Durable execution** that survives crashes

### Architecture Pattern 🏗️

```
User Query 👤
    ↓
Temporal Workflow (orchestration layer) 🎭
    ↓
Activity: Call LLM with tools 🤖
    ↓
[If tool needed] Activity: Execute tool 🔧
    ↓
Activity: Get final LLM response 💬
    ↓
Return to user ✅
```

Each activity can retry independently, and the entire flow is durable! 💪

## 🐛 Troubleshooting

### Environment Issues 🔧

**Problem:** `OPENAI_API_KEY` not found ❌

```bash
# Check your .env file exists
ls -la .env

# Verify the key is set
python scripts/check_env.py
# Or run: make env
```

**Fix:** Create `.env` from `.env.sample` and add your API key 🔑

---

**Problem:** Temporal server not running ❌

```bash
# Check if it's running
pgrep -f temporal

# Start it
make temporal-up

# Or manually
temporal server start-dev
```

**Fix:** The Temporal dev server must be running for exercises 2, 3, and 4! ⚡

---

### Exercise Issues 📓

**Problem:** Import errors when running exercises ❌

```bash
# Reinstall dependencies
make setup
# Or: pip install -e ".[dev]"
```

---

**Problem:** Notebook kernel not found ❌

```bash
# Install ipykernel
pip install ipykernel
python -m ipykernel install --user --name temporal-workshop
```

Then select the `temporal-workshop` kernel in your notebook! 🎯

---

**Problem:** Can't access Temporal UI at localhost:8233 ❌

**In Codespaces:** The port should be automatically forwarded. Check the "Ports" tab in VS Code and make sure port 8233 is forwarded and public. 🌐

**Local:** Make sure Temporal server is running (`make temporal-up`) and visit http://localhost:8233

---

**Problem:** Tests fail with "module not found" ❌

```bash
# Make sure you're in the project root and have installed in editable mode
cd /path/to/temporal-openai-agents-sdk
pip install -e ".[dev]"
```

## 📖 Additional Resources

- 📚 [Temporal Documentation](https://docs.temporal.io/)
- 🤖 [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- 🎯 [OpenAI Agents SDK](https://platform.openai.com/docs/guides/function-calling)
- 🐍 [Temporal Python SDK](https://docs.temporal.io/dev-guide/python)
- 💡 [Workshop Slides](https://docs.google.com/presentation/d/1ZKj-PUm8-swnwP7jQPyQNMs4NIBAuCuglU3iByWn4CM/edit?slide=id.g38cc80f1e1e_1_0#slide=id.g38cc80f1e1e_1_0)

## 🎓 Instructor Notes

### Timing Breakdown ⏱️

- **00:00-05:00** 🚀 Introduction & Setup verification
- **05:00-15:00** 🤖 OpenAI Agents SDK Introduction (slides)
- **15:00-30:00** 🏃 Exercise 1 + Q&A
- **30:00-35:00** ✅ Solution to 1
- **35:00-40:00** 🌊 Intro to Temporal (slides)
- **40:00-55:00** 🏃 Exercise 2 + Q&A
- **55:00-60:00** ✅ Solution to 2
- **60:00-65:00** 🛡️ OpenAI Agents SDK + Temporal (slides)
- **65:00-80:00** 🏃 Exercise 3 (THE KEY EXERCISE! 🎯)
- **80:00-90:00** 🎉 Exercise 4 (Optional) + Wrap-up

### Common Pitfalls ⚠️

1. **Students skip checking `.env`** 🔑
   - Do environment check before starting (`make env`)
   - Emphasize that exercises 1, 3, 4 need API key
   
2. **Temporal not running** ⚡
   - Remind students to run `make temporal-up` for Exercise 2+
   - Show them how to verify at http://localhost:8233
   
3. **Confusion between exercise and solution** 📓
   - Clearly explain: work in `exercises/`, compare with `solutions/`
   - Solution notebooks are complete standalone implementations
   
4. **Activity timeouts** ⏳
   - Explain `start_to_close_timeout` defaults
   - Show how to adjust for longer-running operations
   
5. **Notebook vs Python files** 📝
   - All exercises are Jupyter notebooks (`.ipynb`)
   - No command-line `main.py` files - everything in notebooks!

### Key Teaching Points 🎯

- **Exercise 1:** Emphasize tool calling as the foundation of agentic behavior 🤖
  - Show how the agent decides to use tools
  - Highlight the real API integration (National Weather Service)
  
- **Exercise 2:** Show the Temporal UI extensively - it's powerful for debugging! 🔍
  - Walk through execution history
  - Demonstrate the retry mechanism
  
- **Exercise 3:** THIS IS THE KEY 🌟
  - Show how activities make LLM calls durable
  - The agent code doesn't change - Temporal wraps it!
  - Emphasize: production-ready with zero agent modifications
  
- **Exercise 4:** Advanced - focus on the routing pattern and context passing 🤝
  - Multi-agent systems are orchestrated workflows
  - Each agent is specialized for specific tasks

## 📝 License

MIT License - feel free to use this workshop material for educational purposes! 🎓

## 🤝 Contributing

Found a bug or have a suggestion? Please open an issue or submit a pull request! We welcome contributions to make this workshop even better! 🌟

---

**Happy coding!** 🚀 Build amazing durable AI agents! 🤖✨
