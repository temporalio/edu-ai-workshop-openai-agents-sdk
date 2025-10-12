# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a 90-minute workshop repository teaching developers how to build **durable AI agents** using **OpenAI Agents SDK + Temporal**. The workshop is designed to run in GitHub Codespaces with zero local setup required.

**Target Audience:** Beginner-intermediate Python developers
**Workshop Format:** 30 minutes instruction + 4×15 minute exercises

## Tech Stack

- **Python 3.11** - Primary language
- **openai** - OpenAI Agents SDK for LLM-based agents
- **temporalio** - Workflow orchestration for durability and retries
- **Temporal CLI** - Local development server
- **Development tools:** `rich`, `typer`, `pytest`, `ruff`, `mypy`
- **Interactive environment:** Jupyter notebooks for hands-on exercises
- **Deployment:** GitHub Codespaces (devcontainer-based)

## Common Commands

### Setup & Environment

```bash
make setup          # Install dependencies and set up environment
make env            # Validate environment variables (OPENAI_API_KEY)
```

### Development

```bash
make lint           # Run ruff linter
make test           # Run pytest test suite
```

### Temporal Server

```bash
make temporal-up    # Start Temporal local dev server (idempotent)
```

### Exercises

```bash
make exercise-1     # Run Exercise 1: Agent Hello World
make exercise-2     # Run Exercise 2: Temporal Hello World
make exercise-3     # Run Exercise 3: Durable Agent
make exercise-4     # Run Exercise 4: Multi-Agent Handoff

# Or open Jupyter notebooks directly:
# exercises/01_agent_hello_world/exercise.ipynb
# exercises/02_temporal_hello_world/ (Python files - temporal workflows in notebooks coming)
# exercises/03_durable_agent/ (Python files)
# exercises/04_multi_agent_handoff/ (Python files)
```

## Repository Architecture

### Four-Exercise Progression

The workshop follows a progressive learning path:

1. **Exercise 1 - Agent Hello World** (`exercises/01_agent_hello_world/`)
   - Minimal OpenAI agent: model + system instructions + 1 tool
   - Demonstrates basic agent patterns
   - Available as Jupyter notebook (`exercise.ipynb`) and Python script
   - No Temporal integration yet

2. **Exercise 2 - Temporal Hello World** (`exercises/02_temporal_hello_world/`)
   - 1 workflow + 1 activity in Python
   - Introduces Temporal concepts without AI complexity
   - Shows durability and retry mechanisms

3. **Exercise 3 - Durable Agent** (`exercises/03_durable_agent/`)
   - **Core integration:** LLM/tool calls wrapped in Temporal activities
   - Workflow-based state persistence
   - Includes `trace_id` for observability correlation
   - Demonstrates retry logic and durability for AI operations

4. **Exercise 4 - Multi-Agent Handoff** (`exercises/04_multi_agent_handoff/`)
   - Advanced: Multiple specialized agents
   - Triage agent routes queries to specialists
   - Context maintained across agent handoffs
   - Workflow orchestration of agent-to-agent transitions

### Directory Structure

```
exercises/     # Starter code for workshop participants
solutions/     # Complete reference implementations
slides/        # Workshop presentation materials
scripts/       # Bootstrap, environment checks, Temporal startup
.devcontainer/ # Codespaces configuration
```

Each exercise directory contains:

- Exercise-specific Python files (activities.py, workflows.py, main.py)
- Jupyter notebooks for interactive learning (where applicable)
- `README.md` with: Goal, Steps (≤5), Expected Output, Stretch Goal, Timebox

**Note on Notebooks:** Exercise 1 includes both `.ipynb` (interactive) and `.py` (script) versions. Temporal workflows (Ex 2-4) use Python scripts since workflow execution requires the Temporal worker process running continuously.

## Key Architectural Patterns

### Durability Through Activities

In Exercise 3, LLM calls are wrapped in **Temporal activities** rather than called directly in workflows. This provides:

- Automatic retries on failure
- State persistence across crashes
- Replay-safe execution

### Observability Integration

The durable agent implementation connects two observability systems:

- **Temporal UI:** Shows workflow execution, retries, state
- **OpenAI Traces:** Shows LLM calls and tool usage
- **`trace_id`:** Correlation key printed to link both systems

### Teaching-First Code Style

All code follows these principles:

- **Clarity over abstraction:** Linear, readable flow
- **Verbose naming:** Self-documenting variable and function names
- **Instructional logging:** Log activity starts/ends, retries, workflow resumptions
- **Explanatory comments:** Focus on _why_ (durability, retries, state), not _what_
- **Length constraint:** Keep files ≤80 lines

## Environment & Secrets

### Required Environment Variables

- `OPENAI_API_KEY` - Required for exercises 1 and 3

### Security Model

- `.env.sample` provides template (never commit `.env`)
- `scripts/check_env.py` validates environment before exercises run
- Tests mock OpenAI calls so CI passes without real keys

## Testing Strategy

- Mock OpenAI responses to avoid requiring API keys in CI
- Each exercise has corresponding tests verifying expected behavior
- Tests should pass in CI without real credentials

## DevEx & Codespaces

### Bootstrap Flow

1. Codespaces creates container from `.devcontainer/`
2. Post-create: `scripts/bootstrap.sh` runs automatically
   - Installs Python dependencies
   - Installs Temporal CLI
   - Validates environment
3. Ready to run exercises in ≤90 seconds

### Idempotent Temporal Startup

`scripts/run_temporal.sh` checks if Temporal is already running. If yes, exits cleanly without error.

## Working with This Repository

### When Adding New Exercises

- Follow the 15-minute timebox constraint
- Include README with 5 or fewer steps
- Mirror in `/solutions/` with complete, commented implementation
- Keep code files under 80 lines

### When Modifying Existing Code

- Maintain teaching clarity - avoid clever abstractions
- Add logs for observable events (retries, state changes)
- Update corresponding solution if changing exercise starter code
- Ensure comments explain the "why" behind durability patterns

### When Debugging

- Check `make env` output for missing environment variables
- Verify Temporal is running: `make temporal-up`
- Exercise 3 prints Temporal UI URL and `trace_id` for correlation
- Look for activity retry logs in Temporal UI

## CI/CD

GitHub Actions workflow (`.github/workflows/ci.yml`):

- Runs on push/PR
- Tests on Python 3.11
- Executes: `ruff` → `mypy` → `pytest -q`
- Must pass without real OpenAI API key (mocked tests)
