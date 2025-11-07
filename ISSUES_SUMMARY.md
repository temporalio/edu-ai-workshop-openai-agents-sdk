# Workshop Issues - Quick Reference

**Full Report:** See [WORKSHOP_ISSUES_REPORT.md](./WORKSHOP_ISSUES_REPORT.md) for detailed analysis

## 🔴 Critical Issues (Must Fix)

| # | Issue | Location | Status |
|---|-------|----------|--------|
| 1 | Setup fails - missing pyproject.toml build config | `pyproject.toml` | ✅ FIXED |
| 2 | CI references non-existent tests/ directory | `.github/workflows/ci.yml` | ❌ Open |
| 3 | Exercise 4 instructions don't match solution code | `exercises/04_agent_routing/README.md` | ❌ Open |
| 4 | Exercise 4 missing import instructions | `exercises/04_agent_routing/README.md` | ❌ Open |

## 🟡 Major Issues (Confusing)

| # | Issue | Location | Status |
|---|-------|----------|--------|
| 5 | Conflicting Temporal setup methods | `README.md`, `bootstrap.sh`, `Makefile` | ❌ Open |
| 6 | Bootstrap references non-existent `make exercise-*` | `scripts/bootstrap.sh` | ❌ Open |
| 7 | Exercise 4 labeled "optional" inconsistently | `README.md` | ❌ Open |

## 🟢 Minor Issues (Polish)

| # | Issue | Location | Status |
|---|-------|----------|--------|
| 8 | Temporal notebook cell behavior unclear | `temporal_installation.ipynb` | ❌ Open |
| 9 | Missing screenshots for setup steps | `README.md` | ❌ Open |
| 10 | Python version requirements inconsistent | Multiple files | ❌ Open |
| 11 | Error messages need enhancement | `scripts/check_env.py` | ❌ Open |

## 🎯 Quick Fixes Checklist

### For Immediate Workshop Readiness:

- [x] Fix pyproject.toml (DONE)
- [ ] Create tests/ directory or remove CI test step
- [ ] Update Exercise 4 README to match solution OR simplify solution
- [ ] Add import statements to Exercise 4 instructions
- [ ] Choose ONE Temporal setup method and update all docs
- [ ] Fix bootstrap.sh to not reference make exercise-*

### For Better Student Experience:

- [ ] Clarify if Exercise 4 is optional
- [ ] Add note in temporal notebook about keeping cell running
- [ ] Add screenshots for port forwarding in Codespaces
- [ ] Standardize Python version message (3.11 vs >=3.11)
- [ ] Enhance check_env.py validation

## 📊 Impact Summary

**Workshop Blockers:** 2 issues (1 fixed)
- Students can't run setup
- CI is broken

**Student Confusion:** 5 issues
- Exercise 4 will cause errors and frustration
- Setup instructions are conflicting
- Missing imports cause NameErrors

**Documentation Issues:** 4 issues
- Minor polish needed
- Won't block workshop but will reduce quality

## 🚀 Recommendations

**For Next Workshop:**
1. Test full workshop in fresh Codespace before presenting
2. Have someone unfamiliar with the code go through exercises
3. Add automated validation cells to notebooks
4. Create instructor troubleshooting guide

**Priority Order:**
1. Create/fix tests directory (5 minutes)
2. Fix Exercise 4 instructions (30 minutes)
3. Standardize Temporal setup docs (15 minutes)
4. Fix bootstrap.sh references (5 minutes)
5. Add remaining polish (as time permits)

---

**Report Date:** 2025-11-07  
**Found By:** Workshop walk-through as student  
**Total Issues:** 11 + 4 observations  
**Fixed:** 1  
**Remaining:** 10
