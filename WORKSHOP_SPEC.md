# Temporal + OpenAI Agents SDK – 90-min Codespaces Workshop Repo Spec

## 🎯 Goal (Outcome, not Tasks)

Create a GitHub Codespaces-ready repository that teaches beginner→intermediate Python devs how to build **durable AI agents** using **OpenAI Agents SDK + Temporal** in **90 minutes**: 30 min instruction + 4×15 min exercises. Everything must run with **zero local setup**.

---

## 🚫 Non-Goals

- No secret keys in repo.
- No complex frameworks; keep code short, didactic, and runnable <60s after Codespace boots.
- No advanced agent orchestration beyond durability, retries, state, and tracing.

---

## 🧰 Tech Stack

- Python 3.11
- `openai` (Agents SDK)
- `temporalio`
- `rich`, `typer`, `pytest`, `ruff`, `mypy`
- Temporal CLI (local dev server)
- GitHub Codespaces (devcontainer)
- Optional: Node only if required by Temporal Web

---

## 📁 Repository Structure

```
temporal-ai-agents-workshop/
├── exercises/
│   ├── 01_agent_hello_world/
│   ├── 02_temporal_hello_world/
│   └── 03_durable_agent/
├── solutions/
│   ├── 01_agent_hello_world/
│   ├── 02_temporal_hello_world/
│   └── 03_durable_agent/
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

## 🧩 Exercise Requirements

### **Exercise 1 – Agent Hello World**

- Minimal agent: model + system instructions + 1 tool.
- Include “handoff” stub (commented).
- Run with: `make exercise-1`

### **Exercise 2 – Temporal Hello World**

- 1 workflow + 1 activity in Python.
- Commands: `make temporal-up` → `make exercise-2`

### **Exercise 3 – Durable Agent**

- Wrap LLM/tool calls in **activities** with retries.
- Persist state via workflow; include a `trace_id`.
- Print Temporal UI URL and `trace_id` for correlation.
- Run with: `make exercise-3`

Each exercise includes its own README:

- Goal, Steps (≤5), Expected Output, Stretch Goal, Timebox (15 min).
- Mirror `/solutions/*` directories with concise, commented solutions.

---

## ⚙️ DevEx / Codespaces

- `devcontainer.json` installs Python 3.11 → calls `scripts/bootstrap.sh` post-create.
- `scripts/bootstrap.sh` installs deps, Temporal CLI, validates env (`OPENAI_API_KEY`).
- `scripts/run_temporal.sh` idempotent: if Temporal running, exit 0.
- **Makefile targets:**
  ```
  setup, env, lint, test, temporal-up, exercise-1, exercise-2, exercise-3
  ```

---

## 🔒 Security & Keys

- `.env.sample` with `OPENAI_API_KEY=`; code reads only from env.
- `check_env.py` fails fast with helpful error if missing key.
- Pre-commit hook guidance to avoid committing secrets.

---

## 🧪 CI (GitHub Actions)

- `ci.yml` runs on push/PR:
  - Python 3.11 → install deps → `ruff`, `mypy`, `pytest -q`
- Tests mock OpenAI calls so CI passes without a real key.

---

## ✅ Acceptance Criteria

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

## 🧾 Docs to Generate

- Root `README.md` with launch, agenda, setup, troubleshooting.
- Each exercise `README.md` (as above).
- “Instructor Notes” section at bottom of root README with timing and pitfalls.

---

## 🧠 Style & Teaching Rules

- Prioritize clarity over abstraction.
- Use linear, readable flow; verbose naming.
- Log start/end of activities, retries, and workflow resumptions.
- Comments explain _why_ (durability, retries, state).

---

## 📦 Deliverables

- Full repo above, runnable in Codespaces with all exercises, solutions, and CI passing.

---

## 🔁 Iteration Prompts (For Claude)

**Tighten code & retries:**

> Refactor `exercises/03_durable_agent/activities.py` to show explicit Temporal retry options and add logs before/after LLM calls. Keep under 40 lines.

**Observability polish:**

> In `03_durable_agent/workflow.py`, print the Temporal UI URL and the `trace_id`. Add comments explaining state persistence and correlation with OpenAI Traces.

**Bootstrap resilience:**

> Make `scripts/run_temporal.sh` idempotent: if Temporal running, print “Temporal already running” and exit 0.

**Docs clarity:**

> Write `/exercises/03_durable_agent/README.md`: Goal, Steps (≤5), Expected Output, Stretch Goal, Timebox (15 min). Include two screenshot placeholders.

**CI without real keys:**

> Add tests mocking OpenAI so `pytest -q` passes. Provide one test per exercise verifying expected return text.

---

## 🧭 Workshop Runbook (Slide Notes)

1. Launch Codespace (60s setup).
2. Walk through `make exercise-1` (Hello World Agent).
3. Explain workflows/activities → run `make exercise-2`.
4. Merge both → run `make exercise-3` (Durable Agent).
5. Show traces in Temporal UI + OpenAI console.
6. Summarize durability, retries, and state.
7. Wrap up and Q&A.
