---
title: Test Slide
date: 2026-04-05
draft: false
layout: slide
---

# Test Slide

Primeiro slide — título e intro

---

## Slide 2

```mermaid
flowchart LR
  A[Active teste]:::active --> B[Review]:::review
  B --> C{Revisar}:::review
  C -->|ok| D[Publicar]:::done
  C -->|refazer| B
  D --> E[Distribuir]:::done
  E --> F[Monitorar]:::done
  C -->|Blocked| G[Pendencia]:::blocked
  G --> H[Review]:::review
  H --> B
```

---

## Slide 6 — fragmentos

- Item 1 <!-- .element: class="fragment" -->
- Item 2 <!-- .element: class="fragment highlight-red" -->
- Item 3 <!-- .element: class="fragment fade-out" -->

---

## Fim

Deck de teste — pronto para conectar o Reveal.js

Note: Notas do palestrante ficam aqui, invisíveis para a audiência.
