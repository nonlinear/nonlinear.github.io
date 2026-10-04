---
title: "Delay Tolerant for AI — conceito e manifestação no Kin"
id: nonlinear_20260920-delay-tolerant
type: article
status: backlog
date: 2026-09-20
owner: nonlinear
goal: "Explicar o conceito de delay tolerant (em vez de offline ready) e como ele se manifesta no Kin — arquitetura, UX, trade-offs. Artifact: artigo /article/delay-tolerant-ai."
promotion:
  deserves: true
  campaign: article
  brief: "Por que 'delay tolerant' é mais preciso que 'offline ready' para sistemas cognitivos — e como Kin implementa isso"
lifecycle:
  - status: backlog
    at: '2026-09-20'
parity:
  protocol_version: 3.5
  status: clean
  last_reconciled_at: '2026-09-20T16:12-04:00'
  note: "Criado durante sessão de sitemap. Como type:article com promotion flag."
---

# Delay Tolerant for AI

## O conceito
Offline ready é um estado binário: o app funciona sem rede ou não.
Delay tolerant é um **espectro**: o app tolera latência, desconexão parcial,
reações assíncronas, e reconcilia quando a rede volta — sem precisar ser
"completamente offline".

No Kin (chat interface com bridge architecture), delay tolerant significa:
- Mensagens saem da fila local mesmo sem confirmação do server
- O estado da UI não depende de round-trip imediato
- O agente responde quando pode (não quando o usuário espera)
- Reconciliação otimista: o que o usuário vê pode ser provisório

## O que este epic precisa investigar
1. **Definição do conceito** — por que "delay tolerant" é mais preciso que
   "offline ready" neste contexto
2. **Manifestação no Kin** — quais componentes da arquitetura implementam isso
   (fila, bridge, optimistic UI, reconciliation)
3. **Trade-offs** — o que se perde (consistência imediata, feedback instantâneo)
   vs. o que se ganha (resiliência, funcionamento em redes instáveis)
4. **Fontes** — artigos, papers, sistemas existentes que inspiraram (CRDTs, OT,
   sistemas de mensageria assíncrona)

## Artefato
- Artigo long-form: `/article/delay-tolerant-ai/`
- Diagrama(s) mermaid: fluxo de mensagem com delay tolerance

## Referências
- `kin/contract.md` — arquitetura do Kin
- `article-pipeline` — pipeline para produzir o artigo
- `article-epic.md` (policy) — campos obrigatórios, quality gates
- `branding-exercise` — tom (pensando em voz alta, não whitepaper acadêmico)
