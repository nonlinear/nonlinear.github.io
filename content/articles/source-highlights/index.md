---
title: "Source Highlights — librarian cites, enumerates, and links sources"
id: nonlinear_20260920-source-highlights
type: article
status: backlog
date: 2026-09-20
owner: nonlinear
goal: "Garantir que o librarian não apenas cite sources mas também os enumere com links e highlights — um padrão de citação rica que vira parte do layout article."
promotion:
  deserves: true
  campaign: article
  brief: "Como tornar cada fonte rastreável — do claim ao highlight ao link"
lifecycle:
  - status: backlog
    at: '2026-09-20'
parity:
  protocol_version: 3.5
  status: clean
  last_reconciled_at: '2026-09-20T16:12-04:00'
  note: "Criado durante sessão de sitemap. Agora como type:article com promotion flag."
---

# Source Highlights

## O problema
Um artigo cita fontes. O normal é link no fim ou nota de rodapé.
Aqui a intenção é diferente: **cada fonte tem link + destaque + enumeração** —
o leitor vê de onde vem cada afirmação, com contexto do trecho relevante.

Não é "bibliografia". É **rastreabilidade pública da pesquisa** que gerou o artigo.

## O que o epic cobre
- Padrão de citação no frontmatter ou shortcode: `&#123;&#123;&lt; source "url" highlight="trecho destacado" &gt;&#125;&#125;`
- Renderização no layout article: enumeração numérica, links clicáveis, destaque inline
- Opcional: highlights expandem em tooltip/hover (popover glossary style)
- Integração com librarian (semantic search → a source é um book chunk, o highlight é o parágrafo relevante)

## O que NÃO cobre
- O mecanismo de busca no librarian (isso é do librarian)
- A pipeline editorial (isso é do article-pipeline)
- Apenas a **camada de apresentação** da source no artigo

## Referências
- `librarian` — ferramenta de busca que encontra os chunks
- `article/single.html` — layout que renderiza
- `glossary popover system` — conceito similar (hover expansion)
- `article-pipeline` — processo editorial que produz o artigo
- `article-epic.md` (policy) — campos obrigatórios, quality gates
