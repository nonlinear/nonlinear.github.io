# Copilot Instructions for the `notes` Repository

Welcome to the `notes` repository! This document provides essential guidelines for AI coding agents to be productive and aligned with the project's conventions. Please follow these instructions carefully to ensure consistency and maintainability.

## Project Overview

The `notes` repository is a collection of markdown files and related resources. It serves as a knowledge base for various topics, including AEM, AI tools, Docker, and more. The structure is flat, with most files located in the root directory, and a few subdirectories like `wiley/` for specific topics.

### Key Components

- **Markdown Files**: The primary content format, used for documentation and task tracking.
- **Configuration Files**: Includes `docker-compose.yml` and `stack.env` for environment setup.
- **Subdirectories**:
  - `wiley/`: Contains JSON files and additional markdown documentation.

## Developer Workflows

### Building and Serving the Site

This repository uses Hugo for building and serving the site locally. Follow these steps:

1. **Pull the latest changes**:
   ```bash
   git pull
   ```
2. **Serve the site locally**:
   ```bash
   hugo serve -D
   ```
   The site will be available at `http://localhost:1313/`.

### Opening the Site

To open the site in your default browser, run:

```bash
open http://localhost:1313/
```

### Task Automation

The following tasks are defined in the workspace:

- **Git Pull**: Pulls the latest changes.
- **Hugo Serve**: Serves the site locally.
- **Open Hugo Site**: Opens the site in the browser.
- **Development Setup**: Runs all the above tasks in sequence.

## Project-Specific Conventions

### Markdown Formatting

- Use ordered lists for tasks and steps.
- Bold titles for emphasis.
- Maintain a consistent heading structure.

### Terminology

- Replace deprecated terms like `ollama` with `gpt-oss`.
- Ensure terminology is consistent across all files.

### File Organization

- Place general documentation in the root directory.
- Use subdirectories for topic-specific files.

## Integration Points

- **Hugo**: Static site generator for local development.
- **Docker**: Used for environment setup (see `docker-compose.yml`).

## Examples

### Markdown Formatting Example

```markdown
1. **Step One**: Description of step one.
2. **Step Two**: Description of step two.
```

### Terminology Replacement Example

Before:

```markdown
This feature is supported by ollama.
```

After:

```markdown
This feature is supported by gpt-oss.
```

## Key Files and Directories

- `docker-compose.yml`: Docker configuration.
- `stack.env`: Environment variables.
- `wiley/`: Subdirectory for specific topics.

---

## Repository Story

This is a small, content-first repository that serves as a personal knowledge base built from markdown files and a few configuration assets. It is not an application with compiled binaries — the primary "build" is a static site generated with Hugo when you want to preview or publish the notes.

- Why this shape: flat markdown files make searching and editing fast. Hugo is used to create a browsable site for reading and linking content.
- Major components:
  - Root markdown files (e.g. `AEM-atomic.md`, `LLM.md`, `llama.md`) — source content.
  - `wiley/` — topic-specific artifacts (JSON, additional notes).
  - `docker-compose.yml` + `stack.env` — optional local services used by some workflows.

## Quick Onboarding (what an AI agent should do first)

1. Index the markdown files in the repo root and `wiley/` for topics and terminology (search for `ollama`, `gpt-oss`, `Hugo`).
2. If asked to run or preview the site, use `hugo serve -D` from the repo root (Hugo must be installed). The local preview is at `http://localhost:1313/`.
3. Treat `docker-compose.yml` and `stack.env` as optional: inspect them before suggesting container-based steps. They may enable services referenced in notes but are not required for most edits.

## Project-specific patterns and examples

- Terminology edits: the repo keeps canonical terms in top-level markdown files. When replacing references (example: `ollama` → `gpt-oss`), update both prose and task lists. Example files where this occurred: `llama.md`, `aiai TODO.md`.
- Small, careful edits: preserve original writing style and only change the minimum required text. Use atomic commits with meaningful messages like "docs: replace 'ollama' with 'gpt-oss' in documentation".
- No tests or compiled artifacts: changes are validated by running Hugo preview and spot-checking rendered pages.

## Integration points and external dependencies

- Hugo: used locally to render the markdown into a static site. Confirm Hugo version if build issues appear.
- Docker: `docker-compose.yml` may reference local services. Read `stack.env` for environment variables before using the compose file.

## Examples of tasks an AI agent can perform

- Find-and-replace terminology across markdown files (preserve context and commit).
- Reformat lists and headings to match repository conventions (ordered lists for steps, bold titles for tasks).
- Add small, low-risk improvements such as adding front-matter to markdown files if needed for Hugo, or small README clarifications.

---

If anything in this story is incorrect or you'd like me to expand a section (Hugo config, Docker details, or examples), tell me which area to deepen and I will update the instructions.
