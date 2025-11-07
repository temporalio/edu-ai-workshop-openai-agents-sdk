# Workshop Issues Report

This document contains a comprehensive list of issues, problems, and confusing portions discovered while navigating the workshop as a student.

**Report Date:** 2025-11-07  
**Tester Perspective:** First-time workshop student  
**Workshop Version:** Current main branch

---

## 🔴 Critical Issues (Blocking)

### Issue #1: Setup Command Fails Immediately ✅ FIXED

**Severity:** Critical - Prevents workshop start  
**Command:** `make setup`  
**Location:** `pyproject.toml`

**Problem:**
When running `make setup` as instructed in the Quick Start, the installation fails with a setuptools error:
```
error: Multiple top-level packages discovered in a flat-layout: ['images', 'solutions'].
```

**Root Cause:**
The `pyproject.toml` file is missing:
1. `[build-system]` section defining the build backend
2. `[tool.setuptools]` configuration to exclude non-package directories

**Impact:**
- Workshop cannot be started
- First instruction in Quick Start fails
- Students are immediately blocked

**Student Experience:**
"I followed the README instructions exactly, but the very first setup command failed. I don't know how to proceed."

**Fix Applied:**
Added build-system section and setuptools configuration to exclude non-package directories.

**Recommendation:**
Test `make setup` in a fresh environment to verify the fix works correctly.

---

### Issue #2: Missing Test Directory Referenced in CI

**Severity:** Critical - CI/CD broken  
**Location:** `.github/workflows/ci.yml` line 36  
**Command:** `pytest -v tests/`

**Problem:**
The CI configuration references a `tests/` directory that doesn't exist in the repository:
```yaml
- name: Run tests
  run: |
    pytest -v tests/
```

**Impact:**
- CI builds will fail on every PR
- Quality checks cannot run
- Contributors cannot validate their changes

**Student Experience:**
"I tried to run tests locally like the CI does, but the tests directory doesn't exist."

**Verification:**
```bash
$ find . -name "tests" -type d
find: 'tests': No such file or directory
```

**Recommendations:**
1. Create the `tests/` directory with mocked tests as mentioned in WORKSHOP_SPEC.md
2. OR update CI to skip tests if directory doesn't exist
3. OR remove test step from CI until tests are implemented

---

## 🟡 Major Issues (Confusing/Broken Features)

### Issue #3: Exercise 4 Instructions Don't Match Solution

**Severity:** Major - Students will get errors  
**Location:** `exercises/04_agent_routing/README.md` vs `solutions/04_agent_routing/workflow.py`

**Problem:**
The Exercise 4 README instructions tell students to use one API pattern, but the solution uses a different pattern:

**README Instructions (Step 2):**
```python
# 2. Execute the triage agent:
result = await Runner.run(triage_agent(), new_message)

# 3. Extract and return the final output:
return result.final_output
```

**Solution Code (workflow.py lines 90-111):**
```python
config = RunConfig()
with trace("Routing example"):
    inputs: list[TResponseInputItem] = [{"content": msg, "role": "user"}]
    result = await Runner.run(
        triage_agent(),
        input=inputs,
        run_config=config,
    )
    workflow.logger.info("Handoff completed")
    inputs = result.to_input_list()
    return f"Response: {result.final_output}"
```

**Key Differences:**
1. Solution uses `RunConfig()` - not mentioned in instructions
2. Solution uses named parameters (`input=`, `run_config=`)
3. Instructions use positional parameter (`new_message`)
4. Solution uses `trace()` context manager - not in instructions
5. Solution formats message as `TResponseInputItem` dict - instructions just use raw message
6. Solution calls `result.to_input_list()` - not in instructions
7. Solution prefixes return with "Response: " - not in instructions

**Impact:**
- Students following instructions will get different behavior than solution
- Code won't work as expected (wrong parameter types)
- Students will be confused when comparing their work to solution
- May cause runtime errors if API signature doesn't support both patterns

**Student Experience:**
"I followed the instructions exactly but my code doesn't work. When I looked at the solution, it's completely different from what the instructions said to do!"

**Recommendations:**
1. Update instructions to match solution code exactly
2. OR update solution to match instructions (simpler version)
3. Add explanation in instructions about why RunConfig and trace are used

---

### Issue #4: Conflicting Temporal Setup Instructions

**Severity:** Major - Confusing setup process  
**Locations:** Multiple files

**Problem:**
The repository provides multiple conflicting ways to start Temporal:

**README.md (line 32-41):**
```markdown
4. Install and start Temporal server using the notebook 📓:
   - Open `temporal_installation.ipynb` in VS Code
   - Run each cell to:
     - Install the Temporal CLI
     - Start the Temporal dev server
```

**README.md (line 151-156):**
```markdown
# ⚡ Temporal server
# Use temporal_installation.ipynb notebook to install and start Temporal:
#   1. Open temporal_installation.ipynb in VS Code
#   2. Run each cell to install Temporal CLI and start dev server
```

**Makefile (line 21-22):**
```makefile
temporal-up:
	@bash scripts/run_temporal.sh
```

**bootstrap.sh (line 37):**
```bash
echo "  2. Run 'make temporal-up' to start Temporal server"
```

**Observations:**
1. README strongly recommends using `temporal_installation.ipynb` notebook
2. Makefile provides `make temporal-up` using shell script
3. Bootstrap script tells users to use `make temporal-up`
4. No clear guidance on which method is preferred
5. Two different installation methods may cause conflicts

**Impact:**
- Students are confused about which method to use
- Some may install Temporal twice (once via notebook, once via make)
- Inconsistent setup across students
- Troubleshooting becomes harder

**Student Experience:**
"The README says to use a notebook to start Temporal, but the bootstrap script says to use `make temporal-up`. Which one should I use? What's the difference?"

**Recommendations:**
1. Choose ONE canonical method (recommend notebook for consistency)
2. Update all documentation to reference that method
3. Consider removing or deprecating the other method
4. Add a note explaining why that method was chosen

---

### Issue #5: Missing Makefile Targets Referenced in Documentation

**Severity:** Major - Broken instructions  
**Location:** `scripts/bootstrap.sh` line 38

**Problem:**
The bootstrap script references Makefile targets that don't exist:

**bootstrap.sh:**
```bash
echo "  3. Run 'make exercise-1' to start the workshop"
```

**Makefile:**
```makefile
# Makefile only has: setup, env, lint, test, temporal-up, temporal-down, clean
# NO exercise-1, exercise-2, exercise-3, or exercise-4 targets
```

**README.md (line 28-34) also says:**
```markdown
# Note: Exercises 1-3 are Jupyter notebooks (.ipynb files)
# Exercise 4 uses separate Python files (production pattern)
# Open them in VS Code or Jupyter Lab:
```

**Impact:**
- Students try to run `make exercise-1` and get error: "make: *** No rule to make target 'exercise-1'"
- Bootstrap guidance is incorrect
- Confusion about how to actually run exercises

**Student Experience:**
"The setup script told me to run `make exercise-1`, but that command doesn't exist. How do I start the exercises?"

**Actual Workflow:**
Exercises are Jupyter notebooks that should be opened in VS Code or Jupyter Lab, not run via Makefile.

**Recommendations:**
1. Remove `make exercise-*` references from bootstrap.sh
2. Update bootstrap.sh to say: "Open exercises/01_agent_hello_world/exercise.ipynb in VS Code"
3. OR add Makefile targets that open the notebooks (e.g., `code exercises/01_agent_hello_world/exercise.ipynb`)
4. Update README to be clearer about the workflow

---

## 🟢 Minor Issues (Polish/Improvements)

### Issue #6: Inconsistent "Exercise 4" Messaging

**Severity:** Minor - Clarity issue  
**Location:** Multiple files

**Problem:**
Exercise 4 is described inconsistently across documentation:

**README.md Timing Section (line 311):**
```markdown
- **80:00-90:00** 🎉 Exercise 4 (Optional) + Wrap-up
```
→ Labeled as "Optional"

**README.md Exercise 4 Section (line 125-138):**
```markdown
### Exercise 4: Routing Workflow 🔀
**Goal:** Build a routing workflow with language-specific agents using production-ready file structure
**What you'll learn:**
- 🎯 Implement agent routing/triage patterns with OpenAI Agents SDK
[...full exercise description with no "optional" mention...]
**Time:** 15 minutes ⏱️
```
→ Presented as regular exercise

**Impact:**
- Instructors may be unsure if Exercise 4 should be covered
- Students don't know if they should skip it
- Time management confusion (is it 15 min or can we skip?)

**Recommendations:**
1. If Exercise 4 is optional, mark it clearly in all locations
2. If Exercise 4 is required, remove "Optional" from timing
3. Add guidance: "Optional if running short on time" or "Recommended for advanced students"

---

### Issue #7: Temporal Installation Cell Behavior Unclear

**Severity:** Minor - User experience  
**Location:** `temporal_installation.ipynb` Cell 4

**Problem:**
The notebook cell that starts Temporal uses `!~/.temporalio/bin/temporal server start-dev` which:

**Cell Instructions:**
```markdown
**Important:** 
- This cell will keep running (showing server logs) - this is normal! ✅
- Do not stop this cell - the server needs to stay running
```

**Technical Reality:**
When running `!command` in Jupyter:
- The cell blocks until command completes
- User cannot run other cells in the same notebook
- Server logs fill the output area continuously
- Stopping the cell stops the server

**Impact:**
- Students may not realize they need to use a different notebook/terminal for exercises
- Output area gets cluttered with logs
- Some may accidentally stop the cell and kill the server
- No clear indication when server is ready (just continuous logs)

**Student Experience:**
"I ran the Temporal start cell and now I can't run anything else in my notebook. Is this right? How do I know when it's ready?"

**Recommendations:**
1. Add explicit instruction: "Open a NEW notebook for exercises after starting this"
2. Consider adding a startup check cell that verifies Temporal is running
3. Show example of successful startup logs so students know what to expect
4. Add troubleshooting: "If you see ERROR or connection refused, Temporal isn't ready yet"

---

### Issue #8: Missing Visual Indicators in Documentation

**Severity:** Minor - Documentation quality  
**Location:** `README.md` and exercise READMEs

**Problem:**
README references images that help with setup:

**exercises/01_agent_hello_world/exercise.ipynb (Cell 2):**
```markdown
Select **Python 3.11** if prompted:
![Select Python 3.11 kernel](../../images/select-kernel.png)
```

**Observation:**
The image exists (`images/select-kernel.png`), but:
1. Other setup steps don't have visual guides
2. Temporal UI access could benefit from screenshots
3. Port forwarding in Codespaces is visual but not shown
4. Exercise completion examples could show screenshots

**Impact:**
- Visual learners have harder time
- Port forwarding step (critical in Codespaces) has no visual guide
- Students may miss UI elements

**Recommendations:**
1. Add screenshot showing port forwarding tab in VS Code
2. Add screenshot of Temporal UI homepage (so students know what to expect)
3. Add screenshot showing where to find workflow ID in Temporal UI
4. Add screenshot of successful agent response format

---

### Issue #9: Python Version Specificity Unclear

**Severity:** Minor - Requirement clarity  
**Location:** Multiple files

**Problem:**
Python version requirements are specified in multiple ways:

**pyproject.toml:**
```toml
requires-python = ">=3.11"
```
→ Says 3.11 or higher

**README.md Prerequisites:**
```markdown
- 🐍 Basic Python knowledge
```
→ No version mentioned

**devcontainer.json:**
```json
"image": "mcr.microsoft.com/devcontainers/python:3.11"
```
→ Exact version 3.11

**temporal_installation.ipynb and exercises:**
```markdown
Select **Python 3.11** if prompted
```
→ Exact version 3.11

**CLAUDE.md:**
```markdown
- Python 3.11 (exact version required)
```
→ Claims exact version required

**Impact:**
- Unclear if students can use Python 3.12 or higher
- CLAUDE.md says "exact version required" but pyproject says ">=3.11"
- May cause unnecessary version downgrades

**Recommendations:**
1. Test with Python 3.12+ to see if it works
2. If 3.12+ works, update docs to say "Python 3.11 or higher"
3. If only 3.11 works, change pyproject.toml to `==3.11.*`
4. Be consistent across all documentation

---

### Issue #10: Error Message Quality in check_env.py

**Severity:** Minor - User experience  
**Location:** `scripts/check_env.py`

**Problem:**
The environment check script provides basic error messages:

```python
if not env_file.exists():
    print("❌ .env file not found")
    print("   Run: cp .env.sample .env")
    print("   Then add your OPENAI_API_KEY")
    return False
```

**Enhancement Opportunities:**
1. Doesn't check if `.env.sample` exists before suggesting copy
2. Doesn't detect if key is placeholder text (e.g., "your_api_key_here")
3. Doesn't validate key format (should start with "sk-")
4. Success message shows partial key but doesn't verify it works with OpenAI

**Recommendations:**
1. Add validation: `if api_key.startswith("sk-") is False: warn about invalid format`
2. Check for common placeholder values: "your_api_key_here", "sk-test", etc.
3. Optionally: Make a test API call to verify key is valid (may cost tokens)
4. Add link to where to get API key in error messages

---

## 📋 Observations & Suggestions

### Observation #1: Workshop Timing May Be Tight

**Location:** README.md Instructor Notes

**Current Timeline:**
- 00:00-30:00: Intro + Exercise 1 (30 min)
- 30:00-60:00: Exercise 2 (30 min)
- 60:00-90:00: Exercise 3 (30 min)
- Exercise 4: Optional

**Concerns:**
1. No buffer time for technical issues (Temporal not starting, API key problems)
2. Each exercise has 15-min timebox but gets 30 min in schedule (includes instruction)
3. If Exercise 4 is "optional", why is it a full exercise?
4. Advanced students may finish early with nothing to do

**Suggestions:**
1. Add 5-min buffer after each major section
2. Prepare "stretch goals" for fast students
3. Have Exercise 4 TODOs ready if time permits
4. Consider async format: students work at own pace

---

### Observation #2: No Automated Solution Validation

**Current State:**
Students complete TODOs, run cells, compare output to "Expected Output" section manually.

**Enhancement Idea:**
Could add validation cells that check if implementation is correct:
```python
# Validation cell (optional)
try:
    assert agent is not None, "Agent not created"
    assert hasattr(agent, 'tools'), "Agent missing tools"
    assert len(agent.tools) > 0, "Agent has no tools"
    print("✅ Agent created correctly!")
except AssertionError as e:
    print(f"❌ Validation failed: {e}")
```

**Benefits:**
- Students get immediate feedback
- Reduces instructor load
- Catches common mistakes
- Builds confidence

---

### Observation #3: Real API Usage May Cause Issues

**Location:** Exercise 1

Exercise 1 uses National Weather Service API which:
- Requires internet connection
- Can be slow or unavailable
- No API key needed (good!)
- But no fallback if down

**Potential Issues:**
1. Workshop in location with poor internet
2. NWS API having outage during workshop
3. Rate limiting if all students hit API simultaneously
4. Workshop outside US might have slow response times

**Suggestions:**
1. Add fallback mock data if API call fails
2. Mention in troubleshooting that API may be unavailable
3. Consider using a more reliable API or providing local mock server
4. Test API reliability in advance

---

### Observation #4: Notebook Kernel Management

**Current Instructions:**
"Select Python 3.11 kernel if prompted"

**Real-World Experience:**
- VS Code may not auto-detect kernel
- May need to manually install ipykernel
- Kernel selection UI differs between VS Code versions
- Codespaces vs local setup has different UX

**Suggestions:**
1. Add explicit `pip install ipykernel` step
2. Show screenshot of kernel selector
3. Add troubleshooting: "If no kernel appears, run: python -m ipykernel install --user"
4. Explain difference between Python interpreter and Jupyter kernel

---

## 🎯 Priority Recommendations

Based on severity and student impact, here's the recommended fix order:

### P0 - Must Fix Before Workshop
1. ✅ **Issue #1**: Fix pyproject.toml setup failure (FIXED)
2. **Issue #2**: Add tests directory or update CI
3. **Issue #3**: Fix Exercise 4 instruction mismatch
4. **Issue #4**: Standardize Temporal setup instructions
5. **Issue #5**: Fix bootstrap script Makefile references

### P1 - Should Fix Soon
6. **Issue #6**: Clarify Exercise 4 optional/required status
7. **Issue #7**: Improve temporal_installation.ipynb UX
8. **Issue #9**: Clarify Python version requirements

### P2 - Nice to Have
9. **Issue #8**: Add more screenshots/visual guides
10. **Issue #10**: Enhance check_env.py validation

### P3 - Future Improvements
- Observation #2: Add automated validation cells
- Observation #3: Add API fallback mechanisms
- Observation #4: Improve kernel setup docs

---

## 🧪 Testing Recommendations

To validate fixes and prevent regressions:

1. **Fresh Environment Test**
   - Spin up new Codespace
   - Follow README from start to finish
   - Document every command run and result

2. **Common Student Mistakes**
   - Forget to add API key
   - Skip Temporal startup
   - Use wrong Python version
   - Stop Temporal cell accidentally

3. **Cross-Platform Testing**
   - Test in Codespaces (primary)
   - Test locally on macOS
   - Test locally on Windows
   - Test locally on Linux

4. **Timing Validation**
   - Time each exercise with fresh student
   - Verify 15-min timeboxes are realistic
   - Check if 90-min total is achievable

---

## 📝 Summary

**Total Issues Found:** 10 major issues + 4 observations

**Critical Blocking Issues:** 2
- Setup failure (FIXED)
- Missing tests directory

**Major Confusing Issues:** 4
- Exercise 4 mismatch
- Temporal setup confusion
- Missing Makefile targets
- Inconsistent messaging

**Minor Polish Issues:** 4
- Documentation clarity
- Error message quality
- Visual guides
- Version specificity

**Key Insight:**
The workshop content is solid, but there are several "paper cuts" that will frustrate students. Most are documentation/consistency issues rather than code bugs. Fixing the critical issues will make the workshop runnable, while addressing the major issues will significantly improve student experience.

---

**Report compiled by:** GitHub Copilot  
**Methodology:** Step-through as first-time student, noting all points of confusion
