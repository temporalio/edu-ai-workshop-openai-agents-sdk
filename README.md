<div align="center">

![Workshop Hero Banner](images/hero-banner.svg)

</div>

---

Learn to build **durable AI agents** using **OpenAI Agents SDK + Temporal** in this hands-on 90-minute workshop. Everything runs in GitHub Codespaces with zero local setup required.

## What You'll Build

<div align="center">

### Master Durable AI Agents

</div>

By the end of this workshop, you'll understand how to:

- **Create AI agents** with tool calling using OpenAI's Agents SDK
- **Build durable workflows** with Temporal for reliability and retries
- **Combine both** to create production-ready AI agents that survive failures
- **Implement multi-agent systems** with handoff patterns
- **Observe and debug** agent execution using Temporal UI

## Prerequisites

<div align="center">

**What You Need to Bring**

</div>

- **Basic Python knowledge** - If you can write a function, you're ready!
- **OpenAI API key** - [Get one here](https://platform.openai.com/api-keys) (free tier works!)
- **GitHub account** - For Codespaces 

## Quick Start

<div align="center">

### Ready, Set, Code!

*Get started in minutes!*

</div>

### GitHub Codespaces (Recommended)

<table>
<tr>
<td width="50px">1.</td>
<td>Open in GitHub Codespaces</td>
</tr>
<tr>
<td>2.</td>
<td>Wait 2-3 minutes for the environment to set up</td>
</tr>
<tr>
<td>3.</td>
<td>Add your OpenAI API key to <code>.env</code>:
   <pre># The .env file is already created during setup
# Edit .env and add your OPENAI_API_KEY</pre>
</td>
</tr>
<tr>
<td>4.</td>
<td>Install and start Temporal server using the notebook:
   <ul>
   <li>Open <code>temporal_installation.ipynb</code> in VS Code</li>
   <li>Run each cell to:
     <ul>
       <li>Install the Temporal CLI</li>
       <li>Start the Temporal dev server</li>
     </ul>
   </li>
   <li><strong>Verify In Codespaces:</strong> Go to the <strong>Ports</strong> tab at the bottom of VS Code → Find port <strong>8233</strong> → Click the <strong>Globe icon</strong> to open the Temporal Web UI</li>
   </ul>
</td>
</tr>
<tr>
<td>5.</td>
<td><strong>You're ready to start the workshop!</strong>
<br><br>
<strong>Workshop Flow:</strong> During the session, you'll explore and run the complete implementations in <code>solutions/</code>. After the workshop, practice building everything yourself using <code>exercises/</code> as homework! Make your changes to the code in the <code>exercises/</code> subdirectories. If you need a hint or want to verify your changes, look at the complete version in the corresponding <code>solutions/</code> subdirectory.
</td>
</tr>
</table>

> **Note:** All workshop instructions use the `temporal_installation.ipynb` notebook for Temporal setup. This ensures a consistent, reliable experience across all environments!

## Workshop Structure

<div align="center">

### 90 Minutes to Mastery

*30 min instruction + 4×15 min hands-on exercises*

**Progress Bar**: `[░░░░░░░░░░] 0%` → `[██████████] 100%`

</div>

**Exercises 1-3** are **Jupyter notebooks** for interactive learning.  
**Exercise 4** uses **separate Python files** to demonstrate production-ready Temporal applications!

**During the workshop**: You'll explore and run the complete implementations in the `solutions/` directory. These are fully working examples that demonstrate production patterns. Learn by running the code, seeing the output, and understanding how everything works together.

**After the workshop**: Practice building everything from scratch using the `exercises/` directory as optional homework! The exercises provide starter code with TODO markers to guide you.

### Repository Navigation

```
temporal-openai-agents-sdk/
├── solutions/                    # Work here during the workshop
│   ├── 01_agent_hello_world/       # Workshop Exercise 1 - OpenAI agent basics (.ipynb)
│   ├── 02_temporal_hello_world/    # Workshop Exercise 2 - Temporal fundamentals (.ipynb)
│   ├── 03_durable_agent/           # Workshop Exercise 3 - Combine both! (.ipynb)
│   └── 04_agent_routing/           # Workshop Exercise 4 - Routing workflow (.py files)
│
├── exercises/                    # Extra homework exercises (optional)
│   ├── 01_agent_hello_world/       # Homework: Build your own agent (.ipynb)
│   ├── 02_temporal_hello_world/    # Homework: Practice workflows (.ipynb)
│   ├── 03_durable_agent/           # Homework: Create durable agent (.ipynb)
│   └── 04_agent_routing/           # Homework: Implement routing (.py files)
│
├── scripts/                     # Helper scripts (bootstrap, env checks)
├── Makefile                     # Common commands (setup, lint, test)
├── WORKSHOP_SPEC.md             # Workshop design specification
└── README.md                    # You are here!
```

## Workshop Exercises

<div align="center">

### Your Learning Journey

*From zero to hero in four exercises!*

</div>

**During the workshop**, you'll explore and run the complete implementations in the `solutions/` directory. These are fully working examples that you'll execute, observe, and learn from—see how production-ready AI agents work in practice. 

**After the workshop**, you can practice building them yourself using the `exercises/` directory as homework! Make your changes to the code in the `exercises/` subdirectories. If you need a hint or want to verify your changes, look at the complete version in the corresponding `solutions/` subdirectory.

---

### Exercise 1: Agent Hello World

<div align="center">

**Your First AI Agent**

*Build it, run it, watch it think!*

</div>

**Goal:** Create a simple AI agent with tool calling using real weather data

**What you'll learn:**
- Build your first OpenAI agent with a weather tool
- Understand the agent → tool → response flow
- See how LLMs decide when to use tools
- Call real APIs (National Weather Service)

**Time:** 15 minutes

**[Workshop Notebook](solutions/01_agent_hello_world/solution.ipynb)** | **[Homework: Build Your Own](exercises/01_agent_hello_world/exercise.ipynb)**

> **Challenge**: Can your agent handle weather queries for multiple cities at once?

---

### Exercise 2: Temporal Hello World

<div align="center">

**Meet Your Reliability Superhero**

*Workflows that never give up!*

</div>

**Goal:** Understand Temporal workflows and activities

**What you'll learn:**
- Create your first Temporal workflow
- Learn about activities as units of work
- Observe execution in the Temporal UI
- Experience automatic retries

**Time:** 15 minutes

**[Workshop Notebook](solutions/02_temporal_hello_world/solution.ipynb)** | **[Homework: Build Your Own](exercises/02_temporal_hello_world/exercise.ipynb)**

> **Pro Tip**: The Temporal UI is your best friend for debugging—explore it thoroughly!

---

### Exercise 3: Durable Agent

<div align="center">

**THE KEY ACTIVITY**

*Where AI meets unbreakable reliability!*

</div>

**Goal:** Combine agents + Temporal for production durability

**What you'll learn:**
- Wrap LLM calls in Temporal activities
- Get automatic retries on failures
- Persist agent state across crashes
- Add observability with trace IDs
- Build production-ready AI agents

**🎯 This is the KEY exercise!** Everything comes together here!

**Time:** 15 minutes

**[Workshop Notebook](solutions/03_durable_agent/solution.ipynb)** | **[Homework: Build Your Own](exercises/03_durable_agent/exercise.ipynb)**

> **Mind Blown Moment**: Your agent code doesn't change—Temporal just wraps it with superpowers!

---

### Exercise 4: Routing Workflow

<div align="center">

**Build a Polyglot Agent Team**

*French, Spanish, English—your agents speak them all!*

</div>

**Goal:** Build a routing workflow with language-specific agents using production-ready file structure

**What you'll learn:**
- Implement agent routing/triage patterns with OpenAI Agents SDK
- Create specialized language agents (French, Spanish, English)
- Use handoff patterns for agent-to-agent transitions
- Structure real Temporal applications (workflow, worker, starter files)
- Run production-style workflows with separate worker processes

**Time:** 15 minutes

**[Workshop Files](solutions/04_agent_routing/)** | **[Homework: Build Your Own](exercises/04_agent_routing/)**

> **Next Level**: This is how real production systems are structured!

## Common Commands

<div align="center">

### Your Command Toolbox

*Everything you need, one command away!*

</div>

```bash
# Setup and validation
make setup          # Install all dependencies
make env            # Check environment variables (OPENAI_API_KEY)

# Code quality
make lint           # Run code linters (ruff, mypy)
make test           # Run test suite (mocked - no API key needed!)

# Temporal server
# Use temporal_installation.ipynb notebook to install and start Temporal:
#   1. Open temporal_installation.ipynb in VS Code
#   2. Run each cell to install Temporal CLI and start dev server
#   3. Verify In Codespaces: Go to the **Ports** tab → Find port **8233** → Click the **Globe icon**

# Working with the workshop
# During the workshop, work through solutions/ notebooks:
#   solutions/01_agent_hello_world/solution.ipynb
#   solutions/02_temporal_hello_world/solution.ipynb
#   solutions/03_durable_agent/solution.ipynb
#
# Exercise 4 uses separate Python files (production pattern):
#   cd solutions/04_agent_routing
#   python worker.py    # Terminal 1
#   python starter.py   # Terminal 2
#
# After the workshop, practice building your own in exercises/:
#   exercises/01_agent_hello_world/exercise.ipynb
#   exercises/02_temporal_hello_world/exercise.ipynb
#   exercises/03_durable_agent/exercise.ipynb
#   exercises/04_agent_routing/  # Python files (workflow.py, worker.py, starter.py)
```

> **Pro Tip**: Run `make setup` first thing, every time!

## Key Concepts

<div align="center">

### The "Aha!" Moments

*Understanding the magic behind durable agents*

</div>

### Why Temporal for AI Agents?

<table>
<tr>
<td width="200px">

**The Problem**

</td>
<td>

AI agents in production face several challenges:

1. **API Failures**: LLM APIs can be rate-limited or temporarily unavailable
2. **Crashes**: Your agent process might crash mid-execution
3. **Long-Running Ops**: Multi-step agent flows need to resume from checkpoints
4. **Observability**: You need to debug what your agent actually did

</td>
</tr>
<tr>
<td>

**The Solution**

</td>
<td>

Temporal solves these by providing:

- **Automatic retries** with configurable policies
- **State persistence** across failures and restarts
- **Execution history** for debugging and auditing
- **Durable execution** that survives crashes

</td>
</tr>
</table>

> **Think of Temporal as**: A time machine + a guardian angel for your code!

### Architecture Pattern

```
       User Query
           ↓
   ┌───────────────────────────┐
   │ Temporal Workflow         │  Orchestration Layer
   │ (orchestration layer)     │     (Your AI's brain)
   └───────────────────────────┘
           ↓
   ┌───────────────────────────┐
   │ Activity: Call LLM        │  AI Decision Making
   │    with tools             │
   └───────────────────────────┘
           ↓
      [If tool needed]
           ↓
   ┌───────────────────────────┐
   │ Activity: Execute tool    │  Take Action
   └───────────────────────────┘
           ↓
   ┌───────────────────────────┐
   │ Activity: Get final       │  Final Response
   │    LLM response           │
   └───────────────────────────┘
           ↓
       Return to user
```

**The Magic:** Each activity can retry independently, and the entire flow is durable!

> **Key Insight**: Your AI agent becomes unstoppable—it will complete its task even if the server crashes!

## Troubleshooting

<div align="center">

### Common Issues & Quick Fixes

*Don't panic—we've got you covered!*

</div>

---

### Environment Issues

<details>
<summary><strong>Problem: <code>OPENAI_API_KEY</code> not found</strong></summary>

```bash
# Check your .env file exists
ls -la .env

# Verify the key is set
python scripts/check_env.py
# Or run: make env
```

**Fix:** If `.env` doesn't exist, create it from `.env.sample` (`cp .env.sample .env`), then add your API key

> **Tip**: Don't commit your `.env` file! It's in `.gitignore` for a reason.

</details>

---

<details>
<summary><strong>Problem: Temporal server not running</strong></summary>

```bash
# Check if it's running
pgrep -f temporal
```

**Fix:** Use the `temporal_installation.ipynb` notebook to install and start Temporal:
1. Open `temporal_installation.ipynb` in VS Code
2. Run each cell to install Temporal CLI and start the dev server
3. **Verify In Codespaces:** Go to the **Ports** tab → Find port **8233** → Click the **Globe icon**

⚠️ The Temporal dev server must be running for exercises 2, 3, and 4! ⚡

</details>

---

### Exercise Issues

<details>
<summary><strong>Problem: Import errors when running exercises</strong></summary>

```bash
# Reinstall dependencies
make setup
# Or: pip install -e ".[dev]"
```

> **Tip**: Run `make setup` whenever you pull new changes!

</details>

---

<details>
<summary><strong>Problem: Notebook kernel not found</strong></summary>

```bash
# Install ipykernel
pip install ipykernel
python -m ipykernel install --user --name temporal-workshop
```

Then select the `temporal-workshop` kernel in your notebook!

</details>

---

<details>
<summary><strong>Problem: Can't access Temporal UI at localhost:8233</strong></summary>

**In Codespaces:** The port should be automatically forwarded. To access it:
1. Go to the **Ports** tab at the bottom of VS Code
2. Find port **8233** 
3. Click the **Globe icon** to open the Temporal Web UI in your browser
4. Make sure the port visibility is set to **Public** if you need to share it

**✅ Solution:** Make sure Temporal server is running using `temporal_installation.ipynb` and follow the Codespaces instructions above.

</details>

---

<details>
<summary><strong>Problem: Tests fail with "module not found"</strong></summary>

```bash
# Make sure you're in the project root and have installed in editable mode
cd /path/to/temporal-openai-agents-sdk
pip install -e ".[dev]"
```

</details>

---

> **Still stuck?** Open an issue on GitHub! We're here to help!

## Additional Resources

<div align="center">

### Continue Your Learning Journey

*Bookmark these for later!*

</div>

<table>
<tr>
<td>
<td><a href="https://docs.temporal.io/">Temporal Documentation</a> - Your complete guide to Temporal</td>
</tr>
<tr>
<td>
<td><a href="https://platform.openai.com/docs/api-reference">OpenAI API Reference</a> - Everything OpenAI</td>
</tr>
<tr>
<td>
<td><a href="https://platform.openai.com/docs/guides/function-calling">OpenAI Agents SDK</a> - Deep dive into function calling</td>
</tr>
<tr>
<td>
<td><a href="https://docs.temporal.io/dev-guide/python">Temporal Python SDK</a> - Python-specific docs</td>
</tr>
<tr>
<td>
<td><a href="https://docs.google.com/presentation/d/1ZKj-PUm8-swnwP7jQPyQNMs4NIBAuCuglU3iByWn4CM/edit?slide=id.g38cc80f1e1e_1_0#slide=id.g38cc80f1e1e_1_0">Workshop Slides</a> - Slide deck from the workshop</td>
</tr>
</table>

> **Recommended Next Steps**: 
> 1. Explore the [Temporal Samples repository](https://github.com/temporalio/samples-python)
> 2. Join the [Temporal Slack community](https://temporal.io/slack)
> 3. Build something awesome and share it!

## Instructor Notes

<div align="center">

### For Workshop Leaders

*Tips from the trenches!*

</div>

### Timing Breakdown

<table>
<tr>
<td width="150px"><strong>00:00-05:00</strong></td>
<td>Introduction & Setup verification</td>
</tr>
<tr>
<td><strong>05:00-15:00</strong></td>
<td>OpenAI Agents SDK Introduction (slides)</td>
</tr>
<tr>
<td><strong>15:00-30:00</strong></td>
<td>Walk through Exercise 1 solution notebook together + Q&A</td>
</tr>
<tr>
<td><strong>30:00-35:00</strong></td>
<td>Discussion & key takeaways from Exercise 1</td>
</tr>
<tr>
<td><strong>35:00-40:00</strong></td>
<td>Intro to Temporal (slides)</td>
</tr>
<tr>
<td><strong>40:00-55:00</strong></td>
<td>Walk through Exercise 2 solution notebook together + Q&A</td>
</tr>
<tr>
<td><strong>55:00-60:00</strong></td>
<td>Discussion & key takeaways from Exercise 2</td>
</tr>
<tr>
<td><strong>60:00-65:00</strong></td>
<td>OpenAI Agents SDK + Temporal (slides)</td>
</tr>
<tr>
<td><strong>65:00-80:00</strong></td>
<td>Walk through Exercise 3 solution notebook (THE KEY EXERCISE!)</td>
</tr>
<tr>
<td><strong>80:00-90:00</strong></td>
<td>🎉 Demo Exercise 4 (production patterns) + Wrap-up</td>
</tr>
</table>

### Common Pitfalls

<details>
<summary><strong>1. Students skip checking <code>.env</code></strong></summary>

- Do environment check before starting (`make env`)
- Emphasize that exercises 1, 3, 4 need API key
- Have backup keys ready for those who forget

</details>

<details>
<summary><strong>2. Temporal not running</strong></summary>

- Remind students to use `temporal_installation.ipynb` notebook to install and start Temporal
- Walk through opening the notebook and running each cell
- Show them how to verify In Codespaces: Go to the **Ports** tab → Find port **8233** → Click the **Globe icon**
- Verify EARLY before Exercise 2!

</details>

<details>
<summary><strong>3. Confusion between workshop and homework</strong></summary>

- Clearly explain: work through `solutions/` during the workshop, practice building your own in `exercises/` afterward
- Solution notebooks are complete implementations to learn from during the workshop
- Exercises are for independent practice after the workshop (optional homework)

</details>

<details>
<summary><strong>4. Temporal Activity timeouts</strong></summary>

- Explain `start_to_close_timeout` defaults
- Show how to adjust for longer-running operations
- Common when students use GPT-4 vs GPT-4-mini

</details>

<details>
<summary><strong>5. Notebook vs Python files</strong></summary>

- Exercises 1-3 are Jupyter notebooks (`.ipynb`) - work through `solutions/` during workshop
- Exercise 4 uses separate Python files (workflow.py, worker.py, starter.py)
- Emphasize Exercise 4 demonstrates production application structure
- After workshop, students can practice building their own using `exercises/` directory

</details>

### Key Teaching Points

<details>
<summary><strong>Exercise 1: Agent Foundations</strong> 🤖</summary>

- Walk through the complete solution notebook together
- Emphasize tool calling as the foundation of agentic behavior
- Show how the agent decides to use tools
- Highlight the real API integration (National Weather Service)
- **Demo tip**: Try queries that do and don't need tools

</details>

<details>
<summary><strong>Exercise 2: Temporal Magic</strong> 🌊</summary>

- Walk through the solution notebook as a group
- Show the Temporal UI extensively - it's powerful for debugging
- Walk through execution history
- Demonstrate the retry mechanism
- **Demo tip**: Kill the worker mid-execution and restart it!

</details>

<details>
<summary><strong>Exercise 3: THE KEY MOMENT</strong></summary>

- Guide students through the solution notebook
- Show how activities make LLM calls durable
- The agent code doesn't change - Temporal wraps it!
- Emphasize: production-ready with zero agent modifications
- **Demo tip**: Show the Temporal UI and OpenAI trace correlation

</details>

<details>
<summary><strong>Exercise 4: Production Patterns</strong> 🔀</summary>

- Walk through the production file structure together
- Language-based routing pattern (French/Spanish/English agents)
- Handoff pattern enables agent-to-agent transitions
- Demonstrates real Temporal application structure (separate worker/starter)
- Show how to run with two terminals (worker + starter)
- **Demo tip**: Show language detection in real-time

</details>

---

> **Golden Rule**: Keep energy high! These concepts are powerful and fun—your enthusiasm is contagious.

## License

MIT License - feel free to use this workshop material for educational purposes!

## Contributing

Found a bug or have a suggestion? Please open an issue or submit a pull request! We welcome contributions to make this workshop even better!

---

<div align="center">

### **Happy Coding!**

**Build amazing durable AI agents!**

---

Made with love by the Temporal Community

[Star us on GitHub](https://github.com/temporal-community/edu-ai-workshop-openai-agents-sdk) | [Follow Temporal](https://twitter.com/temporalio) | [Join Slack](https://temporal.io/slack)

---

### Ready to get started? Scroll back to [Quick Start](#-quick-start)!

</div>
