
---

# AL-TDD: Agentic-Loop Test Driven Development

**AL-TDD** is a software development methodology built for the era of Agentic AI. While traditional Agile was designed to sync human teams, AL-TDD is designed to sync a **Human Architect** with a **CLI-based AI Agent** (like OpenCode, Gemini-CLI, or Antigravity).

## 🚀 The Core Concept

The "Context Window" is the most valuable resource in AI development. AL-TDD treats context as a **stateful file system** rather than a fleeting chat history. By using a local `./context` directory, the Agent gains "External Memory," allowing you to drop and resume work across multiple sessions without losing progress.

## 🔄 The R-G-R-S Loop

1. **RED**: The Agent writes a failing test.
2. **GREEN**: The Agent writes the minimal code to pass.
3. **REFACTOR**: Performance and readability optimization.
4. **SYNC**: The Agent updates the `session_log.md` and `current_sprint.md`.

---

## 📂 Repository Structure

An AL-TDD project follows this mandatory structure to maintain agent alignment:

```text
├── .context/
│   ├── master_plan.md    # High-level architecture & tech stack
│   ├── current_sprint.md # Active tasks & checkboxes
│   └── session_log.md    # Append-only history of decisions & states
├── tests/                # TDD-first test suite
├── src/                  # Implementation code
└── AL-TDD.md             # This specification

```

---

## 🛠 Quick Start

To boot a new project using AL-TDD, paste the following into your Agentic CLI:

> "I want to start a new project using the AL-TDD method. Please initialize the `./context` directory, create a `master_plan.md` for a [Project Description], and set the first 'Red' task in `current_sprint.md`."

---

## 🧠 Why AL-TDD?

* **Zero Context Drift**: The agent reads the `session_log.md` to know exactly where it left off.
* **Deterministic Progress**: Strict TDD ensures the agent doesn't hallucinate "working" features.
* **Tool Agnostic**: Works with any LLM or CLI tool because the state lives in your Markdown files, not the AI's internal memory.

---
