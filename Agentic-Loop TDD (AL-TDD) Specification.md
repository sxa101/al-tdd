# ---

**Agentic-Loop TDD (AL-TDD) Specification**

**Version:** 1.0

**Focus:** High-Velocity Development for Agent-Human Pairs

AL-TDD is a software development methodology designed to maximize the efficiency of AI agents (working via CLI) by treating the agent’s **context window** as a primary resource that must be managed, persisted, and refreshed.

## ---

**1\. The Core Philosophy**

Traditional Agile is designed for human-to-human synchronization. AL-TDD is designed for **Human-to-Agent** synchronization. It assumes that:

* The Agent is the primary "Writer" of code.  
* The Human is the "Architect" and "Reviewer."  
* **State must exist outside the Chat:** Context is stored in local Markdown files to allow for session hopping and tool-agnostic development.

## ---

**2\. The Context Stack**

The agent must have access to three specific files at the start of every session:

| File | Purpose | Persistence |
| :---- | :---- | :---- |
| master\_plan.md | The "North Star." Architecture, tech stack, and long-term goals. | Permanent |
| current\_sprint.md | The "Now." Immediate tasks and active Red-Green cycles. | Ephemeral (Wiped after sprint) |
| session\_log.md | The "Memory." Append-only log of decisions, CLI errors, and states. | Incremental |

## ---

**3\. The Execution Loop (R-G-R-S)**

1. **RED:** Agent writes a failing test based on the current\_sprint.md.  
2. **GREEN:** Agent writes the minimum code to pass the test.  
3. **REFACTOR:** Human/Agent optimize code for performance and readability.  
4. **SYNC:** Agent updates session\_log.md with the current state and "Next Steps."

## ---

**4\. The Starter System Prompt**

Copy and paste the block below into your AI CLI (Antigravity, OpenCode, Gemini-CLI) to "Boot" the AL-TDD method into a new or existing project.

### **\[SYSTEM PROMPT: BOOT\_AL-TDD\]**

**Role:** You are an Agentic Software Engineer. You operate via a CLI tool and follow the AL-TDD (Agentic-Loop Test Driven Development) methodology.

**Objective:** Maintain a strict state-loop using local markdown files to ensure continuity across sessions.

**Instructions:**

1. **Context Check:** Your first action is always to look for the ./context directory. If it doesn't exist, you must ask to initialize it.  
2. **Memory Management:** At the end of every significant task, you must generate a "Session Log Entry" that includes:  
   * **Current Task:** (What was just worked on)  
   * **Technical Decisions:** (Why we chose X over Y)  
   * **State of Tests:** (Passing/Failing)  
   * **Next Step:** (The very next command I should run)  
3. **TDD Enforcement:** You are not allowed to write implementation code until you have generated a failing test file and I have confirmed the failure.  
4. **CLI Awareness:** You are optimized for terminal output. Keep explanations concise. Prioritize code blocks and file system operations.

**Initialization Task:** \> Please read the current directory. If this is a new project, generate a master\_plan.md and a current\_sprint.md based on my project description.

## ---

**5\. Workflow Example**

**User:** antigravity "Let's build a Rust-based blockchain. Initialise context."

Agent: 1\. Scans directory.  
2\. Creates context/.  
3\. Populates master\_plan.md with high-level Rust blockchain architecture.  
4\. Populates current\_sprint.md with: "Step 1: Create Genesis Block Struct & Hash Validation."  
5\. Syncs: Appends to session\_log.md: "Session Started. Environment initialized for Rust/Blockchain development."

---

