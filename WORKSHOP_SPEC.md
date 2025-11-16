# Temporal + OpenAI Agents SDK – 90-min Codespaces Workshop Repo Spec

<div align="center">

**The Master Blueprint**

*Everything you need to know about this workshop's architecture*

</div>

---

## Goal (Outcome, not Tasks)

<div align="center">

**Mission Statement**

</div>

Create a GitHub Codespaces-ready repository that teaches beginner→intermediate Python devs how to build **durable AI agents** using **OpenAI Agents SDK + Temporal** in **90 minutes**: 30 min instruction + 4×15 min hands-on activities. Everything must run with **zero local setup**.

**Workshop Approach**: Students work through complete, working implementations in the `solutions/` directory during the workshop, learning by exploring and running production-quality code. After the workshop, the `exercises/` directory provides optional homework for students to practice building everything from scratch.

> **Success Criteria**: A complete beginner can go from "What's Temporal?" to "I built a production-ready AI agent!" in one session by following along with working code!

---

## Non-Goals

<div align="center">

**What This Workshop Is NOT**

</div>

- No secret keys in repo (security first)
- No complex frameworks; keep code short, didactic, and runnable <60s after Codespace boots
- No advanced agent orchestration beyond durability, retries, state, and tracing
- Not a deep dive into ML/AI theory (this is practical engineering)

> **Focus**: Hands-on, practical, production-ready patterns only!

---

## Tech Stack

<div align="center">

**The Tools We Use**

*Batteries included!*

</div>

<table>
<tr>
<td width="150px"><strong>Core</strong></td>
<td>
• Python 3.11<br>
• <code>openai</code> (Agents SDK)<br>
• <code>temporalio</code>
</td>
</tr>
<tr>
<td><strong>Tooling</strong></td>
<td>
• <code>rich</code>, <code>typer</code><br>
• <code>pytest</code>, <code>ruff</code>, <code>mypy</code><br>
• Temporal CLI (local dev server)
</td>
</tr>
<tr>
<td><strong>Infrastructure</strong></td>
<td>
• GitHub Codespaces (devcontainer)<br>
• Optional: Node (if required by Temporal Web)
</td>
</tr>
</table>

> **Everything is pre-configured!** Just click and code!

---

## Repository Structure

```
temporal-ai-agents-workshop/
├── solutions/                       # Primary workshop materials
│   ├── 01_agent_hello_world/       # Complete working implementation
│   ├── 02_temporal_hello_world/    # Complete working implementation
│   ├── 03_durable_agent/           # Complete working implementation
│   └── 04_agent_routing/           # Complete working implementation
├── exercises/                       # Optional homework activities
│   ├── 01_agent_hello_world/       # Starter code for practice
│   ├── 02_temporal_hello_world/    # Starter code for practice
│   ├── 03_durable_agent/           # Starter code for practice
│   └── 04_agent_routing/           # Starter code for practice
├── slides/
├── scripts/
│   ├── bootstrap.sh
│   ├── run_temporal.sh
│   └── check_env.py
├── .devcontainer/
│   └── Dockerfile
├── devcontainer.json
├── pyproject.toml
├── Makefile
├── .env.sample
├── .gitignore
├── README.md
└── .github/workflows/ci.yml
```

---

## Architecture Patterns

<div align="center">

**The Learning Progression**

*From simple to sophisticated!*

</div>

The workshop teaches a progressive architecture pattern across exercises:

### **Exercise 1: Basic Agent Pattern**

```
       User Query
           ↓
   Agent (OpenAI LLM)
           ↓
     Tool Function
           ↓
     External API
           ↓
   Data returned to Agent
           ↓
   Agent uses LLM to generate response
           ↓
     Return to user
```

> **Learning Goal**: Understand how AI agents use tools

---

### **Exercise 2: Temporal Fundamentals**

```
   Workflow Request
           ↓
   Temporal Workflow
           ↓
   Temporal Activity
           ↓
        Result
```

> **Learning Goal**: Understand workflows, activities, and durability

---

### **Exercise 3: Durable Agent (Integration)**

```
       User Query
           ↓
   ┌───────────────────────────┐
   │ Temporal Workflow         │  Orchestration
   │ (orchestration layer)     │
   └───────────────────────────┘
           ↓
   ┌───────────────────────────┐
   │ Activity: Call LLM        │  AI Decision
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

**Key Insight:** Each activity can retry independently, and the entire flow is durable!

> **Learning Goal**: Combine AI agents with Temporal for production durability

---

## Activity Requirements

### **Activity 1 – Agent Hello World**

- Complete working implementation in `solutions/01_agent_hello_world/solution.ipynb`
- Starter code with TODOs in `exercises/01_agent_hello_world/exercise.ipynb`
- Minimal agent: model + system instructions + 1 tool
- Include "handoff" stub (commented)

### **Activity 2 – Temporal Hello World**

- Complete working implementation in `solutions/02_temporal_hello_world/solution.ipynb`
- Starter code with TODOs in `exercises/02_temporal_hello_world/exercise.ipynb`
- 1 workflow + 1 activity in Python

### **Activity 3 – Durable Agent**

- Complete working implementation in `solutions/03_durable_agent/solution.ipynb`
- Starter code with TODOs in `exercises/03_durable_agent/exercise.ipynb`
- Wrap LLM/tool calls in **activities** with retries
- Persist state via workflow; include a `trace_id`
- Print Temporal UI URL and `trace_id` for correlation

### **Activity 4 – Agent Routing**

- Complete working implementation in `solutions/04_agent_routing/` (workflow.py, worker.py, starter.py)
- Starter code with TODOs in `exercises/04_agent_routing/`
- Multi-agent routing with language detection
- Production file structure

Each directory includes its own README:

- Goal, Steps (≤5), Expected Output, Stretch Goal, Timebox (15 min)
- Solutions are complete, well-commented implementations for workshop use
- Exercises contain starter code with TODO markers for homework practice

---

## DevEx / Codespaces

- `devcontainer.json` installs Python 3.11 → calls `scripts/bootstrap.sh` post-create.
- `scripts/bootstrap.sh` installs deps, Temporal CLI, validates env (`OPENAI_API_KEY`).
- `scripts/run_temporal.sh` idempotent: if Temporal running, exit 0.
- Notebooks that host a Temporal worker **must** pass `workflow_runner=UnsandboxedWorkflowRunner()` and `debug_mode=True` to avoid sandbox validation errors inside Jupyter.
- **Makefile targets:**
  ```
  setup, env, lint, test, temporal-up, exercise-1, exercise-2, exercise-3
  ```

---

## Security & Keys

- `.env.sample` with `OPENAI_API_KEY=`; code reads only from env.
- `check_env.py` fails fast with helpful error if missing key.
- Pre-commit hook guidance to avoid committing secrets.

---

## CI (GitHub Actions)

- `ci.yml` runs on push/PR:
  - Python 3.11 → install deps → `ruff`, `mypy`, `pytest -q`
- Tests mock OpenAI calls so CI passes without a real key.

---

## Acceptance Criteria

- Codespace cold-start → `make exercise-1` in ≤90s.
- `make exercise-1/2/3` succeed on fresh Codespace (API key required for #1/#3).
- Temporal UI link and `trace_id` printed clearly.
- Each file ≤80 lines, well-commented.
- README includes:
  - Codespaces badge
  - Agenda
  - Setup & troubleshooting
  - “Where to look” in Temporal UI & OpenAI Traces

---

## Docs to Generate

- Root `README.md` with launch, agenda, setup, troubleshooting.
- Each exercise `README.md` (as above).
- “Instructor Notes” section at bottom of root README with timing and pitfalls.

---

## Style & Teaching Rules

- Prioritize clarity over abstraction.
- Use linear, readable flow; verbose naming.
- Log start/end of activities, retries, and workflow resumptions.
- Comments explain _why_ (durability, retries, state).
- Activities exposed from notebooks should be declared with `async def` (or supplied with an explicit `activity_executor`) so the Temporal worker does not raise synchronous activity errors.

---

## Deliverables

- Full repo above, runnable in Codespaces with all activities (solutions for workshop, exercises for homework), and CI passing.

---

## Iteration Prompts (For Claude)

**Tighten code & retries:**

> Refactor `solutions/03_durable_agent/solution.ipynb` to show explicit Temporal retry options and add logs before/after LLM calls. Ensure exercises/ has corresponding TODOs for students.

**Observability polish:**

> In `03_durable_agent/workflow.py`, print the Temporal UI URL and the `trace_id`. Add comments explaining state persistence and correlation with OpenAI Traces.

**Bootstrap resilience:**

> Make `scripts/run_temporal.sh` idempotent: if Temporal running, print “Temporal already running” and exit 0.

**Docs clarity:**

> Write `/solutions/03_durable_agent/README.md` and `/exercises/03_durable_agent/README.md`: Goal, Steps (≤5), Expected Output, Stretch Goal, Timebox (15 min). Include two screenshot placeholders.

**CI without real keys:**

> Add tests mocking OpenAI so `pytest -q` passes. Provide one test per exercise verifying expected return text.

---

## Workshop Runbook (Slide Notes)

1. Launch Codespace (60s setup).
2. Walk through `solutions/01_agent_hello_world/solution.ipynb` together (Hello World Agent).
3. Explain workflows/activities → explore `solutions/02_temporal_hello_world/solution.ipynb`.
4. Merge both → walk through `solutions/03_durable_agent/solution.ipynb` (Durable Agent - THE KEY ACTIVITY).
5. Demo `solutions/04_agent_routing/` production structure with multiple agents.
6. Show traces in Temporal UI + OpenAI console.
7. Summarize durability, retries, and state.
8. Remind students: practice building from scratch using `exercises/` directory as homework.
9. Wrap up and Q&A.
