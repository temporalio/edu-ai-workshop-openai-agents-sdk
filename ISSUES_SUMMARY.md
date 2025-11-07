# Workshop Issues Summary

**Date:** November 7, 2025  
**Full Report:** [WORKSHOP_ISSUES_REPORT.md](./WORKSHOP_ISSUES_REPORT.md)

## Overview

Comprehensive review identified **17 issues** affecting workshop usability, ranging from critical blockers to polish improvements.

## Critical Issues (Must Fix) 🔴

### 1. Test Suite Completely Broken
- **Impact:** Cannot run `make test` - all tests fail with import errors
- **Root Cause:** Tests import from non-existent Python modules; solutions are notebooks
- **Quick Fix:** Restructure tests or use nbconvert to extract code
- **Priority:** P0 - Blocks CI/CD validation

### 2. Temporal Setup Instructions Confusing
- **Impact:** Students unsure which method to use (notebook vs `make temporal-up`)
- **Root Cause:** Two different approaches documented without clarity
- **Quick Fix:** Standardize on one method with clear step-by-step
- **Priority:** P0 - Students get stuck before exercises 2-4

### 3. Exercise 3 Markdown Formatting Issues
- **Impact:** Confusing structure, duplicated content, nested code blocks
- **Root Cause:** Copy/paste errors, incorrect markdown nesting
- **Quick Fix:** Reorganize sections, fix markdown syntax
- **Priority:** P1 - Affects learning experience

## High Priority Issues ⚠️

### 4. Lint Errors (132 total)
- 115 auto-fixable with `ruff check . --fix`
- Includes import sorting, unused f-strings, missing newlines
- **Quick Fix:** Run auto-fix, manually fix remaining

### 5. Exercise 2 Missing UnsandboxedWorkflowRunner
- Workers in notebooks need `workflow_runner=UnsandboxedWorkflowRunner()`
- Solution has it, exercise doesn't
- **Quick Fix:** Add 2 lines to Exercise 2

### 6. No Exercise 4 Tests
- Exercises 1-3 have tests (broken), Exercise 4 has none
- **Fix:** Create `test_exercise_04.py` with basic coverage

### 7. Missing API Key Validation
- Exercise 3 and 4 don't check for OPENAI_API_KEY early
- Students get cryptic OpenAI errors instead of helpful workshop errors
- **Quick Fix:** Add validation at start of exercises

### 8. Handoff Pattern Underdocumented
- Exercise 4 uses handoffs but doesn't explain mechanics
- Need diagram and example showing message flow
- **Fix:** Add detailed handoff documentation

## Medium Priority Issues 📋

### 9. No Durability Demonstration
- Exercise 3 titled "Durable Agent" but doesn't show durability
- Optional network disconnect test isn't emphasized
- **Fix:** Add explicit retry demonstration

### 10. Missing Temporal UI Guide
- Exercises link to UI but don't explain what to look for
- **Fix:** Add screenshots and guided tour section

### 11. NWS API Reliability Concerns
- Real API may be down, rate-limited, or geo-restricted
- **Fix:** Add fallback mock data

### 12. Activity Timeout Comments Missing
- 30-second timeouts used without explanation
- **Fix:** Add comments documenting timeout rationale

### 13. Bootstrap Script Outdated
- References `make exercise-1` which doesn't exist
- **Quick Fix:** Update instructions to "Open exercise notebook in VS Code"

### 14. Temporal Installation Notebook UX
- Server start cell blocks indefinitely without explanation
- Students confused whether this is expected
- **Fix:** Add explanatory markdown cell

## Low Priority (Polish) 🎨

### 15. README Command Inconsistency
- Mixes notebook and terminal approaches without clear distinction
- **Fix:** Standardize command formatting

### 16. Emoji Compatibility
- Heavy emoji usage may not work in all terminals
- **Consider:** Provide emoji-free alternative or document UTF-8 requirement

### 17. Missing Newlines at EOF
- Several files missing final newline
- **Quick Fix:** Already flagged by ruff --fix

## Recommended Action Plan

### Phase 1: Critical Fixes (1-2 days)
1. ✅ Fix test imports (restructure or remove tests)
2. ✅ Standardize Temporal startup documentation
3. ✅ Fix Exercise 3 markdown
4. ✅ Run `ruff check . --fix`

### Phase 2: High Priority (2-3 days)
5. ✅ Add UnsandboxedWorkflowRunner to Exercise 2
6. ✅ Add API key validation to exercises 3-4
7. ✅ Create Exercise 4 tests
8. ✅ Document handoff pattern with examples

### Phase 3: Medium Priority (3-5 days)
9. ✅ Add durability demonstration to Exercise 3
10. ✅ Create Temporal UI guide with screenshots
11. ✅ Add API fallback mocks
12. ✅ Improve temporal_installation.ipynb UX

### Phase 4: Polish (as time permits)
13. ✅ Clean up README inconsistencies
14. ✅ Document activity timeouts
15. ✅ Fix bootstrap script
16. ✅ Consider emoji alternatives

## Positive Findings ✅

The workshop has excellent fundamentals:
- **Strong exercise progression** (1→2→3→4 builds knowledge logically)
- **Clear TODOs** (students know exactly what to implement)
- **Good solution references** (complete notebooks for comparison)
- **Real-world examples** (NWS API, multi-language routing)
- **Production patterns** (Exercise 4 file structure)

With the critical fixes, this will be an excellent workshop!

## Testing Notes

All issues verified through:
- ✅ Fresh clone and `make setup`
- ✅ Running `make test` and `make lint`
- ✅ Reading all exercise notebooks and solutions
- ✅ Checking Exercise 4 Python files
- ✅ Verifying bootstrap and scripts
- ✅ Cross-referencing with CLAUDE.md instructions

**Environment:** GitHub Codespaces, Python 3.12.3, Workshop v1.0.0
