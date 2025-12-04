# Copilot Instructions for the nonlinear.github.io Repository

This repository is a Hugo-powered static site for personal knowledge management. It is content-first, with most logic and structure in markdown and HTML files, and a few configuration assets. Follow these guidelines to be immediately productive as an AI coding agent:

## Big Picture Architecture

- **Content lives in `content/`**: Markdown and HTML files are organized by topic. Subfolders (e.g. `curva/`) group related notes and pages.
- **Static assets in `assets/` and `static/`**: CSS, images, fonts, and JS for site styling and interactivity.
- **Site build and output**: Hugo builds the site from `content/` and outputs to `docs/` for publishing (GitHub Pages).
- **No backend/server code**: All logic is static; no runtime services except optional local Docker for experiments.

## Developer Workflows

1. **Preview the site locally**:

```zsh
hugo serve -D
```

Access at [http://localhost:1313/](http://localhost:1313/). 2. **Update content**: Edit markdown/HTML in `content/`. Use ordered lists and bold headings for tasks/steps. 3. **Terminology consistency**: Replace deprecated terms everywhere, including lists and prose. 4. **Optional Docker**: Use `docker-compose.yml` and `stack.env` only if referenced in notes. Not required for Hugo or most edits.

## Project-Specific Conventions

- **Markdown formatting**: Use ordered lists for steps, bold for task titles, and consistent heading levels.
- **Atomic edits**: Make small, focused changes. Preserve original style and context.
- **Commit messages**: Use descriptive, context-aware messages (e.g. `docs: update terminology in llama.md`).
- **No tests or build artifacts**: Validate changes by running Hugo preview and checking rendered pages.

## Integration Points & External Dependencies

- **Hugo**: Main build tool. Confirm version if build issues arise.
- **Docker**: Only for optional local services. Inspect `docker-compose.yml` and `stack.env` before suggesting container steps.

## Examples from Codebase

- Terminology edits: See `llama.md`, `aiai TODO.md` for canonical term updates.
- List formatting: Ordered lists for steps in markdown (see `readme.md`).
- Content organization: Topic-specific folders in `content/curva/`, assets in `assets/` and `static/`.

---

If any section is unclear or missing, request feedback to iterate and improve these instructions.

## Dynamic Chatmode Indexing and Recommendations

To ensure chatmode guidance is always current:

- **Always index the contents of `.github/chatmodes/` at runtime.**
- For each chatmode file, extract the name and summary from its frontmatter or description.
- List and briefly describe all available chatmodes in the workspace.
- When prompted, analyze the current conversation and context to recommend the most suitable chatmode(s).
- Do not use a hardcoded list—changes to chatmode files (additions, removals, edits) are automatically reflected.

**Example prompt:**

> “Index all chatmodes in `.github/chatmodes/`, summarize their purpose and ideal use case, and recommend the best chatmode(s) for my current workflow based on recent conversation.”
