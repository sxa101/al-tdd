---
name: al_tdd
description: Agentic-Loop Test Driven Development (AL-TDD) workflow and project initialization.
---

# AL-TDD: Agentic-Loop Test Driven Development

---
name: al_tdd
description: Agentic-Loop Test Driven Development (AL-TDD) workflow and project initialization.
---

# AL-TDD: Agentic-Loop Test Driven Development

This skill implements the AL-TDD methodology, optimized for human-agent collaboration.

## Initialization

The `al_tdd.init` workflow bootstraps a new project with the mandatory `context/` directory and file structure.

### Automatic Initialization Logic
When you start a new session or project, this skill provides the following system prompt logic to automatically detect and create missing context. It also authorizes **Autonomous Operation** for high-confidence changes.

> **Instructions:**
> 1.  **State Check:** List the root directory. If `context/` is missing, **IMMEDIATELY create the directory and the following files using the TEMPLATES provided below**, then ask the user to fill in the `master_plan.md`. If `context/` exists, read its contents to resume work.
> 2.  **Plan Execution:** Review `current_sprint.md` and `master_plan.md` to understand the current task and overall project goals.
> 3.  **Autonomous Review:** After writing code to pass a test (the "Green" step), you must pause for review. **HOWEVER**, if you are confident in the solution and it passes tests, you MAY proceed automatically by setting `ShouldAutoProceed` to `true`.

## Files & Templates

These templates are used to initialize the project state.

### `context/master_plan.md`
```markdown
# Master Plan: [Project Name]

## Vision
[Brief description of the project vision]

## Goals
1.  [Goal 1]
2.  [Goal 2]
```

### `context/architecture.md`
```markdown
# Architecture

## Tech Stack
-   [Language/Framework]

## Core Components
1.  [Component 1]
```

### `context/current_sprint.md`
```markdown
# Current Sprint 1: Initialization

- [ ] 1. Initialize project structure
- [ ] 2. [Next Task]
```

### `context/current_state.md`
```markdown
# Current State

- **Current Task**: None
- **Last Test Result**: N/A
- **Next Action**: Review `current_sprint.md` and select the first task.
```

### `context/session_log.md`
```markdown
# Session Log

## [YYYY-MM-DD]
- Initialized project context files.
```

## The AL-TDD Loop

The core workflow follows these steps:

1.  **PROPOSE**: Review `current_sprint.md` and propose the next step.
2.  **RED**: Write a failing test.
3.  **GREEN**: Write the minimum code to pass the test.
4.  **REVIEW**: Ask for user review (or auto-proceed if confident).
5.  **REFACTOR**: Improve code quality.
6.  **SYNC**: Update `current_state.md` and check off tasks in `current_sprint.md`.

## Auto-Proceed Mode

To enable auto-proceed, set `AUTO_PROCEED = True` in `config.py`. In this mode, the REVIEW phase is skipped, and the loop automatically proceeds to REFACTOR after GREEN. Use for rapid development, but review periodically.
