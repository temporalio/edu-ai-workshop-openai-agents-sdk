# Workshop Issues and Confusions Report

**Date:** November 7, 2025  
**Objective:** Navigate the workshop as a student and identify problems or confusing portions

## Executive Summary

This report documents **17 distinct issues** found while navigating through the workshop from a student's perspective. Issues range from **critical blocking problems** (broken tests, confusing setup) to **polish items** (emoji compatibility, documentation gaps).

**Key Findings:**
- ✅ **Workshop structure is solid** - Good progression, clear TODOs, real-world examples
- ❌ **Test suite is completely broken** - Cannot run `make test` successfully
- ⚠️ **Temporal setup is confusing** - Two different methods mentioned without clarity
- 📝 **Documentation has gaps** - Missing durability demo, unclear handoff pattern, no UI guide
- 🔧 **Bootstrap script has outdated instructions** - References non-existent commands

**Impact Assessment:**
- **3 Critical issues** block workshop execution or validation
- **8 High/Medium issues** cause student confusion or missing features
- **6 Low priority issues** affect polish and professional presentation

Issues are categorized by severity and organized by exercise/component below.

## Critical Issues (Blocking Workshop Progress)

### 1. ❌ Test Suite Completely Broken

**Location:** `tests/test_exercise_*.py`  
**Severity:** CRITICAL  
**Impact:** CI/CD pipeline fails, instructors cannot validate workshop

**Problem:**
- All three test files have incorrect import paths
- Test file imports use non-existent module names that don't match directory structure
- Python syntax errors in imports (numbers in module names without proper escaping)

**Current State:**
```python
# test_exercise_01.py - WRONG PATH
from solutions.ex01_agent_hello_world.main import get_weather
# Expected: solutions/01_agent_hello_world/
# Actual: Only solution.ipynb exists (not a Python module)

# test_exercise_02.py - SYNTAX ERROR
from solutions.02_temporal_hello_world.activities import process_data
# Python sees "02" as decimal literal: 0.2_temporal_hello_world
# Module names cannot start with numbers

# test_exercise_03.py - SYNTAX ERROR  
from solutions.03_durable_agent.activities import get_weather
# Python sees "03" as decimal literal: 0.3_durable_agent
# Module names cannot start with numbers
```

**Error Output:**
```
ERROR tests/test_exercise_01.py - ModuleNotFoundError: No module named 'solutions.ex01_agent_hello_world'
ERROR tests/test_exercise_02.py - SyntaxError: invalid decimal literal
ERROR tests/test_exercise_03.py - SyntaxError: invalid decimal literal
```

**Student Impact:**
- Instructors cannot run `make test` to validate setup
- Students attempting to verify their solutions will get confusing errors
- Zero test coverage for the workshop exercises
- CI/CD pipeline fails, blocking automated validation

**Root Cause:**
The tests were written for a Python module structure that doesn't exist. Solutions are Jupyter notebooks (`.ipynb` files), but tests try to import from Python modules with classes/functions. This is a **fundamental architecture mismatch**.

**Correct Approaches:**
1. **Option A:** Extract code from notebooks and run as Python scripts
2. **Option B:** Use `nbconvert` to convert notebooks to Python, then import
3. **Option C:** Mock the expected behavior without importing actual code
4. **Option D:** Remove tests and rely on manual validation (not recommended)

**Fix Required:**
Choose and implement one of the approaches above. Most realistic: Use nbconvert or restructure solutions as both notebooks AND Python modules.

---

### 2. ⚠️ Temporal Server Setup Instructions Are Confusing

**Location:** Multiple locations (README, Exercise 2, 3, 4)  
**Severity:** HIGH  
**Impact:** Students may get stuck before starting exercises 2-4

**Problem:**
The workshop uses **two different methods** to start Temporal server, creating confusion:

**Method 1: `temporal_installation.ipynb` (RECOMMENDED in README)**
```markdown
# From README.md
4. Install and start Temporal server using the notebook 📓:
   - Open `temporal_installation.ipynb` in VS Code
   - Run each cell to install Temporal CLI and start dev server
```

**Method 2: `make temporal-up` (Mentioned in multiple places)**
```bash
# From Makefile and various exercise READMEs
make temporal-up
# Or manually: temporal server start-dev
```

**Confusion Points:**

1. **README emphasizes notebook approach** but Makefile and exercises mention `make temporal-up`
2. **Notebook approach is interactive** (stays in foreground, blocks the cell), but students need to run exercises afterward
3. **No clear guidance** on whether to:
   - Keep the notebook cell running in background?
   - Use `make temporal-up` after notebook installation?
   - Run notebook then restart server differently?

4. **Exercise READMEs have inconsistent instructions:**
   - Exercise 2: "make temporal-up"
   - Exercise 3: Suggests notebook in Prerequisites
   - Exercise 4: Shows both methods without clarifying which to use

**Student Confusion Scenarios:**

**Scenario A:** Student runs `temporal_installation.ipynb` cell
- Cell blocks (server runs in foreground)
- Student can't run other cells or code
- Unsure if they should interrupt it or open another terminal

**Scenario B:** Student follows Exercise 2 README
- Sees "make temporal-up" command
- Wonders why README said to use notebook
- May try to install Temporal CLI twice

**Scenario C:** Student uses `make temporal-up`
- Gets error "temporal: command not found"
- Realizes they need to run notebook first
- Confused about whether to keep notebook running

**Fix Required:**
- Standardize on ONE approach with clear instructions
- If using notebook for installation, provide clear next steps
- Explain background vs foreground execution
- Add troubleshooting for "already running" scenarios

---

### 3. ⚠️ Exercise 3 Has Confusing Structure Comments

**Location:** `exercises/03_durable_agent/exercise.ipynb`  
**Severity:** MEDIUM  
**Impact:** Students confused about exercise structure

**Problem:**
Exercise 3 introduces a "4-component pattern" but the notebook is self-contained:

```markdown
### Component Structure 📦

```bash
   make temporal-up
   # Or manually: temporal server start-dev
   ```
   Verify at: http://localhost:8233
```

**Issue:** This documentation fragment appears to be misplaced or incorrectly formatted. The component structure explanation is interrupted by code blocks about starting Temporal.

**Expected vs Actual:**
- **Expected:** Clear explanation of 4 components: activities, workflow, worker, starter
- **Actual:** Fragmented documentation with nested code blocks in wrong places
- **Student sees:** Confusing markdown that suggests running commands inside markdown headers

**Fix Required:**
- Fix markdown formatting in Exercise 3
- Clarify that notebook combines all 4 components for learning
- Explain Exercise 4 will show them separated into files

---

## High Priority Issues

### 4. 🔧 Lint Errors Throughout Codebase

**Location:** Multiple files  
**Severity:** MEDIUM  
**Impact:** `make lint` fails, may confuse students trying to validate code

**Problem:** Running `make lint` shows 132 errors including:

**Import Ordering Issues (I001):**
- Notebooks have unsorted imports
- Solution files have unsorted imports  
- Affects: `example-notebook/*`, `solutions/*`, `exercises/04_agent_routing/*`

**F-string Without Placeholders (F541):**
```python
# solutions/04_agent_routing/worker.py
print(f"🚀 Worker started successfully")  # Should be regular string
print(f"⏳ Polling for tasks... (Press Ctrl+C to stop)\n")  # Should be regular string
```

**Missing Newline at EOF (W292):**
```python
# solutions/04_agent_routing/workflow.py:111
return f"Response: {result.final_output}"
# No newline after this line
```

**Unused Imports (F401):**
```python
# tests/test_exercise_01.py
import pytest  # Imported but never used
```

**Student Impact:**
- Students running `make lint` see overwhelming error output
- Instructors cannot demonstrate clean code practices
- Uncertainty about what matters vs what doesn't

**Fix Required:**
- Run `ruff check . --fix` to auto-fix 115 errors
- Manually fix remaining syntax errors
- Add `.ruff.toml` config to ignore notebook-specific issues

---

### 5. 📝 Exercise 3 Has Duplicate Content in Markdown

**Location:** `exercises/03_durable_agent/exercise.ipynb`  
**Severity:** LOW  
**Impact:** Confusing for students reading through

**Problem:**
The notebook has inconsistent section ordering with duplicated concepts:

1. "What You'll Learn" section appears twice
2. "Prerequisites" section shows code blocks in wrong context
3. "Flow Diagram" explanation comes before actual setup
4. Markdown formatting errors (nested code blocks inside headers)

**Example of Confusing Ordering:**
```markdown
## Prerequisites
Before starting, ensure you have:
1. **Temporal Server Running:**
### Flow Diagram 🔄
```

This creates nested headers and unclear flow.

**Fix Required:**
- Reorganize notebook sections logically
- Remove duplicate content
- Ensure one clear learning path

---

### 6. 🔄 Exercise 4 Handoff Pattern May Be Unclear

**Location:** `exercises/04_agent_routing/`  
**Severity:** MEDIUM  
**Impact:** Students may not understand how handoffs work

**Problem:**
While the README explains handoffs, there's no clear example or diagram showing:

1. **When handoff happens** - Does triage agent immediately hand off?
2. **What triggers handoff** - Language detection? Explicit tool call?
3. **How result returns** - Does it come from specialist agent directly?
4. **What triage sees** - Does triage get the specialist's response?

**Current Documentation:**
```markdown
### Handoff Pattern
Enable agent handoffs with the `handoffs` parameter:
```python
Agent(
    name="Triage Agent",
    handoffs=[agent1(), agent2(), agent3()],
    ...
)
```

**What's Missing:**
- Code example showing actual handoff in action
- Diagram showing message flow through handoff
- Explanation of OpenAI's handoff mechanism
- How Runner.run() handles handoffs internally

**Student Questions (Anticipated):**
- "Does the triage agent return its own response or the specialist's?"
- "Can the specialist hand back to triage?"
- "How does the workflow know which agent ran?"
- "What if no handoff is needed?"

**Fix Required:**
- Add detailed handoff flow diagram
- Include code example with comments explaining handoff
- Document expected vs actual behavior
- Add troubleshooting for handoff issues

---

## Medium Priority Issues

### 7. 📦 Missing Exercise 4 Test Coverage

**Location:** `tests/` directory  
**Severity:** MEDIUM  
**Impact:** No validation for Exercise 4 implementations

**Problem:**
Tests exist for Exercises 1-3 (though broken), but no tests for Exercise 4.

**Current State:**
```
tests/
├── test_exercise_01.py  ✅ (exists, broken imports)
├── test_exercise_02.py  ✅ (exists, broken imports)  
├── test_exercise_03.py  ✅ (exists, broken imports)
└── test_exercise_04.py  ❌ (MISSING)
```

**What Should Be Tested:**
- Agent creation functions (french_agent, spanish_agent, etc.)
- Triage agent has correct handoffs configuration
- Workflow execution with mocked OpenAI responses
- Language routing logic
- Worker and starter basic imports/structure

**Student Impact:**
- No automated way to verify Exercise 4 solution
- Instructors cannot validate student work programmatically
- Inconsistent test coverage across exercises

**Fix Required:**
- Create `tests/test_exercise_04.py`
- Mock OpenAI Agents SDK responses
- Test agent configurations
- Test workflow execution flow

---

### 8. 🔑 Environment Variable Checking is Inconsistent

**Location:** Various exercise files  
**Severity:** LOW-MEDIUM  
**Impact:** Students may not realize they need API key until mid-exercise

**Problem:**

**Exercise 1 (Good):** Checks API key early with clear error
```python
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not set. Add it to your .env file.")
```

**Exercise 3 (Missing):** No API key check in notebook
- Students won't know they need key until OpenAI call fails
- Error message will be OpenAI SDK error, not helpful workshop error

**Exercise 4 (Missing):** No API key check in any file
- starter.py, worker.py, workflow.py all assume API key exists
- First error happens deep in OpenAI execution

**Fix Required:**
- Add API key validation to Exercise 3 notebook
- Add API key validation to Exercise 4 starter.py
- Provide consistent, helpful error messages
- Reference `make env` command in error messages

---

### 9. 📋 Exercise 2 Missing Explicit UnsandboxedWorkflowRunner

**Location:** `exercises/02_temporal_hello_world/exercise.ipynb`  
**Severity:** MEDIUM  
**Impact:** May cause sandbox errors when running in notebooks

**Problem:**

According to custom instructions:
> When running Temporal workers inside notebooks, always pass `workflow_runner=UnsandboxedWorkflowRunner()` and `debug_mode=True`

**Exercise 2 Current Code:**
```python
async with Worker(
    client,
    task_queue=task_queue,
    workflows=[HelloWorkflow],
    activities=[process_data],
):
```

**Missing:**
```python
from temporalio.worker import UnsandboxedWorkflowRunner

async with Worker(
    client,
    task_queue=task_queue,
    workflows=[HelloWorkflow],
    activities=[process_data],
    workflow_runner=UnsandboxedWorkflowRunner(),  # MISSING
):
```

**Student Impact:**
- May get cryptic sandbox errors in Jupyter
- Error: "Workflow does not have __file__ attribute"
- Students won't know this is a notebook-specific issue

**Fix Required:**
- Add UnsandboxedWorkflowRunner import and usage to Exercise 2
- Add explanatory comment about notebook requirements
- Verify Exercise 3 has this (needs checking)

---

### 10. 🌐 National Weather Service API May Be Unreliable

**Location:** Exercise 1 and 3  
**Severity:** LOW-MEDIUM  
**Impact:** Students may get API failures unrelated to their code

**Problem:**
Exercises use real NWS API: `https://api.weather.gov/alerts/active/area/{state}`

**Potential Issues:**
1. **API Rate Limiting:** Class of 30 students hitting API simultaneously
2. **API Downtime:** Government APIs can be unavailable
3. **Geographic Restrictions:** May not work from all regions/countries
4. **No HTTPS cert validation:** Students behind corporate firewalls may have issues

**Example Failure Scenario:**
```
Student runs exercise → API is down → Gets 503 error → Thinks their code is broken
```

**Better Approach:**
- Use mock API responses by default
- Provide optional "real API" mode
- Include fallback mock data
- Document API limitations

**Fix Required:**
- Add try/except with fallback mock data
- Document API limitations in troubleshooting
- Consider using httpx mocking for exercises
- Provide alternative APIs or mock server

---

## Low Priority Issues (Polish)

### 11. 📝 README Has Inconsistent Command Examples

**Location:** README.md  
**Severity:** LOW  
**Impact:** Minor confusion

**Problem:**
Command examples show both approaches without clarifying:

```markdown
# ⚡ Temporal server
# Use temporal_installation.ipynb notebook...

# 📓 Working with exercises  
# Exercises 1-3 are Jupyter notebooks:
```

Some sections use "Run notebook", others show bash commands. Not always clear when to use notebook vs terminal.

**Fix Required:**
- Standardize command examples
- Make terminal vs notebook distinction clearer
- Use consistent formatting

---

### 12. ⏱️ Activity Timeout Comments Inconsistent

**Location:** Exercise 3 and 4  
**Severity:** LOW  
**Impact:** Students may copy inconsistent patterns

**Problem:**
Different timeouts used without explanation:

**Exercise 3:**
```python
ModelActivityParameters(
    start_to_close_timeout=timedelta(seconds=30)
)
```

**Exercise 4 TODOs suggest:**
```python
ModelActivityParameters(
    start_to_close_timeout=timedelta(seconds=30)
)
```

But no explanation of:
- Why 30 seconds?
- What happens if exceeded?
- How to adjust for slower APIs?
- Default if not specified?

**Fix Required:**
- Add comments explaining timeout choice
- Document what happens on timeout
- Add to troubleshooting section

---

### 13. 🎨 Emoji Usage May Cause Display Issues

**Location:** All files  
**Severity:** LOW  
**Impact:** May not display correctly in some terminals/editors

**Problem:**
Heavy emoji usage throughout (🚀, 🤖, ✅, ❌, etc.)

**Potential Issues:**
- SSH sessions without UTF-8 support
- Windows terminals without Unicode
- Screen readers for accessibility
- Copy/paste into some environments

**Example:**
```python
print("🚀 Starting workflow...")  # May show as "?? Starting workflow..." 
```

**Fix Required:**
- Consider providing emoji-free alternative outputs
- Document UTF-8 terminal requirement
- Or reduce emoji reliance in critical messages

---

## Documentation Gaps

### 14. 📖 Missing: What Makes Exercise 3 "Durable"?

**Location:** Exercise 3 documentation  
**Severity:** MEDIUM  
**Impact:** Students may not understand core concept

**Problem:**
Exercise 3 is titled "Durable Agent" but doesn't clearly demonstrate durability.

**What's Missing:**
1. **No failure demonstration** - Exercise doesn't show what happens when things fail
2. **No retry examples** - Doesn't show Temporal retrying failed activities
3. **No crash recovery demo** - Doesn't show resuming from checkpoint
4. **No before/after comparison** - Doesn't contrast with Exercise 1's non-durable version

**Documentation Says:**
```markdown
### Testing Durability (Optional):
If you disconnect your network **while the workflow is executing**...
```

But this is:
- Marked "optional"
- Not part of main exercise flow
- Difficult to test in Codespaces
- Not demonstrated in solution

**Fix Required:**
- Add explicit durability demonstration
- Include simulated failure in activity code
- Show Temporal UI retry timeline
- Compare Exercise 1 (fails) vs Exercise 3 (retries)
- Make durability demonstration required, not optional

---

### 15. 🔍 Missing: Temporal UI Navigation Guide

**Location:** Exercises 2, 3, 4  
**Severity:** LOW-MEDIUM  
**Impact:** Students don't know what to look for in UI

**Problem:**
Exercises link to Temporal UI but don't explain:
- What to look for
- Where to find execution history
- How to interpret timeline
- Where retry attempts show up
- How to debug failures

**Current:**
```python
print(f"🔗 View in Temporal UI: http://localhost:8233/namespaces/default/workflows/{workflow_id}")
```

**What Students Need:**
- Screenshot of what they should see
- Guided tour of UI elements
- What "good" looks like vs "error" state
- How to find worker logs
- How to see activity retries

**Fix Required:**
- Add "Temporal UI Guide" section to README
- Include screenshots of key UI views
- Add numbered steps for UI exploration
- Link to official Temporal UI docs

---

### 16. ⚠️ Bootstrap Script References Non-Existent Commands

**Location:** `scripts/bootstrap.sh`  
**Severity:** LOW  
**Impact:** Students following bootstrap instructions get confused

**Problem:**
The bootstrap completion message references a command that doesn't exist:

```bash
echo "Next steps:"
echo "  3. Run 'make exercise-1' to start the workshop"
```

**Issue:** `make exercise-1` doesn't exist in the Makefile. No exercise shortcuts are defined.

**Student Impact:**
- Copy/paste `make exercise-1` → Error: "No rule to make target 'exercise-1'"
- Confusion about how to actually start exercises
- No clear guidance on opening notebooks

**Fix Required:**
- Remove reference to non-existent command
- Replace with: "Open exercises/01_agent_hello_world/exercise.ipynb in VS Code"

---

### 17. 🔄 Temporal Installation Notebook Has UX Issues

**Location:** `temporal_installation.ipynb`  
**Severity:** MEDIUM  
**Impact:** Students unclear how to use the installation notebook

**Problem:**
The notebook's second cell starts Temporal server but provides no guidance:

```python
!~/.temporalio/bin/temporal server start-dev
```

**Issues:**
1. **Cell blocks indefinitely** - Server runs in foreground, never completes
2. **No explanation** - Students don't know this is expected
3. **No guidance** - Unclear whether to keep running or restart elsewhere

**Student Confusion:**
- "Why is this cell still running?"
- "Should I interrupt it?"
- "How do I run exercises if this is blocking?"

**Fix Required:**
Add explanatory markdown cell before the server cell explaining:
- Cell will block (expected behavior)
- Leave notebook open with server running
- Open exercises in new tabs
- How to stop server when done

---

## Positive Observations

### ✅ What Works Well

1. **Exercise Progression is Logical** - 1→2→3→4 builds knowledge incrementally
2. **TODOs are Clear** - Students know exactly what to implement
3. **Solution Notebooks Provided** - Good reference for stuck students
4. **Makefile Simplifies Commands** - `make setup`, `make env`, etc. are helpful
5. **Real-World APIs** - NWS API makes Exercise 1 interesting and practical
6. **Multi-Language Routing** - Exercise 4 showcases compelling use case
7. **Production Pattern** - Exercise 4 separating files teaches real-world structure

---

## Recommendations Summary

### Immediate Fixes (Before Next Workshop)

1. **Fix test imports** - Restructure tests to work with notebook/directory structure
2. **Standardize Temporal startup** - Pick one method, document clearly
3. **Add UnsandboxedWorkflowRunner** - To Exercise 2 and verify Exercise 3
4. **Fix Exercise 3 markdown** - Clean up formatting, remove duplicates
5. **Run lint auto-fixes** - Clean up 115 auto-fixable errors

### Important Improvements (Next Sprint)

6. **Add Exercise 4 tests** - Provide validation coverage
7. **Add API key checks** - To all exercises that need them
8. **Document handoff pattern** - With diagrams and examples
9. **Add durability demonstration** - Make Exercise 3 actually show durability
10. **Create Temporal UI guide** - Help students navigate and understand

### Nice-to-Have Enhancements

11. **Mock API fallbacks** - For NWS API reliability
12. **Add timeout explanations** - Document activity timeout choices
13. **Standardize command examples** - README consistency improvements
14. **Consider emoji alternatives** - For accessibility/compatibility
15. **Fix bootstrap script** - Remove reference to non-existent `make exercise-1`
16. **Improve temporal_installation.ipynb UX** - Add explanations for blocking behavior

---

## Testing Methodology

This report was generated by:

1. ✅ Running `make setup` - Verified dependency installation
2. ✅ Running `make test` - Identified broken test suite
3. ✅ Running `make lint` - Found 132 lint errors
4. ✅ Reading all exercise notebooks - Identified structure/content issues
5. ✅ Reviewing Exercise 4 files - Found missing tests and documentation gaps
6. ✅ Checking README consistency - Found multiple instruction approaches
7. ✅ Analyzing custom instructions - Cross-referenced with actual implementation

**Environment:**
- Platform: GitHub Codespaces / Linux
- Python: 3.12.3
- Workshop Version: 1.0.0

---

## Conclusion

The workshop has a **solid foundation** with good exercise progression and clear learning objectives. However, several **critical issues** prevent smooth execution:

- **Broken tests** block validation
- **Unclear Temporal setup** creates confusion
- **Missing durability demonstration** undermines key concept
- **Inconsistent patterns** across exercises

Addressing the **Immediate Fixes** will make the workshop usable. The **Important Improvements** will make it excellent.

**Priority Order:** Fix tests → Clarify Temporal setup → Demonstrate durability → Add missing tests → Polish documentation
