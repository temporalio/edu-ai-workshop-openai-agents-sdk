# Workshop Issues - Quick Summary

## Critical Blockers (Must Fix)

### 1. 🔴 Test Suite Broken
- **File:** `tests/*.py`
- **Problem:** Tests import from invalid Python module names (digits in names)
- **Fix:** Rename solution directories or remove tests

### 2. 🔴 Temporal Installation Hangs
- **File:** `temporal_installation.ipynb`
- **Problem:** Cell runs blocking server command, hangs notebook
- **Fix:** Add background execution or direct to `make temporal-up`

### 3. 🔴 Exercise 4 API Mismatch
- **Files:** `exercises/04_agent_routing/*`
- **Problem:** README, exercise template, and solution use different APIs
- **Fix:** Align all three to use same API (RunConfig vs simple Runner.run)

### 4. 🔴 Wrong Codespaces Link
- **File:** `README.md` line 3
- **Problem:** Links to `nadvolod/temporal-openai-agents-sdk` (wrong repo)
- **Fix:** Change to `temporal-community/edu-ai-workshop-openai-agents-sdk`

## Major Issues (Should Fix)

### 5. ⚠️ Bootstrap Script Wrong Commands
- **File:** `scripts/bootstrap.sh`
- **Problem:** Says "run 'make exercise-1'" but command doesn't exist
- **Fix:** Update to correct instructions (open Jupyter notebooks)

### 6. ⚠️ Undocumented Example Notebooks
- **File:** `example-notebook/` directory
- **Problem:** Not mentioned in README, unclear purpose
- **Fix:** Document purpose or move to extras/

### 7. ⚠️ Starter Method Inconsistency
- **File:** `exercises/04_agent_routing/starter.py`
- **Problem:** TODOs suggest start_workflow, solution uses execute_workflow
- **Fix:** Pick one approach consistently

## Quick Reference

**Total Issues:** 10 (4 critical, 3 major, 3 minor)

**Full Details:** See `ISSUES_FOUND.md`

**Priority Order:**
1. Fix tests (#1)
2. Fix temporal installation (#2)
3. Fix Exercise 4 mismatch (#3)
4. Fix Codespaces link (#4)
5. Fix bootstrap commands (#5)
6. Document example-notebook (#6)
7. Fix starter method (#7)

**Student Impact:**
- Cannot run tests after setup ❌
- Get stuck on Temporal installation ❌
- Cannot complete Exercise 4 ❌
- Cannot launch via Codespaces badge ❌

**Estimated Fix Time:**
- Critical issues: ~4-6 hours
- Major issues: ~2-3 hours
- Minor issues: ~1-2 hours
- **Total: ~7-11 hours**
