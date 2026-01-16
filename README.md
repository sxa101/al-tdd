# AL-TDD Skill for Gemini CLI

The **Agentic-Loop Test Driven Development (AL-TDD)** skill enables AI agents to autonomously drive software development using a rigorous "Propose-Red-Green-Review-Refactor-Sync" loop.

## Overview

This repository hosts the `al_tdd` skill, designed to be installed into the Gemini CLI. It provides:
1.  **Project Initialization**: Automatically sets up the required `context/` directory and state files.
2.  **Autonomous Development**: A structured workflow for agents to plan, test, implement, and verify code.
3.  **Continuous Operation**: Support for continuous task execution (auto-looping).

## Installation

To install this skill, copy the `skills/al_tdd` directory to your local Gemini skills folder (e.g., `~/.gemini/skills/`).

For detailed instructions, see [skills/INSTALL.md](skills/INSTALL.md).

## Usage

In your Gemini CLI:

```bash
gemini "Initialize this project using AL-TDD"
```

The agent will detect the missing context and guide you through the setup.

## Methodology

This skill implements the AL-TDD v2.0 methodology.
-   **State**: Maintained in `context/*.md` files.
-   **Loop**:
    1.  **PROPOSE**: Plan the next step.
    2.  **RED**: Write a failing test.
    3.  **GREEN**: Make it pass.
    4.  **REVIEW**: Verify (or auto-proceed).
    5.  **REFACTOR**: Clean up.
    6.  **SYNC**: Update state and loop.
