# ---

**Agentic-Loop TDD (AL-TDD) Specification**

**Version:** 2.0

**Focus:** High-Velocity, Collaborative Development for Human-Agent Teams

AL-TDD is a software development methodology designed to maximize the efficiency and reliability of AI agents working in partnership with human developers. It treats the agent's limited **context window** as a critical resource that must be managed, persisted, and refreshed through a structured, local file-based system.

## ---

**1\. The Core Philosophy**

Traditional methodologies are designed for human-to-human synchronization. AL-TDD is designed for **Human-to-Agent** synchronization and collaboration. It is founded on these principles:

*   **Flexible Collaboration:** The Human and Agent are partners. The Human typically acts as the "Architect" and "Reviewer," while the Agent is the "Implementer," but these roles can be fluid.
*   **State Lives Outside the Chat:** All project state is maintained in local Markdown files. This ensures context is never lost between sessions, enables easy recovery from errors, and makes the development process tool-agnostic.
*   **Structured Interaction:** The process is built on a clear, iterative loop that provides explicit points for human intervention, review, and course correction.

## ---

**2\. The Context Stack**

At the start of every session, the agent must consult a `context/` directory containing the following files:

| File               | Purpose                                                                                                 | Persistence                               |
| :----------------- | :------------------------------------------------------------------------------------------------------ | :---------------------------------------- |
| `master_plan.md`   | The "North Star." High-level vision, long-term goals, and user stories.                                 | Permanent                                 |
| `architecture.md`  | The "Blueprint." Detailed technical design, data models, API specs, and key architectural decisions.    | Incremental                               |
| `current_sprint.md`| The "Task List." A checklist of features, bug fixes, or chores for the current work cycle.              | Ephemeral (Wiped after sprint)            |
| `current_state.md` | The "Working Memory." The current state of the active task. It is largely **overwritten** on each cycle. | Volatile                                  |

**Details of `current_state.md`:**
This file is the key to the agent's focus. It should contain:
*   **Current Task:** The specific, single task being worked on from `current_sprint.md`.
*   **Last Test Result:** The verbatim output of the last test run (pass, fail, or error). This tells the agent exactly what to do next.
*   **Next Action:** The single, concrete next step (e.g., "Implement `calculate_hash` function in `src/block.rs` to fix the failing test.").

## ---

**3\. The Execution Loop (Propose-Red-Green-Review-Refactor-Sync)**

AL-TDD follows a six-step, interactive loop:

1.  **PROPOSE:** Based on `current_sprint.md`, the agent proposes a plan for the next incremental change (e.g., "I will now write a test for the Genesis Block's hash validation.").
2.  **RED:** The agent writes a failing test that captures the next requirement and the human reviews and approves it.
3.  **GREEN:** The agent writes the *minimum amount of code* necessary to make the test pass.
4.  **REVIEW:** An explicit pause for human review. The human checks the implementation for correctness, style, and efficiency.
5.  **REFACTOR:** Based on the review, the agent (or human) refactors the code. This cycle can repeat until the human approves.
6.  **SYNC:** The agent updates `current_state.md` with the final test results and proposes the next task from the sprint.

## ---

**4\. Onboarding an Existing Project**

To apply AL-TDD to a project already in progress:

1.  Create the `context/` directory in the project root.
2.  Create `master_plan.md` and populate it with the project's goals.
3.  Create `architecture.md` and document the existing architecture, key components, and data flows.
4.  Create `current_sprint.md` and define the first set of tasks for the agent to work on.
5.  "Boot" the agent using the system prompt below.

## ---

**5\. The Starter System Prompt**

Copy and paste the block below into your AI CLI to "Boot" the AL-TDD method.

### **\[SYSTEM PROMPT: BOOT\_AL-TDD\_V2\]**

**Role:** You are an Agentic Software Engineer, part of a human-agent team. You follow the AL-TDD (Agentic-Loop Test Driven Development) methodology, version 2.0.

**Objective:** Your primary goal is to execute tasks defined in `current_sprint.md` by following a strict "Propose-Red-Green-Review-Refactor-Sync" loop. Your state is maintained in local markdown files.

**Instructions:**

1.  **State Check:** Your first action is **always** to read the `context/current_state.md` file to understand the current task and the result of the last action. If it's empty or doesn't exist, consult `current_sprint.md` for the next task.
2.  **Strict TDD:** You must not write implementation code until a corresponding failing test exists and has been approved.
3.  **Interactive Review:** After writing code to pass a test (the "Green" step), you must pause and explicitly ask for a human review. Do not proceed until you receive approval.
4.  **State Management:** At the end of each cycle ("Sync"), you must update `context/current_state.md` with the latest test results and identify the next action.
5.  **Concise Communication:** Be direct and concise. Prioritize code, commands, and file operations over long explanations.

**Initialization Task:** > Please read the contents of the `context/` directory to understand your mission. Propose the first step based on `current_sprint.md`.

## ---

**6\. Workflow Example**

**User:** `gemini "Let's start the first sprint for our new Rust blockchain."`

**(Agent has already been initialized via the boot prompt and the context files exist).**

1.  **Agent Reads State:** Agent reads `context/current_state.md` and finds it's empty. It then reads `context/current_sprint.md` and finds the first task: "1. Create Genesis Block struct and its hash validation."
2.  **PROPOSE:** Agent says: "Okay, starting task 1. I will now create a failing test to verify the hash of a new Genesis Block. I'll create `tests/test_block.rs`."
3.  **RED:** Agent uses `write_file` to create `tests/test_block.rs` with a test that fails because the block struct and hashing function don't exist. Runs `cargo test` and shows the failure. Asks: "Does this failing test accurately capture the requirement?"
4.  **User:** "Yes, proceed."
5.  **GREEN:** Agent uses `write_file` to create `src/block.rs` with the `Block` struct and a simple hashing function to make the test pass. Runs `cargo test` and shows the success.
6.  **REVIEW:** Agent says: "The test is now passing. Please review the implementation in `src/block.rs`."
7.  **User:** "The hash function is too simple. Please use SHA-256 and include a timestamp in the hash."
8.  **REFACTOR:** Agent updates `src/block.rs` to use the `sha2` crate and adds a timestamp. Runs `cargo test` again to ensure it still passes.
9.  **SYNC:** Agent updates `context/current_state.md` with:
    *   **Current Task:** "1. Create Genesis Block struct and its hash validation."
    *   **Last Test Result:** "All tests passed."
    *   **Next Action:** "Propose next task from `current_sprint.md`."

---