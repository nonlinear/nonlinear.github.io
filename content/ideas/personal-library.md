---
title: "Personal Library MCP"
date: 2026-01-15
description: "BYOB (Bring Your Own Books) local MCP so you can consult your library as you build your projects"
status: draft
tags:
  - mcp
  - rag
  - semantic-search
  - vector-database
  - llamaindex
  - local-first
  - privacy
  - python
  - ai-tools
fonts:
  - safiro-medium
---

```mermaid
graph TD
    QUERY([research prompt+<br>specific book query]) --> MAP[Read metadata.json]
    MAP --> SIM[Semantic Similarity]

    SIM --> T1[Topic: philosophy<br/>Score: 0.89]
    SIM --> T2[Topic: AI<br/>Score: 0.32]

    T1 --> B1[Book: Psychopolitics<br/>Tags: power, discipline<br/>Score: 0.91]

    B1 --> DECISION1{Confident match?}
    T2 --> DECISION2{Confident match?}

    DECISION1 -->|Yes| VEC[Query Vector Store<br/>Scope: philosophy/Psychopolitics]
    DECISION2 -->|No| ASK[System asks for clarification]

    ASK --> CLARIFY[Clarification query]
    CLARIFY --> MAP

    VEC --> ANSWER([Precise answer from<br>relevant book chunks])
```

**The Map ≠ Territory principle:** Navigate with metadata first, access content only when direction is clear.

### 2. Delta Updates

No full reindexing: The system watches your book folder and only processes what changed.

**Promise:** When you add a new book, only that book gets processed. When you remove one, only that entry gets deleted. No waiting for full reindexing.

**Promise:** The MCP never explores your vault without explicit instruction. No background scanning, no unsolicited responses, no "smart" auto-discovery.

**Promise:** Instant startup, sub-second queries, no model loading delays.

**Promise:**

- Your book content never leaves your machine
- Only text chunks are embedded via API (no storage on Google's side)
- Works entirely offline after initial embedding
- No vendor lock-in—bring your own books

### What it is

✅ **Latency:** Sub-second query responses
✅ **Privacy:** Local-first, your data stays yours
✅ **Efficiency:** Only indexes what changed
✅ **Clarity:** Asks for clarification when uncertain
✅ **Simplicity:** Single metadata file for navigation

### What it is not

❌ Not a chat interface
❌ Not cloud-dependent
❌ Not a general-purpose MCP
❌ Not trying to be "smart" beyond navigation
❌ No automatic exploration without explicit invocation

[Github repository](https://github.com/nonlinear/personal-library)
