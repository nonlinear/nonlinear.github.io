# Agents sync — como o site aprende os tiers

Fonte de verdade: `~/.openclaw/agents/<agent>/workspace/IDENTITY.md` (`tier:`, `title:`).
Espelho: `data/agents.yaml` + `content/<slug>/index.md`.

## Tiers válidos

```
flagship | experimental | collab
```

**`article` NÃO é tier.** Artigo é gênero editorial, não maturidade. Página de
artigo não declara tipo — cai na `_default` (a cover).

**`writing` não existe.** Sem pasta, sem página de índice de escrita.

## Os dois scripts, e por que são dois

| Script | Faz | Não faz |
|---|---|---|
| `scripts/agent-sync-check.py` | lê fonte e espelho, **aponta** conflitos | não escreve nada. Nunca. |
| `scripts/agent-sync-heartbeat.py` | roda o check, **lembra** o que já foi apontado | não corrige. Escala para o owner. |

**Por que skill não resolve:** tier é decidido top-down pelo owner (P02E034).
Nenhuma skill tem autoridade para decidir tier. O que existe é um detector —
ele aponta, o owner decide.

Separação de camadas (nurtured-cognition):

```
skill     → executa e corrige     (formato, syntax, sequência)
check     → aponta               (puro, verificável, sem estado)
heartbeat → lembra e escala       (estado entre rodadas)
owner     → decide                (julgamento)
```

## Conflitos que o check detecta

- `TIER INVENTADO` — site declara tier que o IDENTITY não declara
- `TIER DIVERGE` — site e IDENTITY discordam
- `TIER INVÁLIDO` — valor fora do enum
- `NOME DIVERGE` — `title:` do site ≠ `title:` do IDENTITY
- `SEM PÁGINA` — agente declara tier e não tem `content/<slug>/`
- `PÁGINA SEM MD` — pasta em content sem `index.md`

## Uso

```sh
python3 scripts/agent-sync-check.py        # aponta (exit 1 se houver)
python3 scripts/agent-sync-heartbeat.py    # novos / persistem / resolvidos
python3 scripts/agent-sync-heartbeat.py --json
```

## Estado atual (2026-10-23)

15 conflitos `TIER INVENTADO`: agentes sem tier no IDENTITY foram publicados
como `experimental` por inferência. **Resolução = o owner declara o tier no
IDENTITY.md** (ou decide que esses agentes não têm página). O script nunca
conserta isso sozinho, porque é julgamento.
