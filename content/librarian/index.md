---
title: "Librarian"
status: done
type: project
date: 2026-09-21
description: "Semantic search for your books. Private. Local. BYOB."
audience: "Devs, researchers, knowledge workers who own a book collection"
promotion:
  deserves: true
  campaign: project
  brief: "Stop bullshitting me — show receipts."
doors:
  admire: true
  learn: "/article/source-highlights/"
  help:
    needs:
      - "Knowledge management — people who think about how humans organize, retrieve, preserve knowledge"
      - "RAG / indexing — where naive vector search falls down"
      - "Librarians / research practitioners — user testing: I want to watch how you use it"
    note: "Open source. No paid contributor work. Your contribution is credited."
---

## "You know that feeling when an AI cites a book it never read?"

Librarian doesn't do that. It searches **your** books and shows you the exact passage, highlighted, link included, with full bibliographic metadata.

```mermaid
flowchart LR
    USER[You add a book] --> WATCHER[Folder watcher]
    WATCHER --> INDEX[Auto-index: FAISS + embeddings]
    INDEX --> MCP[MCP server ready]
    MCP --> AGENT[Your agent queries with citations]
    AGENT --> YOU[Answer + highlight + page + link]
```

Trust is nice. **Verification is better.**

---

### What it is

A BYOB (Bring Your Own Books) semantic search engine. All local — books, embedding
models, database. Connect your AI assistant via MCP and ask questions. Every answer
includes the exact passage, highlighted, with a link back to the source.

### Why I built it

I got tired of AI tools citing books they never read. Librarian is the antidote:
your library stays yours, the search is local, and the citations are real.

---

### Want to understand it deeper?

→ [Source Highlights — how Librarian makes every source traceable](/article/source-highlights/)

Or ask your agent: copy this prompt and paste it wherever your AI lives:

```
> Tell me about Nonlinear's Librarian project.
> What is it, why does it exist, what's the architecture,
> and should I care?
```

Your agent consults the Cyborg Support MCP and comes back with the full context —
stack, install, philosophy, current state, everything.

---

### Want to help?

Librarian is open source. I'm specifically looking for:

- **Knowledge management** — people who actually think about how humans organize, retrieve, preserve, and use knowledge
- **RAG / indexing** — where naive vector search falls down, and what better approaches look like
- **Real research practitioners** — use Librarian for actual work? I want to watch you. Where does it get in your way? What did you expect?

No paid contributor work. Your contribution is credited.

**Know someone?** → [Tell me](/contact/)
